# RAT-IN-MAZE

Nama: Fina Aprilia

NIM:  21120124140125

Rat in Maze solver using backtracking algorithm.

## Deskripsi
Program ini merupakan implementasi algoritma **Backtracking** untuk menyelesaikan permasalahan *Rat in a Maze*.  
Tujuannya adalah menemukan jalur dari titik awal ke titik tujuan dalam sebuah maze (labirin).

Maze direpresentasikan dalam bentuk matriks 2D:
- `1` = jalan yang dapat dilewati
- `0` = rintangan / tembok

---

## Algoritma
Algoritma yang digunakan adalah **Backtracking**, yaitu:
- Mencoba semua kemungkinan jalur
- Jika jalur buntu, kembali ke langkah sebelumnya (backtracking)
- Berhenti ketika jalur menuju tujuan ditemukan

---

## Cara Kerja
1. Mulai dari posisi `(0,0)`
2. Cek apakah posisi valid
3. Tandai jalur yang dilewati
4. Coba 4 arah:
   - Bawah
   - Kanan
   - Atas
   - Kiri
5. Jika tidak ada jalan → lakukan backtracking
6. Berhenti saat mencapai `(N-1, N-1)`
