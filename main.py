"""
Aplikasi Deteksi Gempa Terkini
"""

def ekstrasi_data():
    """

    Tanggal: 15 Agustus 2023, 16:29:17 WIB
    Magnitudo: 2.6
    Kedalaman: 6 km
    Lokasi: LS=6.82 LS - BT=107.13 BT
    Pusat Gempa : Pusat gempa berada di darat 1 km barat laut Kab. Cianjur
    Dirasakan : Dirasakan (Skala MMI): II Cugenang, II Kota Cianjur, II Karangtengah, II Warungkondang
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '24 agustus 2023'
    hasil['waktu'] = '16:29:17 WIB'
    return hasil


def tampilkan_data(result):
    pass


if __name__ == '__main__':
    print('aplikasi utama')
    result = ekstrasi_data()
    tampilkan_data(result)




