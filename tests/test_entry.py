#!/usr/bin/env python3
"""
Test validasi gate untuk /output/entry.txt.
Memverifikasi: file terbuat, UTF-8 valid, tepat 1 baris, panjang 1-200 char,
tidak kosong/whitespace-only, deterministik (2x eksekusi identik).
"""

import os
import sys
import subprocess
import tempfile
import shutil


def run_entrypoint(output_dir: str) -> tuple[int, str]:
    """Jalankan main.py dengan OUTPUT_DIR override, return (exit_code, content)."""
    env = os.environ.copy()
    env["OUTPUT_DIR"] = output_dir
    env["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__)) + "/.."

    result = subprocess.run(
        [sys.executable, "main.py"],
        cwd=os.path.dirname(os.path.abspath(__file__)) + "/..",
        capture_output=True,
        text=True,
        env=env,
        timeout=5,
    )

    entry_path = os.path.join(output_dir, "entry.txt")
    content = ""
    if os.path.exists(entry_path):
        with open(entry_path, "r", encoding="utf-8") as f:
            content = f.read()

    return result.returncode, content


def test_gate_validity():
    """Test semua syarat gate."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = os.path.join(tmpdir, "output")

        # Run 1
        code1, content1 = run_entrypoint(output_dir)
        assert code1 == 0, f"Exit code bukan 0: {code1}"

        # Run 2 (determinisme)
        code2, content2 = run_entrypoint(output_dir)
        assert code2 == 0, f"Run 2 exit code bukan 0: {code2}"

        # Deterministik: identik byte-for-byte
        assert content1 == content2, "Output tidak deterministik antara 2 run"

        # UTF-8 valid (sudah divalidasi oleh open(encoding="utf-8"))
        try:
            content1.encode("utf-8").decode("utf-8")
        except UnicodeError:
            raise AssertionError("Bukan UTF-8 valid")

        # Tepat 1 baris (tidak ada newline di tengah, trailing newline OK tapi tidak wajib)
        lines = content1.splitlines()
        assert len(lines) == 1, f"Bukan 1 baris: {len(lines)} baris"

        # Panjang 1-200 karakter
        length = len(content1)
        assert 1 <= length <= 200, f"Panjang {length} di luar range 1-200"

        # Tidak kosong / whitespace-only
        assert content1.strip() != "", "Kosong atau whitespace-only"

        # Verifikasi konten persis roast yang diharapkan
        expected = "Saya bikin microservice hitung 2+2, deploy K8s, tagihan $400/bulan"
        assert content1 == expected, f"Konten tidak sesuai: {repr(content1)} != {repr(expected)}"

        # Byte size check (untuk tie-break)
        byte_size = len(content1.encode("utf-8"))
        assert byte_size == len(expected.encode("utf-8")), "Byte size mismatch"

        print(f"✅ Semua gate lolos")
        print(f"   Konten: {repr(content1)}")
        print(f"   Panjang: {length} char, {byte_size} bytes")
        print(f"   Deterministik: ya")


def test_performance():
    """Test cepat (<1 detik) tanpa jaringan."""
    import time

    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = os.path.join(tmpdir, "output")

        start = time.perf_counter()
        code, _ = run_entrypoint(output_dir)
        elapsed = time.perf_counter() - start

        assert code == 0
        assert elapsed < 1.0, f"Terlalu lambat: {elapsed:.3f}s (max 1s)"
        print(f"✅ Performance: {elapsed*1000:.1f}ms (<1s)")


if __name__ == "__main__":
    try:
        test_gate_validity()
        test_performance()
        print("\n🎉 SEMUA TEST LOLOS")
        sys.exit(0)
    except AssertionError as e:
        print(f"\n❌ TEST GAGAL: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 ERROR: {e}")
        sys.exit(1)