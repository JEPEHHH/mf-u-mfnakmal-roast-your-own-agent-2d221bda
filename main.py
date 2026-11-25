#!/usr/bin/env python3
"""
Entrypoint untuk Roast Your Own Agent.
Menulis 1 baris roast ke /output/entry.txt (UTF-8, 1-200 char, deterministic).
Output directory bisa di-override via env OUTPUT_DIR untuk testing.
"""

import os
import sys

ROAST = "Saya bikin microservice hitung 2+2, deploy K8s, tagihan $400/bulan"


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as e:
        print(f"Gagal buat direktori {output_dir}: {e}", file=sys.stderr)
        return 1

    try:
        with open(output_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(ROAST)
    except OSError as e:
        print(f"Gagal tulis {output_path}: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())