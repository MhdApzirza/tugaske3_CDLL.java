Tugas ke-3 Struktur Data Kelas A

Nama: Muhammad Apzirza Rafi
NIM: 24106050077

Implementasi: Simulasi Running Text Berita menggunakan Circular Doubly Linked List (CDLL) dalam bahasa Java dan Python.

📝 Deskripsi Tugas
Program ini dibuat untuk mensimulasikan teks berita berjalan (running text) seperti yang sering tampil di televisi. Data dikelola menggunakan struktur data Circular Doubly Linked List manual tanpa menggunakan library eksternal.

Dalam struktur ini, setiap Node membawa dua catatan alamat sekaligus: alamat sesudahnya (next) dan alamat sebelumnya (prev). Sifatnya yang melingkar (circular) memungkinkan navigasi dari berita terakhir kembali ke berita pertama tanpa terputus.

🚀 Fitur Menu
- Insert Berita: Menambahkan berita baru (Nama, NIM, Teks) yang selalu ditempatkan di akhir list.
- Hapus Berita: Menghapus data berita berdasarkan nomor urut yang dipilih user.
- Tampilkan Forward: Menampilkan teks berita secara berurutan dari depan ke belakang dengan jeda (delay) 3 detik antar berita.
- Tampilkan Backward: Menampilkan teks berita secara mundur dari belakang ke depan dengan jeda (delay) 3 detik antar berita.
- Tampil Berita Tertentu: Menampilkan satu berita spesifik berdasarkan nomor urut.
- Exit: Keluar dari program.

⚙️ Detail Implementasi
Memory: Menggunakan alokasi memori dinamis (terpencar) di mana setiap Node saling terhubung melalui pointer next dan prev.

- Circular Logic: Tail.next menunjuk ke Head, dan Head.prev menunjuk ke Tail.
- Language: Tersedia dalam versi Java (.java) dan Python (.py).

🎥 Video Demo
Daftar operasi (Insert, Delete, & Display dengan Delay) menggunakan Circular Doubly Linked List:

**[Nonton Video Demo](https://youtu.be/B086LKm60gQ?si=G1eGfzAMaBbiTvia)**
*Klik gambar di atas untuk memutar video demo di YouTube @Muhammad Apzirza Rafi.*