# CAPSTONE PROJECT
# ------------------- DATA NILAI SISWA -------------------

# ------------------------------------ IMPORT -------------------------------------
from tabulate import tabulate
import re
# -------------------------------- DATABASE --------------------------------
database_siswa = [
    {'NIS': 1, 'Nama': 'Bambang Pacul', 'Kelas': 'IPA 1', 'Tugas': 80, 'UTS': 90, 'UAS': 100, 'Status': 'Lulus'},
    {'NIS': 2, 'Nama': 'Anton Medan', 'Kelas': 'IPA 1', 'Tugas': 100, 'UTS': 90, 'UAS': 70, 'Status': 'Lulus'},
    {'NIS': 3, 'Nama': 'Tumini', 'Kelas': 'IPA 1', 'Tugas': 85, 'UTS': 88, 'UAS': 95, 'Status': 'Lulus'},
    {'NIS': 4, 'Nama': 'Cak Anto', 'Kelas': 'IPA 2', 'Tugas': 90, 'UTS': 92, 'UAS': 88, 'Status': 'Lulus'},
    {'NIS': 5, 'Nama': 'Suharti', 'Kelas': 'IPA 2', 'Tugas': 75, 'UTS': 80, 'UAS': 85, 'Status': 'Lulus'},
    {'NIS': 6, 'Nama': 'Tojoyo', 'Kelas': 'IPA 3', 'Tugas': 95, 'UTS': 65, 'UAS': 60, 'Status': 'Tidak Lulus'},
    {'NIS': 7, 'Nama': 'Nyonya Menir', 'Kelas': 'IPA 3', 'Tugas': 78, 'UTS': 85, 'UAS': 82, 'Status': 'Lulus'},
    {'NIS': 8, 'Nama': 'Sujiwo Tejo', 'Kelas': 'IPA 2', 'Tugas': 88, 'UTS': 91, 'UAS': 94, 'Status': 'Lulus'},
    {'NIS': 9, 'Nama': 'Iwan Setiawan', 'Kelas': 'IPA 3', 'Tugas': 80, 'UTS': 78, 'UAS': 84, 'Status': 'Lulus'},
    {'NIS': 10, 'Nama': 'Ponidi', 'Kelas': 'IPA 1', 'Tugas': 70, 'UTS': 75, 'UAS': 80, 'Status': 'Lulus'},
    {'NIS': 11, 'Nama': 'Lina Maulida', 'Kelas': 'IPA 2', 'Tugas': 82, 'UTS': 85, 'UAS': 90, 'Status': 'Lulus'},
    {'NIS': 12, 'Nama': 'Mira Santika', 'Kelas': 'IPA 1', 'Tugas': 60, 'UTS': 88, 'UAS': 60, 'Status': 'Tidak Lulus'},
    {'NIS': 13, 'Nama': 'Eros Chandra', 'Kelas': 'IPA 3', 'Tugas': 87, 'UTS': 90, 'UAS': 85, 'Status': 'Lulus'},
    {'NIS': 14, 'Nama': 'Michael Jackson', 'Kelas': 'IPA 1', 'Tugas': 65, 'UTS': 75, 'UAS': 70, 'Status': 'Tidak Lulus'},
    {'NIS': 15, 'Nama': 'Budiono Siregar', 'Kelas': 'IPA 2', 'Tugas': 75, 'UTS': 78, 'UAS': 80, 'Status': 'Lulus'},
    {'NIS': 16, 'Nama': 'Denny Caknan', 'Kelas': 'IPA 3', 'Tugas': 88, 'UTS': 84, 'UAS': 86, 'Status': 'Lulus'},
    {'NIS': 17, 'Nama': 'Bio Paulin', 'Kelas': 'IPA 1', 'Tugas': 80, 'UTS': 80, 'UAS': 75, 'Status': 'Lulus'},
    {'NIS': 18, 'Nama': 'Marten Paes', 'Kelas': 'IPA 2', 'Tugas': 92, 'UTS': 91, 'UAS': 89, 'Status': 'Lulus'},
    {'NIS': 19, 'Nama': 'Moh Salah', 'Kelas': 'IPA 3', 'Tugas': 85, 'UTS': 87, 'UAS': 90, 'Status': 'Lulus'},
    {'NIS': 20, 'Nama': 'Frank Lampard', 'Kelas': 'IPA 2', 'Tugas': 78, 'UTS': 79, 'UAS': 80, 'Status': 'Lulus'}
]

database_backup = []

# --------------------------------------- FUNCTION PENDUKUNG ---------------------------------------
# function untuk login -> admin/siswa
def login():
    username = input("Masukkan username: ").strip().lower()
    password = input("Masukkan password: ").strip().lower()

    if username == 'admin' and password == 'admin123':
        return 'admin'
    elif username in [data['Nama'].replace(' ','').lower().strip() for data in database_siswa] and password == 'siswa':
        return 'siswa'
    else:
        print("Login gagal! Username atau password salah.")

# function untuk input berupa huruf dan beberapa karakter
def input_alphabet(prompt, validasi = 'alphabet'):
    while True:
        value = input(prompt).strip()
        if re.match(r"^[a-zA-Z0-9\s'-]+$", value):
            return value
        else:
            print('Input tidak valid')
    
# function untuk input berupa angka dan dimasukan kategori string juga untuk perintah tertentu
def input_number(prompt):
    while True:
        value = input(prompt)
        if value.lower() == 'b' or value.lower() == 'c':
            return value
        elif value.isdigit():
            return int(value)
        else:
            print('Input tidak valid')

# function untuk mengetahui kelulusan setiap siswa
def status_lulus(tugas, UTS, UAS):
    rata_rata = (tugas + UTS + UAS) / 3
    return 'Lulus' if rata_rata >= 75 else 'Tidak Lulus'

# function untuk mengurutkan database
def sort_database(database, key):
    return sorted(database, key=key)

# function untuk mendapatkan kunci pengurutan database
def sort_key(pilihan):
    if pilihan == 1:
        return lambda x: x['NIS']
    elif pilihan == 2:
        return lambda x: x['Nama']
    elif pilihan == 3:
        return lambda x: (x['Kelas'].split()[0], int(x['Kelas'].split()[1]))

# function untuk mencari database
def search_database(database, search_type, search_value):
    if search_type == 'nis':
        return [data for data in database if str(data['NIS']) == search_value]
    elif search_type == 'nama':
        return [data for data in database if data['Nama'].lower() == search_value.lower()]
    elif search_type == 'kelas':
        return [data for data in database if data['Kelas'].lower() == search_value.lower()]

# function untuk menampilkan data siswa yang tidak lulus 
def siswa_tidak_lulus():
    siswa_tidak_lulus = [data for data in database_siswa if data['Status'] == 'Tidak Lulus']
    if not siswa_tidak_lulus:
        print("Tidak ada siswa yang statusnya 'Tidak Lulus'.")
        return
    print("Perhatikan! Siswa yang wajib mengikuti perbaikan nilai: ")
    print(tabulate(siswa_tidak_lulus, headers='keys', tablefmt='rounded_outline'))

    
# --------------------------------------- FUNCTION UTAMA ---------------------------------------
# function untuk menampilkan data siswa pada pilihan menu utama admin dan siswa
def tampilkan_data():
    print('Pilih kategori untuk mengurutkan data:')
    print('[1] NIS')
    print('[2] Nama')
    print('[3] Kelas')

    pilihan = input_number('Masukkan pilihan Anda (1/2/3) atau ketik "c" untuk melakukan pencarian: ')
    if pilihan in [1, 2, 3]:
        sorted_database = sort_database(database_siswa, sort_key(pilihan))
        print(tabulate(sorted_database, headers='keys', tablefmt='rounded_outline'))
    elif pilihan == 'c':
        pencarian = input_alphabet('Masukkan kategori pencarian (NIS/Nama/Kelas): ').strip().lower()
        search_value = input('Masukkan data pencarian: ').strip()
        hasil_cari = search_database(database_siswa, pencarian, search_value)
        
        if not hasil_cari:
            print('Data tidak ditemukan')
        else:
            print(tabulate(hasil_cari, headers='keys', tablefmt='rounded_outline'))
    else:
        print('Pilihan tidak valid')

# function untuk menambahkan data siswa dalam menu utama admin
def tambah_data():
    nis = max([data['NIS'] for data in database_siswa], default = 0) + 1 
    nama = input_alphabet('Masukkan Nama atau "b" untuk kembali: ').title() 
    if nama.lower() == 'b':
        return
    kelas = input_alphabet('Masukkan Kelas atau "b" untuk kembali: ').upper()
    if kelas.lower() == 'b':
        return
    tugas = input_number('Masukkan Nilai Tugas atau "b" untuk kembali: ')
    if tugas == 'b':
        return
    uts = input_number('Masukkan Nilai UTS atau "b" untuk kembali: ')
    if uts == 'b':
        return
    uas = input_number('Masukkan Nilai UAS atau "b" untuk kembali: ')
    if uas == 'b':
        return
    
    for data in database_siswa:
        if data['Nama'].lower() == nama.lower() and data['Kelas'].lower() == kelas.lower():
            print('Data sudah ada')
            return
    status = status_lulus(tugas, uts, uas)    
    database_siswa.append({'NIS': nis, 'Nama': nama, 'Kelas': kelas, 'Tugas': tugas, 'UTS': uts, 'UAS': uas, 'Status': status})
    print(f'Data siswa berhasil ditambahkan: {database_siswa[-1]}')

# function untuk mengubah data siswa dalam menu utama admin
def ubah_data():
    siswa_tidak_lulus()
    nis = input_number('Masukkan NIS untuk data yang akan diubah atau perbaikan nilai: ')
    if nis == 'b':
        return
    else:
        if 1 <= nis <= len(database_siswa):
            data_sebelumnya = database_siswa[nis - 1]
            print(f'Data siswa yang ingin diubah: {data_sebelumnya}')
            
            print('Pilih data yang ingin diubah:')
            print('[1] Nama')
            print('[2] Kelas')
            print('[3] Nilai Tugas')
            print('[4] Nilai UTS')
            print('[5] Nilai UAS')
            print('[6] Berikan Remidi') 
            print('[7] Kembali')


            pilihan = input_number('Masukkan pilihan Anda: ')
            if pilihan == 1:
                nama = input_alphabet('Masukkan Nama baru: ')
                data_sebelumnya['Nama'] = nama
            elif pilihan == 2:
                kelas = input_alphabet('Masukkan Kelas baru: ')
                data_sebelumnya['Kelas'] = kelas
            elif pilihan == 3:
                tugas = input_number('Masukkan Nilai Tugas baru: ')
                data_sebelumnya['Tugas'] = tugas
            elif pilihan == 4:
                uts = input_number('Masukkan Nilai UTS baru: ')
                data_sebelumnya['UTS'] = uts
            elif pilihan == 5:
                uas = input_number('Masukkan Nilai UAS baru: ')
                data_sebelumnya['UAS'] = uas
            elif pilihan == 6:
                if data_sebelumnya['Tugas'] < 75:
                    data_sebelumnya['Tugas'] = 75
                    print(f'Nilai Tugas untuk {data_sebelumnya["Nama"]} diubah menjadi 75.')
                if data_sebelumnya['UTS'] < 75:
                    data_sebelumnya['UTS'] = 75
                    print(f'Nilai UTS untuk {data_sebelumnya["Nama"]} diubah menjadi 75.')
                if data_sebelumnya['UAS'] < 75:
                    data_sebelumnya['UAS'] = 75
                    print(f'Nilai UAS untuk {data_sebelumnya["Nama"]} diubah menjadi 75.')

                # status kelulusan setelah perubahan
                data_sebelumnya['Status'] = status_lulus(
                    data_sebelumnya['Tugas'],
                    data_sebelumnya['UTS'],
                    data_sebelumnya['UAS']
                )
            elif pilihan == 7:
                return
            else:
                print('Pilihan tidak valid')
                return
            
            print(f'Data siswa berhasil diubah: {data_sebelumnya}')
        else:
            print('NIS tidak valid.')

# function untuk menghapus data siswa dalam menu utama admin
def hapus_data():
    print('DATA SISWA:')
    print(tabulate(database_siswa, headers='keys', tablefmt='rounded_outline'))
    nis = input_number('Masukkan NIS yang ingin dihapus atau "b" untuk kembali: ')
    if nis == 'b':
        return
    else:
        if 1 <= nis <= len(database_siswa):
            database_backup.append(database_siswa[nis - 1])
            del database_siswa[nis - 1]
            print(f'Data siswa dengan NIS {nis} berhasil dihapus')
        else:
            print('NIS tidak valid')

# function untuk menampilkan history data dalam menu utama admin
def history_data():
    if len(database_backup) == 0:
        print('Tidak ada data yang dihapus')
    else:
        print('DATA SISWA YANG DIHAPUS:')
        print(tabulate(database_backup, headers='keys', tablefmt='rounded_outline'))

# function untuk menghapus history data dalam menu utama admin
def hapus_history():
    global database_backup
    database_backup.clear()
    print('History data berhasil dibersihkan.')

# ----------------------------------------- FUNCTION LOGIN -----------------------------------------
# function utama admin
def menu_admin():
    while True:
        print('----------------------- INFORMASI NILAI SISWA SMA NEGERI 1 KOREA -----------------------')
        print('--------------------------------------|MENU UTAMA|--------------------------------------')
        print('[1] Tampilkan Data Siswa')
        print('[2] Tambah Data Siswa')
        print('[3] Ubah Data Siswa')
        print('[4] Hapus Data Siswa')
        print('[5] History Data')
        print('[6] Hapus History Data')
        print('[7] Keluar')

        pilih = input_number('Pilih menu: ')
        if pilih == 1:
            tampilkan_data()
        elif pilih == 2:
            tambah_data()
        elif pilih == 3:
            ubah_data()
        elif pilih == 4:
            hapus_data()
        elif pilih == 5:
            history_data()
        elif pilih == 6:
            hapus_history()
        elif pilih == 7:
            print('Terima kasih')
            break
        else:
            print('Pilihan tidak valid')

# function utama siswa
def menu_siswa():
    while True:
        print('----------------------- INFORMASI NILAI SISWA SMA NEGERI 1 KOREA -----------------------')
        print('--------------------------------------|MENU UTAMA|--------------------------------------')
        print('[1] Tampilkan Data Siswa')
        print('[2] Keluar')

        pilih = input_number('Pilih menu: ')
        if pilih == 1:
            tampilkan_data()
        elif pilih == 2:
            print('Terima kasih')
            break
        else:
            print('Pilihan tidak valid')

# function utama yang akan dijalankan sesuai login admin/siswa
def menu_utama():
        while True:
            user = login()
            if user == 'admin':
                menu_admin()
                return
            elif user == 'siswa':
                menu_siswa()
                return
menu_utama()
    