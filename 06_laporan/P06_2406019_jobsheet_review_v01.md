# LANGKAH 5 – PEMERIKSAAN ACTIVITY DIAGRAM SIA

## A. Tujuan Pemeriksaan

Pemeriksaan Activity Diagram dilakukan untuk memastikan bahwa diagram proses Input Nilai Mata Kuliah sampai Lihat KHS telah sesuai dengan ketentuan Jobsheet Praktikum Pertemuan 6. Pemeriksaan meliputi kelengkapan simbol, alur aktivitas, penggunaan Decision dan Guard, pasangan Fork dan Join, serta kesesuaian penempatan aktivitas pada swimlane.

Diagram yang diperiksa merupakan satu Activity Diagram yang menggabungkan SIA-UC08 (Input Nilai Mata Kuliah) dan SIA-UC09 (Lihat KHS).

## B. Checklist Pemeriksaan

| No. | Aspek Pemeriksaan                                                                                                               | Hasil |
| --- | ------------------------------------------------------------------------------------------------------------------------------- | ----- |
| 1   | Terdapat tepat satu Initial Node dan tepat satu Activity Final Node. Tidak ada action yang terputus dari alur.                  | ✓     |
| 2   | Setiap Decision memiliki Guard pada seluruh alur keluarnya, yaitu `[lengkap]` dan `[belum lengkap]`.                            | ✓     |
| 3   | Cabang Decision kembali melalui Merge sebelum proses dilanjutkan ke pengesahan nilai.                                           | ✓     |
| 4   | Fork memiliki pasangan Join untuk membagi dan menggabungkan kembali dua proses paralel.                                         | ✓     |
| 5   | Setiap action ditempatkan pada swimlane aktor yang melakukan aktivitas, sedangkan aktivitas sistem berada pada swimlane Sistem. | ✓     |
| 6   | Setiap action disesuaikan dengan langkah pada tabel skenario SIA Pertemuan 5 dan instruksi tugas Pertemuan 6.                   | ✓     |
| 7   | Collaboration tidak digambarkan sebagai action maupun sebagai swimlane.                                                         | ✓     |
| 8   | Nama aktor, nama action, dan ID use case konsisten dengan dokumen SIA Pertemuan 4 dan 5.                                        | ✓     |
| 9   | Dokumen P04 dan P05 tetap dipertahankan dan tidak diubah.                                                                       | ✓     |

## C. Pemeriksaan Swimlane dan Aktivitas

| No. | Swimlane       | Aktivitas yang Diperiksa                            | Hasil |
| --- | -------------- | --------------------------------------------------- | ----- |
| 1   | Dosen          | Memasukkan Nilai Mata Kuliah                        | ✓     |
| 2   | Sistem         | Menyimpan Nilai                                     | ✓     |
| 3   | Dosen          | Melengkapi Nilai Mata Kuliah yang Belum Lengkap     | ✓     |
| 4   | Admin Akademik | Memeriksa dan Mengesahkan Nilai                     | ✓     |
| 5   | Sistem         | Menyiapkan Publikasi Hasil Studi                    | ✓     |
| 6   | Sistem         | Menerbitkan KHS pada Portal Akademik                | ✓     |
| 7   | Sistem         | Mengirim Pemberitahuan Hasil Studi kepada Mahasiswa | ✓     |
| 8   | Mahasiswa      | Melihat KHS                                         | ✓     |

## D. Pemeriksaan Simbol dan Alur Diagram

| No. | Unsur Diagram           | Kriteria Pemeriksaan                                                          | Hasil |
| --- | ----------------------- | ----------------------------------------------------------------------------- | ----- |
| 1   | Initial Node            | Menjadi titik awal seluruh aktivitas.                                         | ✓     |
| 2   | Decision Node           | Digunakan untuk memeriksa apakah nilai sudah lengkap.                         | ✓     |
| 3   | Guard `[lengkap]`       | Mengarahkan alur menuju pemeriksaan dan pengesahan nilai oleh Admin Akademik. | ✓     |
| 4   | Guard `[belum lengkap]` | Mengarahkan alur menuju aktivitas melengkapi nilai oleh Dosen.                | ✓     |
| 5   | Merge Node              | Menggabungkan kembali alur setelah nilai dilengkapi.                          | ✓     |
| 6   | Fork Node               | Membagi proses menjadi dua aktivitas yang berjalan paralel.                   | ✓     |
| 7   | Join Node               | Menggabungkan kembali proses penerbitan KHS dan pengiriman pemberitahuan.     | ✓     |
| 8   | Activity Final Node     | Menjadi titik akhir setelah Mahasiswa melihat KHS.                            | ✓     |

## E. Hasil Pemeriksaan

Berdasarkan checklist penilaian pada Bagian C.4, Activity Diagram SIA telah disusun dengan menggunakan satu Initial Node dan satu Activity Final Node. Diagram juga dilengkapi Decision Node dengan dua kondisi, yaitu `[lengkap]` dan `[belum lengkap]`, serta Merge Node untuk menggabungkan kembali alur setelah Dosen melengkapi nilai.

Selain itu, diagram menggunakan satu pasang Fork dan Join untuk menggambarkan proses penerbitan KHS pada portal akademik dan pengiriman pemberitahuan hasil studi kepada mahasiswa yang berjalan secara paralel. Setiap aktivitas ditempatkan pada swimlane sesuai dengan pihak yang bertanggung jawab, yaitu Dosen, Sistem, Admin Akademik, dan Mahasiswa.

Dengan dilakukannya pemeriksaan ini, Activity Diagram SIA diharapkan telah memenuhi ketentuan penyusunan diagram pada Jobsheet Praktikum Pertemuan 6 dan siap dilanjutkan ke tahap penyimpanan serta ekspor PNG.
