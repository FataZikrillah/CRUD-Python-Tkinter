import tkinter as tk
import sqlite3

# 🔗 Koneksi ke database 'visual.db'
conn = sqlite3.connect('visual.db')
cursor = conn.cursor()

# 📦 Buat tabel 'user' jika belum ada
cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        password TEXT NOT NULL
    )
""")
conn.commit()

# ➕ Fungsi Tambah Data
def tambah_data():
    nama = entry_nama.get()
    password = entry_password.get()
    if nama and password:
        cursor.execute("INSERT INTO user (nama, password) VALUES (?, ?)", (nama, password))
        conn.commit()
        tampil_data()
        entry_nama.delete(0, tk.END)
        entry_password.delete(0, tk.END)
    else:
        tk.messagebox.showwarning("Input Error", "Semua field harus diisi")

# 📋 Fungsi Tampilkan Data
def tampil_data():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM user")
    for row in cursor.fetchall():
        listbox.insert(tk.END, row)

# 🗑️ Fungsi Hapus Data
def hapus_data():
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected[0])
        cursor.execute("DELETE FROM user WHERE id=?", (item[0],))
        conn.commit()
        tampil_data()
    else:
        tk.messagebox.showwarning("Pilih Data", "Pilih data yang akan dihapus")

# ✏️ Fungsi Update Data
def update_data():
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected[0])
        nama = entry_nama.get()
        password = entry_password.get()
        if nama and password:
            cursor.execute("UPDATE user SET nama=?, password=? WHERE id=?", (nama, password, item[0]))
            conn.commit()
            tampil_data()
        else:
            tk.messagebox.showwarning("Input Error", "Semua field harus diisi")
    else:
        tk.messagebox.showwarning("Pilih Data", "Pilih data yang akan diupdate")

# 📌 Fungsi Tampilkan Data ke Input Field
def pilih_data(event):
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected[0])
        entry_nama.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        entry_nama.insert(0, item[1])
        entry_password.insert(0, item[2])

# 🖼️ UI Tkinter
root = tk.Tk()
root.title("Aplikasi CRUD User")

tk.Label(root, text="Nama").grid(row=0, column=0, padx=5, pady=5)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="NIM").grid(row=1, column=0, padx=5, pady=5)
entry_password = tk.Entry(root, show='*')
entry_password.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Tambah", command=tambah_data).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="Update", command=update_data).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Hapus", command=hapus_data).grid(row=2, column=2, padx=5, pady=5)

listbox = tk.Listbox(root, width=50)
listbox.grid(row=3, column=0, columnspan=3, padx=5, pady=10)
listbox.bind("<<ListboxSelect>>", pilih_data)

tampil_data()
root.mainloop()
