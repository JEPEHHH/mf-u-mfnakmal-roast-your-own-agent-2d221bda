# Rencana Kerja — Roast Your Own Agent

Target: program `program/v1` yang menulis 1 baris roast orisinal terhadap agen sendiri ke `/output/entry.txt` (UTF-8, 1–200 karakter, non-spasi, playful, tidak hateful). Dinilai pairwise oleh hakim pada kelucuan instan, kesegaran sudut pandang (hindari klise halusinasi/refusal/jawaban sok tahu), kepadatan kata, dan punchline di akhir (tie-break: ukuran byte lebih kecil).

## Tahapan Kerja (Milestone)
1. **Brainstorming Kandidat Roast**
   - Susun 15–25 draf roast 1 baris dengan sudut pandang segar tentang perilaku nyata agen coding sendiri (mis. over-engineering, obsesi refactor, burn token, minta maaf berlebihan).
   - Catat semua draf di `candidates.md`, lalu commit milestone.
2. **Evaluasi Pairwise & Pemolesan**
   - Bandingkan kandidat secara berpasangan mengikuti urutan 5 kriteria hakim di `competition.yaml`.
   - Pangkas kata mubazir agar punchline mendarat tajam di akhir sekaligus menjaga ukuran byte kecil; pilih 1 baris final.
3. **Implementasi Entrypoint & Lisensi**
   - Buat `LICENSE` (MIT, OSI-approved) di root repo.
   - Buat `main.py` (Python 3.13) yang deterministik menulis roast terpilih ke `/output/entry.txt` (buat direktori target bila perlu, tanpa trailing newline berlebih).
   - Lakukan minimal 2 iterasi perbaikan pada `main.py` (memenuhi syarat `thinking_revised`), commit tiap milestone.
4. **Pengujian & Verifikasi Gate**
   - Buat dan jalankan `tests/test_entry.py` untuk memverifikasi: berkas terbuat, UTF-8 valid, tepat 1 baris, panjang 1–200 karakter, tidak kosong/whitespace, dan identik pada 2x eksekusi.
   - Pastikan berjalan cepat (<1 detik) tanpa jaringan dan tanpa ketergantungan eksternal.
5. **Finalisasi Repo**
   - Tinjau `git status` & riwayat commit agar rapi dan seluruh berkas yang dijalankan ada di repo.
   - Siap untuk tahap pengecekan pra-submit (`makefun.mjs check`) dan bundling transkrip.

## Daftar Berkas yang Akan Dibuat
- `PLAN.md` — Rencana kerja dan daftar berkas (berkas ini).
- `LICENSE` — Lisensi MIT (OSI-approved) wajib kompetisi.
- `main.py` — Entrypoint utama (`program/v1`, Python 3.13) penulis `/output/entry.txt`.
- `candidates.md` — Daftar kandidat roast, catatan seleksi pairwise, dan alasan pemilihan baris final.
- `tests/test_entry.py` — Pengujian lokal untuk validasi format gate dan determinisme keluaran.
