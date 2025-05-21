# Proyek Akhir Data Science
## Latar Belakang:
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus
## Permasalahan Bisnis:
.....
## Cakupan Proyek:
- Mengidentifikasi Faktor Penyebab Tinggi Tingkat Attrisi 
- Mengembangkan Dashboard Bisnis untuk Pemantauan Real-Time
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
- Dari overtime (lembur): Pegawai yang tidak melakukan lembur justru cenderung melakukan attrisi. Hal ini dapat menunjukkan bahwa keterlibatan rendah atau beban kerja yang tidak mencukupi mungkin membuat pegawai merasa kurang tertantang atau kurang terikat secara emosional dengan pekerjaannya.
- Dari usia (age group): Pegawai dengan rentang usia 18–30 tahun menunjukkan tingkat attrisi tertinggi dibandingkan kelompok usia lainnya. Kemungkinan ini disebabkan oleh keinginan eksplorasi karier, kebutuhan pertumbuhan lebih cepat, atau ketidakcocokan budaya kerja.
- Dari gender: Pegawai laki-laki memiliki tingkat attrisi yang lebih tinggi dibandingkan perempuan.
- Dari posisi/jabatan: Teknisi laboratorium (Laboratory Technician) adalah posisi yang memiliki tingkat attrisi tertinggi di antara semua peran. Hal ini mungkin disebabkan oleh tekanan pekerjaan, rutinitas yang monoton, atau kurangnya jenjang karier yang jelas.
- Dari masa kerja (working years): Pegawai dengan pengalaman kerja 0–10 tahun adalah kelompok paling banyak yang mengalami attrisi. Ini menunjukkan pentingnya strategi onboarding, engagement, dan retensi di awal masa kerja pegawai.
## Conclusion
Berdasarkan hasil analisis data pegawai, perusahaan menghadapi tantangan signifikan dalam mengelola tingkat attrisi, terutama di kalangan pegawai muda, pria, dan mereka yang berada pada posisi awal karier. Beberapa pola penting yang berhasil diidentifikasi mencerminkan adanya potensi masalah dalam keterlibatan karyawan dan strategi retensi jangka panjang.
Overtime (Lembur): Pegawai yang tidak melakukan lembur justru memiliki tingkat attrisi yang lebih tinggi. Hal ini dapat mengindikasikan kurangnya keterlibatan dalam pekerjaan, minimnya tantangan, atau beban kerja yang terlalu ringan sehingga menurunkan motivasi kerja.
Kelompok Usia: Pegawai berusia 18–30 tahun menunjukkan tingkat attrisi tertinggi dibanding kelompok usia lainnya. Hal ini kemungkinan besar dipicu oleh keinginan eksplorasi karier, kebutuhan akan pertumbuhan cepat, atau ketidakcocokan dengan lingkungan kerja.
Gender: Tingkat attrisi lebih tinggi ditemukan pada pegawai laki-laki dibandingkan perempuan. Hal ini membuka kemungkinan adanya perbedaan persepsi terhadap beban kerja, peluang karier, atau keseimbangan kehidupan kerja.
Posisi/Jabatan: Posisi teknisi laboratorium menjadi posisi dengan tingkat attrisi tertinggi. Hal ini bisa mencerminkan pekerjaan yang monoton, tekanan kerja yang tinggi, atau kurangnya jalur karier yang jelas dalam posisi tersebut.
Masa Kerja: Pegawai dengan pengalaman kerja 0–10 tahun mendominasi kelompok yang mengalami attrisi. Ini menunjukkan pentingnya perhatian khusus terhadap proses onboarding dan pengembangan awal karier untuk meningkatkan loyalitas dan keterikatan pegawai sejak awal.
## Rekomendasi
Untuk mengatasi permasalahan ini, perusahaan perlu membangun strategi retensi yang lebih holistik dan berbasis data. Langkah awal dapat dimulai dengan menciptakan program engagement yang ditujukan khusus bagi pegawai yang tidak terlibat dalam lembur, agar mereka tetap merasa tertantang dan dihargai. Selain itu, perusahaan juga perlu menyediakan jalur pengembangan karier yang jelas serta program mentoring bagi pegawai usia muda, agar mereka melihat prospek jangka panjang yang lebih menjanjikan dalam perusahaan. Evaluasi mendalam terhadap posisi teknisi laboratorium juga menjadi hal yang krusial, baik dari sisi beban kerja maupun potensi pengembangan karier. Proses onboarding serta pembinaan bagi pegawai baru perlu diperkuat agar sejak awal mereka memiliki keterikatan emosional dengan perusahaan. Terakhir, penting untuk melakukan analisis lebih lanjut mengenai penyebab tingginya attrisi pada pegawai laki-laki, serta menyusun kebijakan yang mendukung keseimbangan kerja dan kehidupan yang lebih baik bagi semua pegawai tanpa memandang gender. Dengan pendekatan yang tepat, perusahaan diharapkan dapat menurunkan tingkat attrisi secara signifikan dan membangun lingkungan kerja yang lebih stabil, produktif, dan berkelanjutan.
