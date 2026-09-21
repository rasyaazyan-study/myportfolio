Nama: Rasya Azyan Kautsar
NPM: 2506538981
Kelas: PBP C

#PERTANYAAN REFLEKTIF
1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti <section>, <article>, atau <aside>? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?

Ya, selama mengerjakan TI 1 saya menggunakan <section> untuk membagi masing-masing bagian dalam web saya. Dengan adanya <section>, saya dapat mengkonfigurasi isi class yang diperlukan (melalui HTML) & warna halaman, padding, ataupun membuat section yang berbentuk miring melalui CSS.

2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?

Selama TI 1, saya biasa mendevelop responsive web dengan secara aktif melihat update di localhost (viewport mobile), jika memang terasa tidak nyaman atau tidak dapat dilihat sama sekali, maka saya akan menambah setting overlap di bagian @media, agar ukuran device yang lebih kecil (mobile) bisa tetap mendapat tampilan yang informatif dan aesthetc.

3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?

Sejauh ini yang saya ketahui dan coba pertimbangkan adalah opsi untuk sekaligus membangun CMS (mungkin menggunakan Django Admin). Agar saya dapat langsung mengubah konten yang ditampilkan tanpa harus mengubah HTML secara terus menerus.

#AI DISCLOSURE

Tugas 1: Dengan ini saya menyatakan menggunakan bantuan Generative AI dengan model Claude (Sonnet 5, Medium Effort) untuk bertanya dan membantu mencari tag HTML / CSS yang belum saya ketahui, sekaligus melakukan debugging jika terdapat bug yang tidak dapat/belum saya pahami letak maupun penyelesaiannya. Namun, penggunaan AI tetap melaui proses pengetikan ulang, pengecekan, serta perbaikan yang dapat dipertanggungjawabkan.

=== TUGAS INDIVIDU 2 ===

#PERTANYAAN REFLEKTIF

1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.

Ketika user membuka web, maka Django akan mengecek melalui portfolio/urls.py apakah user membuka web admin atau web utama, ketika membuka web utama, maka akan diarahkan menuju main/urls.py untuk diarahkan menuju halaman utama (Profile). Di main/urls.py, Django secara default memanggil function show_main di main/views.py yang memanggil model dan merender data ke dalam file html, begitu juga ketika user memilih untuk berpindah halaman maka Django akan memanggil show_experience atau show_education dengan proses yang serupa. Setelah itu, function show akan mengembalikan return file html dengan digabungkan dengan data context dari model untuk diisi ke dalam tag. Dan setelah itu dikirim kembali kepada user sebagai response dari request.

2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.

Karena kode akan jadi sangat panjang, dan setiap menambah data kita harus membuat 1 elemen baru (misal card) yang harus di-deploy ulang. Sedangkan dengan model kita bisa mengupdate via admin tanpa menyentuh kode html sama sekali. Secara kemudahan pemeliharaan dan pengembangan, tentu akan lebih mudah, karena dalam skala tertentu dimana penambahan data dilakukan secara berkala oleh beberapa orang, ini akan sangat memudahkan dan minim potensi konflik pada git.

3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.

makemigrations hanya mencatat rencana perubahan model, sedangkan migrate untuk menjalankan proses pemindahan ke database. Contohnya adalah ketika mau menambah atau menghapus field pada main/models.py, setelah perubahan kita save, maka harus makemigrations dan migrate supaya perubahan tersimpan di database.

#AI DISCLOSURE

Tugas 2: Dengan ini saya menyatakan menggunakan bantuan Generative AI dengan model Claude (Sonnet 5, Medium Effort) untuk membantu melakukan Troubleshooting Organizational Experience saya yang tidak mau di-seed ke Database (karena file seed_portfolio.py masih di gitignore), serta membuat Drawer pada mobile view untuk memudahkan navigasi setelah adanya penambahan menu baru yaitu Education. Penggunaan AI dalam hal ini tetap melewati proses pengecekan lebih lanjut, pemahaman kode, dan dapat dipertanggungjawabkan.

=== TUGAS INDIVIDU 3 ===
1. Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan {% csrf_token %} pada form tersebut!

Dengan ModelForm kita tidak perlu menulis ulang form yang di HTML secara manual, yang mana jika datanya berjumlah banyak akan membuat pengelolaan kode menjadi semakin sulit dan tidak rapi terutama saat terdapat eror atau typo. Dengan ModelForm kita cukup menyediakan template field yang perlu diterapkan di halaman yang diinginkan. 

CSRF Token merupakan kode rahasia yang sifatnya unik dan dibuat oleh server untuk melindungi aplikasi dari unauthorized request, dengan menggunakan {% csrf_token %}, kita dapat mencegah penyerang aplikasi mengubah request yang awalnya ke server Django menjadi ke suatu API yang berbahaya dan mengirim data request ke mereka.

2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?

Karena JSON lebih ringkas, mudah dibaca, dan browser dapat mengubah JSON menjadi objek, tanpa perlu parsing rumit seperti XML.

3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?

Ketika client membuka url, Django akan meneruskan view ke fungsi yang sesuai. Setelah itu, view akan mengambil data dari database, Data diubah menjadi JSON lalu view mengirim teks sebagai response yang dapat dibaca client.

#AI DISCLOSURE

Tugas 3: Dengan ini saya menyatakan menggunakan bantuan Generative AI dengan model Claude (Sonnet 5, Medium Effort) untuk membantu membuat floating button, timeline pada experience, model & views update untuk fitur edit dan delete, serta troubleshooting beberapa kesalahan dalam menulis kode (typo). Penggunaan AI dalam hal ini tetap melewati proses pengecekan lebih lanjut, pemahaman kode, dan dapat dipertanggungjawabkan.