
from pathlib import Path
import xml.etree.ElementTree as ET
import copy

folder = Path(__file__).resolve().parent
sumber = folder / "P06_2406019__LAB_skenario_v01.drawio"

root = ET.parse(sumber).getroot()
halaman = root.findall("diagram")

print("Jumlah halaman:", len(halaman))

for nomor, diagram in enumerate(halaman, 1):
    print(f"{nomor}. {diagram.get('name')}")

nama_diagram = [
    "peminjaman",
    "pengembalian",
    "lihat_ketersediaan",
    "kelola_data",
    "cetak_bukti",
    "keputusan",
    "laporan",
]

if len(halaman) != 7:
    raise ValueError(
        "Jumlah halaman bukan 7. Periksa urutan dan isi halaman dulu."
    )

konfirmasi = input(
    "Apakah urutan halaman sesuai daftar di atas? (ya/tidak): "
)

if konfirmasi.lower() != "ya":
    print("Dibatalkan. Tidak ada file yang dibuat.")
    exit()

for diagram, nama in zip(halaman, nama_diagram):
    hasil = folder / f"P06_2406019_LAB_activity_{nama}_v01.drawio"

    if hasil.exists():
        print("Dilewati, file sudah ada:", hasil.name)
        continue

    dokumen = ET.Element("mxfile", root.attrib)
    dokumen.set("pages", "1")

    halaman_baru = copy.deepcopy(diagram)
    halaman_baru.set("name", nama)
    dokumen.append(halaman_baru)

    ET.ElementTree(dokumen).write(
        hasil, encoding="utf-8", xml_declaration=True
    )
    print("Berhasil:", hasil.name)

print("Selesai. Periksa semua diagram di Draw.io.")

