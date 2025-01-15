import pickle
import streamlit as st
import numpy as np

# Membaca model
try:
    alzheimer_model = pickle.load(open('RFModel.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model tidak ditemukan. Pastikan file 'RFModel.pkl' tersedia di direktori yang sesuai.")
    st.stop()

    # Sidebar navigasi
st.sidebar.title('Aplikasi Prediksi Risiko Penyakit Alzheimer')
halaman = st.sidebar.radio('Pilih Halaman', ['Penjelasan Aplikasi','Prediksi Risiko Alzheimer'])

# Judul aplikasi
def prediksi_risiko_alzheimer():
    st.title('Aplikasi Prediksi Risiko Penyakit Alzheimer')
    st.markdown("""
    Aplikasi ini dirancang untuk membantu mendeteksi risiko awal penyakit Alzheimer 
    berdasarkan faktor-faktor gaya hidup dan kesehatan. Hasil prediksi ini bukan diagnosis medis, 
    dan konsultasikan dengan dokter untuk kepastian lebih lanjut.
    """)


# Input nilai di fitur
    st.sidebar.header("Masukkan Data untuk Prediksi")
    

    Age = st.sidebar.number_input('Usia (tahun)', min_value=0, max_value=120, step=1)
    Job = st.sidebar.selectbox('Status Pekerjaan', ['Tidak bekerja', 'Kuli', 'Pekerja kantoran', 'Pekerja Profesional', 'Pensiunan'])
    BMI = st.sidebar.number_input('Indeks Massa Tubuh (BMI)', min_value=0.0, step=0.1)
    SleepDuration = st.sidebar.number_input('Durasi Tidur (jam/hari)', min_value=0, max_value=24, step=1)
    SocialInteraction = st.sidebar.number_input('Interaksi Sosial (hari/minggu)', min_value=0, step=1)
    CognitiveExercise = st.sidebar.selectbox('Latihan Kognitif', ['Sangat Jarang', 'Kadang-kadang', 'Sering'])
    ScreenTime = st.sidebar.number_input('Penggunaan Gadget Dalam 1 Hari)',min_value=0, max_value=20, step=1)
    DailySteps = st.sidebar.number_input('Langkah Harian', min_value=0, step=100)
    ProcessedFoodFrequency = st.sidebar.number_input('Frekuensi Konsumsi Makanan Olahan (kali/minggu)', min_value=0, step=1)
    MemoryDifficultyNewInformation = st.sidebar.number_input('Kesulitan Mengingat Informasi Baru',min_value=0, max_value=5, step=0)
    FocusLossFrequency = st.sidebar.number_input('Frekuensi Kehilangan Fokus',min_value=0, max_value=5, step=0)
    RepetitiveQuestions = st.sidebar.number_input('Bertanya Berulang-Ulang',min_value=0, max_value=5, step=0)
    DifficultyFollowingInstructions = st.sidebar.number_input('Kesulitan Mengikuti Perintah',min_value=0, max_value=5, step=0)
    ConfusionFrequency = st.sidebar.number_input('Frekuensi Kebingungan',min_value=0, max_value=5, step=0)

    # Validasi input sebelum prediksi
    def validate_inputs():
        return all([
            Age > 0,
            Job != "",
            BMI > 0.0,
            SleepDuration > 0,
            SocialInteraction > 0,
            CognitiveExercise != "",
            ScreenTime > 0,
            DailySteps > 0,
            ProcessedFoodFrequency > 0,
            MemoryDifficultyNewInformation > 0,
            FocusLossFrequency > 0,
            RepetitiveQuestions > 0,
            DifficultyFollowingInstructions > 0,
            ConfusionFrequency > 0
        ])

# Prediksi risiko Alzheimer
    if st.sidebar.button('Prediksi Risiko Alzheimer'):
        if not validate_inputs():
            st.error("Harap isi semua kolom sebelum melakukan prediksi!")
    else:
        try:
            # Konversi input ke format model
            input_data = np.array([[ 
                Age,
                {'Tidak bekerja': 0, 'Kuli': 1, 'Pekerja kantoran': 2, 'Pekerja Profesional': 3, 'Pensiunan': 4}[Job],
                BMI,
                SleepDuration,
                SocialInteraction,
                {'Sangat Jarang': 0, 'Kadang-kadang': 1, 'Sering': 2}[CognitiveExercise],
                ScreenTime,
                DailySteps,
                ProcessedFoodFrequency,
                MemoryDifficultyNewInformation,
                FocusLossFrequency,
                RepetitiveQuestions,
                DifficultyFollowingInstructions,
                ConfusionFrequency
            ]])

            # Prediksi menggunakan model
            prediction = alzheimer_model.predict(input_data)

            # Menampilkan hasil prediksi
            if prediction[0] == 1:
                st.success('Disarankan untuk konsultasi ke dokter.')
            else:
                st.success('Tidak disarankan untuk konsultasi ke dokter.')
        
        except ValueError as e:
            st.error(f"Terjadi kesalahan dalam proses prediksi: {e}")
        
        except Exception as e:
            st.error(f"Kesalahan tak terduga: {e}")




# if st.sidebar.button('Prediksi Risiko Alzheimer'):
#         st.success("Prediksi risiko telah dilakukan (contoh output).")

def penjelasan_aplikasi():
    st.title('Penjelasan Aplikasi')
    st.markdown("""
    **Fitur Utama Aplikasi**:
    1. Umur 
    Usia seseorang, salah satu faktor risiko utama untuk penyakit Alzheimer.
    2. Pekerjaan
    Jenis pekerjaan mencerminkan aktivitas mental dan sosial, yang dapat memengaruhi risiko Alzheimer.
    3.  Indeks Massa Tubuh (BMI)
    pengukuran yang digunakan untuk menilai status berat badan seseorang berdasarkan berat badan dan tinggi badan.
    4. Durasi Tidur
    jumlah waktu tidur seseorang dalam satu hari, biasanya diukur dalam jam. Kualitas dan durasi tidur sangat penting untuk menjaga kesehatan fisik, mental, dan kognitif.
    5. Interaksi Sosial 
    Aktivitas sosial yang rendah dapat meningkatkan risiko penurunan kognitif.
    6. Latihan Kognitif 
    Aktivitas yang melatih otak, seperti membaca atau bermain teka-teki, dapat meningkatkan fungsi kognitif.
    7. Screen Time
    Screen time merujuk pada waktu yang dihabiskan seseorang untuk menggunakan perangkat elektronik seperti ponsel, tablet, komputer, dan televisi.
    8. Langkah Per Hari
    Berjalan atau aktivitas fisik ringan mendukung kesehatan otak dan tubuh secara keseluruhan.
    9. Frekuensi Konsumsi Makanan Olahan
    Konsumsi makanan olahan yang tinggi dapat meningkatkan risiko peradangan dan kerusakan otak.
    10. Kesulitan Mengingat Informasi Baru
    Kesulitan dalam mengingat informasi baru, seperti nama orang yang baru ditemui atau instruksi yang baru diterima.
    11. Frekuensi Kehilangan Fokus
    Seberapa sering seseorang kehilangan fokus atau tidak mampu berkonsentrasi pada tugas tertentu
    12. Bertanya Berulang-Ulang
    Kebiasaan seseorang untuk mengulang pertanyaan yang sama meskipun telah mendapatkan jawaban sebelumnya.
    13. Kesulitan Mengikuti Perintah
    Kesulitan dalam memahami dan mengikuti instruksi, terutama yang melibatkan beberapa langkah.
    14. Frekuensi Kebingungan
    Seberapa sering seseorang merasa bingung tentang waktu, tempat, atau situasi tertentu.""")
    
    st.title('Cara Penggunaan')
    st.markdown("""
    **Langkah-Langkah**:
    1. Pilih Halaman Prediksi Risiko Alzheimer
    1. Isi semua data di sidebar.
    2. Klik tombol **Prediksi Risiko Alzheimer**.
    3. Lihat hasil prediksi di layar utama.
    """)
    st.title('Tujuan Aplikasi')
    st.markdown("""
    **Tujuan Utama**:
    - Meningkatkan kesadaran tentang risiko Alzheimer.
    - Membantu pengguna memahami faktor risiko.
    - Memberikan panduan untuk tindakan preventif.
    """)

# Kondisi untuk navigasi antar halaman
if halaman == 'Prediksi Risiko Alzheimer':
    prediksi_risiko_alzheimer()
elif halaman == 'Penjelasan Aplikasi':
    penjelasan_aplikasi()
