# README.md
Nawala Patra: Tugas UTS PBP.

## *Anggota Kelompok E-12*
- Alma Putri Nashrida (2206814671)
- Azka Nydia Estiningtyas (2206028970)
- Natanael Bonaparte Halomoan Nababan (2206828310)
- Naufal Aulia (2206082455)
- Mochammad Wahyu Suryansyah (2206083142)

## *Latar Belakang*
Nawala Patra adalah aplikasi daring yang dibuat untuk membantu misi Kongres Bahasa Indonesia XII yaitu “Literasi dalam Kebhinekaan untuk Kemajuan Bangsa.” Nawala Patra sendiri berasal dari bahasa sansekerta yang artinya tulisan atau karangan. Aplikasi ini memiliki cakupan tidak hanya user sebagai pembaca, tetapi user dapat mengunggah buku atau karangannya sendiri sebagai penulis. User juga dapat menyarankan ataupun me-request buku yang user inginkan. Selain itu, kami sangat meyakini user sangat ingin berdiskusi terkait buku yang mereka baca. Maka kami menyediakan sebuah forum diskusi mengenai topik yang user inginkan. User dapat membuka topik, ataupun merespon topik yang user lain buka.

## *Dataset*

Nawala Patra menggunakan dataset pada link [berikut.](https://github.com/uchidalab/book-dataset/blob/master/Task1/book30-listing-test.csv)


## *Daftar Modul*

Nawala Patra memiliki beberapa modul yaitu:

### 🏛️ Library 🏛️

Berisi kumpulan-kumpulan buku yang tersedia pada Nawala Patra. User dapat mencari buku yang diinginkan dengan menggunakan fitur search yang tersedia. User Login dapat menggunakan fitur bookmark buku untuk menyimpan buku pilihannya.


### 📚 MyBooks 📚
Berisi kumpulan-kumpulan buku yang sudah disimpan menggunakan fitur bookmark dan buku-buku yang sudah di-publish. Hanya User Login yang dapat mengakses modul MyBooks.


### 🎖️ LeaderBoard 🎖️
Menampilkan sebuah LeaderBoard Buku berdasarkan voting dari User Login. User Guest hanya bisa melihat LeaderBoard tanpa bisa melakukan voting.


### 🧵 Discussion Forum 🧵
Menampilkan forum-forum diskusi yang dibuat/dimulai oleh User Login. Forum diskusi bisa membahas spesifik suatu buku atau sekedar topik-topik mengenai literasi. User Guest hanya bisa membaca dan melihat diskusi yang tersedia tanpa bisa ikut andil dalam forum yang tersedia. 


### 🧩 Writer’s Jam 🧩
Sebuah section dimana User Login dapat melakukan submisi karya atau buku setiap minggunya. Pada bagian ini, terdapat tema-tema yang berbeda. User Guest hanya bisa melihat karya yang ditampilkan, tidak bisa melakukan submisi.



## *Role dan Peran pengguna*

| Fitur | User (Logged in) | Guest |
| - | - | - |
| Library |  Dapat menggunakan fitur search dan add bookmark. | Hanya bisa menggunakan fitur search buku. |
| MyBooks | Dapat lihat buku yang sedang atau selesai dibaca dan melihat karya sendiri. | Tidak dapat mengakses MyBooks. |
| LeaderBoard | Bisa melihat semua leaderboard dan berpartisipasi dalam poll/voting (menambah opsi / memberi suara). | Hanya bisa melihat leaderboard ranking atas saja dan tidak dapat berpartisipasi dalam poll/voting. |
| Discussion Forum | Dapat membaca dan berpartisipasi dalam diskusi di comment section seperti memulai diskusi atau me-reply sebuah diskusi. | Hanya bisa membaca comment section, tetapi tidak bisa berpartisipasi dalam diskusi. |
| Writer's Jam | Dapat mengunggah karya pada prompt yang diberikan di minggu tersebut dan dapat melihat karya-karya pada prompt sebelumnya. | Dapat melihat prompt minggu ini dan karya penulis, tetapi tidak bisa melihat prompt sebelumnya atau berpartisipasi dalam writer's jam. |

## *tes dev merge*
