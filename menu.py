import warnings
warnings.filterwarnings('ignore')
import streamlit as st
import xgboost
from streamlit_option_menu import option_menu


with st.sidebar:
    selected = option_menu('Pilih Halaman',
    ['Tentang Saya',
     'Proyek', 'Kontak'],                       
    default_index=0)
    
if selected == 'Proyek':
    import delivery
    delivery.delivery_predict()
elif selected == 'Kontak':
    import kontak
    kontak.tampilkan_kontak()
elif selected == 'Tentang Saya':
    import tentang
    tentang.tentang()