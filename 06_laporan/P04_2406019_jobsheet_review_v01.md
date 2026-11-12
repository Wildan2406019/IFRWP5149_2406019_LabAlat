## Review dan Revisi

Berdasarkan pemeriksaan diagram dan hasil uji konsistensi, terdapat beberapa hal yang perlu diperiksa dan diperbaiki:

| No. | Temuan                                                     | Perbaikan yang diperlukan                                                                                                          | Alasan                                                                   |
| --- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| 1   | Hubungan generalization aktor belum tergambar dengan jelas | Rapikan hubungan Mahasiswa dan Dosen menuju Civitas Akademika menggunakan garis utuh dengan segitiga kosong mengarah ke aktor umum | Generalization menunjukkan bahwa aktor khusus mewarisi fungsi aktor umum |
| 2   | Dosen terhubung ke use case Ajukan KRS                     | Hapus asosiasi tersebut jika memang menghubungkan Dosen dengan UC-01 Ajukan KRS                                                    | Pengajuan KRS dilakukan oleh Mahasiswa, bukan Dosen                      |
| 3   | ID collaboration pada diagram tidak sama dengan katalog    | Samakan ID collaboration dengan katalog, yaitu SIA-CO01 untuk Input Nilai Mata Kuliah dan SIA-CO02 untuk Lihat KHS                 | ID harus konsisten di seluruh dokumentasi dan diagram                    |
| 4   | Notasi collaboration perlu dipastikan                      | Sesuaikan simbol dan hubungan collaboration dengan contoh pada modul                                                               | Model harus menggunakan notasi yang sesuai dengan ketentuan tugas        |
| 5   | Posisi aktor dekat atau menyentuh batas sistem             | Pindahkan semua aktor ke luar batas sistem dan rapikan garis asosiasinya                                                           | Aktor merupakan pihak eksternal yang berinteraksi dengan sistem          |

## Kesimpulan

Berdasarkan pengujian tiga situasi, model Sistem Informasi Akademik dapat menggambarkan aturan akses dan pengelolaan data sesuai skenario. Namun, diagram masih perlu dirapikan, khususnya pada generalization aktor, asosiasi aktor dengan use case, konsistensi ID collaboration, dan notasi collaboration. Setelah revisi selesai, diagram dan deskripsi use case disimpan sebagai versi revisi.
