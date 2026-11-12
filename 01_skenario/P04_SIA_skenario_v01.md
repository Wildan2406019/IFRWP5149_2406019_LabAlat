# Pertemuan 4 — Sistem Informasi Akademik, Layanan Hasil Studi

## Langkah 1 — Catat kebutuhan dan batas

Tugas ini berbeda dari tugas pertemuan sebelumnya. Tugas Pertemuan 2
adalah jadwal kuliah dan tugas Pertemuan 3 adalah pengajuan KRS. Tugas
Pertemuan 4 adalah layanan hasil studi, dengan teknik generalization dan
collaboration yang sama seperti studi kasus, tetapi diterapkan pada skenario
baru tanpa contoh jawaban.
Skenario tugas berikut fiktif untuk praktikum dan berbeda dari tugas
Pertemuan 2 (jadwal kuliah) dan Pertemuan 3 (pengajuan KRS).
Mahasiswa dan dosen sama-sama merupakan Civitas Akademika yang
dapat melihat kalender akademik. Dosen menginput nilai mata kuliah yang
diampunya setelah masa perkuliahan berakhir. Mahasiswa melihat Kartu
Hasil Studi (KHS) untuk semester yang nilainya sudah dipublikasikan. Admin
Akademik mengelola data mahasiswa: menambah data mahasiswa baru,
mengubah data mahasiswa, dan menghapus data mahasiswa. Dua use case
utama, Input Nilai Mata Kuliah dan Lihat KHS, ditunjukkan realisasinya oleh
collaboration yang bersesuaian.

## Langkah 2 — Identifikasi Aktor dan Use Case

### A. Katalog Use Case

| ID       | Nama Use Case             | Aktor Terkait                  | Sumber Kebutuhan | Status |
| -------- | ------------------------- | ------------------------------ | ---------------- | ------ |
| SIA-UC01 | Lihat Jadwal Kuliah       | Mahasiswa                      | SIA-R01          | Tetap  |
| SIA-UC02 | Kelola Jadwal Kuliah      | Admin Akademik                 | SIA-R02          | Tetap  |
| SIA-UC03 | Ajukan KRS                | Mahasiswa                      | SIA-R03          | Tetap  |
| SIA-UC04 | Validasi KRS              | Sistem (bagian dari pengajuan) | SIA-R04          | Tetap  |
| SIA-UC05 | Unduh Bukti Pengajuan KRS | Mahasiswa                      | SIA-R05          | Tetap  |
| SIA-UC06 | Proses Keputusan KRS      | Dosen Wali                     | SIA-R06          | Tetap  |
| SIA-UC07 | Lihat Kalender Akademik   | Civitas Akademika              | SIA-R07          | Baru   |
| SIA-UC08 | Input Nilai Mata Kuliah   | Dosen                          | SIA-R08          | Baru   |
| SIA-UC09 | Lihat KHS                 | Mahasiswa                      | SIA-R09          | Baru   |
| SIA-UC10 | Kelola Data Mahasiswa     | Admin Akademik                 | SIA-R10          | Baru   |
| SIA-UC11 | Tambah Data Mahasiswa     | Admin Akademik                 | SIA-R11          | Baru   |
| SIA-UC12 | Ubah Data Mahasiswa       | Admin Akademik                 | SIA-R11          | Baru   |
| SIA-UC13 | Hapus Data Mahasiswa      | Admin Akademik                 | SIA-R11          | Baru   |

### B. Daftar Aktor

| Nama Aktor        | Jenis        | Keterangan                                                                               |
| ----------------- | ------------ | ---------------------------------------------------------------------------------------- |
| Civitas Akademika | Aktor umum   | Dapat melihat kalender akademik.                                                         |
| Mahasiswa         | Aktor khusus | Dapat melihat jadwal kuliah, mengajukan KRS, mengunduh bukti pengajuan, dan melihat KHS. |
| Dosen             | Aktor khusus | Dapat menginput nilai mata kuliah yang diampunya dan melihat kalender akademik.          |
| Admin Akademik    | Aktor utama  | Mengelola jadwal kuliah dan data mahasiswa.                                              |
| Dosen Wali        | Aktor utama  | Memproses keputusan pengajuan KRS mahasiswa.                                             |

### C. Catatan Identifikasi

Katalog use case menggabungkan fungsi dari Pertemuan 2 dan Pertemuan 3 dengan fungsi baru pada Pertemuan 4. ID SIA-UC01 sampai SIA-UC06 dipertahankan, sedangkan fungsi baru menggunakan ID SIA-UC07 sampai SIA-UC13.

Use case SIA-UC10 Kelola Data Mahasiswa merupakan fungsi umum, sedangkan SIA-UC11 Tambah Data Mahasiswa, SIA-UC12 Ubah Data Mahasiswa, dan SIA-UC13 Hapus Data Mahasiswa merupakan fungsi khusus. Hubungan generalization untuk aktor dan use case akan ditentukan pada langkah berikutnya.

## Langkah 3 — Tetapkan Generalization Aktor

### A. Hierarki Aktor

| Aktor Umum        | Aktor Khusus | Fungsi yang Diwarisi    | Alasan Pemodelan                                                                        |
| ----------------- | ------------ | ----------------------- | --------------------------------------------------------------------------------------- |
| Civitas Akademika | Mahasiswa    | Lihat Kalender Akademik | Mahasiswa merupakan bagian dari civitas akademika dan berhak melihat kalender akademik. |
| Civitas Akademika | Dosen        | Lihat Kalender Akademik | Dosen merupakan bagian dari civitas akademika dan berhak melihat kalender akademik.     |

### B. Penjelasan Generalization

Civitas Akademika ditetapkan sebagai aktor umum karena fungsi melihat kalender akademik dapat digunakan bersama oleh mahasiswa dan dosen. Mahasiswa dan Dosen menjadi aktor khusus yang mewarisi fungsi tersebut.

Dengan generalization, hubungan ke use case Lihat Kalender Akademik cukup digambarkan dari aktor umum Civitas Akademika. Mahasiswa dan Dosen mewarisi fungsi tersebut melalui hubungan generalization, sehingga tidak perlu dibuat hubungan asosiasi yang sama secara berulang.

## Langkah 4 — Tetapkan Generalization Use Case

### A. Hierarki Use Case

| Use Case Umum                  | Use Case Khusus                | Fungsi yang Diwarisi                   | Alasan Pemodelan                                                         |
| ------------------------------ | ------------------------------ | -------------------------------------- | ------------------------------------------------------------------------ |
| SIA-UC10 Kelola Data Mahasiswa | SIA-UC11 Tambah Data Mahasiswa | Fungsi umum pengelolaan data mahasiswa | Penambahan data merupakan salah satu bentuk pengelolaan data mahasiswa.  |
| SIA-UC10 Kelola Data Mahasiswa | SIA-UC12 Ubah Data Mahasiswa   | Fungsi umum pengelolaan data mahasiswa | Perubahan data merupakan salah satu bentuk pengelolaan data mahasiswa.   |
| SIA-UC10 Kelola Data Mahasiswa | SIA-UC13 Hapus Data Mahasiswa  | Fungsi umum pengelolaan data mahasiswa | Penghapusan data merupakan salah satu bentuk pengelolaan data mahasiswa. |

### B. Penjelasan Generalization

Use case SIA-UC10 Kelola Data Mahasiswa ditetapkan sebagai use case umum karena mewakili fungsi pengelolaan data mahasiswa secara keseluruhan. Use case tersebut memiliki tiga use case khusus, yaitu SIA-UC11 Tambah Data Mahasiswa, SIA-UC12 Ubah Data Mahasiswa, dan SIA-UC13 Hapus Data Mahasiswa.

Ketiga use case khusus tersebut merupakan bentuk pelaksanaan yang lebih spesifik dari pengelolaan data mahasiswa. Generalization digunakan agar hubungan antara fungsi umum dan fungsi khusus dapat ditampilkan secara terstruktur, sehingga model lebih mudah dipahami dan tidak perlu mengulang konsep pengelolaan data mahasiswa.

### C. Ketentuan Penggambaran

- SIA-UC10 Kelola Data Mahasiswa menjadi use case umum.
- SIA-UC11 Tambah Data Mahasiswa, SIA-UC12 Ubah Data Mahasiswa, dan SIA-UC13 Hapus Data Mahasiswa menjadi use case khusus.
- Hubungan generalization digambarkan dengan garis utuh dan ujung segitiga kosong yang mengarah ke use case umum SIA-UC10 Kelola Data Mahasiswa.

## Langkah 5 — Tetapkan Collaboration

### A. Daftar Collaboration

| ID Collaboration | Nama Collaboration      | Use Case yang Direalisasikan     | Aktor Terkait |
| ---------------- | ----------------------- | -------------------------------- | ------------- |
| SIA-CO01         | Input Nilai Mata Kuliah | SIA-UC08 Input Nilai Mata Kuliah | Dosen         |
| SIA-CO02         | Lihat KHS               | SIA-UC09 Lihat KHS               | Mahasiswa     |

### B. Penjelasan Collaboration

**1. SIA-CO01 — Input Nilai Mata Kuliah**

Collaboration ini merealisasikan use case Input Nilai Mata Kuliah. Dosen memilih mata kuliah yang diampunya, memasukkan nilai mahasiswa, kemudian sistem memeriksa dan menyimpan nilai tersebut sesuai ketentuan. Nilai yang belum dipublikasikan belum dapat dianggap sebagai nilai resmi yang dapat ditampilkan dalam KHS.

**2. SIA-CO02 — Lihat KHS**

Collaboration ini merealisasikan use case Lihat KHS. Mahasiswa memilih semester yang ingin dilihat, kemudian sistem memeriksa status publikasi nilai. Jika nilai semester tersebut sudah dipublikasikan, sistem menampilkan KHS. Jika belum dipublikasikan, sistem tidak menampilkan KHS sebagai hasil studi yang sudah tersedia.

### C. Hubungan Collaboration dengan Use Case

Setiap collaboration memiliki nama yang sama dengan use case yang direalisasikannya. SIA-CO01 merealisasikan SIA-UC08 Input Nilai Mata Kuliah, sedangkan SIA-CO02 merealisasikan SIA-UC09 Lihat KHS.

Kedua collaboration memiliki alur yang saling berkaitan. Nilai yang diinput dosen harus dipublikasikan sesuai ketentuan sebelum dapat ditampilkan kepada mahasiswa melalui KHS.

## Langkah 6 — Susun Use Case Description

<!-- Deskripsi Use Case — Input Nilai Mata Kuliah -->

### A. SIA-UC08 — Input Nilai Mata Kuliah

| Elemen        | Deskripsi                                                                             |
| ------------- | ------------------------------------------------------------------------------------- |
| ID Use Case   | SIA-UC08                                                                              |
| Nama Use Case | Input Nilai Mata Kuliah                                                               |
| Aktor Utama   | Dosen                                                                                 |
| Tujuan        | Memasukkan nilai mahasiswa untuk mata kuliah yang diampu dosen.                       |
| Prasyarat     | Dosen sudah login, memiliki hak akses, dan data mata kuliah serta mahasiswa tersedia. |
| Pemicu        | Dosen memilih fungsi input nilai mata kuliah.                                         |

**Alur Utama**

1. Dosen membuka menu input nilai mata kuliah.
2. Sistem menampilkan daftar mata kuliah yang diampu dosen.
3. Dosen memilih mata kuliah yang akan diinput nilainya.
4. Sistem menampilkan daftar mahasiswa yang mengikuti mata kuliah tersebut.
5. Dosen memasukkan nilai mahasiswa.
6. Dosen menyimpan nilai yang telah dimasukkan.
7. Sistem memeriksa kelengkapan dan validitas nilai.
8. Jika nilai valid, sistem menyimpan nilai dan menampilkan konfirmasi.

**Alur Alternatif**

- Jika nilai belum lengkap atau tidak valid, sistem menampilkan pesan kesalahan dan meminta dosen memperbaikinya.
- Jika penyimpanan gagal, sistem menampilkan pemberitahuan bahwa nilai belum berhasil disimpan.

**Pascakondisi**

- Jika berhasil, nilai tersimpan dalam sistem.
- Nilai belum otomatis dianggap telah dipublikasikan hanya karena berhasil disimpan.
- Jika gagal, perubahan nilai tidak dinyatakan berhasil disimpan.

<!-- Deskripsi Use Case — Lihat KHS -->

### B. SIA-UC09 — Lihat KHS

| Elemen        | Deskripsi                                                                          |
| ------------- | ---------------------------------------------------------------------------------- |
| ID Use Case   | SIA-UC09                                                                           |
| Nama Use Case | Lihat KHS                                                                          |
| Aktor Utama   | Mahasiswa                                                                          |
| Tujuan        | Melihat Kartu Hasil Studi untuk semester yang nilai-nilainya sudah dipublikasikan. |
| Prasyarat     | Mahasiswa sudah login dan memiliki data akademik pada semester yang dipilih.       |
| Pemicu        | Mahasiswa memilih menu Kartu Hasil Studi (KHS).                                    |

**Alur Utama**

1. Mahasiswa membuka menu KHS.
2. Sistem menampilkan pilihan semester yang tersedia.
3. Mahasiswa memilih semester yang ingin dilihat.
4. Sistem memeriksa status publikasi nilai pada semester tersebut.
5. Jika nilai sudah dipublikasikan, sistem mengambil data hasil studi mahasiswa.
6. Sistem menampilkan KHS untuk semester yang dipilih.

**Alur Alternatif**

- Jika nilai belum dipublikasikan, sistem menampilkan pemberitahuan bahwa KHS belum tersedia.
- Jika mahasiswa belum memiliki data akademik pada semester tersebut, sistem menampilkan pemberitahuan bahwa data KHS belum tersedia.
- Jika terjadi kesalahan saat mengambil data, sistem menampilkan pesan bahwa KHS belum dapat ditampilkan.

**Pascakondisi**

- Jika berhasil, KHS semester yang dipilih ditampilkan kepada mahasiswa.
- Jika nilai belum dipublikasikan, KHS tidak ditampilkan sebagai hasil studi yang sudah tersedia.
- Proses melihat KHS tidak mengubah nilai akademik mahasiswa.

## Langkah 7 — Gambar Diagram

Gambar diagram kumulatif dengan cara yang sama seperti Langkah 8 pada studi
kasus. Mulai dari salinan diagram SIA Pertemuan 3 (berkas asli tidak diubah),
lalu tambahkan bertahap: aktor umum dan aktor khusus beserta generalization
aktor, use case layanan hasil studi, use case pengelolaan data mahasiswa
beserta generalization use case, dan terakhir dua collaboration beserta
realization. Simpan hasilnya pada folder 04*model_analisis/P04/SIA/ dengan
nama P04*<2406020>\_SIA_notasi_usecase_v01.drawio beserta ekspor PNG dengan versi
yang sama. Diagram akhir memuat fungsi jadwal, fungsi KRS, dan fungsi hasil
studi dalam satu diagram Sistem Informasi Akademik.

# Langkah 8 — Uji Konsistensi, Review, dan Revisi

## A. Uji Konsistensi

### Situasi A — Mahasiswa melihat kalender akademik tanpa asosiasi langsung

**Hasil pengujian:** Mahasiswa tetap dapat melihat kalender akademik karena merupakan aktor khusus dari Civitas Akademika. Melalui hubungan generalization, Mahasiswa mewarisi fungsi yang dimiliki aktor umum, sehingga tidak harus memiliki asosiasi langsung dengan use case Lihat Kalender Akademik.

**Kesimpulan:** Konsisten jika generalization aktor digambarkan dengan benar dan Mahasiswa mewarisi fungsi dari Civitas Akademika.

### Situasi B — Dosen yang bukan pengampu mencoba menginput nilai

**Hasil pengujian:** Sistem menolak akses penginputan nilai karena dosen tersebut tidak mengampu mata kuliah yang dipilih. Sistem menampilkan pemberitahuan bahwa dosen tidak memiliki hak untuk menginput nilai pada mata kuliah tersebut.

**Kesimpulan:** Konsisten dengan aturan bahwa dosen hanya dapat menginput nilai mata kuliah yang diampunya.

### Situasi C — Admin menghapus data mahasiswa yang masih memiliki data akademik aktif

**Hasil pengujian:** Sistem menolak penghapusan data mahasiswa karena mahasiswa tersebut masih memiliki data akademik aktif. Sistem menampilkan alasan penolakan agar data akademik tetap terjaga.

**Kesimpulan:** Konsisten dengan batasan tugas bahwa data mahasiswa yang masih memiliki data akademik aktif tidak boleh dihapus.

<!-- Riview & Revisi disimpan di folder 06_laporan/P04_2406020_jobsheet_review_v01.md -->
