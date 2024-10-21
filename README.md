
# CAPSTONE PROJECT
## MANAJEMEN DATA NILAI SISWA

### Deskripsi
Proyek ini adalah sistem manajemen data nilai siswa untuk SMA Negeri 1 Korea. Sistem ini memungkinkan admin untuk melakukan operasi CRUD (Create, Read, Update, Delete) pada data siswa serta melakukan login sebagai admin atau siswa.

### Fitur Utama
1. **Login**
- Pengguna dapat login sebagai admin dengan username dan password yang ditentukan. Siswa dapat login dengan nama dan password default.

2. **Menu Admin**
- Admin memiliki akses ke berbagai fungsi:
     - **Tampilkan Data Siswa (Read)**: Menampilkan semua data siswa dengan opsi pengurutan berdasarkan NIS, Nama, atau Kelas.
     - **Tambah Data Siswa (Create)**: Menambahkan data siswa baru, termasuk NIS, Nama, Kelas, dan nilai (Tugas, UTS, UAS). Status kelulusan dihitung otomatis.
     - **Ubah Data Siswa (Update)**: Mengubah data siswa berdasarkan NIS, termasuk pemberian remidi untuk siswa yang tidak lulus.
     - **Hapus Data Siswa (Delete)**: Menghapus data siswa dari database dan menyimpan backup data yang dihapus.
     - **History Data**: Menampilkan daftar siswa yang telah dihapus.
     - **Hapus History Data**: Menghapus semua riwayat data yang dihapus.
     - **Keluar**: Mengakhiri sesi admin.

3. **Menu Siswa**
- Siswa dapat:
     - **Tampilkan Data Siswa (Read)**: Melihat data mereka sendiri.
     - **Keluar**: Mengakhiri sesi siswa.

### Fungsi Pendukung
- **Validasi Input**: Fungsi untuk memastikan input pengguna valid, baik untuk huruf maupun angka.
- **Status Kelulusan**: Fungsi untuk menentukan status kelulusan siswa berdasarkan nilai rata-rata.
- **Pencarian Data**: Fungsi untuk mencari data siswa berdasarkan NIS, Nama, atau Kelas.
- **Sortir Data**: Fungsi untuk mengurutkan data berdasarkan NIS, Nama, dan Kelas.
- **Automatisasi Remidi**: Fungsi untuk menampilkan siswa yang diharuskan melakukan perbaikan dan akan dilakukan update otomatis untuk nilai yang telah diperbaiki.

### Struktur Database
- Database disimpan dalam bentuk list of dictionaries, dengan setiap dictionary mewakili data seorang siswa.
- Setiap siswa memiliki atribut seperti NIS, Nama, Kelas, Tugas, UTS, UAS, dan Status.

### Contoh Penggunaan
- Admin login menggunakan username dan password.
- Admin memilih opsi untuk menampilkan data siswa.
- Admin dapat menambah, mengubah, atau menghapus data siswa.
- Siswa dapat melihat data mereka dan keluar dari sistem.

### Catatan
- Sistem ini menggunakan `tabulate` untuk menampilkan data dalam format tabel yang mudah dibaca.
- Validasi input menggunakan regex untuk memastikan keamanan dan keakuratan data.

### Teknologi yang Digunakan
- Python sebagai bahasa pemrograman.
- Library `tabulate` untuk format tabel. 

### CRUD (Create, Read, Update, Delete)
Proyek ini mengikuti prinsip CRUD sebagai berikut:
- **Create**: Admin dapat menambahkan siswa baru ke dalam database.
- **Read**: Admin dan siswa dapat melihat data siswa yang ada.
- **Update**: Admin dapat mengubah informasi siswa, termasuk pemberian remidi untuk siswa yang tidak lulus.
- **Delete**: Admin dapat menghapus data siswa dari database, dan data yang dihapus disimpan dalam backup untuk referensi.

Dengan sistem ini, diharapkan manajemen data siswa menjadi lebih efisien dan terorganisir.


