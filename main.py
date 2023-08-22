"""
Aplikasi Deteksi Gempa Terkini
MODULARISASI DENGAN FUNCTION
"""

import data_gempa

if __name__ == '__main__':
    print('APLIKASI UTAMA>>>>>>>>>>>//////////<<<<<<<<<<')
    result = data_gempa.ekstrasi_data()
    data_gempa.tampilkan_data(result)




