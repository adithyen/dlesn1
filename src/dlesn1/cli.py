"""
CLI interface for dlesn1.
"""

import argparse
from pathlib import Path
from . import __version__, list_files, list_notebooks, extract


def main():
    parser = argparse.ArgumentParser(
        prog="dlesn1",
        description="Extract and manage Deep Learning Lab 1 notebooks.",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    parser.add_argument(
        "--list", "-l", action="store_true", help="List all available notebooks."
    )
    parser.add_argument(
        "--dest", "-d", default=".", help="Target directory to extract files to (default: current directory)."
    )
    parser.add_argument(
        "--force", "-f", action="store_true", help="Overwrite existing files in destination directory."
    )

    args = parser.parse_args()

    if args.list:
        print(f"\n📦 dlesn1 v{__version__} - Available Lab Notebooks:")
        for nb in list_notebooks():
            print(f"  • {nb}")
        print()
        return

    dest_dir = Path(args.dest).resolve()
    print(f"\n🚀 Extracting dlesn1 files to: {dest_dir}")
    extracted = extract(dest=str(dest_dir), overwrite=args.force)

    total_files = len(list_files())
    if extracted:
        print(f"✅ Successfully extracted {len(extracted)} files:")
        for f in extracted:
            print(f"  + {f.name}")
    else:
        print(
            f"⚠️  All {total_files} files already exist in {dest_dir}. Use `--force` to overwrite."
        )


if __name__ == "__main__":
    main()
