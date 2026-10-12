Mahasiswa mengajukan peminjaman peralatan dengan memilih alat,
jumlah, dan rentang waktu. Sistem memeriksa ketersediaan. Jika
tersedia dan data lengkap, sistem menyimpan pengajuan berstatus
menunggu keputusan. Pada tampilan konfirmasi, mahasiswa dapat
memilih mencetak bukti pengajuan. Petugas mengelola data peralatan
serta menyetujui atau menolak pengajuan. Kepala laboratorium melihat
laporan peminjaman.

ID          Kebutuhan
LAB-R01     Mahasiswa dapat melihat ketersediaan peralatan
LAB-R02     Petugas dapat mengelola data peralatan
LAB-R03     Mahasiswa dapat mengajukan peminjaman; sistem memeriksa ketersediaan sebelum menyimpa pengajuan
LAB-R04     Mahasiswa dapat mencetak bukti pada konfirmasi pengajuan jika memilihnya
LAB-R05     Petugas dapat menetapkan persetujuan atau penolakan pengajuan
LAB-R06     Kepala laboratorium dapat melihat laporan peminjaman

Batas sistem dan aturan:
• Sistem mencatat dan menyediakan informasi; perpindahan fisik alat tidak
terjadi di dalam perangkat lunak.
• Pengguna telah terautentikasi dan memiliki hak akses sesuai peran.
• Pengajuan yang diterima sistem berstatus Menunggu keputusan, bukan otomatis Disetujui. Pengajuan dengan peralatan tidak tersedia tidak disimpan sebagai pengajuan berhasil.
• Pencetakan bukti tidak menjadi syarat keberhasilan pengajuan.
• Persetujuan petugas belum dimodelkan sebagai reservasi teknis stok.
• Pengambilan, pengembalian, kondisi alat, dan denda belum dianalisis pada potongan model ini.

Aktor                   Tujuan terhadap sistem
Mahasiswa               Melihat ketersediaan, mengajukan peminjaman, dan mencetak bukti
Petugas laboratorium    Mengelola peralatan dan memproses keputusan
Kepala laboratorium     Melihat laporan peminjaman

# P03 — Kebutuhan Sistem Peminjaman Laboratorium

## 1. Studi Kasus

**Sistem Informasi Peminjaman dan Pengembalian Peralatan Laboratorium Kampus**

Skenario ini merupakan bahan latihan untuk menganalisis kebutuhan sistem peminjaman peralatan laboratorium.

Mahasiswa mengajukan peminjaman peralatan dengan memilih alat, jumlah, dan rentang waktu. Sistem memeriksa ketersediaan alat. Jika tersedia dan data lengkap, sistem menyimpan pengajuan dengan status Menunggu keputusan. Mahasiswa dapat mencetak bukti pengajuan pada tampilan konfirmasi. Petugas mengelola data peralatan serta menyetujui atau menolak pengajuan. Kepala laboratorium melihat laporan peminjaman.

## 2. Daftar Kebutuhan

| ID      | Kebutuhan                                                                                            |
| ------- | ---------------------------------------------------------------------------------------------------- |
| LAB-R01 | Mahasiswa dapat melihat ketersediaan peralatan.                                                      |
| LAB-R02 | Petugas dapat mengelola data peralatan.                                                              |
| LAB-R03 | Mahasiswa dapat mengajukan peminjaman dan sistem memeriksa ketersediaan sebelum menyimpan pengajuan. |
| LAB-R04 | Mahasiswa dapat mencetak bukti pada konfirmasi pengajuan jika memilihnya.                            |
| LAB-R05 | Petugas dapat menyetujui atau menolak pengajuan.                                                     |
| LAB-R06 | Kepala laboratorium dapat melihat laporan peminjaman.                                                |

## 3. Aturan dan Batas Sistem

1. Sistem hanya mencatat dan menyediakan informasi. Perpindahan fisik alat tidak dilakukan oleh perangkat lunak.
2. Pengguna sudah terautentikasi dan memiliki hak akses sesuai perannya.
3. Pengajuan yang diterima sistem memiliki status Menunggu keputusan, bukan otomatis Disetujui.
4. Pengajuan untuk alat yang tidak tersedia tidak disimpan sebagai pengajuan berhasil.
5. Pencetakan bukti bukan syarat keberhasilan pengajuan.
6. Persetujuan petugas belum dimodelkan sebagai reservasi teknis stok.
7. Pengambilan, pengembalian, kondisi alat, dan denda belum dianalisis dalam model ini.

# P03 — Skenariogf Sistem Peminjaman Laboratorium

## Langkah 2 — Tentukan Aktor

| Aktor                | Tujuan terhadap sistem                                                |
| -------------------- | --------------------------------------------------------------------- |
| Mahasiswa            | Melihat ketersediaan alat, mengajukan peminjaman, dan mencetak bukti. |
| Petugas laboratorium | Mengelola data peralatan dan memproses pengajuan peminjaman.          |
| Kepala laboratorium  | Melihat laporan peminjaman.                                           |

## Langkah 4 — Tetapkan Relasi

### 1. Relasi Include

LAB-UC03 «include» LAB-UC04

**Alasan:** Pemeriksaan ketersediaan menjadi bagian wajib saat mahasiswa mengajukan peminjaman. Sistem harus memeriksa alat, jumlah, dan waktu sebelum pengajuan disimpan.

### 2. Relasi Extend

LAB-UC05 «extend» LAB-UC03

**Alasan:** Cetak bukti merupakan fitur tambahan yang bisa dipilih mahasiswa setelah pengajuan berhasil dilakukan. Pengajuan tetap berhasil meskipun mahasiswa tidak mencetak bukti.

### Kesimpulan

Sistem peminjaman laboratorium memiliki tiga aktor dan tujuh use case. Pemeriksaan ketersediaan wajib dilakukan saat pengajuan, sedangkan pencetakan bukti bersifat opsional.
