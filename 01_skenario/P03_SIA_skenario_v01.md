# Kebutuhan Sistem Informasi Akademik

## 1. Kebutuhan Fungsional

| ID | Kebutuhan |
|---|---|
| SIA-R03 | Mahasiswa memiliki kemampuan untuk mengajukan KRS. |
| SIA-R04 | Sistem melakukan pemeriksaan validitas KRS dalam proses pengajuan. |
| SIA-R05 | Mahasiswa dapat mengunduh bukti pengajuan apabila memilih opsi tersebut saat konfirmasi pengajuan. |
| SIA-R06 | Dosen wali dapat menentukan persetujuan atau penolakan terhadap pengajuan KRS. |

## 2. Kebutuhan dari Pertemuan Sebelumnya

| ID | Kebutuhan |
|---|---|
| SIA-R01 | Mahasiswa dapat mengakses informasi jadwal perkuliahan. |
| SIA-R02 | Admin akademik memiliki wewenang untuk mengatur jadwal kuliah. |

## 3. Batasan dan Asumsi Sistem

1. Pengguna sudah berhasil melakukan autentikasi.
2. Informasi mata kuliah, persyaratan mata kuliah, dan jadwal perkuliahan telah tersedia.
3. Apabila validasi tidak berhasil, pengajuan belum dianggap berhasil disimpan.
4. Pengunduhan bukti tidak menjadi ketentuan wajib agar pengajuan dinyatakan berhasil.
5. Pengajuan KRS yang sudah tersimpan masih memerlukan persetujuan dosen wali.
6. Proses pembayaran, pengelolaan nilai, dan penerapan basis data tidak termasuk dalam ruang lingkup tugas.

## 4. Alur Utama Sistem

1. Mahasiswa menentukan mata kuliah yang ingin diajukan.
2. Sistem memeriksa kelengkapan data, persyaratan mata kuliah, serta kemungkinan benturan jadwal.
3. Apabila seluruh pemeriksaan berhasil, sistem menyimpan pengajuan KRS dengan status menunggu persetujuan dosen wali.
4. Sistem memberikan informasi bahwa pengajuan telah berhasil disimpan.
5. Mahasiswa menentukan apakah bukti pengajuan akan diunduh.
6. Dosen wali memiliki kewenangan untuk menyetujui atau menolak pengajuan KRS disertai catatan keputusan.

## Langkah 2 — Identifikasi Aktor dan Use Case

### A. Daftar Aktor

| No. | Nama Aktor | Deskripsi |
|---|---|---|
| 1 | Mahasiswa | Mengirimkan pengajuan KRS dan menentukan apakah bukti pengajuan perlu diunduh. |
| 2 | Dosen Wali | Menilai pengajuan KRS, menetapkan persetujuan atau penolakan, serta menyertakan catatan keputusan. |

### B. Katalog Use Case

| ID | Nama Fungsi | Aktor Terkait | Sumber Kebutuhan |
|---|---|---|---|
| UC-01 | Ajukan KRS | Mahasiswa | SIA-R03 |
| UC-02 | Validasi KRS | Sistem, sebagai bagian dari pengajuan oleh Mahasiswa | SIA-R04 |
| UC-03 | Unduh Bukti Pengajuan | Mahasiswa | SIA-R05 |
| UC-04 | Proses Keputusan KRS | Dosen Wali | SIA-R06 |

### C. Batas Identifikasi

Pengenalan aktor dan use case dibatasi pada kegiatan pengajuan KRS, pemeriksaan validitas pengajuan, pengunduhan bukti, serta penetapan keputusan oleh dosen wali. SIA-R01 dan SIA-R02 tetap digunakan dengan identitas awalnya sebagai kebutuhan dari Pertemuan 2, tetapi keduanya tidak dicantumkan sebagai fungsi utama dalam katalog use case ini.

## Langkah 3 — Menentukan Include

### Relasi Include

- **Sumber:** UC-01 — Ajukan KRS.
- **Tujuan:** UC-02 — Validasi KRS.
- **Proses yang disertakan:** Pemeriksaan kelengkapan pengajuan, persyaratan mata kuliah, dan kemungkinan benturan jadwal.

### Alasan Penggunaan Relasi

Relasi `<<include>>` diterapkan karena validasi merupakan tahapan wajib dalam setiap proses pengajuan KRS. Apabila hasil pemeriksaan menunjukkan adanya ketidaksesuaian, pengajuan tidak dapat dinyatakan berhasil disimpan.

## Langkah 4 — Menentukan Extend

### Relasi Extend

- **Sumber:** UC-03 — Unduh Bukti Pengajuan.
- **Tujuan:** UC-01 — Ajukan KRS.
- **Kondisi:** Pengajuan KRS sudah berhasil disimpan, sistem telah menampilkan konfirmasi penyimpanan, dan mahasiswa memilih opsi untuk mengunduh bukti.
- **Perilaku tambahan:** Sistem menyiapkan bukti pengajuan agar dapat diunduh oleh mahasiswa.

### Alasan Penggunaan Relasi

Relasi `<<extend>>` digunakan karena pengunduhan bukti merupakan aktivitas tambahan yang tidak wajib dilakukan dalam pengajuan KRS. Mahasiswa bebas menentukan apakah ingin mengunduh bukti atau melewati pilihan tersebut. Dengan demikian, pengajuan yang sudah berhasil disimpan tetap dinyatakan berhasil meskipun mahasiswa tidak mengunduh buktinya.

## Langkah 5 — Deskripsi Use Case

### UC-01 — Ajukan KRS

**Aktor:** Mahasiswa

**Tujuan:** Mengirimkan rencana pengambilan mata kuliah untuk memperoleh persetujuan dari dosen wali.

**Prasyarat:**

- Mahasiswa sudah terautentikasi.
- Informasi mata kuliah dan jadwal perkuliahan tersedia.

**Alur Utama:**

1. Mahasiswa menentukan mata kuliah yang akan dimasukkan ke dalam pengajuan KRS.
2. Mahasiswa mengirimkan pengajuan KRS kepada sistem.
3. Sistem melakukan pemeriksaan melalui UC-02 Validasi KRS.
4. Jika pemeriksaan berhasil, sistem menyimpan pengajuan dengan status menunggu persetujuan dosen wali.
5. Sistem menampilkan pemberitahuan bahwa pengajuan berhasil disimpan.
6. Mahasiswa memiliki pilihan untuk mengunduh bukti pengajuan melalui UC-03.

**Alur Alternatif:**

- Apabila pemeriksaan tidak berhasil, sistem menampilkan keterangan mengenai kegagalan tersebut dan pengajuan belum dinyatakan berhasil tersimpan.

**Pascakondisi:**

- Jika proses berhasil, pengajuan KRS tersimpan dengan status menunggu persetujuan dosen wali.
- Jika proses gagal, pengajuan belum berhasil disimpan.

### UC-02 — Validasi KRS

**Aktor:** Sistem, sebagai bagian dari UC-01.

**Tujuan:** Memastikan bahwa pengajuan KRS telah memenuhi ketentuan yang berlaku.

**Prasyarat:**

- Mahasiswa telah menentukan mata kuliah yang akan diajukan.
- Data mata kuliah, persyaratan, dan jadwal perkuliahan tersedia.

**Alur Utama:**

1. Sistem memeriksa apakah data pengajuan sudah lengkap.
2. Sistem memverifikasi persyaratan mata kuliah yang dipilih.
3. Sistem mengecek apakah terdapat jadwal kuliah yang saling berbenturan.
4. Jika seluruh pemeriksaan terpenuhi, sistem menetapkan hasil validasi sebagai berhasil.

**Alur Alternatif:**

- Apabila terdapat pemeriksaan yang tidak terpenuhi, sistem menetapkan validasi sebagai gagal dan menyampaikan penyebabnya.

**Pascakondisi:**

- Hasil pemeriksaan tersedia sebagai dasar untuk menentukan apakah pengajuan KRS dapat disimpan.

### UC-03 — Unduh Bukti Pengajuan

**Aktor:** Mahasiswa.

**Tujuan:** Memperoleh dokumen atau bukti atas pengajuan KRS yang telah dilakukan.

**Prasyarat:**

- Pengajuan KRS sudah berhasil disimpan.
- Sistem telah menampilkan konfirmasi penyimpanan.

**Alur Utama:**

1. Sistem memberikan opsi untuk mengunduh bukti pengajuan.
2. Mahasiswa memilih opsi pengunduhan.
3. Sistem menyiapkan bukti pengajuan agar dapat diunduh.

**Alur Alternatif:**

- Jika mahasiswa melewati opsi pengunduhan, proses pengajuan KRS tetap dinyatakan berhasil.
- Apabila bukti tidak berhasil disediakan, pengajuan yang sudah tersimpan tetap dipertahankan.

**Pascakondisi:**

- Bukti pengajuan tersedia untuk diunduh apabila proses pengunduhan berhasil.
- Aktivitas mengunduh bukti tidak mengubah status pengajuan KRS.

### UC-04 — Proses Keputusan KRS

**Aktor:** Dosen Wali.

**Tujuan:** Menetapkan keputusan atas pengajuan KRS melalui persetujuan atau penolakan.

**Prasyarat:**

- Pengajuan KRS sudah tersimpan dalam sistem.
- Status pengajuan masih menunggu persetujuan dosen wali.

**Alur Utama:**

1. Dosen wali membuka data pengajuan KRS milik mahasiswa.
2. Dosen wali meninjau isi pengajuan tersebut.
3. Dosen wali menentukan apakah pengajuan disetujui atau ditolak.
4. Dosen wali menambahkan catatan yang menjelaskan keputusan.
5. Sistem menyimpan keputusan beserta catatan yang diberikan.

**Alur Alternatif:**

- Apabila data pengajuan belum tersedia atau belum memenuhi kondisi untuk diproses, sistem belum dapat mencatat keputusan.

**Pascakondisi:**

- Keputusan persetujuan atau penolakan beserta catatan dari dosen wali telah tercatat pada pengajuan KRS.

## Langkah 6 — Menggambar Diagram Use Case

Diagram use case dibuat dengan melibatkan dua aktor dan empat use case berikut.

| Jenis | Nama |
|---|---|
| Aktor | Mahasiswa |
| Aktor | Dosen Wali |
| Use Case | UC-01 — Ajukan KRS |
| Use Case | UC-02 — Validasi KRS |
| Use Case | UC-03 — Unduh Bukti Pengajuan |
| Use Case | UC-04 — Proses Keputusan KRS |

## Langkah 7 — Pengujian Konsistensi

### a. Validasi Berhasil, tetapi Mahasiswa Tidak Mengunduh Bukti

Pemeriksaan KRS dinyatakan berhasil karena seluruh persyaratan telah terpenuhi. Sistem kemudian menyimpan pengajuan dengan status menunggu persetujuan dosen wali dan menampilkan konfirmasi penyimpanan. Mahasiswa memutuskan untuk tidak mengunduh bukti sehingga aktivitas pengunduhan tidak dijalankan.

**Hasil pengujian:** Konsisten. UC-01 Ajukan KRS tetap berhasil meskipun UC-03 Unduh Bukti Pengajuan tidak dijalankan. Hal ini sesuai dengan relasi `<<extend>>` karena pengunduhan bukti bersifat opsional.

### b. Validasi Gagal

Pemeriksaan KRS tidak berhasil karena terdapat persyaratan yang belum terpenuhi, seperti jadwal kuliah yang berbenturan atau prasyarat mata kuliah yang belum dipenuhi. Sistem memberikan informasi mengenai kegagalan tersebut dan tidak menyimpan pengajuan sebagai pengajuan yang berhasil.

**Hasil pengujian:** Konsisten. UC-02 Validasi KRS merupakan tahapan wajib melalui relasi `<<include>>` dalam UC-01 Ajukan KRS. Jika pemeriksaan gagal, proses tidak berlanjut ke penyimpanan yang berhasil. Oleh karena itu, mahasiswa tidak dapat mengunduh bukti dari pengajuan yang belum berhasil disimpan.

### c. Validasi Berhasil dan Mahasiswa Memilih Mengunduh Bukti

Pemeriksaan KRS berhasil dilakukan, kemudian sistem menyimpan pengajuan dengan status menunggu persetujuan dosen wali. Setelah konfirmasi penyimpanan ditampilkan, mahasiswa memilih untuk mengunduh bukti. Sistem selanjutnya menyediakan bukti pengajuan tersebut.

**Hasil pengujian:** Konsisten. UC-03 Unduh Bukti Pengajuan dapat dijalankan sebagai aktivitas tambahan melalui relasi `<<extend>>` apabila mahasiswa memilih opsi pengunduhan setelah pengajuan berhasil disimpan.

### Kesimpulan Uji Konsistensi

Dari ketiga skenario pengujian tersebut, diagram dan deskripsi use case menunjukkan kesesuaian. Validasi menjadi tahapan wajib dalam pengajuan KRS, sedangkan pengunduhan bukti hanya dilakukan apabila pengajuan berhasil disimpan dan mahasiswa memilih opsi tersebut. Pengajuan yang berhasil disimpan tetap berstatus menunggu persetujuan dosen wali sampai keputusan diberikan.