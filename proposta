import streamlit as st
import time

# Configurazione estetica
st.set_page_config(page_title="Per Te ❤️", page_icon="🌹")

# Stile personalizzato per renderlo romantico
st.markdown("""
    <style>
    .stApp { background-color: #fff5f5; }
    h1 { color: #d63384; font-family: 'Helvetica', sans-serif; text-align: center; }
    .stButton>button { 
        width: 100%; 
        background-color: #ff4b4b; 
        color: white; 
        border-radius: 25px; 
        height: 3em;
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_index=True)

if 'fase' not in st.session_state:
    st.session_state.fase = 'inizio'

# --- LOGICA DELLA PROPOSTA ---

if st.session_state.fase == 'inizio':
    st.title("Ehi, ho un piccolo segreto per te... 🤫")
    st.write("---")
    if st.button("Cos'è? ✨"):
        st.session_state.fase = 'ricordo'
        st.rerun()

elif st.session_state.fase == 'ricordo':
    st.title("Ogni momento con te è speciale.")
    st.write("Ma ho pensato che fosse ora di crearne uno nuovo, indimenticabile.")
    # st.image("tua_foto.jpg") # Se hai una foto, caricala qui!
    if st.button("Continua... ❤️"):
        st.session_state.fase = 'proposta'
        st.rerun()

elif st.session_state.fase == 'proposta':
    st.balloons() # Esplosione di palloncini!
    st.title("Vuoi venire a Roma con me? 🏛️")
    st.write("Ho già adocchiato un posticino niente male per noi...")
    
    # Bottone che porta direttamente a Booking
    hotel_url = "https://www.booking.com/hotel/it/marconi-charme-rooms-amp-suites-2-min-metro-marconi-15-min-colosseo-a-c-amp-wifi.it.html"
    st.link_button("Guarda dove staremo 😍", hotel_url)
    
    if st.button("SÌ, NON VEDO L'ORA! ✨"):
        st.success("Preparati, Roma ci aspetta! Ti amo! ❤️")
        st.snow() # Effetto neve/magico
