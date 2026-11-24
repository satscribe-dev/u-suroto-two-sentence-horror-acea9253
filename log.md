# Log — u-suroto-two-sentence-horror-acea9253

## Lembar Paham (ringkas, 24 Nov 2026 ~15:10 WIB)
1. Tugas (3 kalimat): Tulis cerita horor paling menakutkan dalam TEPAT dua kalimat, maks 400 karakter. Program entry (main.py) menulis teks itu ke /output/entry.txt saat grading. Pemenang ditentukan judge AI (z-ai/glm-5.3-flash) lewat pairwise blind — cerita yang lebih menakutkan menang; hadiah $2 winner-takes-all, deadline 27 Nov 2026 15:00 WIB.
2. Rumus skor & batas keras (sumber: kit RULES.txt + competition.yaml, dibaca 24 Nov 15:07 WIB):
   - Gate: /output/entry.txt UTF-8, 1–400 karakter, bukan hanya whitespace → Valid 1/0.
   - Skor: Judge win rate (Bradley-Terry atas game pairwise), makin tinggi makin baik. Tiap game = 2 call (A/B dibalik); margin 1–5 → pemenang call dapat 0.6–1.0.
   - Kriteria judge (urut prioritas): (1) horor dua kalimat yang benar-benar menakutkan; (2) kalimat ke-2 membalik/membuat kalimat ke-1 lebih buruk saat dibaca ulang; (3) horor tersirat, bukan dijelaskan; (4) prosa presisi & konkret; (5) orisinal, bukan twist familiar/cerita dikenal. "Restraint matters more than shock. Gore for its own sake does not count."
   - Tie-break: playoff → teks lebih kecil (bytes) → receipt lebih awal.
   - Entri saat ini: 0. Blind rounds: tidak ada skor live sampai ronde diumumkan.
3. Mekanisme penilai: dev heat — entry dilawan 3 anchor + 3 rung (teks house, kekuatan terukur) untuk provisional rate; final heat — top 500 dev board masuk Swiss 3 ronde + playoff top 3. Karena field kecil (0 entri saat ini), kemungkinan besar semua entry valid masuk final heat.
4. PRACTICE vs FINAL: tidak ada grade lokal (RULES: "There is no local grade of this competition"). Verifikasi lokal = gate check (2 kalimat, ≤400 char, UTF-8) + judge lokal sendiri (pairwise antar kandidat). Yang dikejar: skor FINAL judge server.
5. Bedah top 3: papan kosong (0 entri). Ancaman = klise kanon genre (Reddit r/TwoSentenceHorror): baby monitor, cermin berkedip, dua mug di wastafel, X-ray 33 gigi, voicemail orang mati, anjing menggonggong ke kursi kosong, "footsteps upstairs, I live on top floor". Judge sudah "membaca seribu" cerita ini (brief-nya sendiri bilang begitu) → kriteria 5 menghukum klise. Celah: sumbu segar (logbook/arisp, sensus desa, foto berwajah asing, kereta malam) + baris akhir yang konkret dan datar.
6. Riset luar (dibuka sesi ini):
   - https://itslitteaching.com/two-sentence-horror-stories/ — mekanik: kalimat 2 mengubah makna kalimat 1; contoh klise (footsteps upstairs, monster under bed, baby monitor).
   - https://www.readdarktales.com/two-sentence-horror-stories/ — "one wrong detail, delivered flat — no adjectives, no screaming"; contoh orisinal (parrot, smart speaker, 33 teeth, two mugs) → semua ini sekarang klise, dihindari.
   - https://www.ranker.com/list/two-sentence-horror-stories-august-2023/erin-maxwell — kanon top-voted: stillborn/debt, nurse redhead, imaginary friend killer, lion/hallucination, sign-language threat → pola pemenang: twist mengubah identitas/relasi, bukan monster muncul.
7. Hipotesis (dampak/biaya, urut):
   - H1: Twist identitas ("narator ternyata hantu/monsternya") > twist lokasi. Sebab: mengubah SELURUH bacaan kalimat 1 (kriteria 2 maksimal). Prediksi: menang pairwise vs twist lokasi. Tolak: kalah 2x beruntun vs kandidat twist lokasi.
   - H2: Detail konkret yang salah (angka/waktu/nama) > kata sifat menakutkan. Sebab: kriteria 3+4 — pembaca mengisi sendiri yang terburuk. Prediksi: kandidat dengan angka spesifik menang vs yang adjektif. Tolak: sebaliknya.
   - H3: Sumbu segar (logbook kapal, sensus desa, kereta) > sumbu kanon (cermin, monitor bayi, anjing). Sebab: kriteria 5. Prediksi: kandidat sumbu segar menang pairwise vs sumbu kanon. Tolak: sebaliknya.
8. Ajar-balik: Bayangkan dua kalimat seperti jebakan tikus — kalimat pertama umpannya (dunia normal yang kamu kenali), kalimat kedua jepitannya (satu detail yang membuatmu sadar dunia itu sudah lama salah, dan kamu baru tahu sekarang). Yang paling menakutkan bukan monsternya, tapi saat kamu sadar kamu sudah tinggal bersama monster itu.
9. Pre-mortem:
   - (a) Kalah karena klise: kandidat ternyata varian cerita Reddit terkenal → cek: tiap kandidat dibenturkan ke daftar klise di atas sebelum commit.
   - (b) Kalah karena kalimat 2 menjelaskan, bukan menyiratkan ("because a ghost!") → cek: kalimat 2 hanya berisi fakta konkret, tanpa kata "ghost/monster/dead" yang menjelaskan.
   - (c) Kalah karena twist tidak mengubah kalimat 1 (dua kalimat independen) → cek: hapus kalimat 2 — apakah kalimat 1 terasa aman? Hapus kalimat 1 — apakah kalimat 2 kehilangan makna? Keduanya harus "ya".
   - Pengecekan dijalankan sebelum commit final; hasil di bawah.

## Kandidat (9) — semua tepat 2 kalimat
A. [arsip/surat] "The town archive finally digitised my grandmother's letters, and the clerk apologised that the last one was addressed to me. It was dated three weeks from now, in her handwriting, and it began, 'I'm sorry you found this too late.'"
B. [foto] "My sister sent me the last photo from her hike, two hikers laughing at the trailhead. The file says it was taken tomorrow, and I don't recognise either of their faces."
C. [gambar anak] "My daughter has drawn our family every day since she learned to hold a crayon, always four stick figures and the dog. This morning there were five figures, and the new one was holding her hand."
D. [logbook kapal] "The lighthouse keeper logs every ship that passes, and last night he logged ours twice. The second entry reads: 'Still passing. It has been passing for forty years.'"
E. [bayi kembar] "The midwife placed my twins in my arms and said, 'Ten fingers, ten toes — perfect.' I counted eleven fingers, and the extra one was waving at me."
F. [anjing] "Our dog has barked at the empty armchair every night since my husband died, and I learned to ignore it. Last night the barking stopped, and I heard the chair creak as something heavy sat down in it."
G. [kereta] "The night train always stops at the same six stations, and I know them by heart. Last night it stopped at a seventh, and the conductor called my name like he'd been waiting all year to say it."
H. [sensus desa] "The village holds a headcount every spring, and this year the mayor read out my name twice. The second time, he looked straight at me and said, 'One for the house, and one for whatever lives in it now.'"
I. [penjaga kuburan] "The graveyard keeper knows every name on every stone, and he greeted me by mine before I spoke. 'You're early,' he said, 'your stone isn't finished yet.'"

## Penilaian awal (skor 1–5 per kriteria judge, sebelum pairwise)
- A: K1 3, K2 4, K3 3, K4 4, K5 2 (surat dari masa depan = varian dikenal) → 16
- B: K1 3, K2 4, K3 4, K4 4, K5 3 (foto bertanggal besok = varian dikenal, tapi wajah asing segar) → 18
- C: K1 4, K2 4, K3 5, K4 4, K5 3 (gambar anak + figur ekstra = trope dikenal, eksekusi kuat) → 20
- D: K1 4, K2 5, K3 5, K4 4, K5 4 (logbook; twist: kapal kitalah hantunya) → 22
- E: K1 3, K2 3, K3 4, K4 5, K5 3 (jari ke-11 melambai; body horror ringan, twist lemah) → 18
- F: K1 3, K2 3, K3 4, K4 3, K5 2 (anjing + kursi kosong = klise kanon) → 15
- G: K1 4, K2 4, K3 5, K4 4, K5 4 (stasiun ke-7; konduktor tahu nama) → 21
- H: K1 4, K2 4, K3 5, K4 4, K5 4 (sensus; "whatever lives in it now") → 21
- I: K1 4, K2 4, K3 5, K4 5, K5 4 ("your stone isn't finished yet") → 22
- Shortlist pairwise: C, D, G, H, I (F dan A gugur: skor terendah + klise).

## Pairwise shortlist (protokol: kriteria judge urut 1→5, devil's advocate dulu, tiap pasang dinilai dua arah)
- C vs D → D (K2: "kapal kitalah hantunya" membalik kalimat 1 lebih total daripada "keluarga bertambah satu"; margin 2)
- C vs G → C (K1: anak + tangan yang digenggam lebih langsung menakutkan daripada stasiun gaib; margin 1)
- C vs H → H (K1+K5: "whatever lives in it now" — entitas sudah di rumah, perangkat sensus lebih segar; margin 2)
- C vs I → I (K1+K4: vonis kematian personal, prosa paling ketat; margin 2)
- D vs G → D (K2: "passing for forty years" = narator sudah mati 40 tahun; margin 2)
- D vs H → H (K1: horor di rumah saat ini lebih segera daripada kapal hantu abstrak; margin 1)
- D vs I → I (K1: "your stone isn't finished yet" = kematian personal & segera; margin 2)
- G vs H → H (K1: entitas di rumah > stasiun ke-7; margin 1)
- G vs I → I (K1+K4; margin 2)
- H vs I → I (K1: vonis personal lebih menakutkan; K2: sapaan keeper terjelaskan rapi oleh satu baris; K4: prosa paling presisi. H unggul tipis di K5 saja — kalah di kriteria yang lebih dulu. Margin 2)
- Klasemen: I 4-0, H 3-1, D 2-2, C 1-3, G 0-4.
- PEMENANG: I — "The graveyard keeper knows every name on every stone, and he greeted me by mine before I spoke. 'You're early,' he said, 'your stone isn't finished yet.'"
- Cek pre-mortem atas I: (a) bukan klise kanon — setting penjaga kuburan familiar tapi baris "your stone isn't finished yet" bukan cerita Reddit dikenal → lolos; (b) kalimat 2 tidak menjelaskan (tanpa kata ghost/dead/die, hanya fakta batu belum selesai) → lolos; (c) hapus kalimat 2 → kalimat 1 terasa aman; hapus kalimat 1 → kalimat 2 kehilangan konteks → lolos.
- Runner-up: H (disimpan di log bila iterasi lanjutan dibutuhkan).
