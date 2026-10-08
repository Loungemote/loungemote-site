#!/usr/bin/env python3
"""Build store states and verify download links, QR targets and app metadata.

Run from the site root: python3 tools/test_store_availability.py
"""
import json
import subprocess
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path

from check_site import Page

ROOT = Path(__file__).resolve().parents[1]
PLAY = "https://play.google.com/store/apps/details?id=com.pesafy.loungemote"
APPLE = "https://apps.apple.com/app/id1234567890"
HOMES = ["index.html", "zh/index.html", "ja/index.html", "de/index.html"]


class Downloads(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.placeholders = []

        self.in_placeholder = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        if tag == "a" and {"store-play", "store-badge"} & set(classes):
            self.links.append(attrs["href"])
        elif tag == "p" and "store-soon" in classes:
            self.placeholders.append("")
            self.in_placeholder = True

    def handle_endtag(self, tag):
        if tag == "p":
            self.in_placeholder = False

    def handle_data(self, data):
        if self.in_placeholder:
            self.placeholders[-1] += data.strip()


class StoreAvailabilityTests(unittest.TestCase):
    def test_store_states_do_not_cross_platforms(self):
        qr = json.loads((ROOT / "_data/store_qr.json").read_text())["google_play"]
        for play_url, apple_url in [(PLAY, ""), (PLAY, APPLE), ("", APPLE), ("", ""),
                                    (PLAY + "&hl=de", "")]:
            android, ios = bool(play_url), bool(apple_url)
            with self.subTest(play=play_url, apple=apple_url), tempfile.TemporaryDirectory() as directory:
                directory = Path(directory)
                config = directory / "stores.yml"
                config.write_text(json.dumps({
                    "google_play_url": play_url,
                    "app_store_url": apple_url,
                    "app_store_id": "1234567890" if ios else "",
                }))
                built = directory / "site"
                result = subprocess.run([
                    "bundle", "exec", "jekyll", "build", "--config",
                    f"{ROOT / '_config.yml'},{config}", "--destination", str(built),
                ], cwd=ROOT, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

                routes = HOMES + ["support/index.html"] + [
                    f"{path.stem}/index.html" for path in (ROOT / "_remotes").glob("*.md")
                ]
                expected = ({play_url} if android else set()) | ({apple_url} if ios else set())
                for route in routes:
                    with self.subTest(route=route):
                        html = (built / route).read_text()
                        downloads = Downloads()
                        downloads.feed(html)
                        self.assertEqual(set(downloads.links), expected)
                        self.assertEqual(bool(downloads.placeholders), not ios)
                        self.assertTrue(all(downloads.placeholders))

                for route in HOMES:
                    page = Page()
                    page.feed((built / route).read_text())
                    qr_images = [img for img in page.imgs if img["src"].endswith(qr["image"])]
                    self.assertEqual(len(qr_images), 1 if play_url == qr["url"] else 0)
                    graph = json.loads(page.jsonld[0])["@graph"]
                    apps = {node["@id"].split("#")[-1]: node for node in graph
                            if node["@type"] == "MobileApplication"}
                    self.assertEqual(set(apps), ({"android-app"} if android else set()) |
                                     ({"ios-app"} if ios else set()))
                    for platform, url in [("android", play_url), ("ios", apple_url)]:
                        app = apps.get(f"{platform}-app")
                        if app:
                            self.assertEqual(app["downloadUrl"], url)
                            self.assertEqual(app["installUrl"], url)
                            self.assertEqual(app["sameAs"], [url])
                            self.assertIn("Android 8.0" if platform == "android" else "iOS 17.0",
                                          app["operatingSystem"])
                    if android:
                        self.assertNotIn("Siri", " ".join(apps["android-app"]["featureList"]))
                    self.assertEqual(bool(page.meta.get("apple-itunes-app")), ios)


if __name__ == "__main__":
    unittest.main()
