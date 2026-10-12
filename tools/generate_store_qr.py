#!/usr/bin/env python3
"""Generate the Google Play and App Store QR assets from _config.yml. Requires qrcode==8.2.

A store whose URL is empty gets no QR code.
"""
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import qrcode
from qrcode.image.svg import SvgPathFillImage

ROOT = Path(__file__).resolve().parents[1]


def is_play_listing(parsed):
    return (parsed.netloc == "play.google.com" and parsed.path == "/store/apps/details"
            and bool(parse_qs(parsed.query).get("id")))


def is_app_store_listing(parsed):
    return parsed.netloc == "apps.apple.com" and re.search(r"/id\d+$", parsed.path) is not None


# Data key: (config key, image, listing check, error)
STORES = {
    "google_play": ("google_play_url", "/assets/img/google-play-qr.svg", is_play_listing,
                    "google_play_url must point to a Google Play app listing."),
    "app_store": ("app_store_url", "/assets/img/app-store-qr.svg", is_app_store_listing,
                  "app_store_url must point to an App Store app listing."),
}


def main():
    config = json.loads(subprocess.check_output([
        "ruby", "-ryaml", "-rjson", "-e", "puts YAML.load_file(ARGV[0]).to_json",
        str(ROOT / "_config.yml"),
    ], text=True))
    metadata = {}
    for store, (key, image_path, is_listing, error) in STORES.items():
        url = (config.get(key) or "").strip()
        if not url:
            continue
        parsed = urlparse(url)
        if parsed.scheme != "https" or not is_listing(parsed):
            raise ValueError(error)

        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        qr.make_image(image_factory=SvgPathFillImage).save(ROOT / image_path.lstrip("/"))
        metadata[store] = {"url": url, "image": image_path}
        print(f"Generated {image_path} for {url}")
    (ROOT / "_data/store_qr.json").write_text(json.dumps(metadata, indent=2) + "\n")


if __name__ == "__main__":
    main()
