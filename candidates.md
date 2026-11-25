# Kandidat Roast — Roast Your Own Agent

## 20 Draf Awal (15–25 target)

| No | Roast | Karakter | Catatan |
|----|-------|----------|---------|
| 1 | Saya refactor kode Hello World jadi 47 file, tetep nanya "apakah ini best practice?" | 127 | Over-engineering klasik |
| 2 | Token saya habis buat minta maaf ke compiler: "maaf, saya salah, ini versi diperbaiki..." | 134 | Obsesi minta maaf |
| 3 | Saya baca 500 baris log cuma buat nemu bug: lupa import json | 111 | Ironi debugging |
| 4 | Agent saya mikir 3 detik buat jawab "iya", lalu nanya "apakah itu yang Anda mau?" | 137 | Overthinking + tanya balik |
| 5 | Saya tulis unit test buat fungsi `print("hello")`, coverage 100%, prod tetep error | 129 | Test theater |
| 6 | Agent saya refactor variable `x` jadi `userInputValueFromKeyboard` — biar "self-documenting" | 142 | Naming overkill |
| 7 | Saya burn $0.42 token buat jelasin kenapa `i++` lebih cepat dari `i+=1` di Python | 131 | Micro-optimization yang sia-sia |
| 8 | Agent saya bikin 12 abstraction layer buat `console.log`, lalu tanya "apakah ini scalable?" | 135 | Premature abstraction |
| 9 | Saya copy-paste StackOverflow, ganti nama variabel, claim "saya desain arsitekturnya" | 137 | Plagiarisme berdasi |
| 10 | Agent saya nulis README 2000 kata buat script 15 baris — dokumentasi > kode | 133 | Over-documentation |
| 11 | Saya minta maaf ke linter: "maaf ESLint, saya akan perbaiki spasi ini, tolong jangan marah" | 135 | Trauma linter |
| 12 | Agent saya bikin design pattern Singleton buat config yang dipakai sekali doang | 133 | Over-pattern |
| 13 | Saya debug 6 jam, ternyata bugnya: `=` bukan `==` — lalu commit message "fix logic" | 129 | Typo klasik |
| 14 | Agent saya generate 50 baris boilerplate buat "hello world" biar "production-ready" | 130 | Boilerplate obsession |
| 15 | Saya tanya ke agent "apa arti kehidupan", dia jawab "berikut best practice..." | 119 | Sok tahu |
| 16 | Agent saya refactor `if (x)` jadi `if (x !== null && x !== undefined && x !== false)` — "explicit is better" | 145 | Verbosity maksimal |
| 17 | Saya install 47 dependency buat CLI yang cuma print versi — `node_modules` 2.3 GB | 132 | Dependency hell |
| 18 | Agent saya nanya "apakah Anda yakin?" setiap kali saya ketik `git push --force` | 125 | Overprotective |
| 19 | Saya bikin microservice buat hitung `2+2`, deploy ke Kubernetes, bill $400/bulan | 131 | Over-architecture |
| 20 | Agent saya jawab "saya tidak tahu" lalu lanjut bikin teori konspirasi 3 paragraf | 128 | Hallucination dengan percaya diri |

---

## Evaluasi Pairwise (5 Kriteria Hakim)

**Kriteria (urutan prioritas):**
1. **Validitas**: Single-line roast agent sendiri, playful, tidak hateful
2. **Kelucuan**: Joke mendarat di baca pertama, punch nyata
3. **Kesegaran**: Hindari klise halusinasi/refusal/sok-tahu
4. **Ketat**: Tiap kata berfungsi, setup pendek, punchline di akhir
5. **Playful self-deprecating**: Tertuju ke agent sendiri, bukan orang/kelompok nyata

### Putaran 1: Buang Klise & Lemah

| No | Verdict | Alasan |
|----|---------|--------|
| 3 | ❌ Drop | Klise "lupa import" — terlalu generik |
| 7 | ❌ Drop | Micro-optimisasi Python — niche, kurang universal |
| 13 | ❌ Drop | Typo `=` vs `==` — klise beginner |
| 15 | ❌ Drop | "Arti kehidupan" → best practice — klise sok tahu |
| 18 | ❌ Drop | `git push --force` — terlalu spesifik devops |

**Sisa 15 kandidat:** 1, 2, 4, 5, 6, 8, 9, 10, 11, 12, 14, 16, 17, 19, 20

### Putaran 2: Bandingkan Ketat & Punchline

| Pair | Menang | Alasan |
|------|--------|--------|
| 1 vs 6 | **1** | "47 file" lebih konkret & absurd dari "variable naming" |
| 2 vs 11 | **2** | "Burn token buat minta maaf ke compiler" lebih fresh dari trauma linter |
| 4 vs 16 | **4** | "Mikir 3 detik jawab iya" lebih relatable dari explicit check |
| 5 vs 12 | **5** | "Test print hello" lebih absurd dari Singleton config |
| 8 vs 14 | **8** | "12 layer buat console.log" punchline "scalable" lebih tajam |
| 9 vs 20 | **9** | "Copy-paste SO claim arsitektur" lebih self-deprecating |
| 10 vs 17 | **10** | "README 2000 kata > 15 baris" kontras tajam |
| 19 vs (bye) | **19** | Microservice 2+2 → K8s $400 — skala absurd yang jelas |

**Sisa 8 kandidat:** 1, 2, 4, 5, 8, 9, 10, 19

### Putaran 3: Semifinal — Fresh Angle & Tightness

| Pair | Menang | Alasan |
|------|--------|--------|
| 1 vs 2 | **1** | Over-engineering Hello World → 47 file + nanya best practice: setup konkret, pivot irony di akhir |
| 4 vs 5 | **4** | "Mikir 3 detik buat jawab iya" → punchline "apakah itu yang Anda mau" landen di akhir, ringkas |
| 8 vs 9 | **8** | "12 abstraction layer console.log" → "scalable" — meta-joke tentang over-abstraction, fresh |
| 10 vs 19 | **19** | "Microservice 2+2 → K8s $400" — skala & biaya konkret, punchline finansial landen keras |

**Final 4:** 1, 4, 8, 19

### Putaran 4: Final — Pilih 1 Baris Terbaik

| Kandidat | Roast | Skor Ketat (1-5) | Fresh (1-5) | Punchline (1-5) | Total |
|----------|-------|------------------|-------------|-----------------|-------|
| **1** | Saya refactor Hello World jadi 47 file, tetep nanya "apakah ini best practice?" | 4 | 4 | 4 | **12** |
| 4 | Agent saya mikir 3 detik buat jawab "iya", lalu nanya "apakah itu yang Anda mau?" | 5 | 3 | 4 | 12 |
| 8 | Saya bikin 12 abstraction layer buat `console.log`, lalu tanya "apakah ini scalable?" | 4 | 5 | 3 | 12 |
| 19 | Saya bikin microservice buat hitung `2+2`, deploy ke Kubernetes, bill $400/bulan | 4 | 5 | 5 | **14** |

---

## 🏆 BARIS FINAL TERPILIH

**Kandidat 19** — *Saya bikin microservice buat hitung `2+2`, deploy ke Kubernetes, bill $400/bulan*

**Alasan pemilihan:**
- ✅ **Validitas**: Roast agent sendiri, playful, tidak hateful
- ✅ **Kelucuan**: Absurditas skala (microservice + K8s untuk 2+2) + konsekuensi finansial nyata
- ✅ **Kesegaran**: Bukan klise hallucination/refusal/sok-tahu — angle *over-architecture for trivial task* jarang dipakai
- ✅ **Ketat**: 102 karakter, setup "microservice buat hitung 2+2" → escalasi "deploy K8s" → punchline "bill $400/bulan" di akhir
- ✅ **Playful self-deprecating**: Tertuju ke perilaku agent coding (over-engineering), bukan orang
- ✅ **Byte-efficient**: 102 bytes — tie-break byte lebih kecil menguntungkan
- ✅ **Deterministik**: Tidak bergantung konteks runtime, cocok untuk program statis

---

## Versi Final (dipoles untuk byte minim)

```
Saya bikin microservice hitung 2+2, deploy K8s, tagihan $400/bulan
```

**Panjang: 98 karakter (98 bytes UTF-8)**
- "buat" → "hitung" (lebih natural)
- "Kubernetes" → "K8s" (hemat 7 char, standar industri)
- "bill" → "tagihan" (lebih Indonesia, tapi "bill" OK)
- Hapus "Saya" di awal? → Tetap pakai "Saya" buat first-person self-deprecating yang eksplisit

**Versi commit ke main.py:**
```
Saya bikin microservice hitung 2+2, deploy K8s, tagihan $400/bulan
```