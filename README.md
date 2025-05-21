# Proyek Akhir Data Science
## Latar Belakang:
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan telah mencetak banyak lulusan berkualitas. Meskipun memiliki reputasi baik, data internal menunjukkan bahwa tingkat dropout (mahasiswa yang tidak menyelesaikan pendidikan) masih cukup tinggi. Fenomena ini tentu menjadi perhatian serius karena dropout tidak hanya berdampak pada reputasi institusi, tetapi juga pada efektivitas proses pendidikan dan efisiensi sumber daya.

Untuk itu, Jaya Jaya Institut berinisiatif menggunakan data science untuk memahami dan menganalisis pola dropout, sehingga dapat mendeteksi lebih awal potensi mahasiswa yang berisiko tinggi keluar dari institusi, dan memberikan bimbingan khusus untuk meningkatkan retensi mahasiswa.
## Permasalahan Bisnis:
Bagaimana Jaya Jaya Institut dapat:
- Mengidentifikasi faktor-faktor yang paling memengaruhi mahasiswa untuk melakukan dropout?
- Memonitor status mahasiswa secara real-time menggunakan dashboard interaktif?
- Mengembangkan strategi berbasis data untuk mengurangi angka dropout dan meningkatkan tingkat kelulusan?
## Cakupan Proyek:
- Mengidentifikasi faktor penyebab utama tingginya angka dropout.
- Menganalisis hubungan antara beasiswa, status pernikahan, jurusan, dan asal negara terhadap kelulusan.
- Mengembangkan dashboard bisnis untuk memantau data mahasiswa secara visual dan real-time.
## Persiapan:
### Sumber data : https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/employee/employee_data.csv
### Setup Environment - Anaconda:
- conda create --name main-ds python=3.9
- conda activate main-ds
- pip install -r requirements.txt
### Setup Environment - Shell/Terminal:
- mkdir proyek_analisis_data
- cd proyek_analisis_data
- pipenv install
- pipenv shell
- pip install -r requirements.txt
### Run steamlit app
https://drive.google.com/file/d/1lXUQORRzwqrV8w1pX2TANBiLEhEQ6VX8/view?usp=sharing
## Business Dashboard
https://drive.google.com/file/d/1lXUQORRzwqrV8w1pX2TANBiLEhEQ6VX8/view?usp=sharing
![Dashboard](./nuraisah_oxzV_dicoding-dashboard.png)
Insight Berdasarkan Data:
- Asal Mahasiswa: Mayoritas mahasiswa berasal dari Portugal, dan sebagian besar yang dropout juga berasal dari negara ini.
- Jurusan Terpopuler: Jurusan dengan jumlah mahasiswa terbanyak adalah Manajemen (terutama kelas malam) dan Keperawatan, yang juga memiliki proporsi dropout tinggi.
- Beasiswa dan Dropout: Mahasiswa penerima beasiswa cenderung lebih rendah tingkat dropout-nya. Hal ini mengindikasikan bahwa beasiswa mungkin berperan sebagai motivasi untuk menyelesaikan studi.
- Status Pernikahan: Mahasiswa lajang memiliki jumlah dropout dan kelulusan yang tinggi, sedangkan yang menikah atau bercerai jumlahnya sedikit, namun tetap terdapat dropout dari kelompok ini.
- Gender: Berdasarkan warna visual, data dapat dipilah berdasarkan gender, meskipun belum ditampilkan secara eksplisit pada pie chart atau bar chart.
## Conclusion
Berdasarkan hasil analisis data pegawai, perusahaan menghadapi tantangan signifikan dalam mengelola tingkat attrisi, terutama di kalangan pegawai muda, pria, dan mereka yang berada pada posisi awal karier. Beberapa pola penting yang berhasil diidentifikasi mencerminkan adanya potensi masalah dalam keterlibatan karyawan dan strategi retensi jangka panjang.
Overtime (Lembur): Pegawai yang tidak melakukan lembur justru memiliki tingkat attrisi yang lebih tinggi. Hal ini dapat mengindikasikan kurangnya keterlibatan dalam pekerjaan, minimnya tantangan, atau beban kerja yang terlalu ringan sehingga menurunkan motivasi kerja.
Kelompok Usia: Pegawai berusia 18–30 tahun menunjukkan tingkat attrisi tertinggi dibanding kelompok usia lainnya. Hal ini kemungkinan besar dipicu oleh keinginan eksplorasi karier, kebutuhan akan pertumbuhan cepat, atau ketidakcocokan dengan lingkungan kerja.
Gender: Tingkat attrisi lebih tinggi ditemukan pada pegawai laki-laki dibandingkan perempuan. Hal ini membuka kemungkinan adanya perbedaan persepsi terhadap beban kerja, peluang karier, atau keseimbangan kehidupan kerja.
Posisi/Jabatan: Posisi teknisi laboratorium menjadi posisi dengan tingkat attrisi tertinggi. Hal ini bisa mencerminkan pekerjaan yang monoton, tekanan kerja yang tinggi, atau kurangnya jalur karier yang jelas dalam posisi tersebut.
Masa Kerja: Pegawai dengan pengalaman kerja 0–10 tahun mendominasi kelompok yang mengalami attrisi. Ini menunjukkan pentingnya perhatian khusus terhadap proses onboarding dan pengembangan awal karier untuk meningkatkan loyalitas dan keterikatan pegawai sejak awal.
## Rekomendasi
Untuk mengatasi permasalahan ini, perusahaan perlu membangun strategi retensi yang lebih holistik dan berbasis data. Langkah awal dapat dimulai dengan menciptakan program engagement yang ditujukan khusus bagi pegawai yang tidak terlibat dalam lembur, agar mereka tetap merasa tertantang dan dihargai. Selain itu, perusahaan juga perlu menyediakan jalur pengembangan karier yang jelas serta program mentoring bagi pegawai usia muda, agar mereka melihat prospek jangka panjang yang lebih menjanjikan dalam perusahaan. Evaluasi mendalam terhadap posisi teknisi laboratorium juga menjadi hal yang krusial, baik dari sisi beban kerja maupun potensi pengembangan karier. Proses onboarding serta pembinaan bagi pegawai baru perlu diperkuat agar sejak awal mereka memiliki keterikatan emosional dengan perusahaan. Terakhir, penting untuk melakukan analisis lebih lanjut mengenai penyebab tingginya attrisi pada pegawai laki-laki, serta menyusun kebijakan yang mendukung keseimbangan kerja dan kehidupan yang lebih baik bagi semua pegawai tanpa memandang gender. Dengan pendekatan yang tepat, perusahaan diharapkan dapat menurunkan tingkat attrisi secara signifikan dan membangun lingkungan kerja yang lebih stabil, produktif, dan berkelanjutan.
