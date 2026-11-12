# Skenario Use Case LAB — Pertemuan 5

Nama: Wildan Sonhajul M.
NIM: 2406019
Kelas: Informatika A

## LAB-UC01 — Lihat Ketersediaan Peralatan

| Komponen | Keterangan |
|---|---|
| Nama use case | Lihat Ketersediaan Peralatan |
| Aktor | Peminjam |
| Tujuan | Mengetahui ketersediaan peralatan laboratorium sebelum mengajukan peminjaman. |
| Kondisi awal | Peminjam telah mengakses sistem. |
| Kondisi akhir | Informasi ketersediaan peralatan atau pesan tidak ada peralatan ditampilkan. |

### Skenario Normal

| Langkah | Kegiatan Aktor | Respons Sistem |
|---|---|---|
| 1 | Membuka menu Lihat Ketersediaan Peralatan. | Menampilkan halaman ketersediaan peralatan. |
| 2 | Meminta informasi ketersediaan peralatan. | Memeriksa data peralatan. |
| 3 | Melihat informasi peralatan. | Menampilkan daftar peralatan beserta status ketersediaannya. |

### Skenario Alternatif

| Langkah | Kondisi | Respons Sistem |
|---|---|---|
| 2a | Tidak ada data peralatan. | Menampilkan pesan bahwa data peralatan belum tersedia. |

## LAB-UC02 — Kelola Data Peralatan

| Komponen | Keterangan |
|---|---|
| Nama use case | Kelola Data Peralatan |
| Aktor | Petugas Laboratorium |
| Tujuan | Menambah, mengubah, atau menghapus data peralatan laboratorium. |
| Kondisi awal | Petugas Laboratorium telah masuk ke sistem. |
| Kondisi akhir | Perubahan data tersimpan atau sistem menampilkan alasan perubahan ditolak. |

### Skenario Normal

| Langkah | Kegiatan Aktor | Respons Sistem |
|---|---|---|
| 1 | Membuka menu Kelola Data Peralatan. | Menampilkan daftar peralatan dan pilihan pengelolaan. |
| 2 | Memilih bentuk pengelolaan: tambah, ubah, atau hapus. | Menampilkan layanan sesuai pilihan petugas. |
| 3 | Mengisi data baru, mengubah data, atau memilih peralatan yang akan dihapus. | Memeriksa kelengkapan dan keabsahan data. Untuk penghapusan, memeriksa bahwa peralatan tidak sedang dipinjam dan tidak memiliki pengajuan aktif. |
| 4 | Mengonfirmasi penyimpanan perubahan. | Menyimpan perubahan dan menampilkan konfirmasi. |

### Rincian Pilihan Pengelolaan

| Use Case | Kegiatan Aktor | Respons Sistem |
|---|---|---|
| LAB-UC08 — Tambah Data Peralatan | Mengisi data peralatan baru. | Menampilkan formulir data peralatan baru, lalu memeriksa data yang diisi. |
| LAB-UC09 — Ubah Data Peralatan | Memilih peralatan, lalu mengubah datanya. | Menampilkan data peralatan saat ini, lalu memeriksa perubahan data. |
| LAB-UC10 — Hapus Data Peralatan | Memilih peralatan yang akan dihapus. | Memeriksa bahwa peralatan tidak sedang dipinjam dan tidak memiliki pengajuan aktif. |

### Skenario Alternatif

| Langkah | Kondisi | Respons Sistem |
|---|---|---|
| 3a | Data peralatan yang akan diubah tidak ditemukan. | Menampilkan pesan data peralatan tidak ditemukan. |
| 3b | Peralatan yang akan dihapus sedang dipinjam atau memiliki pengajuan aktif. | Menolak penghapusan dan menampilkan pesan peralatan masih terpakai. |
| 3c | Data tidak lengkap atau tidak sah. | Menolak penyimpanan dan menampilkan pesan kesalahan data. Petugas memperbaiki data, lalu sistem memeriksanya kembali. |

## LAB-UC03 — Ajukan Peminjaman

| Komponen | Keterangan |
|---|---|
| Nama use case | Ajukan Peminjaman |
| Aktor | Mahasiswa sebagai Peminjam |
| Tujuan | Mengajukan peminjaman peralatan laboratorium. |
| Kondisi awal | Mahasiswa telah masuk ke sistem dan memilih peralatan yang akan dipinjam. |
| Kondisi akhir | Pengajuan tersimpan dengan status Menunggu Keputusan atau sistem menampilkan alasan pengajuan tidak dapat disimpan. |
| Include | LAB-UC04 — Periksa Ketersediaan. |
| Extend | LAB-UC05 — Cetak Bukti Pengajuan, jika mahasiswa memilih mencetak bukti. |

### Skenario Normal

| Langkah | Kegiatan Aktor | Respons Sistem |
|---|---|---|
| 1 | Membuka menu Ajukan Peminjaman. | Menampilkan formulir pengajuan peminjaman. |
| 2 | Mengisi peralatan, jumlah, jadwal peminjaman, dan keperluan. | Menerima data formulir pengajuan. |
| 3 | Mengirim pengajuan peminjaman. | Memeriksa kelengkapan dan keabsahan data. |
| 4 | — | Memeriksa ketersediaan peralatan sesuai jumlah dan jadwal melalui LAB-UC04. |
| 5 | — | Menyimpan pengajuan dengan status Menunggu Keputusan dan membuat nomor pengajuan. |
| 6 | Melihat konfirmasi pengajuan. | Menampilkan nomor pengajuan, status Menunggu Keputusan, dan pilihan cetak bukti. |

### Skenario Alternatif

| Langkah | Kondisi | Respons Sistem dan Tindak Lanjut |
|---|---|---|
| 3a | Data tidak lengkap atau tidak sah. | Sistem menampilkan pesan kesalahan. Mahasiswa memperbaiki formulir, lalu mengirim ulang pengajuan. |
| 4a | Peralatan tidak tersedia sesuai jumlah atau jadwal. | Sistem menampilkan pesan peralatan tidak tersedia. Mahasiswa mengubah pilihan, jumlah, atau jadwal, lalu mengirim ulang pengajuan untuk diperiksa kembali. |
| 6a | Mahasiswa memilih cetak bukti. | Sistem menjalankan LAB-UC05 — Cetak Bukti Pengajuan. |
| 6b | Mahasiswa tidak memilih cetak bukti. | Proses selesai dan pengajuan tetap tersimpan dengan status Menunggu Keputusan. |

## LAB-UC04 — Periksa Ketersediaan

| Komponen | Keterangan |
|---|---|
| Nama use case | Periksa Ketersediaan |
| Aktor | Mahasiswa melalui proses Ajukan Peminjaman |
| Tujuan | Memastikan peralatan tersedia sesuai jumlah dan jadwal pengajuan. |
| Kondisi awal | Data pengajuan sudah lengkap dan sah. |
| Kondisi akhir | Hasil pemeriksaan ketersediaan diperoleh. |
| Hubungan | Di-include oleh LAB-UC03 — Ajukan Peminjaman. |

### Skenario Normal

| Langkah | Kegiatan Aktor | Respons Sistem |
|---|---|---|
| 1 | Mengirim pengajuan melalui LAB-UC03. | Mengambil data peralatan, jumlah, dan jadwal yang diajukan. |
| 2 | — | Memeriksa jumlah peralatan yang tersedia dan benturan jadwal peminjaman. |
| 3 | — | Menyatakan peralatan tersedia dan mengembalikan hasil pemeriksaan ke proses Ajukan Peminjaman. |

### Skenario Alternatif

| Langkah | Kondisi | Respons Sistem |
|---|---|---|
| 2a | Jumlah peralatan tidak mencukupi atau jadwal berbenturan. | Menyatakan peralatan tidak tersedia dan mengembalikan hasil pemeriksaan ke proses Ajukan Peminjaman agar mahasiswa dapat memperbaiki pengajuan. |

## LAB-UC05 — Cetak Bukti Pengajuan

| Komponen | Keterangan |
|---|---|
| Nama use case | Cetak Bukti Pengajuan |
| Aktor | Mahasiswa |
| Tujuan | Mencetak bukti pengajuan peminjaman peralatan. |
| Kondisi awal | Pengajuan sudah tersimpan dengan status Menunggu Keputusan dan pilihan cetak bukti tersedia. |
| Kondisi akhir | Bukti pengajuan dicetak atau proses selesai tanpa mencetak; pengajuan tetap tersimpan. |
| Hubungan | Extend terhadap LAB-UC03 — Ajukan Peminjaman. |
| Extension point | Bukti pengajuan tersedia. |
| Kondisi extend | Mahasiswa memilih cetak bukti. |

### Skenario Normal

| Langkah | Kegiatan Aktor | Respons Sistem |
|---|---|---|
| 1 | Memilih cetak bukti pengajuan. | Menampilkan bukti pengajuan yang memuat nomor pengajuan dan status Menunggu Keputusan. |
| 2 | Mengonfirmasi pencetakan. | Mencetak bukti pengajuan. |

### Skenario Alternatif

| Langkah | Kondisi | Respons Sistem dan Tindak Lanjut |
|---|---|---|
| 1a | Mahasiswa tidak memilih cetak bukti. | Proses selesai tanpa mencetak dan pengajuan tetap tersimpan. |
| 2a | Mahasiswa membatalkan pencetakan. | Sistem menutup konfirmasi tanpa mencetak bukti dan pengajuan tetap tersimpan. |

## LAB-UC06 — Proses Keputusan Peminjaman

| Komponen | Keterangan |
|---|---|
| Nama use case | Proses Keputusan Peminjaman |
| Aktor | Petugas Laboratorium |
| Tujuan | Menetapkan persetujuan atau penolakan pengajuan peminjaman. |
| Kondisi awal | Petugas Laboratorium telah masuk ke sistem. |
| Kondisi akhir | Status pengajuan berubah menjadi Disetujui atau Ditolak, atau sistem menampilkan pesan pengajuan tidak dapat diproses. |

### Skenario Normal

| Langkah | Kegiatan Aktor | Respons Sistem |
|---|---|---|
| 1 | Membuka daftar pengajuan berstatus Menunggu Keputusan. | Menampilkan daftar pengajuan berstatus Menunggu Keputusan. |
| 2 | Memilih pengajuan yang akan diproses. | Memeriksa bahwa pengajuan ditemukan dan masih berstatus Menunggu Keputusan. |
| 3 | — | Menampilkan rincian pengajuan yang dapat diproses. |
| 4 | Memeriksa rincian dan menetapkan keputusan Disetujui atau Ditolak. | Menerima keputusan petugas. |
| 5 | Mengonfirmasi keputusan. | Menyimpan keputusan dan mengubah status pengajuan sesuai keputusan petugas. |
| 6 | Melihat hasil pemrosesan. | Menampilkan konfirmasi beserta status terbaru pengajuan. |

### Skenario Alternatif

| Langkah | Kondisi | Respons Sistem |
|---|---|---|
| 2a | Pengajuan tidak ditemukan atau statusnya sudah bukan Menunggu Keputusan. | Menampilkan pesan pengajuan tidak dapat diproses dan tidak mengubah status pengajuan. |

### Hasil Keputusan

| Keputusan Petugas | Respons Sistem |
|---|---|
| Disetujui | Mengubah status pengajuan menjadi Disetujui. |
| Ditolak | Mengubah status pengajuan menjadi Ditolak. |

## LAB-UC07 — Lihat Laporan Peminjaman

| Komponen | Keterangan |
|---|---|
| Nama use case | Lihat Laporan Peminjaman |
| Aktor | Kepala Laboratorium |
| Tujuan | Melihat laporan peminjaman peralatan berdasarkan periode yang dipilih. |
| Kondisi awal | Kepala Laboratorium telah masuk ke sistem. |
| Kondisi akhir | Laporan ditampilkan atau sistem menampilkan pesan tidak ada data peminjaman pada periode tersebut. |

### Skenario Normal

| Langkah | Kegiatan Aktor | Respons Sistem |
|---|---|---|
| 1 | Membuka fungsi Lihat Laporan Peminjaman. | Menampilkan daftar periode laporan. |
| 2 | Memilih periode laporan. | Memeriksa keberadaan data peminjaman pada periode tersebut. |
| 3 | Melihat laporan peminjaman. | Menampilkan laporan peminjaman periode tersebut. |

### Skenario Alternatif

| Langkah | Kondisi | Respons Sistem |
|---|---|---|
| 2a | Tidak ada data peminjaman pada periode yang dipilih. | Menampilkan pesan tidak ada data peminjaman pada periode tersebut. |

## LAB-UC08 — Tambah Data Peralatan

| Komponen | Keterangan |
|---|---|
| Nama use case | Tambah Data Peralatan |
| Aktor | Petugas Laboratorium |
| Tujuan | Menambahkan data peralatan baru ke sistem. |
| Kondisi awal | Petugas membuka Kelola Data Peralatan dan memilih tambah. |
| Kondisi akhir | Data peralatan baru tersimpan atau sistem menampilkan kesalahan data. |
| Hubungan | Varian tambah pada LAB-UC02 — Kelola Data Peralatan. |

### Skenario Normal

| Langkah | Kegiatan Aktor | Respons Sistem |
|---|---|---|
| 1 | Memilih tambah data peralatan. | Menampilkan formulir data peralatan baru. |
| 2 | Mengisi data peralatan baru. | Menerima data yang diisi. |
| 3 | Mengirim data untuk diperiksa. | Memeriksa kelengkapan dan keabsahan data. |
| 4 | Mengonfirmasi penyimpanan. | Menyimpan data peralatan baru dan menampilkan konfirmasi. |

### Skenario Alternatif

| Langkah | Kondisi | Respons Sistem dan Tindak Lanjut |
|---|---|---|
| 3a | Data tidak lengkap atau tidak sah. | Sistem menolak penyimpanan dan menampilkan pesan kesalahan data. Petugas memperbaiki data, lalu mengirimnya kembali untuk diperiksa. |

## LAB-UC08 — Tambah Data Peralatan

| Komponen | Keterangan |
|---|---|
| Nama use case | Tambah Data Peralatan |
| Aktor | Petugas Laboratorium |
| Tujuan | Menambahkan data peralatan baru ke sistem. |
| Kondisi awal | Petugas membuka Kelola Data Peralatan dan memilih tambah. |
| Kondisi akhir | Data peralatan baru tersimpan atau sistem menampilkan kesalahan data. |
| Hubungan | Varian tambah pada LAB-UC02 — Kelola Data Peralatan. |

### Skenario Normal

| Langkah | Kegiatan Aktor | Respons Sistem |
|---|---|---|
| 1 | Memilih tambah data peralatan. | Menampilkan formulir data peralatan baru. |
| 2 | Mengisi data peralatan baru. | Menerima data yang diisi. |
| 3 | Mengirim data untuk diperiksa. | Memeriksa kelengkapan dan keabsahan data. |
| 4 | Mengonfirmasi penyimpanan. | Menyimpan data peralatan baru dan menampilkan konfirmasi. |

### Skenario Alternatif

| Langkah | Kondisi | Respons Sistem dan Tindak Lanjut |
|---|---|---|
| 3a | Data tidak lengkap atau tidak sah. | Sistem menolak penyimpanan dan menampilkan pesan kesalahan data. Petugas memperbaiki data, lalu mengirimnya kembali untuk diperiksa. |

## LAB-UC10 — Hapus Data Peralatan

| Komponen | Keterangan |
|---|---|
| Nama use case | Hapus Data Peralatan |
| Aktor | Petugas Laboratorium |
| Tujuan | Menghapus data peralatan yang memenuhi syarat penghapusan. |
| Kondisi awal | Petugas membuka Kelola Data Peralatan dan memilih hapus. |
| Kondisi akhir | Data peralatan dihapus atau sistem menampilkan alasan penghapusan ditolak. |
| Hubungan | Varian hapus pada LAB-UC02 — Kelola Data Peralatan. |

### Skenario Normal

| Langkah | Kegiatan Aktor | Respons Sistem |
|---|---|---|
| 1 | Memilih data peralatan yang akan dihapus. | Memeriksa bahwa peralatan tidak sedang dipinjam dan tidak memiliki pengajuan aktif. |
| 2 | Mengonfirmasi penghapusan. | Menghapus data peralatan dan menampilkan konfirmasi. |

### Skenario Alternatif

| Langkah | Kondisi | Respons Sistem |
|---|---|---|
| 1a | Peralatan sedang dipinjam atau memiliki pengajuan aktif. | Menolak penghapusan dan menampilkan pesan peralatan masih terpakai. |

## LAB-UC11 — Catat Pengembalian Peralatan

| Komponen | Keterangan |
|---|---|
| Nama use case | Catat Pengembalian Peralatan |
| Aktor | Petugas Laboratorium, dengan keterlibatan Mahasiswa sebagai pengembali peralatan. |
| Tujuan | Mencatat pengembalian dan kondisi peralatan setelah dipinjam. |
| Kondisi awal | Terdapat peminjaman aktif dan mahasiswa menyerahkan peralatan yang dipinjam. |
| Kondisi akhir | Pengembalian tercatat beserta hasil pemeriksaan kondisi peralatan. |
| Include | LAB-UC12 — Periksa Kondisi Peralatan. |

### Skenario Normal

| Langkah | Kegiatan Aktor | Respons Sistem |
|---|---|---|
| 1 | Mahasiswa menyerahkan peralatan kepada Petugas Laboratorium. | — |
| 2 | Petugas membuka fungsi Catat Pengembalian Peralatan dan memilih data peminjaman. | Menampilkan rincian peminjaman aktif. |
| 3 | Petugas memeriksa kondisi peralatan melalui LAB-UC12. | — |
| 4 | Petugas memasukkan hasil pemeriksaan kondisi dan data pengembalian. | Menerima data pengembalian. |
| 5 | Petugas mengonfirmasi pengembalian. | Menyimpan catatan pengembalian, memperbarui status peminjaman menjadi selesai, dan memperbarui status peralatan sesuai hasil pemeriksaan. |
| 6 | Mahasiswa menerima konfirmasi pengembalian dari petugas. | Menampilkan konfirmasi pengembalian. |

### Skenario Alternatif

| Langkah | Kondisi | Respons Sistem dan Tindak Lanjut |
|---|---|---|
| 3a | Kondisi peralatan rusak. | Petugas mencatat kerusakan. Sistem menyimpan kondisi rusak bersama catatan pengembalian dan menandai peralatan tidak tersedia untuk dipinjam. |

## LAB-UC12 — Periksa Kondisi Peralatan

| Komponen | Keterangan |
|---|---|
| Nama use case | Periksa Kondisi Peralatan |
| Aktor | Petugas Laboratorium |
| Tujuan | Mengetahui kondisi peralatan yang dikembalikan. |
| Kondisi awal | Mahasiswa telah menyerahkan peralatan dan rincian peminjaman telah ditampilkan. |
| Kondisi akhir | Hasil pemeriksaan kondisi diperoleh untuk dicatat pada proses pengembalian. |
| Hubungan | Di-include oleh LAB-UC11 — Catat Pengembalian Peralatan. |

### Skenario Normal

| Langkah | Kegiatan Aktor | Respons Sistem |
|---|---|---|
| 1 | Memeriksa kondisi fisik dan fungsi peralatan yang dikembalikan. | — |
| 2 | Menetapkan hasil pemeriksaan kondisi baik. | — |
| 3 | Melanjutkan pencatatan hasil pemeriksaan pada LAB-UC11. | Menerima hasil pemeriksaan sebagai bagian dari data pengembalian. |

### Skenario Alternatif

| Langkah | Kondisi | Respons Sistem dan Tindak Lanjut |
|---|---|---|
| 2a | Ditemukan kerusakan pada peralatan. | Petugas menetapkan kondisi rusak dan menjelaskan kerusakannya, lalu melanjutkan pencatatan pada LAB-UC11. |