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

# Catatan Kuliah
materi_titles = {
    "Kimia Fisika 🔬": {
        1: "Gas Ideal dan Gas Nyata",
        2: "Hukum Thermodinamika"
    },
    "Spektrofotometri 🧪": {
        1: "Spektrofotometri Infrared",
        2: "Flame Photometry",
        3: "ICP AES"
    },
    "Biokimia 🧬": {
        1: "Karbohidrat",
        2: "Protein",
        3: "Enzim"
    }
}

elif menu == "Catatan Kuliah 📒":
    st.title("📒 Catatan Kuliah")
    
    # Inisialisasi session_state jika belum ada
    if "selected_matkul_simple" not in st.session_state:
        st.session_state.selected_matkul_simple = None
    if "selected_pertemuan_simple" not in st.session_state:
        st.session_state.selected_pertemuan_simple = None
    
    # Dropdown Mata Kuliah
    matkul_options = list(materi_titles.keys())
    selected_matkul = st.selectbox("Pilih Mata Kuliah", matkul_options, key="matkul_dropdown_simple")
    
    # Jika mata kuliah dipilih (saat selectbox berubah)
    if selected_matkul != st.session_state.selected_matkul_simple:
        st.session_state.selected_matkul_simple = selected_matkul
        st.session_state.selected_pertemuan_simple = None # Reset pertemuan jika matkul berubah
    
    # Tampilkan tombol pertemuan hanya jika mata kuliah sudah dipilih
    if st.session_state.selected_matkul_simple:
        st.subheader(f"Catatan untuk {st.session_state.selected_matkul_simple}")
        st.markdown("---")
        st.write("Pilih Materi Pertemuan:")
        
        # Mendapatkan judul materi untuk mata kuliah yang sedang dipilih
        current_matkul_titles = materi_titles.get(st.session_state.selected_matkul_simple, {})
        
        # Menentukan berapa banyak kolom yang dibutuhkan berdasarkan jumlah pertemuan
        num_pertemuan = len(current_matkul_titles)
        cols = st.columns(num_pertemuan if num_pertemuan > 0 else 1) # Buat kolom sebanyak jumlah pertemuan
    
        # Loop melalui nomor pertemuan yang ada untuk mata kuliah ini
        sorted_pertemuan_nums = sorted(current_matkul_titles.keys()) 
        
        for idx, pertemuan_num in enumerate(sorted_pertemuan_nums):
            with cols[idx]: # Menggunakan indeks untuk menempatkan tombol di kolom yang berbeda
                button_label = current_matkul_titles.get(pertemuan_num, f"Pertemuan {pertemuan_num}")
                
                def set_pertemuan_simple_callback(p_num): # Ganti nama fungsi callback agar tidak bentrok
                    st.session_state.selected_pertemuan_simple = p_num
                
                st.button(button_label, key=f"materi_btn_simple_{pertemuan_num}", on_click=set_pertemuan_simple_callback, args=(pertemuan_num,))
    
        # Menampilkan Konten Pertemuan
        if st.session_state.selected_pertemuan_simple:
            st.markdown("---")
            konten_subheader_title = current_matkul_titles.get(st.session_state.selected_pertemuan_simple, f"Konten Pertemuan {st.session_state.selected_pertemuan_simple}")
            st.subheader(f"Konten: {konten_subheader_title}")
            st.write(f"Ini adalah detail untuk {st.session_state.selected_matkul_simple} - {konten_subheader_title}.")
            
elif menu == "Tentang ℹ️":
    st.title("ℹ️Tentang MindTrack")
    st.write("MindTrack adalah sebuah web yang dirancang untuk membantu mahasiswa khusunya di lingkungan Politeiknik AKA Bogor dalam memahami konsep-konsep penting di mata kuliah teori.")
    
