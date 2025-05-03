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
* Debtor: apakah mahasiswa pemiliik hutang.
* Tuition fees up to date: parameter ketertiban pembayaran iuran
* Gender: jenis kelamin
* Scholarship holder: parameter pemegang beasiswa
* Age at enrollment: usia pada saat mendaftar
* International: parameter murid yang datang dari luar negeri
* Curricular units 1st sem (credited): jumlah unit yang di kreditkan mahasiswa di semester 1  
* Curricular units 1st sem (enrolled): jumlah unit yang dihadiri mahasiswa di semester 1
* Curricular units 1st sem (evaluations): jumlah unit yang perlu dievaluasi mahasiswa di semester 1
* Curricular units 1st sem (approved): jumlah unit yang berhasil diluluskan oleh mahasiswa di semester 1
* Curricular_units_1st_sem_grade: nilai dari unit pada semester 1
* Curricular_units_2nd_sem_without_evaluations: jumlah unit pada semester 2 yang lulus tanpa evaluasi
* Curricular units 2nd sem (credited): jumlah unit yang di kreditkan mahasiswa di semester 2  
* Curricular units 2nd sem (enrolled): jumlah unit yang dihadiri mahasiswa di semester 2
* Curricular units 2nd sem (evaluations): jumlah unit yang perlu dievaluasi mahasiswa di semester 2
* Curricular units 2nd sem (approved): jumlah unit yang berhasil diluluskan oleh mahasiswa di semester 2
* Curricular_units_2nd_sem_grade: nilai dari unit pada semester 2
* Curricular_units_2nd_sem_without_evaluations: jumlah unit pada semester 2 yang lulus tanpa evaluasi
* unemployment_rate: tingkat pengangguran
* inflation rate: persentase inflasi
* GDP: pendapatan perkapita
* status: parameter yang menyatakan kelulusan atau dropout mahasiswa.
  
### Permasalahan Bisnis
1. Terdapat nilai persentase dropout yang tinggi pada mahasiswa Jaya Jaya Institut mengindikasikan terdapat faktor negatif yang memengaruhinya.
2. Faktor-faktor penyebab dropout perlu diketahui oleh institusi secepatnya untuk menargetkan intervensi yang tepat demi menyelesaikan permasalahan dropout rate yang tinggi.
3. Tidak adanya sistem prediksi dini untuk mengidentifikasi siswa yang berpotensi dropout.
   

### Cakupan Proyek
1. Mencari variabel yang paling berdampak terhadap peningkatan persentase dropout mahasiswa setelah melakukan analisis data yang berisi hubungan antara data akademik mahasiswa dengan performa akademik mahasiswa.
2. Melakukan penarikan kesimpulan dari hasil analisi data untuk bisa menentukan langkah tepat yang perlu diambil Jaya Jaya Institu untuk mencegah penurunan performa akademik mahasiswa.
3. Membuat dashboard untuk memvisualisasikan informasi penting tentang variabel yang berkaitan dengan droprate mahasiswa untuk membantu Jaya Jaya Institut memahami hasil analisis.
4. Membuat model machine learning sebagai solusi untuk memecahkan masalah tingginya dropout rate mahasiswa dengan cara memberikan input berupa data akademik mahasiswa ke model machine learning lalu model tersebut dapat mengklasifikasikan mahasiswa ke dalam kategori performa akademik yang normal atau buruk yang berpotensi dropout. 

### Persiapan
**1. Sumber data:**
Dataset sudah disediakan dari pihak Jaya Jaya Maju institut sehingga dataset [student's performance](https://drive.google.com/drive/folders/1u2GLYrJxST154AbItZBKriXDrL7dHLSP) dapat diakses untuk dianalisa. Dataset tersebut tersusun setelah mengumpulkan beberapa database dari institusi perguruan tinggi. Database-database tersebut berhubungan dengan data mahasiswa-mahasiswa yang mengikuti program sarjana seperti program studi agronomi, desain, edukasi, perawatan, jurnalis, manajemen, layanan sosial, dan teknologi. dataset berisi catatan informasi masing-masing mahasiswa selama mereka berkuliah, seperti jalur akademik, demografi, faktor sosial ekonomi, dan juga performa akademik mahasiswa pada akhir periode semester pertama dan kedua.

**2. Mempersiapkan environment project:**
Memanfaatkan Jupyter Notebook Google Colab untuk dapat menulis dan menjalankan model machine learning atau analisis data secara langsung, memanfaatkan CPU atau GPU yang disediakan secara gratis. Persiapan environment project dengan Google Colabs relatif mudah karena beberapa library yang dibutuhkan sudah terinstal. Untuk library yang belum tersedia di Google Colab, library dapat di-instal dengan perintah pip install.  

Librari yang diperlukan dalam project ini diantaranya sebagai berikut.
* sqlalchemy: untuk menghubungkan dataframe ke tabel yang ada di database
* pandas
* numpy


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
Analisis yang dilakukan menunjukkan bahwa siswa yang berstatus dropout dari Jaya Jaya Institute memiliki performa akademik yang menunjukkan adanya pola saat dilihat dari statistik prestasi yang didapat selama belajar di Jaya Jaya Institute. 

Dashboard yang dibuat menggunakan tools metabase mempermudah dalam meneliti hubungan antara beberapa variabel yang berpotensi mempengaruhi keberhasilan mahasiswa lulus dari Jaya Jaya Institute. Variabel-variabel tersebut diantaranya nilai rerata unit yang diampu pada semester 1 dan semester 2 semua mahasiswa, nilai rerata unit semester 1 dan 2 yang berhasil diluluskan semua mahasiswa, nilai rerata ujian masuk dari semua mahasiswa, nilai rata-rata semua unit pada semester 1 dan semester 2, nilai rerata pendidikan sebelumnya dari semua mahasiswa, nilai rerata semua unit semester 1 dan semester 2 yang diselesaikan tanpa evaluasi, dan rerata usia semua mahasiswa pada saat pertama kali terdaftar menjadi mahasiswa Jaya Jaya Institut.

Dari hasil rata-rata nilai rerata unit yang diampu pada semester 1 dan semester 2, didapatkan pola bahwa mahasiswa-mahasiswa yang berhasil lulus dan berstatus Graduate memiliki nilai unit rata-rata di semester 1 dan semester 2 yang lebih besar dari mahasiswa yang berstatus Dropout dan Enrolled. Mahasiswa dengan status Graduate memiliki nilai rerata 6.65 sedangkan mahasiswa dengan status Dropout dan Enrolled hanya di angka 5.8 dan 5.95 saja.

Pola yang sama juga terjadi pada hasil analisis data yang dilakukan pada variabel  nilai rerata unit semester 1 dan 2 yang berhasil diluluskan mahasiswa, nilai rerata ujian masuk dari semua mahasiswa, nilai rata-rata semua unit pada semester 1 dan semester 2, nilai rerata pendidikan sebelumnya dari semua mahasiswa, nilai rerata semua unit semester 1 dan semester 2 yang diselesaikan tanpa evaluasi. Hasil yang didapatkan mengatakan variabel-variabel tersebut memberikan nilai paling tinggi pada mahasiswa yang berstatus "Graduate", selanjutnya nilai tertinggi kedua selalu dipegang oleh mahasiswa-mahasiswa yang berstatus "Enrolled". Sedangkan mahasiswa-mahasiswa yang berstatus "Dropout" memiliki rerata performa akademik yang paling rendah dibanding mahasiswa berstatus yang lain. Mahasiswa berstatus Dropout menunjukkan nilai rerata yang paling rendah di variabel-variabel yang diteliti. 

Seluruh mahasiswa yang berstatus Dropout memiliki nilai rata-rata usia yang tertinggi dibanding mahasiswa golongan yang lain pada saat pertama kali mendaftar Jaya Jaya Institut. Sementara mahasiswa dengan status Graduate memiliki nilai rerata usia yang terendah dibanding mahasiswa golongan Dropout dan Enrolled. Hal ini membuktikan bahwa mahasiswa yang berstatus Graduate kebanyakan masih relatif lebih muda dibandingkan dengan mahasiswa yang berstatus selain Graduate. Mahasiswa dengan status Enrolled memiliki selisih rerata usia yang sedikit berbeda tetapi masih lebih tinggi sedikit dari rerata usia yang dimiliki mahasiswa berstatus Graduate.

Performa akademik yang rendah di awal masa studi berpotensi tinggi menyebabkan mahasiswa untuk dropout. Dengan menggunakan model prediksi random forest yang dibangun berdasarkan data akademik dan faktor lainnya, pihak Jaya Jaya Institut dapat memberikan intervensi dini kepada siswa yang berisiko. Dashboard yang dibuat memungkinkan pihak institusi untuk memonitor performa siswa secara real-time dan mengambil tindakan yang tepat sesuai data yang disajikan.


### Rekomendasi Action Items

Berdasarkan hasil analisis dan modeling, berikut adalah beberapa rekomendasi action items yang dapat dilakukan oleh Jaya Jaya Institut untuk mengurangi angka dropout dan meningkatkan performa akademik siswa:

- **Peningkatan Layanan Bimbingan Akademik**

Meningkatkan kegiatan pembelajaran  secara keseluruhan supaya lebih efektif menghasilkan performa akademik mahasiswa yang mampu mendapatkan nilai yang lebih tinggi dari rerata nilai yang tergolong mahasiswa berstatus Dropout. 

Menerapkan perlakuan lebih untuk membantu meningkatkan performa akademik khusus bagi siswa yang teridentifikasi memiliki rasio performa akademik rendah di semester awal. Hal ini diharapkan dapat meningkatkan rata-rata nilai rerata unit yang diampu mahasiswa pada semester 1 dan semester 2, nilai rerata unit semester 1 dan 2 yang berhasil diluluskan mahasiswa, nilai rata-rata semua unit pada semester 1 dan semester 2,  nilai rerata semua unit semester 1 dan semester 2 yang diselesaikan tanpa evaluasi. Conoth program yang dapat dicoba mencakup mentoring, bantuan pengajaran tambahan, dan pemantauan yang lebih dekat oleh dosen.

- **Meningkatkan ambang batas minimum yang menjadi sarat pendaftaran mahasiswa Jaya Jaya Institute**

Data yang divisualisaikan oleh dashboard mengatakan bahwa nilai rerata ujian masuk dan nilai rerata pendidikan sebelumnya dari semua mahasiswa yang berstatus "Dropout" merupakan yang paling rendah dibandingkan dengan yang dimiliki oleh mahasiswa berstatus "Enrolled" dan "Graduate". Hal ini mengindikasikan bahwa adanya kemungkinan pengaruh antara performa mahasiswa Dropout dengan nilai ujian masuk dan nilai pendidikan mahasiswa sebelumnya. Dengan cara menseleksi lebih ketat calon mahasiswa yang memilii nilai yang kurang diharapkan mampu menurunkan tingkat dropout rate Jaya Jaya Institut.

- **Memberikan perlakuan khusus untuk mahasiswa dengan rerata usia tinggi**

Pola mahasiswa yang berstatus dropout juga ditunjukkan dari sebaran rerata usianya pada saat mendaftar ke Jaya Jaya Institute. Mahasiswa yang tergolong berstatus dropout memiliki rerata usia yang lebih tinggi pada saat pertama kali mendaftar dibandingkan dengan golongan mahasiswa berstatus Enrolled dan Graduate. 

Hal yang bisa dilakukan untuk menurunkan dropout rate Jaya Jaya Institute yang pertama adalah dengan menurunkan batas maksimal usia yang diperbolehkan untuk mendaftar ke Jaya Jaya Institute.

Kedua, terdapat kemungkinan mahasiswa yang terdaftar Dropout dan memiliki usia tinggi karena merupakan golongan karyawan yang kuliah sekaligus bekerja. Untuk golongan tersebut dapat diberikan keringanan dengan diperbolehkannya mengampu “kelas malam” atau blended learning.


link streamlit deployment aplikasi 
Student Drop Rate Predictor App: 

 [https://penerapandatascience-submisifinal.streamlit.app/]
