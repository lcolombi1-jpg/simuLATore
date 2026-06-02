import streamlit as st

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Ludus", page_icon="🏛️", layout="wide")

# --- ESTETICA EUPHORIA + ROMA ANTICA (CSS INIETTATO) ---
euphoria_css = """
<style>
    /* Importiamo Montserrat per i testi normali e Cinzel per lo stile epigrafico romano */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Montserrat:wght@400;700;900&display=swap');

    /* Sfondo globale scuro stile Euphoria */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1a0033 0%, #0b001a 100%);
        color: #ffffff;
        font-family: 'Montserrat', sans-serif;
    }

    /* Nascondi header e footer di default Streamlit */
    header, footer {visibility: hidden;}

    /* Contenitore per centrare perfettamente il titolo */
    .title-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        margin-top: -40px;
        margin-bottom: 50px;
    }

    /* Titolo LUDUS Centrato e Neon */
    .neon-title {
        font-size: 6rem;
        font-weight: 900;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 15px;
        color: #fff;
        text-shadow: 
            0 0 10px #b537f2, 
            0 0 20px #b537f2, 
            0 0 40px #ff00c8, 
            0 0 80px #ff00c8;
        margin: 0;
        padding: 0;
        margin-left: 15px; /* Compensa il letter-spacing per la centratura perfetta */
    }

    .subtitle {
        font-size: 1.2rem;
        text-align: center;
        color: #00f3ff;
        text-shadow: 0 0 8px #00f3ff;
        margin-top: 5px;
        letter-spacing: 3px;
        text-transform: lowercase;
    }

    /* --- STILE DELLE PORTE AD ARCO DI TRIONFO --- */
    /* Forza dimensioni identiche per tutti i bottoni */
    div.stButton > button {
        height: 450px !important;
        width: 100% !important;
        
        /* Forma ad Arco: tanto arrotondamento sopra, angoli retti sotto */
        border-radius: 200px 200px 15px 15px !important;
        
        /* Effetto vetro/pietra scura */
        background: rgba(30, 10, 50, 0.4) !important;
        border: 2px solid rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px);
        
        /* Ombreggiatura interna per dare profondità all'arco */
        box-shadow: inset 0 20px 50px rgba(0,0,0,0.8), 0 10px 20px rgba(0,0,0,0.5) !important;
        
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 20px !important;
    }

    /* Rimuove i margini di default del testo nei bottoni */
    div.stButton > button p {
        margin: 0 !important;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
    }

    /* --- STILE EPIGRAFICO (Incisione su pietra) --- */
    /* Usiamo il tag <strong> (attivato tramite Markdown nel bottone Python) */
    div.stButton > button strong {
        font-family: 'Cinzel', serif !important;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        letter-spacing: 4px;
        color: #d1d1d1;
        
        /* Effetto inciso (Engraved): ombra scura in alto a sx, luce in basso a dx */
        text-shadow: 
            -1px -1px 2px rgba(0, 0, 0, 0.9),
             1px  1px 1px rgba(255, 255, 255, 0.15);
             
        display: block;
        margin-bottom: 20px;
    }

    /* Stile per la traduzione inglese (usiamo il tag <em>) */
    div.stButton > button em {
        font-family: 'Montserrat', sans-serif !important;
        font-size: 1.1rem !important;
        font-style: normal !important;
        text-transform: uppercase;
        letter-spacing: 5px;
        color: rgba(255, 255, 255, 0.4);
        
        /* Effetto inciso più leggero */
        text-shadow: -1px -1px 1px rgba(0,0,0,0.8), 1px 1px 1px rgba(255,255,255,0.1);
        display: block;
    }

    /* --- EFFETTI NEON HOVER (Le porte si accendono quando passi il mouse) --- */
    
    /* Porta 1: Ciano */
    div[data-testid="column"]:nth-child(1) button:hover {
        border-color: #00f3ff !important;
        box-shadow: 0 0 40px rgba(0, 243, 255, 0.3), inset 0 20px 50px rgba(0, 243, 255, 0.1) !important;
        transform: translateY(-15px);
    }
    div[data-testid="column"]:nth-child(1) button:hover strong {
        color: #00f3ff !important;
        text-shadow: 0 0 15px #00f3ff, -1px -1px 2px rgba(0,0,0,0.9);
    }

    /* Porta 2: Viola */
    div[data-testid="column"]:nth-child(2) button:hover {
        border-color: #b537f2 !important;
        box-shadow: 0 0 40px rgba(181, 55, 242, 0.3), inset 0 20px 50px rgba(181, 55, 242, 0.1) !important;
        transform: translateY(-15px);
    }
    div[data-testid="column"]:nth-child(2) button:hover strong {
        color: #b537f2 !important;
        text-shadow: 0 0 15px #b537f2, -1px -1px 2px rgba(0,0,0,0.9);
    }

    /* Porta 3: Fucsia */
    div[data-testid="column"]:nth-child(3) button:hover {
        border-color: #ff00c8 !important;
        box-shadow: 0 0 40px rgba(255, 0, 200, 0.3), inset 0 20px 50px rgba(255, 0, 200, 0.1) !important;
        transform: translateY(-15px);
    }
    div[data-testid="column"]:nth-child(3) button:hover strong {
        color: #ff00c8 !important;
        text-shadow: 0 0 15px #ff00c8, -1px -1px 2px rgba(0,0,0,0.9);
    }
    
</style>
"""
st.markdown(euphoria_css, unsafe_allow_html=True)

# --- LOGICA DI NAVIGAZIONE ---
if 'level' not in st.session_state:
    st.session_state.level = None

# --- SCHERMATA INIZIALE (LOBBY ARCHI DI TRIONFO) ---
if st.session_state.level is None:
    
    # Titolo centrato
    st.markdown("""
        <div class="title-container">
            <h1 class="neon-title">LUDUS</h1>
            <p class="subtitle">scegli il tuo destino</p>
        </div>
    """, unsafe_allow_html=True)

    # Creiamo 3 colonne con un po' di spazio ai lati per centrare le porte
    _, col1, col2, col3, _ = st.columns([0.5, 2, 2, 2, 0.5])

    # NOTA: Usiamo il markdown nei bottoni. 
    # **testo** diventa <strong> (per il latino), *testo* diventa <em> (per l'inglese).
    # Il CSS sopra intercetta questi tag e li stila in modo diverso!
    
    with col1:
        if st.button("**DISCIPVLVS**\n\n*beginner*", use_container_width=True):
            st.session_state.level = "Discipulus"
            st.rerun()

    with col2:
        if st.button("**GLADIATOR**\n\n*intermediate*", use_container_width=True):
            st.session_state.level = "Gladiator"
            st.rerun()

    with col3:
        if st.button("**IMPERATOR**\n\n*pro*", use_container_width=True):
            st.session_state.level = "Imperator"
            st.rerun()

# --- SCHERMATA DEI TEST ---
else:
    level = st.session_state.level
    st.markdown(f"""
        <div class="title-container" style="margin-top: 20px;">
            <h1 class="neon-title" style="font-size:4rem;">{level}</h1>
            <p class="subtitle">arena attiva</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Spazio temporaneo per i test
    st.info(f"Benvenuto nell'arena, {level}. Qui appariranno gli esercizi.")
    
    # Bottone di ritorno (stilizzato standard)
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("← Torna agli Archi"):
        st.session_state.level = None
        st.rerun()
