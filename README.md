# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Jaya Jaya Institut adalah sebuah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan dikenal memiliki reputasi lulusan yang baik. Walaupun telah mencetak banyak lulusan dengan reputasi yang sangat baik, masalah tingginya angka dropout masih menjadi tantangan yang belum mampu diselesaikan bagi Jaya Jaya Institut yang mana akan berpotensi mengurangi kepercayaan publik terhadap kualitas pendidikannya. Maka dari itu, pihak institusi ingin mendeteksi siswa yang berpotensi dropout sedini mungkin, untuk memberikan bimbingan yang lebih personal guna meningkatkan peluang mereka menyelesaikan studi.  Untuk merealisasikan tujuan tersebut institusi berencana untuk membuat dashboard yang memudahkan dalam membaca faktor-faktor yang memengaruhi performa masing-masing mahasiswa dan membuat model yang mampu mengklasifikasikan mahasiswa yang berpotensi dropout sehingga institusi dapat memberikan perlakuan yang khusus kepada mahasiswa yang berpotensi dropout secara tepat sasaran. 

faktor-faktor yang kemungkinan memengaruhi performa akademik mahasiswa adalah sebagai berikut. 
* Marital status: status pernikahan
* Application mode: metode pendaftaran 
* Application order: parameter pilihan institusi yang diprioritaskan calon mahasiswa
* Course: course yang diambil
* Daytime/evening attendance: waktu kehadiran (siang/malam)
* Previous qualification: pendidikan terakhir
* Previous qualification (grade): nilai pendidikan terakhir
* Nationality: kewarganegaraan
* Mother's qualification: pendidikan ibu
* Father's qualification: pendidikan ayah
* Mother's occupation: pekerjaan ibu
* Father's occupation: pekerjaan ayah
* Admission grade: nilai kualifikasi admisi
* Displaced: pelajar yang tidak berdomisili di daerah asal
* Educational special needs: parameter penentu kebutuhan khusus akan pendidikan
* Tuition fees up to date: parameter ketertiban pembayaran iuran
* Gender: jenis kelamin
* Scholarship holder: parameter pemegang beasiswa
* Age at enrollment: usia pada saat mendaftar
* International: parameter murid yang datang dari luar negeri
* Curricular units 1st sem (credited): jumlah unit yang di kreditkan mahasiswa di semester 1  
* Curricular units 1st sem (enrolled): jumlah unit yang dihadiri mahasiswa di semester 1
* Curricular units 1st sem (evaluations): jumlah unit yang perlu dievaluasi mahasiswa di semester 1
* Curricular units 1st sem (approved): jumlah unit yang berhasil diluluskan oleh mahasiswa di semester 1
  
### Permasalahan Bisnis
1. Terdapat nilai persentase dropout yang tinggi pada mahasiswa Jaya Jaya Institut mengindikasikan terdapat faktor negatif yang memengaruhinya.
2. Faktor-faktor penyebab dropout perlu diketahui oleh institusi secepatnya untuk menargetkan intervensi yang tepat demi menyelesaikan permasalahan dropout rate yang tinggi.
3. Tidak adanya sistem prediksi dini untuk mengidentifikasi siswa yang berpotensi dropout.
   

### Cakupan Proyek
1. Mengidentifikasi variabel-variabel yang menjadi penyebab dropout mahasiswa setelah melakukan analisis data yang berisi hubungan antara data akademik mahasiswa dengan performa akademik mahasiswa.
2. Menganalisis data yang dimiliki untuk memahami pola dan tren drop rate yang meningkat.
3. Membuat dashboard yang membantu manajemen Jaya Jaya Institut dalam memahami informasi penting tentang faktor-faktor yang berkaitan dengan droprate mahasiswa.
4. Membuat model machine learning sebagai solusi untuk memecahkan masalah tingginya dropout rate mahasiswa dengan cara memberikan input berupa data akademik mahasiswa ke model machine learning lalu model tersebut dapat mengklasifikasikan mahasiswa ke dalam kategori performa akademik yang normal atau buruk yang berpotensi dropout. 

### Persiapan
Sumber data:
1. Dataset sudah disediakan dari pihak Jaya Jaya Maju institut sehingga dataset [student's performance](https://drive.google.com/drive/folders/1u2GLYrJxST154AbItZBKriXDrL7dHLSP) dapat diakses untuk dianalisa. Dataset tersebut tersusun setelah mengumpulkan beberapa database dari institusi perguruan tinggi. Database-database tersebut berhubungan dengan data mahasiswa-mahasiswa yang mengikuti program sarjana seperti program studi agronomi, desain, edukasi, perawatan, jurnalis, manajemen, layanan sosial, dan teknologi. dataset berisi catatan informasi masing-masing mahasiswa selama mereka berkuliah, seperti jalur akademik, demografi, faktor sosial ekonomi, dan juga performa akademik mahasiswa pada akhir periode semester pertama dan kedua.

Mempersiapkan environment project
2. Memanfaatkan Jupyter Notebook Google Colab untuk dapat menulis dan menjalankan model machine learning atau analisis data secara langsung, memanfaatkan CPU atau GPU yang disediakan secara gratis. Persiapan environment project dengan Google Colabs relatif mudah karena beberapa library yang dibutuhkan sudah terinstal. Untuk library yang belum tersedia di Google Colab, library dapat di-instal dengan perintah pip install.  


Setup environment:
* 

1. Akses Google Colab: Membuka Google Colab lewat browser.
2. Dataset hasil analisis faktor-faktor yang memengaruhi attrition rate menggunakan Google Colab dapat diunggah ke database management tool PostgreSQL menggunakan supabase untuk nantinya bisa digunakan untuk membuat dashboard menggunakan metabase.

* Setup Metabase dan Docker 
1. **Install Docker**: Docker bisa diunduh dari website resminya dan dapat di instal dengan mengikuti langkah-langkah yang ditampilkan.

2. **Setup Metabase**: Menggunakan Metabase untuk membuat dashboard yang interaktif dan terhubung ke database. Menyiapkan metabase dengan menggunakan Docker dilakukan dengan perintah docker pull metabase/metabase:v0.46.4 dan jalankan metabase dengan menggunakan perintah docker run -p 3000:3000 --name metabase metabase/metabase

 * Menghubungkan ke Supabase

1. **Upload CSV ke Supabase**: Menggunakan Supabase untuk menyimpan data attrition rate yang sudah disiapkan dengan melakukan feature engineering sebelumnya ke data base agar bisa diakses oleh Metabase. Untuk dapat menggunakan supabase perlu disiapkan terlebih dahulu akun user yang akan digunakan untuk mengakses supabase yang mana juga terdapat opsi menggunakan akun GitHub. Selanjutnya projek baru perlu dibuat dengan mendefinisikan nama, organisasi, dan password. Setelah itu didapatkan username dan password untuk projek ini adalah **postgres.uxzwesijexuasxnywyuf** dan **52H9suDMxF5lWrjq**. Password dan username tersebut dibutuhkan saat akan mengirim data hasil feature engineering ke supabase untuk masuk ke databse PostgreSQL.
   
2.  **Menghubungkan Metabase dengan Supabase**:
Untuk dapat mengolah database PostgreSQL yang ada pada Supabase, diperlukan pengaturan pada metabase dengan memberikan informasi database yang sama dengan yang sudah dikirim ke supabase tersebut. Informasi yang perlu dimasukkan meliputi tipe databse, yaitu PostgreSQL, host, port, database name, username, dan password. Username dadn password yang dipilih untuk menggunakan metabase, yaitu **root@mail.com** dan **root123**. 


## Business Dashboard
Business dashboard yang dibuat menggunakan Metabase terhubung dengan database di Supabase. Dashboard ini memberikan informasi yang jelas mengenai performa akademik siswa dan indikator dropout. Salah satu faktor utama yang ditemukan adalah rasio performa akademik pada semester 1 dan 2. Siswa dengan rasio rendah, dihitung dari jumlah unit kurikulum yang diambil (enrolled) dibandingkan dengan yang lulus (approved), cenderung memiliki risiko dropout yang lebih tinggi.

## Menjalankan Sistem Machine Learning
Dalam proyek ini, dilakukan dua pendekatan untuk membangun model prediksi yang mampu mendeteksi potensi dropout siswa di Jaya Jaya Institut. Model ini menggunakan faktor utama yang ditemukan melalui analisis sebelumnya, yaitu rasio performa akademik siswa (academic_performance_ratio) sebagai variabel fitur utama.

Pendekatan menggunakan Decision Tree mampu memodelkan keputusan berdasarkan beberapa cabang logika. Decision tree cocok untuk menganalisis dataset yang memiliki relasi non-linear antar fitur dan label target.

Parameter yang diuji melalui GridSearchCV untuk decision tree model meliputi:

max_features: 'sqrt' dan 'log2',
max_depth: kedalaman maksimum tree diuji pada nilai 5 hingga 8 
criterion: 'gini' dan 'entropy', 

Setelah menemukan parameter terbaik, model Decision Tree dengan:

criterion='entropy'
max_depth=5
max_features='sqrt'
dipilih sebagai model final. Model ini kemudian dilatih pada data training dan disimpan untuk digunakan di masa mendatang.

Prediksi dengan Decision Tree

Model Decision Tree yang sudah dilatih digunakan untuk memprediksi dropout siswa pada set data training dan test. Prediksi dilakukan berdasarkan nilai academic_performance_ratio dari setiap siswa. Hasil dari prediksi ini menunjukkan probabilitas seorang siswa berpotensi dropout berdasarkan performa akademik mereka.

Secara keseluruhan, kedua model ini memberikan insight yang berharga bagi Jaya Jaya Institut dalam mendeteksi potensi dropout siswa, yang diharapkan dapat digunakan untuk melakukan intervensi dini melalui bimbingan akademik yang tepat. Model ini juga membantu memvisualisasikan hasil melalui dashboard yang terintegrasi dengan Metabase.

## Conclusion
Analisis yang dilakukan menunjukkan bahwa siswa dengan performa akademik rendah di awal masa studi berpotensi tinggi untuk dropout. Dengan menggunakan model prediksi yang dibangun berdasarkan data akademik dan faktor lainnya, pihak Jaya Jaya Institut dapat memberikan intervensi dini kepada siswa yang berisiko. Dashboard yang dibuat memungkinkan pihak institusi untuk memonitor performa siswa secara real-time dan mengambil tindakan yang tepat sesuai data yang disajikan.

Laporan ini memberikan dasar untuk perbaikan strategi pembelajaran dan dukungan akademik di masa depan.

### Rekomendasi Action Items
Berdasarkan hasil analisis dan modeling, berikut adalah beberapa rekomendasi action items yang dapat dilakukan oleh Jaya Jaya Institut untuk mengurangi angka dropout dan meningkatkan performa akademik siswa:

- Program Bimbingan Akademik Khusus
Mengimplementasikan program bimbingan akademik khusus bagi siswa yang teridentifikasi memiliki rasio performa akademik rendah di semester awal. Program ini dapat mencakup mentoring, bantuan pengajaran tambahan, dan pemantauan yang lebih dekat oleh tutor.


nb: 
link streamlit masih dengan bug [https://penerapandatascience-submisifinal.streamlit.app/]
