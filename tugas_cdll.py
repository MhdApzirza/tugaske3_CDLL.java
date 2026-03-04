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
        print("Berita berhasil ditambahkan!")

    def hapus_berita(self, nomor):
        if not self.head or nomor < 1 or nomor > self.size:
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
        print(f"Berita '{curr.berita}' berhasil dihapus.")

    def tampil_forward(self):
        if not self.head: return print("Belum ada berita.")
        curr = self.head
        print("\n--- Running Text (Forward) ---")
        for _ in range(self.size):
            print(f"[{curr.nama} - {curr.nim}] Berita: {curr.berita}")
            curr = curr.next
            time.sleep(3)

    def tampil_backward(self):
        if not self.head: return print("Belum ada berita.")
        curr = self.head.prev
        print("\n--- Running Text (Backward) ---")
        for _ in range(self.size):
            print(f"[{curr.nama} - {curr.nim}] Berita: {curr.berita}")
            curr = curr.prev
            time.sleep(3)

    def tampil_tertentu(self, nomor):
        if not self.head or nomor < 1 or nomor > self.size:
            print("Nomor berita tidak ditemukan!")
            return
        curr = self.head
        for _ in range(nomor - 1):
            curr = curr.next
        print(f"Berita ke-{nomor}: [{curr.nama} - {curr.nim}] {curr.berita}")

def main():
    cdll = CircularDoublyLinkedList()
    while True:
        print("\n=== MENU RUNNING TEXT CDLL ===")
        print("1. Insert Berita")
        print("2. Hapus Berita")
        print("3. Tampilkan Forward (Delay 3s)")
        print("4. Tampilkan Backward (Delay 3s)")
        print("5. Tampil Berita Tertentu")
        print("6. Exit")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            nama = input("Masukkan Nama: ")
            nim = input("Masukkan NIM: ")
            txt = input("Masukkan Teks Berita: ")
            cdll.insert_berita(nama, nim, txt)
        elif pilihan == '2':
            no = int(input("Nomor berita yang dihapus: "))
            cdll.hapus_berita(no)
        elif pilihan == '3':
            cdll.tampil_forward()
        elif pilihan == '4':
            cdll.tampil_backward()
        elif pilihan == '5':
            no = int(input("Nomor berita: "))
            cdll.tampil_tertentu(no)
        elif pilihan == '6':
            break

if __name__ == "__main__":
    main()