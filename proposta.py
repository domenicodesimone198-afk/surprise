import streamlit as st

# Configurazione pagina
st.set_page_config(page_title="Per Te ❤️", page_icon="🌹")

# CSS per rendere tutto più carino
st.markdown("""
    <style>
    .stApp { background-color: #fff5f5; }
    h1 { color: #d63384; text-align: center; }
    .stButton>button { 
        width: 100%; 
        background-color: #ff4b4b; 
        color: white; 
        border-radius: 20px;
    }
    </style>
    """, unsafe_allow_html=True) # <-- CORRETTO QUI

if 'fase' not in st.session_state:
    st.session_state.fase = 'inizio'

if st.session_state.fase == 'inizio':
    st.title("Ehi, ho una sorpresa per te... 🌹")
    if st.button("Cos'è? ✨"):
        st.session_state.fase = 'proposta'
        st.rerun()

elif st.session_state.fase == 'proposta':
    st.balloons()
    st.title("Vuoi venire a Roma con me? 🏛️ ❤️")
    st.write("Ho prenotato un posto speciale per noi ad Aprile!")
    
    hotel_url = "https://www.booking.com/hotel/it/marconi-charme-rooms-amp-suites-2-min-metro-marconi-15-min-colosseo-a-c-amp-wifi.it.html"
    st.link_button("Guarda l'hotel 😍", hotel_url)
    
    if st.button("SÌ! 😍"):
        st.success("Sarà bellissimo! Ti amo! ✨")
        st.snow()
