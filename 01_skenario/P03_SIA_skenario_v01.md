# Kebutuhan Sistem Informasi Akademik

## 1. Kebutuhan Fungsional

| ID      | Kebutuhan                                                                  |
| ------- | -------------------------------------------------------------------------- |
| SIA-R03 | Mahasiswa dapat mengajukan KRS.                                            |
| SIA-R04 | Sistem memvalidasi KRS sebagai bagian dari pengajuan.                      |
| SIA-R05 | Mahasiswa dapat mengunduh bukti jika memilihnya pada konfirmasi pengajuan. |
| SIA-R06 | Dosen wali dapat memproses persetujuan atau penolakan KRS.                 |

## 2. Kebutuhan dari Pertemuan Sebelumnya

| ID      | Kebutuhan                                     |
| ------- | --------------------------------------------- |
| SIA-R01 | Mahasiswa dapat melihat jadwal kuliah.        |
| SIA-R02 | Admin akademik dapat mengelola jadwal kuliah. |

## 3. Batas dan Asumsi

1. Pengguna telah terautentikasi.
2. Data mata kuliah, prasyarat, dan jadwal tersedia.
3. Validasi yang gagal menyebabkan pengajuan belum berhasil tersimpan.
4. Unduh bukti bukan syarat keberhasilan pengajuan.
5. KRS yang tersimpan belum berarti disetujui dosen wali.
6. Pembayaran, pengisian nilai, dan implementasi basis data berada di luar tugas.

## 4. Alur Utama

1. Mahasiswa memilih mata kuliah.
2. Sistem memvalidasi kelengkapan, prasyarat, dan benturan jadwal.
3. Jika validasi berhasil, sistem menyimpan pengajuan KRS dengan status menunggu persetujuan dosen wali.
4. Sistem menampilkan konfirmasi penyimpanan.
5. Mahasiswa memilih apakah akan mengunduh bukti pengajuan.
6. Dosen wali dapat menyetujui atau menolak KRS dan memberikan catatan keputusan.

## Langkah 2 — Identifikasi Aktor dan Use Case

### A. Daftar Aktor

| No. | Nama Aktor | Deskripsi                                                                    |
| --- | ---------- | ---------------------------------------------------------------------------- |
| 1   | Mahasiswa  | Mengajukan KRS dan memilih untuk mengunduh bukti pengajuan.                  |
| 2   | Dosen Wali | Memproses persetujuan atau penolakan KRS serta memberikan catatan keputusan. |

### B. Katalog Use Case

| ID    | Nama Fungsi           | Aktor Terkait                                   | Sumber Kebutuhan |
| ----- | --------------------- | ----------------------------------------------- | ---------------- |
| UC-01 | Ajukan KRS            | Mahasiswa                                       | SIA-R03          |
| UC-02 | Validasi KRS          | Sistem, sebagai bagian dari pengajuan Mahasiswa | SIA-R04          |
| UC-03 | Unduh Bukti Pengajuan | Mahasiswa                                       | SIA-R05          |
| UC-04 | Proses Keputusan KRS  | Dosen Wali                                      | SIA-R06          |

### C. Batas Identifikasi

Identifikasi aktor dan use case difokuskan pada proses pengajuan KRS, validasi pengajuan, pengunduhan bukti, serta pemrosesan keputusan oleh dosen wali. Kebutuhan SIA-R01 dan SIA-R02 tetap dipertahankan dengan ID aslinya sebagai kebutuhan dari Pertemuan 2, tetapi tidak dimasukkan sebagai fungsi utama pada katalog ini.

## Langkah 3 — Menentukan Include

### Relasi Include

- **Sumber:** UC-01 — Ajukan KRS
- **Tujuan:** UC-02 — Validasi KRS
- **Perilaku yang disertakan:** Memeriksa kelengkapan pengajuan, prasyarat mata kuliah, dan benturan jadwal.

### Alasan Relasi

Relasi `<<include>>` digunakan karena validasi merupakan proses wajib yang harus dilakukan setiap kali mahasiswa mengajukan KRS. Jika validasi gagal, pengajuan belum berhasil tersimpan.

## Langkah 4 — Menentukan Extend

### Relasi Extend

- **Sumber:** UC-03 — Unduh Bukti Pengajuan
- **Tujuan:** UC-01 — Ajukan KRS
- **Kondisi:** Pengajuan KRS berhasil disimpan, konfirmasi penyimpanan ditampilkan, dan mahasiswa memilih untuk mengunduh bukti.
- **Perilaku tambahan:** Sistem menyediakan bukti pengajuan untuk diunduh oleh mahasiswa.

### Alasan Relasi

Relasi `<<extend>>` digunakan karena pengunduhan bukti bukan proses wajib dalam pengajuan KRS. Mahasiswa dapat memilih untuk mengunduh bukti atau tidak. Jika mahasiswa tidak memilih unduh bukti, pengajuan yang berhasil disimpan tetap dianggap berhasil.

## Langkah 5 — Deskripsi Use Case

### UC-01 — Ajukan KRS

**Aktor:** Mahasiswa

**Tujuan:** Mengajukan rencana mata kuliah untuk mendapatkan persetujuan dosen wali.

**Prasyarat:**

- Mahasiswa telah terautentikasi.
- Data mata kuliah dan jadwal tersedia.

**Alur Utama:**

1. Mahasiswa memilih mata kuliah yang akan diajukan.
2. Mahasiswa mengirim pengajuan KRS.
3. Sistem menjalankan validasi KRS melalui UC-02.
4. Jika validasi berhasil, sistem menyimpan pengajuan dengan status menunggu persetujuan dosen wali.
5. Sistem menampilkan konfirmasi bahwa pengajuan berhasil disimpan.
6. Mahasiswa dapat memilih untuk mengunduh bukti pengajuan melalui UC-03.

**Alur Alternatif:**

- Jika validasi gagal, sistem menampilkan informasi kegagalan dan pengajuan belum berhasil tersimpan.

**Pascakondisi:**

- Jika berhasil, pengajuan KRS tersimpan dengan status menunggu persetujuan dosen wali.
- Jika gagal, pengajuan belum berhasil tersimpan.

### UC-02 — Validasi KRS

**Aktor:** Sistem, sebagai bagian dari UC-01.

**Tujuan:** Memeriksa apakah pengajuan KRS memenuhi ketentuan yang ditetapkan.

**Prasyarat:**

- Mahasiswa telah memilih mata kuliah.
- Data mata kuliah, prasyarat, dan jadwal tersedia.

**Alur Utama:**

1. Sistem memeriksa kelengkapan pengajuan.
2. Sistem memeriksa prasyarat mata kuliah.
3. Sistem memeriksa benturan jadwal.
4. Jika seluruh pemeriksaan terpenuhi, sistem menyatakan validasi berhasil.

**Alur Alternatif:**

- Jika salah satu pemeriksaan gagal, sistem menyatakan validasi gagal dan menampilkan informasi penyebabnya.

**Pascakondisi:**

- Hasil validasi tersedia untuk menentukan apakah pengajuan dapat disimpan.

### UC-03 — Unduh Bukti Pengajuan

**Aktor:** Mahasiswa.

**Tujuan:** Mendapatkan bukti pengajuan KRS.

**Prasyarat:**

- Pengajuan KRS berhasil disimpan.
- Konfirmasi penyimpanan telah ditampilkan.

**Alur Utama:**

1. Sistem menampilkan pilihan untuk mengunduh bukti pengajuan.
2. Mahasiswa memilih opsi unduh.
3. Sistem menyediakan bukti pengajuan untuk diunduh.

**Alur Alternatif:**

- Jika mahasiswa tidak memilih opsi unduh, proses pengajuan tetap berhasil.
- Jika bukti gagal disediakan, pengajuan yang telah tersimpan tidak dibatalkan.

**Pascakondisi:**

- Bukti tersedia untuk diunduh jika proses berhasil.
- Status pengajuan tidak berubah hanya karena aktivitas unduh bukti.

### UC-04 — Proses Keputusan KRS

**Aktor:** Dosen Wali.

**Tujuan:** Memproses pengajuan KRS melalui persetujuan atau penolakan.

**Prasyarat:**

- Pengajuan KRS telah tersimpan.
- Status pengajuan menunggu persetujuan dosen wali.

**Alur Utama:**

1. Dosen wali membuka pengajuan KRS mahasiswa.
2. Dosen wali memeriksa pengajuan.
3. Dosen wali memilih menyetujui atau menolak KRS.
4. Dosen wali memberikan catatan keputusan.
5. Sistem mencatat keputusan dan catatan tersebut.

**Alur Alternatif:**

- Jika pengajuan belum tersedia atau belum dapat diproses, keputusan belum dapat dicatat.

**Pascakondisi:**

- Keputusan persetujuan atau penolakan beserta catatan dosen wali tercatat pada pengajuan.

## Langkah 6 — Gambar Diagram Usecase

Disini saya akan menggunakan dua aktor dan empat use case berikut:

| Jenis   | Nama                          |
| ------- | ----------------------------- |
| Aktor   | Mahasiswa                     |
| Aktor   | Dosen Wali                    |
| Usecase | UC-01 - Ajukan KRS            |
| Usecase | UC-02 - Validasi KRS          |
| Usecase | UC-03 - Unduh Bukti Pengajuan |
| Usecase | UC-04 - Proses Keputusan KRS  |

## Langkah 7 — Uji Konsistensi

### a. Validasi berhasil dan mahasiswa tidak mengunduh bukti

Validasi KRS berhasil karena semua persyaratan terpenuhi. Sistem menyimpan pengajuan KRS dengan status menunggu persetujuan dosen wali dan menampilkan konfirmasi. Mahasiswa tidak memilih untuk mengunduh bukti, sehingga proses pengunduhan tidak dilakukan.

**Hasil pengujian:** Konsisten. Use case `UC-01 Ajukan KRS` tetap berhasil meskipun `UC-03 Unduh Bukti Pengajuan` tidak dijalankan, karena pengunduhan merupakan proses opsional (`<<extend>>`).

### b. Validasi gagal

Validasi KRS gagal karena terdapat persyaratan yang tidak terpenuhi, misalnya jadwal kuliah bentrok atau prasyarat mata kuliah belum terpenuhi. Sistem menampilkan pesan kegagalan dan pengajuan KRS tidak disimpan sebagai pengajuan yang berhasil.

**Hasil pengujian:** Konsisten. Use case `UC-02 Validasi KRS` merupakan bagian wajib (`<<include>>`) dari `UC-01 Ajukan KRS`. Jika validasi gagal, proses pengajuan tidak dilanjutkan ke penyimpanan yang berhasil dan mahasiswa tidak dapat mengunduh bukti pengajuan yang berhasil.

### c. Validasi berhasil dan mahasiswa memilih mengunduh bukti

Validasi KRS berhasil dan sistem menyimpan pengajuan dengan status menunggu persetujuan dosen wali. Setelah konfirmasi ditampilkan, mahasiswa memilih untuk mengunduh bukti pengajuan dan sistem menyediakan bukti tersebut.

**Hasil pengujian:** Konsisten. `UC-03 Unduh Bukti Pengajuan` dapat dijalankan sebagai proses tambahan (`<<extend>>`) ketika mahasiswa memilih mengunduh bukti setelah pengajuan berhasil disimpan.

### Kesimpulan Uji Konsistensi

Ketiga situasi menunjukkan bahwa diagram dan deskripsi use case sudah konsisten. Validasi selalu menjadi bagian wajib dari pengajuan KRS, sedangkan pengunduhan bukti hanya dilakukan jika pengajuan berhasil dan mahasiswa memilihnya. Status pengajuan yang berhasil disimpan tetap menunggu persetujuan dosen wali, bukan langsung disetujui.
