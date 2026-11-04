Nama : Matthew Raeann Alexandra
NPM : 2506544763
Kelas : PBP B

## Deskripsi Proyek
myportofolio adalah website portofolio pribadi yang saya kembangkan untuk mata kuliah Pemrograman Berbasis Platform (PBP) Fakultas Ilmu Komputer Universitas Indonesia. Website ini dibangun dengan Django dan menampilkan profil, pengalaman (Experience), riwayat pendidikan (Education), dan proyek (Projects). Bagian Education adalah bagian yang saya kerjakan sendiri pada Tugas 3 sampai Tugas 6, sedangkan bagian Projects mengikuti tutorial.

Website dapat diakses di https://matthew-raeann-myportofolio.pws.cs.ui.ac.id

Fitur utama:
1. Halaman Education yang dapat menampilkan, mencari, menambah, mengedit, memberi star, dan menghapus riwayat pendidikan tanpa reload halaman melalui REST API.
2. Register, login, dan logout, beserta cookie `last_login` yang ditampilkan di halaman utama.
3. Empat peran hak akses, yaitu pengunjung, pengguna biasa, Editor, dan pemilik portofolio.
4. REST API dengan Django REST Framework di bawah prefix `/api/v1/`, yang juga bisa dibuka melalui Browsable API.

Teknologi yang digunakan: Python, Django 5.2, Django REST Framework 3.18, SQLite (lokal), PostgreSQL (PWS), WhiteNoise, dan Gunicorn.

## Cara Menjalankan Proyek
1. Clone repositori lalu masuk ke folder proyek.
```bash
git clone https://github.com/matthewraeann/myportofolio.git
cd myportofolio
```
2. Buat dan aktifkan virtual environment. Di Windows gunakan `env\Scripts\activate`, sedangkan di macOS/Linux gunakan `source env/bin/activate`.
```bash
python -m venv env
```
3. Install dependencies.
```bash
pip install -r requirements.txt
```
4. Buat file `.env` di root proyek yang berisi `PRODUCTION=False`, agar proyek memakai SQLite saat dijalankan secara lokal.
5. Jalankan migrasi database.
```bash
python manage.py migrate
```
6. Buat akun pemilik portofolio (superuser).
```bash
python manage.py createsuperuser
```
7. Untuk peran Editor, buka `/admin/`, buat Group bernama `Editor`, lalu tambahkan akun yang ingin dijadikan Editor ke group tersebut.
8. Jalankan server, lalu buka http://localhost:8000/education/ untuk halaman Education dan http://localhost:8000/api/v1/educations/ untuk Browsable API.
```bash
python manage.py runserver
```
9. Jalankan seluruh test. Gunakan `test main` agar hanya test aplikasi main yang dijalankan.
```bash
python manage.py test main
```

## Hak Akses
| Aksi pada Education | Pengunjung | Pengguna biasa | Editor | Pemilik (superuser) |
|---|---|---|---|---|
| Melihat daftar, detail, dan mencari | ✅ | ✅ | ✅ | ✅ |
| Memberi atau membatalkan star | ❌ | ✅ | ✅ | ✅ |
| Mengubah data (PUT/PATCH) | ❌ | ❌ | ✅ | ✅ |
| Menambah (POST) dan menghapus (DELETE) data | ❌ | ❌ | ❌ | ✅ |

Hak akses ini diperiksa di server oleh permission class `IsPortfolioOwnerOrEditorOrReadOnly` dan `IsAuthenticated`, bukan hanya dengan menyembunyikan tombol di template.

## Daftar Endpoint API
| Method | Endpoint | Fungsi | Akses |
|---|---|---|---|
| GET | `/api/v1/educations/?institution=<kata kunci>` | Daftar Education, bisa dicari berdasarkan nama institusi | Semua |
| POST | `/api/v1/educations/` | Menambah Education (201) | Pemilik |
| GET | `/api/v1/educations/<id>/` | Detail satu Education (404 jika tidak ada) | Semua |
| PUT / PATCH | `/api/v1/educations/<id>/` | Mengubah seluruh atau sebagian data | Editor, Pemilik |
| DELETE | `/api/v1/educations/<id>/` | Menghapus Education (204) | Pemilik |
| POST | `/api/v1/educations/<id>/star/` | Memberi atau membatalkan star | Pengguna yang login |
| GET | `/api/v1/projects/?title=<kata kunci>` | Daftar Project (Tutorial 7) | Semua |
| POST | `/api/v1/projects/` | Menambah Project | Pemilik |
| GET / PUT / PATCH / DELETE | `/api/v1/projects/<id>/` | Detail, mengubah, dan menghapus Project | GET semua, sisanya Pemilik |
| POST | `/api/v1/projects/<id>/star/` | Memberi atau membatalkan star Project | Pengguna yang login |

Input yang tidak valid dijawab dengan 400 beserta pesan per field, dan aksi yang tidak diizinkan dijawab dengan 403. Setiap request yang mengubah data wajib menyertakan header `X-CSRFToken`.

## Progres Mingguan
1. Tugas 1: Membuat website portofolio statis dengan HTML dan CSS, terdiri dari section profil dan Experience, serta tampilan yang responsive.
2. Tugas 2: Memindahkan portofolio ke Django dengan pola MVT, membuat model dan halaman Experience, menambahkan navbar, dan melakukan deployment ke PWS.
3. Tugas 3: Membuat model dan halaman Education beserta form tambah, edit, hapus, pencarian berdasarkan nama institusi, dan endpoint JSON.
4. Tugas 4: Menambahkan register, login, logout, cookie `last_login`, empat peran hak akses (Editor memakai Group), dan fitur star pada Education.
5. Tugas 5: Mengubah halaman Education agar memakai AJAX (fetch), modal tambah data, toast, pencarian dengan debouncing, dan pembersihan input dengan `strip_tags` untuk mencegah XSS.
6. Tugas 6: Membuat REST API Education dengan Django REST Framework (serializer, permission class, API view, dan test `APITestCase`), lalu menghubungkan halaman Education ke API tersebut, termasuk modal edit yang mengirim PATCH.

## Pertanyaan Reflektif dan AI Disclosure

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

### Tugas 4
Pada pekan ini pertanyaan reflektif ditiadakan.

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

### Tugas 6
1. REST (Representational State Transfer) adalah gaya arsitektur yang memandang data sebagai resource. Setiap resource memiliki alamat URI sendiri, misalnya /api/education/ untuk daftar education dan /api/education/5/ untuk satu data education, lalu dimanipulasi menggunakan metode HTTP standar. Mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful, karena JSON hanyalah format data. Endpoint seperti GET /deleteEducation?id=5 bisa saja mengembalikan JSON, tetapi tidak RESTful karena URI-nya berupa aksi dan metode GET dipakai untuk menghapus data. Sebuah API disebut RESTful jika URI-nya berupa kata benda (resource), metode HTTP dipakai sesuai fungsinya (GET untuk membaca, POST untuk membuat, PUT/PATCH untuk mengubah, dan DELETE untuk menghapus), status code yang dikembalikan bermakna (misalnya 201, 204, 400, 403, 404, bukan selalu 200), dan bersifat stateless, artinya setiap request membawa semua informasi yang dibutuhkan server.

Perbedaan PUT dan PATCH ada pada cara mengubah data. PUT mengganti seluruh resource, sehingga semua field wajib harus dikirim. Field yang tidak dikirim dianggap kosong dan akan ditolak jika field tersebut wajib. PUT cocok digunakan untuk form edit lengkap yang selalu mengirim ulang semua field. Sementara itu, PATCH hanya mengubah sebagian field, dan field yang tidak dikirim tetap seperti semula. PATCH cocok digunakan untuk perubahan kecil, misalnya ketika saya sudah lulus dan hanya perlu mengisi tahun selesai dengan mengirim {"end_year": "2029-06-01"}. Pada tugas ini saya menggunakan PATCH untuk modal edit education, karena pengguna bisa mengubah beberapa field saja tanpa harus mengirim ulang seluruh data.

2. Serializer pada Django REST Framework berfungsi sebagai penerjemah data dua arah. Saat data keluar, serializer mengubah objek model atau QuerySet menjadi data yang bisa di-render menjadi JSON. Saat data masuk, serializer memvalidasi data dari request melalui is_valid(), kemudian save() akan membuat atau memperbarui objek di database. Dibandingkan merakit dictionary secara manual dengan JsonResponse seperti pada Tutorial 05, serializer memiliki beberapa keuntungan. Pertama, tidak ada duplikasi kode, karena field cukup didefinisikan sekali di serializer tanpa perlu menulis ulang dictionary di setiap view. Jika model mendapat field baru, kita tidak perlu mengubah banyak tempat. Kedua, validasi dilakukan secara otomatis berdasarkan model, misalnya tipe data, field wajib, dan max_length. Jika data tidak valid, serializer langsung mengembalikan error 400 beserta pesan untuk setiap field. Ketiga, kita bisa mengatur field read_only, misalnya star_count dan is_starred, sehingga klien tidak bisa memalsukan jumlah star atau status star melalui body request. Keempat, serializer terintegrasi langsung dengan fitur DRF lainnya seperti generic views, partial=True untuk PATCH, dan Browsable API, sehingga kode view menjadi jauh lebih ringkas.

3. Autentikasi adalah proses untuk mengetahui siapa yang mengirim request. Pada DRF, authentication class seperti SessionAuthentication akan mengidentifikasi pengguna lalu mengisi request.user. Jika tidak ada kredensial yang valid, pengguna dianggap sebagai AnonymousUser. Sementara itu, otorisasi adalah proses untuk menentukan apa saja yang boleh dilakukan oleh pengguna tersebut. Pada DRF, hal ini ditangani oleh permission class seperti IsAuthenticated atau permission yang kita buat sendiri, misalnya hanya pemilik data atau admin yang boleh mengubah dan menghapus. Secara umum, request yang belum terautentikasi dijawab dengan 401, sedangkan pengguna yang sudah terautentikasi tetapi tidak memiliki izin dijawab dengan 403. Namun, karena API saya hanya memakai SessionAuthentication yang tidak mengirim header WWW-Authenticate, DRF mengembalikan 403 untuk keduanya, misalnya ketika pengunjung tanpa login mencoba memberi star. Hak akses harus diperiksa di server karena menyembunyikan tombol di template hanya mengubah tampilan dan tidak mengamankan apa pun. Endpoint API tetap ada dan tetap bisa dipanggil secara langsung melalui DevTools browser, curl, atau Postman tanpa perlu menekan tombol tersebut. Oleh karena itu, permission class di server wajib memeriksa setiap request, sedangkan menyembunyikan tombol hanya berfungsi sebagai pelengkap tampilan.

4. SessionAuthentication menggunakan cookie session untuk mengenali pengguna, dan browser akan mengirim cookie tersebut secara otomatis ke server, termasuk ketika request dipicu dari situs lain. Akibatnya, jika pengguna sedang login lalu membuka situs jahat, situs tersebut bisa mengirim request POST atau DELETE ke API kita atas nama pengguna tersebut. Serangan ini disebut Cross-Site Request Forgery (CSRF). Token CSRF mencegah serangan ini karena token hanya bisa dibaca oleh halaman dari origin kita sendiri dan harus dikirim melalui header X-CSRFToken pada setiap request yang mengubah data. Situs lain tidak bisa membaca token tersebut, sehingga request palsunya akan ditolak dengan status 403. Test yang memakai force_authenticate tidak cukup untuk membuktikan perlindungan CSRF, karena force_authenticate langsung menandai request sebagai milik pengguna tertentu dan melewati proses autentikasi. Akibatnya, SessionAuthentication beserta pemeriksaan CSRF di dalamnya tidak pernah dijalankan, sehingga test tetap lulus walaupun token CSRF tidak dikirim. Untuk membuktikan bahwa perlindungan CSRF berjalan, test harus menggunakan APIClient(enforce_csrf_checks=True), melakukan login sungguhan melalui session, lalu memastikan bahwa request tanpa token menghasilkan 403 dan request dengan token yang valid berhasil.

#### Fitur Tambahan Tugas 6
Selain checklist pada soal, saya menambahkan beberapa fitur berikut:
1. Validasi tahun selesai yang tidak boleh lebih awal dari tahun mulai. Validasi ini tetap berjalan saat PATCH, karena tahun yang tidak dikirim diambil dari data lama di database.
2. Modal edit yang langsung terisi dengan data card yang dipilih, tanpa perlu request tambahan ke server.
3. Pencarian langsung saat mengetik dengan debouncing 300 ms dan `AbortController`, sehingga hasil pencarian lama tidak menimpa hasil pencarian terbaru.
4. Tampilan loading, data kosong, dan error saat memuat data dari API.
5. Konfirmasi sebelum menghapus data, serta tombol yang dinonaktifkan selama request berjalan agar data tidak terkirim dua kali.
6. Tooltip pada tombol star yang menampilkan nama pengguna yang sudah memberi star. Pengunjung yang belum login diarahkan ke halaman login.
7. Field read-only `is_ongoing`, sehingga card dapat menampilkan "Present" untuk pendidikan yang masih berjalan.
8. Field star yang dipakai bersama oleh Project dan Education dipisahkan ke `StarFieldsMixin`, dan data star diambil dengan `prefetch_related` agar tidak terjadi query berulang untuk setiap data (N+1 query).
9. Endpoint Education lama dari Tugas 3 sampai Tugas 5 (JSON, AJAX, star, dan hapus) dihapus, sehingga halaman Education hanya memakai satu sumber data, yaitu API `/api/v1/educations/`.

#### AI Disclosure Tugas 6
Pada tugas ini saya menggunakan Claude Code (model Claude Opus 5.5, aplikasi desktop Claude) untuk membantu saya mengerjakan tugas ini. 
AI tersebut saya gunakan untuk:
1. Membaca soal Tugas 6 lalu memecahnya menjadi 8 langkah kecil (serializer, permission dan API view, URL, test, integrasi halaman, modal edit, dokumentasi, dan deployment). Saya memberikan aturan agar AI menjelaskan setiap langkah secara rinci dan tidak lanjut ke langkah berikutnya sebelum saya minta, serta bertanya jika ada yang kurang jelas alih-alih membuat asumsi.
2. Menanyakan keputusan desain kepada saya sebelum mengerjakan, yaitu cara mengubah data (saya memilih modal edit baru dengan PATCH), konfirmasi hapus (saya memilih `window.confirm()`), dan strategi commit (saya memilih commit per langkah).
3. Menulis kode secara langsung di workspace saya, yaitu `EducationSerializer` (termasuk `validate_<field>` dengan `strip_tags` dan validasi tahun selesai yang tetap bekerja saat PATCH), API view `education_list`, `education_detail`, dan `education_star`, pesan 403 pada `IsPortfolioOwnerOrEditorOrReadOnly`, routing `/api/v1/educations/`, 14 test `APITestCase` untuk keempat peran, perubahan JavaScript `education.html` agar memakai API, serta modal edit dengan `EducationForm(prefix="edit")`.
4. Menjelaskan konsep di balik setiap langkah, seperti urutan pemeriksaan DRF (autentikasi → permission → 405 → 404 → 400), perbedaan PUT dan PATCH (`partial=True`), field read-only hasil perhitungan, alasan `{% csrf_token %}` tetap dibutuhkan untuk fetch, serta alasan test CSRF harus memakai `.login()` dan bukan `force_authenticate`.
5. Menguji hasil pekerjaan melalui Django shell, menjalankan `python manage.py test main`, dan mengecek halaman Education di browser bawaan sebagai pengunjung. Pengujian saat login (tambah, edit, star, hapus) saya lakukan sendiri di browser karena AI tidak menggunakan akun saya.
6. Menjelaskan maksud pertanyaan reflektif beserta poin-poin yang perlu dibahas. Jawaban pertanyaan reflektif saya tulis sendiri, kemudian diperiksa kembali oleh AI. AI menemukan tiga bagian yang kurang tepat dan membantu saya memperbaikinya, yaitu contoh PATCH yang tidak sesuai dengan endpoint star saya (star memakai POST), contoh field read-only `owner` yang tidak ada di model Education, dan status 401 yang ternyata tidak dipakai oleh SessionAuthentication (DRF mengembalikan 403).
7. Membuat commit dengan format conventional commits dan membuat transkrip chat log.
8. Memeriksa kembali seluruh pengerjaan terhadap checklist dan rubrik Tugas 6 setelah tugas selesai. Dari pemeriksaan ini, AI memperbaiki jawaban reflektif (lihat poin 6), menambahkan deskripsi proyek, cara menjalankan proyek, tabel hak akses, daftar endpoint API, progres mingguan, dan fitur tambahan ke README, memindahkan field star yang ditulis ganda ke `StarFieldsMixin`, menambahkan docstring, serta menghapus endpoint Education lama yang sudah digantikan API beserta test-nya.

Secara keseluruhan output yang dikeluarkan oleh AI sudah benar, tetapi tidak sepenuhnya bebas dari kesalahan sehingga tetap perlu saya periksa kembali. Berbeda dengan Tugas 4 dan Tugas 5, pada tugas ini AI menulis kode secara langsung, sehingga saya memastikan pemahaman dengan meminta penjelasan rinci di setiap langkah sebelum lanjut. AI juga sempat membuat kesalahan, yaitu melakukan commit integrasi halaman tanpa menjalankan seluruh test terlebih dahulu sehingga satu test lama (`test_education_page`) gagal karena masih mengharapkan endpoint JSON lama. Kesalahan ini kemudian diperbaiki pada commit terpisah, dan setelahnya seluruh test dijalankan sebelum setiap commit.

Log Claude: Claude Code belum menyediakan fitur share chat log melalui link. Sebagai pengganti saya salin log AI ke dalam file /AI_CHAT_LOG/Tugas6.md
