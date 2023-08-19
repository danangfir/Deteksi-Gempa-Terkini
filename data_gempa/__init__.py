"""
Aplikasi Deteksi Gempa Terkini
MODULARISASI DENGAN FUNCTION
"""

def ekstrasi_data():
    """

    Tanggal: 15 Agustus 2023, 16:29:17 WIB
    Magnitudo: 2.6 skala richter
    Kedalaman: 6 km
    Lokasi: ls=6.82 LS - ls=107.13 BT
    Pusat Gempa : Pusat gempa berada di darat 1 km barat laut Kab. Cianjur
    Dirasakan : Dirasakan (Skala MMI): II Cugenang, II Kota Cianjur, II Karangtengah, II Warungkondang
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '24 agustus 2023'
    hasil['waktu'] = '16:29:17 WIB'
    hasil['magnitudo'] = '2.6 skala richter'
    hasil['lokasi'] = {'ls': 6.82, 'bt': 107.13}
    hasil['pusat'] = 'Pusat gempa berada di darat 1 km barat laut Kab. Cianjur'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II Cugenang, II Kota Cianjur, II Karangtengah, II Warungkondang'

    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"pusat: {result['pusat']}")
    print(f"dirasakan: {result['dirasakan']}")


