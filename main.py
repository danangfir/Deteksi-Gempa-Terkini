"""
Aplikasi Deteksi Gempa Terkini
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE
"""
from gempa_terkini import ekstrasi_data, tampilkan_data

if __name__ == '__main__':
    print('aplikasi utama')
    print('\n')
    result = ekstrasi_data()
    tampilkan_data(result)
