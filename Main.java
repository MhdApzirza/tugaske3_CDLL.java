import java.util.Scanner;

// Kelas Node untuk menyimpan data dan pointer
class Node {
    String nama, nim, berita;
    Node next, prev;

    Node(String nama, String nim, String berita) {
        this.nama = nama;
        this.nim = nim;
        this.berita = berita;
        this.next = null;
        this.prev = null;
    }
}

// Struktur data Circular Doubly Linked List
class CircularDoublyLinkedList {
    Node head = null;
    int size = 0;

    // 1. Insert Berita (Selalu di akhir)
    public void insertBerita(String nama, String nim, String berita) {
        Node newNode = new Node(nama, nim, berita);
        if (head == null) {
            head = newNode;
            head.next = head;
            head.prev = head;
        } else {
            Node tail = head.prev;
            tail.next = newNode;
            newNode.prev = tail;
            newNode.next = head;
            head.prev = newNode;
        }
        size++;
        System.out.println("Berita berhasil ditambahkan ke sistem.");
    }

    // 2. Hapus Berita (Berdasarkan nomor urut)
    public void hapusBerita(int nomor) {
        if (head == null) {
            System.out.println("List kosong, tidak ada berita untuk dihapus.");
            return;
        }
        if (nomor < 1 || nomor > size) {
            System.out.println("Nomor berita tidak valid!");
            return;
        }

        Node curr = head;
        for (int i = 1; i < nomor; i++) {
            curr = curr.next;
        }

        if (size == 1) {
            head = null;
        } else {
            curr.prev.next = curr.next;
            curr.next.prev = curr.prev;
            if (curr == head) {
                head = curr.next;
            }
        }
        size--;
        System.out.println("Berita '" + curr.berita + "' telah dihapus.");
    }

    // 3. Tampilkan Forward (Maju dengan delay 3 detik)
    public void tampilForward() {
        if (head == null) {
            System.out.println("Belum ada berita untuk ditampilkan.");
            return;
        }
        System.out.println("\n--- RUNNING TEXT (FORWARD) ---");
        Node curr = head;
        for (int i = 0; i < size; i++) {
            System.out.println("[" + curr.nama + " - " + curr.nim + "] Berita: " + curr.berita);
            curr = curr.next;
            try {
                Thread.sleep(3000); // Jeda 3 detik
            } catch (InterruptedException e) {
                System.out.println("Error pada delay.");
            }
        }
    }

    // 4. Tampilkan Backward (Mundur dengan delay 3 detik)
    public void tampilBackward() {
        if (head == null) {
            System.out.println("Belum ada berita untuk ditampilkan.");
            return;
        }
        System.out.println("\n--- RUNNING TEXT (BACKWARD) ---");
        Node curr = head.prev; // Mulai dari Tail
        for (int i = 0; i < size; i++) {
            System.out.println("[" + curr.nama + " - " + curr.nim + "] Berita: " + curr.berita);
            curr = curr.prev;
            try {
                Thread.sleep(3000); // Jeda 3 detik
            } catch (InterruptedException e) {
                System.out.println("Error pada delay.");
            }
        }
    }

    // 5. Tampilkan Berita Tertentu
    public void tampilTertentu(int nomor) {
        if (head == null || nomor < 1 || nomor > size) {
            System.out.println("Berita tidak ditemukan!");
            return;
        }
        Node curr = head;
        for (int i = 1; i < nomor; i++) {
            curr = curr.next;
        }
        System.out.println("Hasil: [" + curr.nama + " - " + curr.nim + "] " + curr.berita);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        CircularDoublyLinkedList cdll = new CircularDoublyLinkedList();
        int pilihan;

        do {
            System.out.println("\n=== MENU SIMULASI BERITA TV (CDLL) ===");
            System.out.println("1. Insert Berita");
            System.out.println("2. Hapus Berita (Nomor Urut)");
            System.out.println("3. Tampilkan Forward (Delay 3s)");
            System.out.println("4. Tampilkan Backward (Delay 3s)");
            System.out.println("5. Tampil Berita Tertentu");
            System.out.println("6. Exit");
            System.out.print("Pilih Menu: ");
            pilihan = input.nextInt();
            input.nextLine(); // membersihkan buffer

            switch (pilihan) {
                case 1:
                    System.out.print("Masukkan Nama: ");
                    String nama = input.nextLine();
                    System.out.print("Masukkan NIM: ");
                    String nim = input.nextLine();
                    System.out.print("Masukkan Teks Berita: ");
                    String txt = input.nextLine();
                    cdll.insertBerita(nama, nim, txt);
                    break;
                case 2:
                    System.out.print("Masukkan Nomor Berita yang akan dihapus: ");
                    int noHapus = input.nextInt();
                    cdll.hapusBerita(noHapus);
                    break;
                case 3:
                    cdll.tampilForward();
                    break;
                case 4:
                    cdll.tampilBackward();
                    break;
                case 5:
                    System.out.print("Masukkan Nomor Berita yang dicari: ");
                    int noCari = input.nextInt();
                    cdll.tampilTertentu(noCari);
                    break;
                case 6:
                    System.out.println("Program Berhenti. Terima kasih!");
                    break;
                default:
                    System.out.println("Pilihan tidak tersedia.");
            }
        } while (pilihan != 6);

        input.close();
    }
}