# Skenario Use Case SIA — Pertemuan 5

Nama: Wildan Sonhajul M.
NIM: 2406019
Kelas: Informatika A

## SIA-UC08 — Input Nilai Mata Kuliah

| Komponen | Keterangan |
|---|---|
| Nama use case | Input Nilai Mata Kuliah |
| Aktor | Dosen dan Admin Akademik |
| Tujuan | Mencatat nilai mata kuliah hingga diperiksa dan disahkan. |
| Kondisi awal | Dosen telah masuk ke sistem dan memiliki akses pengisian nilai mata kuliah yang diampu. |
| Kondisi akhir | Nilai lengkap telah disahkan oleh Admin Akademik dan siap dipublikasikan. |

### Skenario Normal

| Langkah | Kegiatan Aktor | Respons Sistem |
|---|---|---|
| 1 | Dosen membuka menu Input Nilai Mata Kuliah. | Menampilkan mata kuliah yang diampu. |
| 2 | Dosen memilih mata kuliah. | Menampilkan daftar mahasiswa dan formulir nilai. |
| 3 | Dosen memasukkan nilai mata kuliah. | Menerima nilai yang dimasukkan. |
| 4 | Dosen menyimpan nilai. | Menyimpan nilai dan memeriksa kelengkapannya. |
| 5 | Admin Akademik memeriksa nilai yang sudah lengkap. | Menampilkan data nilai untuk diperiksa. |
| 6 | Admin Akademik mengesahkan nilai. | Menyimpan pengesahan dan menyiapkan publikasi hasil studi. |

### Skenario Alternatif

| Langkah | Kondisi | Respons Sistem dan Tindak Lanjut |
|---|---|---|
| 4a | Nilai belum lengkap. | Sistem menampilkan informasi nilai yang belum lengkap. Dosen melengkapi nilai, lalu menyimpan kembali. Sistem memeriksa ulang sampai nilai lengkap sebelum diteruskan ke Admin Akademik. |

## SIA-UC09 — Lihat KHS

| Komponen | Keterangan |
|---|---|
| Nama use case | Lihat KHS |
| Aktor | Mahasiswa |
| Tujuan | Melihat Kartu Hasil Studi yang telah diterbitkan. |
| Kondisi awal | Nilai telah disahkan oleh Admin Akademik dan sistem telah menyiapkan publikasi hasil studi. |
| Kondisi akhir | Mahasiswa melihat KHS pada portal akademik. |

### Skenario Normal

| Langkah | Kegiatan Aktor | Respons Sistem |
|---|---|---|
| 1 | — | Menerbitkan KHS pada portal akademik dan mengirim pemberitahuan hasil studi kepada mahasiswa secara paralel. |
| 2 | — | Menyelesaikan kedua proses tersebut sebelum melanjutkan layanan melihat KHS. |
| 3 | Mahasiswa membuka portal akademik dan memilih menu Lihat KHS. | Menampilkan pilihan semester. |
| 4 | Mahasiswa memilih semester. | Menampilkan KHS semester yang dipilih. |
| 5 | Mahasiswa melihat KHS. | — |