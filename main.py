"""
Aplikasi Deteksi Gempa Terkini
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE
"""
import gempa_terkini

if __name__ == '__main__':
    print('aplikasi utama')
    print('\n')
    result = gempa_terkini.ekstrasi_data()
    gempa_terkini.tampilkan_data(result)
