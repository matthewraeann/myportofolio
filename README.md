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

### Tugas 5
1. Debouncing adalah teknik untuk menunda sebuah fungsi hingga suatu jeda waktu berlalu tanpa event baru. Selama pengguna masih mengetik, timer sebelumnya dibatalkan dan dimulai lagi. Dengan demikian, browser hanya mengirim permintaan setelah pengguna berhenti mengetik selama sejenak. Debouncing penting agar fungsi tidak dipanggil secara terus menerus untuk event-event yang datangnya berdekatan. Tanpa debouncing ketika kita melakukan search maka setiap karakter yang ditambahkan dan dihapus akan mengirimkan request ke server dan dapat membebani server. Dengan debouncing request hanya terjadi ketika terdapat jeda dalam kurun waktu tertentu antar event. Sehingga jumlah request yang dikirim ke server jauh lebih sedikit dan tidak membuat server menjadi lambat.

2. Await adalah keyword yang hanya bisa digunakan di dalam async function dan berfungsi untuk menunggu sebuah Promise selesai diproses sebelum melanjutkan ke baris kode berikutnya. Fungsi `fetch()` mengembalikan Promise, sehingga dengan `await fetch(url)` kita menunggu sampai server membalas dan mendapatkan objek Response yang bisa dicek dengan `response.ok` lalu dibaca dengan `await response.json()`. Jika tidak menggunakan await, kode berikutnya akan langsung dieksekusi sebelum server membalas, sehingga `response` masih berupa Promise. Akibatnya `response.ok` bernilai `undefined`, `response.json()` error, dan data tidak dapat ditampilkan.

3. Cross-Site Scripting (XSS) adalah serangan ketika penyerang berhasil menyisipkan kode JavaScript miliknya ke dalam halaman web yang kemudian dijalankan di browser pengguna lain. Data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan XSS daripada melalui tempalte django karena Template Django melakukan auto-escaping pada setiap { variabel }. Ketika menggunakan AJAX tidak ada lagi yang melakukan escaping sehingga browser akan memperlakukan setiap tag HTML di dalam data sebagai kode sungguhan.

#### AI Disclosure Tugas 5
Pada tugas ini saya menggunakan Gemini model 3.1 Pro (Antigravity) untuk membantu saya mengerjakan tugas ini. 
AI teresbut saya gunakan untuk:
1. Memandu pengerjaan Tutorial 5 dan Tugas 5 secara bertahap dengan aturan read-only. AI hanya menjelaskan konsep, fungsi/method Django yang dipakai, dan pseudocode, sedangkan logika utama (views, urls, forms, template tag, CSRF) saya tulis sendiri. Bagian yang repetitif (CSS, HTML tampilan, toast.js) disediakan dengan bagian penting diganti #TODO.
2. Membantu memahami konsep baru, seperti `{% load static %}`, Popover API, `prefetch_related` untuk menghindari N+1 query, filter `yesno` untuk mengubah boolean Python ke JavaScript, trik dummy UUID untuk membuat URL di JavaScript, alur fetch AJAX, dan debouncing.
3. Melakukan code review di setiap langkah dan menunjukkan letak kesalahan tanpa memberikan kodenya, misalnya typo `request.GET.get`, filter `title__icontains`, `ProjectForm` tanpa `()`, `form.is_valid` tanpa `()`, indentasi method `clean_` yang salah, dan variabel yang belum di-`escapeHtml`.
4. Menyusun rencana adaptasi pola Tutorial 5 ke halaman Education (endpoint JSON manual, kerangka halaman kosong, modal form, view `create_education_ajax`, dan `strip_tags` pada `EducationForm`).
5. Debugging halaman Education, antara lain modal yang tidak muncul karena id masih `add-project-modal`, data yang tidak tampil karena sisa loop `{% for %}`/`{% empty %}` dan typo `stared_by_names`, id form pencarian yang salah, serta pemanggilan `fetchProjects` yang belum diganti.
6. Mendiskusikan pembagian hak akses antara user, editor, dan superuser.
7. Membuat commit message dengan format conventional commits.

Secara keseluruhan output yang dikeluarkan oleh AI sudah benar dan tidak ada misinformasi. Saya memberikan instruksi dimana AI dilarang untuk menulis kode blok secara langsung, melainkan memberikan penjelasan langkah-langkah dan pseudocodenya. Kemudian hasil pengerjaan saya baru di review oleh AI untuk diperiksa kembali apakah ada kesalahan atau tidak.

Log Gemini: Saat ini Antigravity belum menyediakan fitur share chat log. Sebagai pengganti saya salin log AI ke dalam file /AI_CHAT_LOG/Tugas5.md
