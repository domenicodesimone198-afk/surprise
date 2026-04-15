import streamlit as st

# Configurazione pagina
st.set_page_config(page_title="Per Te ❤️", page_icon="🌹")

# CSS per lo sfondo arancione/giallo e testo scuro
st.markdown("""
    <style>
    /* Sfondo principale arancione/giallo solare */
    .stApp { background-color: #ffd700; } 

    /* Titolo principale rosa shocking */
    h1 { 
        color: #d63384; 
        text-align: center; 
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3); /* Un po' di ombra per leggibilità */
    }

    /* Testo secondario in scuro per contrasto */
    .stMarkdown p { 
        color: #333; 
        font-size: 1.1em; 
        font-weight: bold;
        text-align: center;
    }

    /* Pulsanti principali (rosso passione) */
    .stButton>button { 
        width: 100%; 
        background-color: #ff4b4b; 
        color: white; 
        border-radius: 20px;
        font-weight: bold;
        font-size: 1.2em;
        border: 2px solid #ff4b4b;
    }
    .stButton>button:hover {
        background-color: #d63384; /* Cambia colore al passaggio del mouse */
    }

    /* Pulsante link (verde mela) */
    a.stLinkButton {
        display: block;
        width: 100%;
        text-align: center;
        background-color: #28a745;
        color: white !important;
        border-radius: 20px;
        padding: 10px;
        margin-top: 10px;
        font-weight: bold;
        text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True) 

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
