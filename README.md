##program adu cepat matematika.##

- Setiap 10 detik, program di server akan menggenerate soal matematika secara random dengan min. 4 operator.
  Misal : 7 * 3 + 5 * 6 / 2 
- Program di server akan membroadcast soal matematika tersebut ke setiap klien
- Dari setiap klien, server hanya menganggap jawaban pertama yang dikirimkan di tiap soalnya
- Klien hanya diberi waktu 10 detik untuk mengetik jawaban, yaitu hingga mendapat soal berikutnya.
- Satu putaran terdiri atas 10 soal.
- Di akhir putaran, server akan menginfokan ke semua klien, skor semua peserta dan pemenangnya.
- Skor tiap soal : Benar + 5, Salah / Tidak Menjawab 0
- Putaran akan dimulai beberapa detik setelah server sudah mendapat 3 koneksi aktif dari klien.

Hints :
Untuk membersihkan layar, dapat menggunakan module os.
Gunakanlah thread, queue, dan select untuk mengimplementasikan

Struktur folder:
- nrp1_nrp2
- client
    client.py

- server
    server.py

File program diupload dengan format nrp1_nrp2.zip untuk mempermudah pengecekan plagiarisme.

Cukup salah satu anggota kelompok yang melakukan upload.
Jika ada pertanyaan silakan email ke bagus.jati@gmail.com.