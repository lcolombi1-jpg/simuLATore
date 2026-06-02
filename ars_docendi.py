import streamlit as st

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Ludus", page_icon="🏛️", layout="wide")

# --- ESTETICA EUPHORIA (CSS INIETTATO) ---
# Qui definiamo i colori neon e l'atmosfera dark per abbassare il "filtro affettivo" (l'ansia)
euphoria_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');

    /* Sfondo globale e font */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1a0033 0%, #0b001a 100%);
        color: #ffffff;
        font-family: 'Montserrat', sans-serif;
    }

    /* Nascondi header e footer di default Streamlit per un look full-app */
    header, footer {visibility: hidden;}

    /* Titolo Neon */
    .neon-title {
        font-size: 4.5rem;
        font-weight: 900;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 5px;
        color: #fff;
        text-shadow: 0 0 10px #b537f2, 0 0 20px #b537f2, 0 0 40px #ff00c8, 0 0 80px #ff00c8;
        margin-top: -50px;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 1.3rem;
        text-align: center;
        color: #00f3ff;
        text-shadow: 0 0 8px #00f3ff;
        margin-bottom: 50px;
    }

    /* Styling delle "Porte" (Bottoni Streamlit trasformati) */
    div.stButton > button {
        height: 350px;
        width: 100%;
        background: rgba(255, 255, 255, 0.05) !important;
        border: 2px solid #ffffff !important;
        border-radius: 20px !important;
        color: white !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        transition: all 0.4s ease !important;
        backdrop-filter: blur(10px);
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.1);
    }

    /* Effetti Hover per le Porte */
    /* Beginner */
    button[kind="secondary"]:hover {
        border-color: #00f3ff !important;
        box-shadow: 0 0 40px #00f3ff, inset 0 0 20px #00f3ff !important;
        color: #00f3ff !important;
        transform: translateY(-10px);
    }
    /* Intermediate (Purple) */
    div[data-testid="stVerticalBlock"] > div:nth-child(2) button:hover {
        border-color: #b537f2 !important;
        box-shadow: 0 0 40px #b537f2, inset 0 0 20px #b537f2 !important;
        color: #b537f2 !important;
    }
    /* Pro (Pink/Red) */
    div[data-testid="stVerticalBlock"] > div:nth-child(3) button:hover {
        border-color: #ff0055 !important;
        box-shadow: 0 0 40px #ff0055, inset 0 0 20px #ff0055 !important;
        color: #ff0055 !important;
    }
    
    /* Box Messaggi Pedagocici */
    .didactic-note {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #b537f2;
        margin-top: 40px;
    }
</style>
"""
st.markdown(euphoria_css, unsafe_allow_html=True)

# --- LOGICA DELL'APP ---
if 'level' not in st.session_state:
    st.session_state.level = None

# --- SCHERMATA INIZIALE (LOBBY) ---
if st.session_state.level is None:
    st.markdown('<h1 class="neon-title">Ludus</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Scegli il tuo destino, discipule.</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🚪\n\nDISCIPULUS\n(Beginner)"):
            st.session_state.level = "Beginner"
            st.rerun()

    with col2:
        if st.button("⚔️\n\nGLADIATOR\n(Intermediate)"):
            st.session_state.level = "Intermediate"
            st.rerun()

    with col3:
        if st.button("👑\n\nIMPERATOR\n(Pro)"):
            st.session_state.level = "Pro"
            st.rerun()

    # Nota didattica per te
    st.markdown(f"""
    <div class="didactic-note">
        <b>💡 Tip Didattico:</b> Questo layout usa la <i>Gamification</i> per stimolare la Dopamina. 
        Secondo i manuali di glottodidattica, trasformare il test in un "Level Up" riduce il blocco mentale 
        che i ragazzi hanno davanti al latino tradizionale.
    </div>
    """, unsafe_allow_html=True)

# --- SCHERMATA DEL TEST (AREA DA RIEMPIRE) ---
else:
    level = st.session_state.level
    st.markdown(f'<h1 class="neon-title" style="font-size:3rem;">{level} Mode</h1>', unsafe_allow_html=True)
    
    # Esempio di come apparirà il test
    st.write(f"### Benvenuto nell'arena, {level}!")
    st.write("Qui caricheremo le tue domande e i tuoi esercizi.")
    
    # Bottone per tornare indietro
    if st.button("Torna alla Lobby"):
        st.session_state.level = None
        st.rerun()
