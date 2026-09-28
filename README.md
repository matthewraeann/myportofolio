Nama : Matthew Raeann Alexandra
NPM : 2506544763
Kelas : PBP B

### Tugas 1
1. Ya, saya menggunakan <section>. Section memungkinkan saya untuk membagi halaman web di bagian body menjadi beberapa section seperti section hero dan portofolio. Section memudahkan dalam pemetaan visual sehingga tidak perlu menumpuk tag <div>. Selain itu secara fungsionalitas, penggunaan elemen semantik akan membuat halaman web memiliki aksesibilitas yang lebih baik bagi pengguna screen reader.
2. Saat saya mengatur CSS agar tetap responsive, tantangan yang saya alami adalah ketika mengatur tampilan multi kolom agar tampilan tetap bagus ketika layar menyempit. Untuk mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile, saya memutuskan untuk membuat agar alur informasi yang diberikam tetap sama dan tampilannya tetap enak dilihat. Pada bagian Experience logo berada di kiri sementara contentnya di kanan. Saat layar menjadi sempit saya memutuskan untuk membuat logonya menjadi di atas content dengan ukuran yang lebih kecil dengan cara mengubah flex direction dari row menjadi column dan mengubah weidth dan height.
3. Kekurangan dari web statis adalah ketika ingin menambahkan experience baru, saya perlu mengubah kode html saya secara manual. Saya tidak bisa menambahakannya langsung di website seperti di linked in. Web statis membuat user tidak bisa berinteraksi secara real-time. Untuk iterasi proyek selanjutnya saya ingin mengintegrasikan kode yang sudah ada dengan JavaScript agar dapat menambahkan fungsionalitas dinamis. 

#### AI Disclosure Tugas 1
Pada tugas ini saya menggunakan Gemini model 3.1 Pro untuk membantu saya mengerjakan tugas ini. 
AI teresbut saya gunakan untuk:
1. Membantu memahami kode yang sudah diberikan dari tutorial 1
2. Membantu memahami cara kerja grid, margin, padding.
3. Meminta membuatkan gambaran kasar untuk membuat section Experience
4. Membantu dalam membuat tampilan website tidak rusak ketika lebar layar menjadi sempit dam memiliki tampilan yang lebih baik.
5. Bertanya mengenai git command.

Secara keseluruhan output yang dikeluarkan oleh AI sudah benar dan tidak ada misinformasi. Namun, pada bagian gambaran kasar untuk membuat section Experience. Output dari AI tidak benar benar saya ikuti semua karena tidak sesuai dengan preferensi saya. AI dapat memberikan jawaban dengan benar namun kita tidak bisa 100% mengikutinya karena AI tidak mendapatkan context mengenai bagaimana saya ingin website saya dibuat dan layout website seperti apa yang saya inginkan.

Log Gemini: https://share.gemini.google/3BzUadzycpTK

### Tugas 2
1. Ketika pengguna membuka halaman portofolio baru, browser pengguna akan mengirimkan request ke server django, kemudian Django akan memeriksa urls.py di direktori utama. Jika URL nya cook, maka akan diteruskan ke fungsi include() ke urls.py milik aplikasi (dalam kasus web saya yaitu aplikasi main). Kemudian urls.py milik aplikasi akan mengecek sisa path dan memetakannya ke fungsi view tertentu (misalnya sisa path "education/" ke fungsi "show_education"). Kemudian view akan memerima request tersebut dan akan meminta data dari model/database dan mereturn context yang sudah berisi data dari model. selain model view juga akan mereturn template yang sudah dapat diisi oleh data dari model sehingga dapat menampilkan tampilan website yang sudah bersisi data dari model melalui file html.

2. Agar website menjadi dinamis. Jika ditulis langsung di template website akan menjadi statis. 

Pengruh dalam pemeliharaan :
Jika menuliskan langsung di file html, setiap kali ingin menambahkan data baru (misal pengalaman baru ataupun riwayat edukasi baru), maka perlu mengubah kodenya secara manual di file html, yang mana hal tersebut sangatlah tidak praktis. Sementara jika kita menggunakan Model untuk menyimpan data, kita dapat menambahkan, menghapus, ataupun mengedit data secara instan melalui django admin tanpa perlu menyentuh kode yang sudah dibuat sama sekali. Jika kode tidak diubah, artinya kita tidak perlu men deploy ulang kode html.

Pengaruh dalam pengembangan :
Pemisahan antara tampilan (Template) dengan data (Model) mematuhi prinsip Separation of Concerns. Hal ini memungkinkan kita untuk mengembangkan fitur dengan mudah di masa depan. Contohnya menambahkan fitur filter bedasarkan kategori ataupun fitur sort berdasarkan tanggal.

3. Perintahmakemigration berfungsi untuk mencatat perubahan yang ada pada model dengan membuat file migration. Perintah ini belum mengubah database sama sekali. Sementara migrate berfungsi untuk menjalankan file migrasi yang telah dibuat oleh perintah makemigration dan menerapkannya ke sistem database yang ada.

Contoh: Ketika membuat class education di file models.py di app main, saya perlu untuk menjalankan perintah makemigration dan juga migrate agar django dapat mengimplementasikannya ke dalam database.

#### AI Disclosure Tugas 2
Pada tugas ini saya menggunakan Gemini model 3.8 Flash untuk membantu saya mengerjakan tugas ini. 
AI teresebut saya gunakan untuk:
1. Membantu memahami kode yang sudah diberikan dari tutorial 2
2. Membantu memahami cara mengecek, menambahkan, menghapus, dan mengedit data di database yang ada.
3. Membantu memahami jenis-jenis field yang ada dalam model.

Secara keseluruhan output yang dikeluarkan oleh AI sudah benar dan tidak ada missinformasi. 

Log Gemini: https://share.gemini.google/wkGJh5nWgzZa

### Tugas 3
1. Karena dengan menggunakan ModelForm kita tidak perlu menghabiskan waktu dan energi untuk membuat form HTML secara manual dan menentukan aturan validasinya sendiri. ModelForm dapat membaca model yang sudah kita definisikan di models.py dan secara otomatis membuatkan form HTMLnya beserta dengan aturan validasi field-fieldnya. Fungsi {% csrf_token %} adalah menjaga keamanan web tersebut dari serangan siber. Saat form di render, tag tersebut akan berubah menjadi sebuah kode rahasia yang terdiri dari kombinasi angka dan huruf yang sangat panjang. Saat form dikirim, Django akan memeriksa kode tersebut. Jika sama dengan sisi user, form diterima, jika tidak, form ditolak.
2. Pertama, karena ukuran file JSON lebih kecil dan ringan. JSON menggunakan tanda kurung, sementara XML menggunakan  tag. Hal tersebut membuat file XML menjadi lebih besar dan berat. Ukuran file yang lebih kecil juga membuat pengiriman data menjadi lebih cepat. Kedua, Proses pembacaan JSON lebih cepat. Karena JSON berasal dari struktur objek JavaScript, browser dapt mengubah data JSON menjadi objek siap pakai secara instan. Selain itu, komputer juga membutuhkan waktu dan resource yang lebih sedikit untuk menerjemahkan format JSON dibandingkan dengan XML. Ketiga, JSON memiliki struktur yang lebih sederhana dan mudah dipahami karena menggunakan formay key-value seperti dictionary di python. Keempat, Lebih mudah digunakan di berbagai macam bahasa pemrograman. Hampir semua bahasa pemrograman (Seperti python, java, PHP, dll) memiliki library bawaan untuk mengelola data JSON. Selain itu sebagian besar layanan web dan RESTful API juga menggunakan JSON.
3. Pertama Klien akan mengirim permintaan/request. Aplikasi klien akan mengirimkan permintaan HTTP GET ke url yang sudah disiapkan, misalnya http://localhost:8000/api/projects/. Kemudian Django akan memproses permintaan tersebut dan mencocokan alamat dengan yang ada di urls.py. Jika ditemukan maka akan diarahkan ke fungsi view yang ditetapkan, misalnya get_projects_json. Setelah itu di dalam fungsi views akan diambil data dari model kemudian mengubahnya menjadi format JSON dengan melakukan serialisasi. Setelah itu fungsi view akan membungkusnya ke dalam sebuah HttpResponse untuk kemudian dikirim dan diterima oleh klien. Sebelum datanya dikembalikan, kita perlu melakukan serialisasi untuk mengubah struktur data QuerySet dari Model menjadi data dalam format JSON.

#### AI Disclosure Tugas 3
Pada tugas ini saya menggunakan Gemini model 3.1 Pro untuk membantu saya mengerjakan tugas ini. 
AI teresbut saya gunakan untuk:
1. Membantu memahami kode yang sudah diberikan dari tutorial 3
2. Membantu memahami perbedaan dan fungsi JSON dan XML.
3. Meminta bantuan untuk membuat fitur CRUD pada page dan modul Education
4. Membantu memahami alur kerja pengubahan data menjadi JSON
5. Membantu memahami cara sebuah form bekerja dalam Django

Secara keseluruhan output yang dikeluarkan oleh AI sudah benar dan tidak ada misinformasi. Namun, output dari AI tidak benar benar saya ikuti semua karena AI tersebut tidak memliki data mengenai apa saja yang sudah atau belum ada dalam kode di repositori kita. AI dapat memberikan jawaban dengan benar namun kita tidak bisa 100% mengikutinya karena AI belum tentu memeberikan jawaban sesuai dengan yang kita butuhkan.

Log Gemini: https://share.gemini.google/J0Enz41PVw1S

#### AI Disclosure Tugas 4
Pada tugas ini saya menggunakan Gemini model 3.1 Pro (Antigravity) untuk membantu saya mengerjakan tugas ini. 
AI teresbut saya gunakan untuk:
1. Membantu memahami requirements Tugas 4 dan membuat rencana pengerjaan Tugas 4
2. Memberikan langkah-langkah pengerjaan dan pseudocode agar pengerjaan Tugas menjadi lebih terstruktur
3. Memodifikasi Tempalte (html)
4. Mencari error dan debugging

Secara keseluruhan output yang dikeluarkan oleh AI sudah benar dan tidak ada misinformasi. Saya memberikan instruksi dimana AI dilarang untuk menulis kode blok secara langsung, melainkan memberikan penjelasan langkah-langkah dan pseudocodenya. Kemudian hasil pengerjaan saya baru di review oleh AI untuk diperiksa kembali apakah ada kesalahan atau tidak.

Log Gemini: Saat ini Antigravity belum menyediakan fitur share chat log. Sebagai pengganti saya salin log AI ke dalam file /AI_CHAT_LOG/Tugas4.md