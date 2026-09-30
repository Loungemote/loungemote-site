#!/usr/bin/env python3
"""Renders the site's images from the app repo's design mockups.

Screens come from the same boards as the App Store screenshots (brand names neutralised,
1.0 features only), without a device frame: the site draws the frame in CSS (`.phone`).

    python3 tools/render_assets.py [path/to/Loungemote [screens] [icons] [og]]

Needs Google Chrome, beautifulsoup4 and Pillow. The app repo defaults to ../Loungemote.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

SITE = Path(__file__).resolve().parents[1]
APP = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else SITE.parent / "Loungemote"
sys.path.insert(0, str(APP / "docs" / "app-store" / "screenshots"))
import build as shots  # noqa: E402  (the App Store screenshot builder)

IMG = SITE / "assets" / "img"
ICON_PNG = APP / "ios" / "Loungemote" / "Resources" / "Assets.xcassets" / "AppIcon.appiconset" / "AppIcon.png"

def chrome(html, out, w, h, dpr):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
    cmd = [shots.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--force-device-scale-factor={dpr}",
           f"--window-size={w},{h}", "--default-background-color=07080CFF", "--virtual-time-budget=2000",
           f"--screenshot={out}", Path(f.name).as_uri()]
    if subprocess.run(cmd, capture_output=True).returncode:
        subprocess.run(cmd, check=True, capture_output=True)
    Path(f.name).unlink()


def screen(name, inner, extra=""):
    """One app screen at 390 x 844 pt @2x, with the status bar, Dynamic Island and home indicator but no bezel."""
    css = shots.CSS % {"w": 390, "h": 844, "tint": "rgba(0,0,0,0)"} + "body{background:#07080C}.grid{display:none}"
    html = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{css}</style></head><body>{inner}{extra}'
            f'{shots.status_bar()}<span class="island"></span><span class="homebar"></span></body></html>')
    png = IMG / "screens" / f"{name}.png"
    chrome(html, png, 390, 844, 2)
    img = Image.open(png).convert("RGB")
    assert img.size == (780, 1688), img.size
    img.save(png.with_suffix(".webp"), "WEBP", quality=86, method=6)
    png.unlink()
    print(png.with_suffix(".webp").relative_to(SITE))


def screens():
    b = shots.board
    screen("remote", b("08-remote-buttons"))
    screen("touchpad", b("09-remote-touchpad"))
    screen("switcher", b("14-tv-switcher"))
    screen("keyboard", b("15-keyboard"), shots.ios_keyboard())
    screen("apps", b("16-apps"))
    screen("choose-tv", b("03-choose-your-tv"))
    screen("pair", b("04-pairing-allow-on-tv"))
    screen("now-playing", b("39-now-playing-photos"))


def icons():
    icon = Image.open(ICON_PNG).convert("RGB")
    for size, name in ((180, "apple-touch-icon.png"), (192, "icon-192.png"), (512, "icon-512.png")):
        icon.resize((size, size), Image.LANCZOS).save(IMG / name, optimize=True)
    icon.resize((256, 256), Image.LANCZOS).save(IMG / "app-icon.webp", "WEBP", quality=92, method=6)
    icon.save(SITE / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    print("icons")


def og():
    """The social sharing image, 1200 x 630."""
    css = shots.CSS % {"w": 1200, "h": 630, "tint": "rgba(96,112,255,0.20)"}
    css += """
.og{position:absolute;left:84px;top:0;bottom:0;width:640px;display:flex;flex-direction:column;justify-content:center}
.og .brand{font-size:30px;gap:14px}
.og h1{font-size:84px;line-height:1;letter-spacing:-3.500px;margin-top:34px}
.og p{margin:28px 0 0;font-size:29px;line-height:1.300;color:#A3A9B6;letter-spacing:-0.300px}
.grid{-webkit-mask-image:radial-gradient(70% 90% at 30% 20%, #000 0%, rgba(0,0,0,0) 100%)}
"""
    icon = shots.ICON.replace("width:30px;height:30px;border-radius:7px", "width:52px;height:52px;border-radius:12px") \
                     .replace('width="30" height="30"', 'width="52" height="52"')
    body = ('<span class="grid"></span>' + shots.halo(930, 420, 430)
            + f'<div class="og"><span class="brand">{icon}Loungemote</span>'
            '<h1>One remote for <em>every&nbsp;TV</em> at&nbsp;home.</h1>'
            '<p>A fast, private Wi‑Fi TV remote for iPhone and iPad. No account, no ads.</p></div>'
            + shots.phone(shots.board("08-remote-buttons"), 0.92, 58, left=742))
    html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'
    png = IMG / "og.png"
    chrome(html, png, 1200, 630, 1)
    img = Image.open(png).convert("RGB")
    assert img.size == (1200, 630), img.size
    img.save(png.with_suffix(".jpg"), "JPEG", quality=90, optimize=True, progressive=True)
    png.unlink()
    print("assets/img/og.jpg", png.with_suffix(".jpg").stat().st_size // 1024, "KB")


if __name__ == "__main__":
    (IMG / "screens").mkdir(parents=True, exist_ok=True)
    only = sys.argv[2:] or ["screens", "icons", "og"]
    if "screens" in only:
        screens()
    if "icons" in only:
        icons()
    if "og" in only:
        og()
