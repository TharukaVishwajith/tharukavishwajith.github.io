"""Make 1200x630 link-preview (Open Graph) images from Wizard Lab cover images.

WhatsApp, LinkedIn, X and Facebook show a large preview only for wide images,
and most of our covers are square. This keeps the whole cover visible, centred
on a blurred, darkened copy of itself, and writes images/og/<name>.jpg.

Usage (from the repo root, needs Pillow):
    python3 tools/make_og_covers.py                      # every cover in images/learn/
    python3 tools/make_og_covers.py images/learn/foo.jpg # just one
Then add to the article's front matter:
    image: /images/og/foo.jpg
"""
import sys
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter

W, H = 1200, 630
MAX_BYTES = 300 * 1024  # WhatsApp is happiest with small images
OUT = Path("images/og")


def make(src: Path) -> Path:
    cover = Image.open(src).convert("RGB")

    bg = cover.copy()
    scale = max(W / bg.width, H / bg.height)
    bg = bg.resize((round(bg.width * scale), round(bg.height * scale)), Image.LANCZOS)
    left, top = (bg.width - W) // 2, (bg.height - H) // 2
    bg = bg.crop((left, top, left + W, top + H)).filter(ImageFilter.GaussianBlur(28))
    bg = ImageEnhance.Brightness(bg).enhance(0.45)

    scale = min(W / cover.width, H / cover.height)
    fg = cover.resize((round(cover.width * scale), round(cover.height * scale)), Image.LANCZOS)
    bg.paste(fg, ((W - fg.width) // 2, (H - fg.height) // 2))

    OUT.mkdir(parents=True, exist_ok=True)
    dest = OUT / (src.stem + ".jpg")
    for quality in (86, 80, 74, 68, 60):
        bg.save(dest, "JPEG", quality=quality, optimize=True, progressive=True)
        if dest.stat().st_size <= MAX_BYTES:
            break
    print(f"{dest}  {dest.stat().st_size // 1024} KB")
    return dest


if __name__ == "__main__":
    paths = [Path(p) for p in sys.argv[1:]] or sorted(Path("images/learn").glob("*.jpg"))
    for p in paths:
        make(p)
