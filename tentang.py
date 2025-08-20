import warnings
warnings.filterwarnings('ignore')
import streamlit as st

def tentang():
    st.title("👋 Selamat Datang di Aplikasi Prediksi Waktu Delivery")

    st.markdown("---")

    st.subheader("🧑‍💼 Profil")
    st.markdown("""
    **Nama:** Endar Dwi Haryanto  
    **Profesi:** Data Scientist  
    **Lokasi:** Indonesia  
    """)

    st.subheader("📌 Tentang Aplikasi")
    st.markdown("""
    Aplikasi ini dibuat menggunakan **Streamlit** dengan tujuan untuk:
    - Menyediakan prediksi waktu delivery bedasarkan jarak,jenis kendaraan, kondisi traffic dll
    - Memberikan pengalaman eksplorasi data yang sederhana, cepat, dan efisien.

    Model prediksi dikembangkan menggunakan algoritma **Machine Learning**, dengan fitur-fitur seperti jarak, jenis kendaraan, kondisi lalulintas dan lainnya.
    """)

    st.subheader("🛠️ Tools & Teknologi")
    st.markdown("""
    - Python
    - Streamlit
    - Scikit-Learn
    - Pandas & NumPy
    - Plotly
    """)

    st.subheader("📫 Kontak")
    st.markdown("""
    - 📧 Email: [endardwi507@gmail.com](mailto:endar@example.com)  
    - 💼 LinkedIn: [linkedin.com/in/endardwiharyanto](https://www.linkedin.com/in/endardwiharyanto/)  
    - 🧑‍💻 GitHub: [github.com/endar](https://github.com/Endar06)
    """)

    st.markdown("---")
    st.info("Terima kasih telah mengunjungi aplikasi ini. Silakan gunakan menu di sebelah kiri untuk menjelajahi fitur lainnya.")