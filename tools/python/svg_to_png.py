#!/usr/bin/env python3
"""Convert one or more SVG map files to PNG.

The SVG is the canonical map artifact. This script rasterizes that exact SVG so
PNG and SVG cannot drift in geography, labels, stop numbering, or route geometry.

Usage:
    python tools/python/svg_to_png.py path/to/map.svg
    python tools/python/svg_to_png.py path/to/map-full-route.svg path/to/map-60-40-route.svg --width 2200

Converter preference:
    1. CairoSVG Python package
    2. rsvg-convert
    3. Inkscape
    4. ImageMagick `magick`
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def convert(svg_path: Path, png_path: Path, width: int) -> None:
    try:
        import cairosvg  # type: ignore

        cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=width)
        return
    except Exception:
        pass

    if shutil.which("rsvg-convert"):
        subprocess.run(
            ["rsvg-convert", "-w", str(width), "-o", str(png_path), str(svg_path)],
            check=True,
        )
        return

    if shutil.which("inkscape"):
        subprocess.run(
            [
                "inkscape",
                str(svg_path),
                "--export-type=png",
                f"--export-filename={png_path}",
                f"--export-width={width}",
            ],
            check=True,
        )
        return

    if shutil.which("magick"):
        subprocess.run(
            ["magick", "-density", "220", str(svg_path), str(png_path)],
            check=True,
        )
        return

    raise RuntimeError(
        "No SVG→PNG converter available. Install cairosvg, librsvg, Inkscape, or ImageMagick."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Rasterize canonical SVG maps to PNG")
    parser.add_argument("svg", nargs="+", type=Path, help="SVG file(s) to convert")
    parser.add_argument("--width", type=int, default=2200, help="Output PNG width in pixels")
    args = parser.parse_args()

    for svg in args.svg:
        svg = svg.resolve()
        if svg.suffix.lower() != ".svg":
            raise ValueError(f"Expected .svg input: {svg}")
        if not svg.exists():
            raise FileNotFoundError(svg)
        png = svg.with_suffix(".png")
        convert(svg, png, args.width)
        print(f"{svg} -> {png}")


if __name__ == "__main__":
    main()
