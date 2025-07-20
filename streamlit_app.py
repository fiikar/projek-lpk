import streamlit as st

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="MindTrack", page_icon="🧠")

menu = st.sidebar.selectbox("📚 Pilih Halaman", ["Beranda 🏠", "Latihan Soal ✏️", "Catatan Kuliah 📒", "Tentang ℹ️"])

if menu == "Beranda 🏠":
    st.title("🧠 MindTrack")
    st.write("Selamat datang di MindTrack, 👋")
    st.write("Sudah Siap Untuk Mulai Belajar?")
    st.info("Gunakan menu di sebelah kiri untuk mulai belajar.")

elif menu == "Latihan Soal ✏️":
    st.title("✏️ Latihan Soal")

elif menu == "Catatan Kuliah 📒":
    st.title("📒 Catatan Kuliah")

elif menu == "Tentang ℹ️":
    st.title("ℹ️Tentang MindTrack")
    st.write("MindTrack adalah sebuah web yang dirancang untuk membantu mahasiswa khusunya di lingkungan Politeiknik AKA Bogor dalam memahami konsep-konsep penting di mata kuliah teori.")
    
