import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Mahasiswa")
        self.root.geometry("600x400")
        self.root.configure(bg='white')
        
        # Penyimpanan data dan ID counter
        self.students = []
        self.current_id = 1
        
        self.create_widgets()
    
    def create_widgets(self):
        # Frame utama
        main_frame = tk.Frame(self.root, bg='white', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Frame untuk bidang input
        input_frame = tk.Frame(main_frame, bg='white')
        input_frame.pack(fill='x', pady=(0, 20))
        
        # Bidang ID (readonly)
        id_label = tk.Label(input_frame, text="ID :", font=('Arial', 12), bg='white')
        id_label.grid(row=0, column=0, sticky='e', padx=(0, 10), pady=5)
        
        self.id_entry = tk.Entry(input_frame, font=('Arial', 12), width=40, relief='solid', bd=2, state='readonly')
        self.id_entry.grid(row=0, column=1, pady=5, sticky='w')
        self.id_entry.configure(readonlybackground='white')
        
        # Bidang Nama
        name_label = tk.Label(input_frame, text="NAMA :", font=('Arial', 12), bg='white')
        name_label.grid(row=1, column=0, sticky='e', padx=(0, 10), pady=5)
        
        self.name_entry = tk.Entry(input_frame, font=('Arial', 12), width=40, relief='solid', bd=2)
        self.name_entry.grid(row=1, column=1, pady=5, sticky='w')
        
        # Bidang NIM
        nim_label = tk.Label(input_frame, text="NIM :", font=('Arial', 12), bg='white')
        nim_label.grid(row=2, column=0, sticky='e', padx=(0, 10), pady=5)
        
        self.nim_entry = tk.Entry(input_frame, font=('Arial', 12), width=40, relief='solid', bd=2)
        self.nim_entry.grid(row=2, column=1, pady=5, sticky='w')
        
        # Frame untuk tombol-tombol
        button_frame = tk.Frame(main_frame, bg='white')
        button_frame.pack(fill='x', pady=(0, 20))
        
        # Tombol Tambah
        tambah_btn = tk.Button(button_frame, text="Tambah", font=('Arial', 10), 
                              relief='solid', bd=2, padx=20, command=self.tambah_data)
        tambah_btn.grid(row=0, column=0, padx=(0, 10))
        
        # Tombol Update
        update_btn = tk.Button(button_frame, text="Update", font=('Arial', 10), 
                              relief='solid', bd=2, padx=20, command=self.update_data)
        update_btn.grid(row=0, column=1, padx=(0, 10))
        
        # Tombol Hapus
        hapus_btn = tk.Button(button_frame, text="Hapus", font=('Arial', 10), 
                             relief='solid', bd=2, padx=20, command=self.hapus_data)
        hapus_btn.grid(row=0, column=2)
        
        # Area tampilan data
        display_frame = tk.Frame(main_frame, bg='white', relief='solid', bd=2)
        display_frame.pack(fill='both', expand=True)
        
        # Label header
        header_label = tk.Label(display_frame, text="TAMPILKAN DATA", font=('Arial', 12, 'bold'), 
                               bg='white', pady=10)
        header_label.pack()
        
        # Treeview untuk menampilkan data
        columns = ('ID', 'Nama', 'NIM')
        self.tree = ttk.Treeview(display_frame, columns=columns, show='headings', height=8)
        
        # Konfigurasi heading kolom
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor='center')
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(display_frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Memasang treeview dan scrollbar
        self.tree.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        scrollbar.pack(side='right', fill='y', pady=10)
        
        # Mengikat event pemilihan
        self.tree.bind('<<TreeviewSelect>>', self.on_select)
    
    def tambah_data(self):
        name_val = self.name_entry.get().strip()
        nim_val = self.nim_entry.get().strip()
        
        # Cek apakah field nama dan NIM terisi
        if not all([name_val, nim_val]):
            messagebox.showwarning("Peringatan", "Nama dan NIM harus diisi!")
            return
        
        # Generate ID otomatis
        id_val = str(self.current_id)
        
        # Menambahkan ke data
        self.students.append((id_val, name_val, nim_val))
        self.tree.insert('', 'end', values=(id_val, name_val, nim_val))
        self.clear_entries()
        self.current_id += 1  # Increment ID untuk data berikutnya
        messagebox.showinfo("Sukses", "Data berhasil ditambahkan!")
    
    def update_data(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data yang akan diupdate!")
            return
        
        name_val = self.name_entry.get().strip()
        nim_val = self.nim_entry.get().strip()
        
        # Cek apakah field nama dan NIM terisi
        if not all([name_val, nim_val]):
            messagebox.showwarning("Peringatan", "Nama dan NIM harus diisi!")
            return
        
        # Memperbarui data
        item = selected[0]
        old_values = self.tree.item(item, 'values')
        id_val = old_values[0]  # Menggunakan ID yang sudah ada
        
        # Memperbarui dalam penyimpanan
        for i, student in enumerate(self.students):
            if student[0] == id_val:
                self.students[i] = (id_val, name_val, nim_val)
                break
        
        # Memperbarui dalam treeview
        self.tree.item(item, values=(id_val, name_val, nim_val))
        self.clear_entries()
        messagebox.showinfo("Sukses", "Data berhasil diupdate!")
    
    def hapus_data(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data yang akan dihapus!")
            return
        
        if messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus data ini?"):
            item = selected[0]
            values = self.tree.item(item, 'values')
            
            # Menghapus dari penyimpanan
            self.students = [s for s in self.students if s[0] != values[0]]
            
            # Menghapus dari treeview
            self.tree.delete(item)
            self.clear_entries()
            messagebox.showinfo("Sukses", "Data berhasil dihapus!")
    
    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            item = selected[0]
            values = self.tree.item(item, 'values')
            
            # Mengisi entri dengan data yang dipilih
            self.clear_entries()
            self.id_entry.configure(state='normal')
            self.id_entry.insert(0, values[0])
            self.id_entry.configure(state='readonly')
            self.name_entry.insert(0, values[1])
            self.nim_entry.insert(0, values[2])
    
    def clear_entries(self):
        # Membersihkan semua field entri
        self.id_entry.configure(state='normal')
        self.id_entry.delete(0, tk.END)
        self.id_entry.configure(state='readonly')
        self.name_entry.delete(0, tk.END)
        self.nim_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()