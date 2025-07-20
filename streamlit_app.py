import streamlit as st

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="MindTrack", page_icon="🧠")

menu = st.sidebar.selectbox("📚 Pilih Halaman", ["Beranda 🏠", "Latihan Soal ✏️", "Catatan Kuliah 📒", "Tentang ℹ️"])

