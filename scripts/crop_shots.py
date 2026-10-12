#!/usr/bin/env python3
"""Normalise project screenshots to one 16:10 frame so the README grid lines up.

Taller-than-target shots are cropped (anchored at the top so headers stay);
much wider shots are centred on a blurred, darkened copy of themselves instead
of losing their sides. Requires Pillow. Run: python3 scripts/crop_shots.py
"""
import io
import urllib.request
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter

W, H = 1600, 1000
OUT = Path(__file__).resolve().parent.parent / "profile" / "shots"
RAW = "https://raw.githubusercontent.com/Sanjays2402/"

SHOTS = {
    "gitsight": "gitsight/main/screenshots/commit-graph-hero.png",
    "tilt": "Tilt/main/assets/readme-hero.png",
    "context-clipboard": ("context-clipboard/main/docs/hero.png", (13, 17, 23)),
    "retrace": "retrace/main/docs/assets/feature-recovered.png",
    "optune-dark": "optune/main/docs/screenshots/hero-dark.png",
    "optune-light": "optune/main/docs/screenshots/hero-light.png",
    "city-friction-map": "city-friction-map/main/docs/screenshots/desktop.png",
}


def fetch(path):
    with urllib.request.urlopen(RAW + path, timeout=60) as r:
        return Image.open(io.BytesIO(r.read())).convert("RGB")


def frame(img, fill=None):
    ratio, target = img.width / img.height, W / H
    if ratio > target * 1.15:
        # very wide: fit inside, fill the bands with a solid colour or a blurred copy
        if fill:
            bg = Image.new("RGB", (W, H), fill)
        else:
            bg = img.resize((W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(40))
            bg = ImageEnhance.Brightness(bg).enhance(0.55)
        fg = img.resize((W, round(W / ratio)), Image.LANCZOS)
        bg.paste(fg, (0, (H - fg.height) // 2))
        return bg
    if ratio > target:
        # slightly wide: centre crop the sides
        w = round(img.height * target)
        img = img.crop(((img.width - w) // 2, 0, (img.width - w) // 2 + w, img.height))
    else:
        # tall: keep the top
        img = img.crop((0, 0, img.width, round(img.width / target)))
    return img.resize((W, H), Image.LANCZOS)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, spec in SHOTS.items():
        path, fill = spec if isinstance(spec, tuple) else (spec, None)
        out = OUT / f"{name}.jpg"
        frame(fetch(path), fill).save(out, "JPEG", quality=86, optimize=True, progressive=True)
        print("wrote", out.relative_to(OUT.parent.parent), f"{out.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
