# Sistem Manajemen Data Mahasiswa

Aplikasi manajemen data mahasiswa sederhana yang dibangun dengan Python dan Tkinter yang menyediakan operasi CRUD (Create, Read, Update, Delete).

## Fitur

- Membuat data mahasiswa baru dengan ID yang dibuat otomatis
- Melihat data mahasiswa dalam format tabel
- Memperbarui informasi mahasiswa yang ada
- Menghapus data mahasiswa
- Antarmuka pengguna yang bersih dan modern
- Validasi input untuk field yang wajib diisi

## Detail Teknis

### Dependensi
- Python 3.x
- Tkinter (sudah termasuk dalam pustaka standar Python)

### Komponen
- **Kelas StudentApp**: Kelas utama aplikasi yang menangani:
  - Pembuatan antarmuka pengguna
  - Pengelolaan data
  - Operasi CRUD
  - Penanganan event

### Antarmuka Pengguna
- Field input:
  - ID (dibuat otomatis, hanya baca)
  - Nama
  - NIM
- Tombol aksi:
  - Tambah
  - Update
  - Hapus
- Tampilan data menggunakan Treeview dengan kolom:
  - ID
  - Nama
  - NIM
