# Nama : Muhammad Apzirza Rafi
# NIM  : 24106050077
import time

class Node:
    def __init__(self, nama, nim, berita):
        self.nama = nama
        self.nim = nim
        self.berita = berita
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # 1. Insert Berita (Selalu di akhir)
    def insert_berita(self, nama, nim, berita):
        new_node = Node(nama, nim, berita)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
        self.size += 1
        print("Berita berhasil ditambahkan ke sistem.")

    # 2. Hapus Berita (Berdasarkan nomor urut)
    def hapus_berita(self, nomor):
        if not self.head:
            print("List kosong, tidak ada berita untuk dihapus.")
            return
        if nomor < 1 or nomor > self.size:
            print("Nomor berita tidak valid!")
            return

        curr = self.head
        for _ in range(nomor - 1):
            curr = curr.next

        if self.size == 1:
            self.head = None
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            if curr == self.head:
                self.head = curr.next
        
        self.size -= 1
        print(f"Berita '{curr.berita}' telah dihapus.")

    # 3. Tampilkan Forward (TANPA HENTI)
    def tampil_forward(self):
        if not self.head:
            print("Belum ada berita untuk ditampilkan.")
            return
        print("\n--- RUNNING TEXT (FORWARD) - Putar Terus ---")
        print("(Tekan Ctrl+C untuk berhenti)")
        
        curr = self.head
        try:
            while True:  # Loop tanpa henti secara circular
                print(f"[{curr.nama} - {curr.nim}] Berita: {curr.berita}")
                curr = curr.next
                time.sleep(3) # Jeda 3 detik
        except KeyboardInterrupt:
            print("\nProses dihentikan oleh user.")

    # 4. Tampilkan Backward (TANPA HENTI)
    def tampil_backward(self):
        if not self.head:
            print("Belum ada berita untuk ditampilkan.")
            return
        print("\n--- RUNNING TEXT (BACKWARD) - Putar Terus ---")
        print("(Tekan Ctrl+C untuk berhenti)")
        
        curr = self.head.prev # Mulai dari Tail
        try:
            while True:  # Loop tanpa henti secara circular mundur
                print(f"[{curr.nama} - {curr.nim}] Berita: {curr.berita}")
                curr = curr.prev
                time.sleep(3)
        except KeyboardInterrupt:
            print("\nProses dihentikan oleh user.")

    # 5. Tampilkan Berita Tertentu
    def tampil_tertentu(self, nomor):
        if not self.head or nomor < 1 or nomor > self.size:
            print("Berita tidak ditemukan!")
            return
        curr = self.head
        for _ in range(nomor - 1):
            curr = curr.next
        print(f"Hasil: [{curr.nama} - {curr.nim}] {curr.berita}")

def main():
    cdll = CircularDoublyLinkedList()
    while True:
        print("\n=== MENU SIMULASI BERITA TV (CDLL PYTHON) ===")
        print("1. Insert Berita")
        print("2. Hapus Berita (Nomor Urut)")
        print("3. Tampilkan Forward (LOOPING SELAMANYA)")
        print("4. Tampilkan Backward (LOOPING SELAMANYA)")
        print("5. Tampil Berita Tertentu")
        print("6. Exit")
        
        pilihan = input("Pilih Menu: ")

        if pilihan == '1':
            nama = input("Masukkan Nama: ")
            nim = input("Masukkan NIM: ")
            txt = input("Masukkan Teks Berita: ")
            cdll.insert_berita(nama, nim, txt)
        elif pilihan == '2':
            try:
                no = int(input("Nomor berita yang dihapus: "))
                cdll.hapus_berita(no)
            except ValueError:
                print("Input harus angka!")
        elif pilihan == '3':
            cdll.tampil_forward()
        elif pilihan == '4':
            cdll.tampil_backward()
        elif pilihan == '5':
            try:
                no = int(input("Nomor berita yang dicari: "))
                cdll.tampil_tertentu(no)
            except ValueError:
                print("Input harus angka!")
        elif pilihan == '6':
            print("Program Berhenti. Terima kasih!")
            break
        else:
            print("Pilihan tidak tersedia.")

if __name__ == "__main__":
    main()