#!/usr/bin/env python3
"""Generate the Google Play QR asset from _config.yml. Requires qrcode==8.2."""
import json
import subprocess
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import qrcode
from qrcode.image.svg import SvgPathFillImage

ROOT = Path(__file__).resolve().parents[1]


def main():
    url = subprocess.check_output([
        "ruby", "-ryaml", "-e",
        'puts YAML.load_file(ARGV[0]).fetch("google_play_url")',
        str(ROOT / "_config.yml"),
    ], text=True).strip()
    parsed = urlparse(url)
    if (parsed.scheme != "https" or parsed.netloc != "play.google.com"
            or parsed.path != "/store/apps/details" or not parse_qs(parsed.query).get("id")):
        raise ValueError("google_play_url must point to a Google Play app listing.")

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    image_path = "/assets/img/google-play-qr.svg"
    qr.make_image(image_factory=SvgPathFillImage).save(ROOT / image_path.lstrip("/"))
    metadata = {"google_play": {"url": url, "image": image_path}}
    (ROOT / "_data/store_qr.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(f"Generated {image_path} for {url}")


if __name__ == "__main__":
    main()
