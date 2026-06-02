import streamlit as st

# --- CONFIGURAZIONE DELLA PAGINA ---
st.set_page_config(
    page_title="Ludus",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ESTETICA EUPHORIA E ARCHI ROMANI (CSS INIETTATO) ---
euphoria_css = """
<style>
    /* Importazione dei font da Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@400;700&display=swap');

    /* Sfondo scuro e profondo con gradiente radiale */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #15002b 0%, #05000a 100%) !important;
        color: #ffffff !important;
        font-family: 'Montserrat', sans-serif;
    }

    /* Rimozione di elementi grafici di default di Streamlit per un look pulito */
    header, footer, [data-testid="stHeader"] {
        visibility: hidden !important;
        height: 0px !important;
    }

    /* Contenitore principale per centrare il titolo */
    .title-wrapper {
        text-align: center;
        margin-top: 40px;
        margin-bottom: 60px;
        width: 100%;
    }

    /* Titolo LUDUS con effetto Neon */
    .neon-title {
        font-family: 'Cinzel', serif;
        font-size: 5.5rem;
        font-weight: 700;
        letter-spacing: 15px;
        color: #ffffff;
        text-transform: uppercase;
        text-shadow: 
            0 0 10px #b537f2, 
            0 0 25px #b537f2, 
            0 0 50px #ff00c8;
        margin: 0;
        padding-left: 15px;
    }

    .subtitle {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.1rem;
        color: #00f3ff;
        text-transform: lowercase;
        letter-spacing: 8px;
        text-shadow: 0 0 10px #00f3ff;
        margin-top: 10px;
    }

    /* --- STRUTTURA DELLE PORTE AD ARCO (BOTTONI) --- */
    div.stButton > button {
        height: 480px !important;
        width: 100% !important;
        
        /* Taglio ad arco: tondo sopra, dritto sotto */
        border-radius: 240px 240px 15px 15px !important;
        
        /* Interno dell'arco scuro e semitrasparente */
        background: rgba(8, 2, 18, 0.75) !important;
        backdrop-filter: blur(10px);
        
        /* Bordo che funge da tubo neon */
        border-width: 4px !important;
        border-style: solid !important;
        
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 30px !important;
    }

    /* Testo in grassetto (Latino Epigrafico) */
    div.stButton > button strong {
        font-family: 'Cinzel', serif !important;
        font-size: 1.6rem !important;
        letter-spacing: 3px;
        font-weight: 700 !important;
        display: block;
        margin-bottom: 12px;
        transition: all 0.3s ease;
    }

    /* Testo in corsivo (Sottotitolo livello) */
    div.stButton > button em {
        font-family: 'Montserrat', sans-serif !important;
        font-size: 0.95rem !important;
        font-style: normal !important;
        text-transform: uppercase;
        letter-spacing: 4px;
        color: rgba(255, 255, 255, 0.45);
        display: block;
    }

    /* --- EFFETTI NEON SUI SINGOLI ARCHI --- */

    /* Porta 1: Ciano (Discipulus) */
    div[data-testid="column"]:nth-child(2) button {
        border-color: #00f3ff !important;
        box-shadow: 
            0 0 20px rgba(0, 243, 255, 0.4), 
            inset 0 0 20px rgba(0, 243, 255, 0.4), 
            inset 0 0 50px rgba(0,0,0,0.9) !important;
    }
    div[data-testid="column"]:nth-child(2) button strong { 
        color: #00f3ff !important; 
        text-shadow: 0 0 10px rgba(0, 243, 255, 0.8) !important; 
    }
    div[data-testid="column"]:nth-child(2) button:hover {
        box-shadow: 
            0 0 40px #00f3ff, 
            inset 0 0 30px #00f3ff !important;
        transform: translateY(-12px);
    }

    /* Porta 2: Viola (Gladiator) */
    div[data-testid="column"]:nth-child(3) button {
        border-color: #b537f2 !important;
        box-shadow: 
            0 0 20px rgba(181, 55, 242, 0.4), 
            inset 0 0 20px rgba(181, 55, 242, 0.4), 
            inset 0 0 50px rgba(0,0,0,0.9) !important;
    }
    div[data-testid="column"]:nth-child(3) button strong { 
        color: #d884ff !important; 
        text-shadow: 0 0 10px rgba(181, 55, 242, 0.8) !important; 
    }
    div[data-testid="column"]:nth-child(3) button:hover {
        box-shadow: 
            0 0 40px #b537f2, 
            inset 0 0 30px #b537f2 !important;
        transform: translateY(-12px);
    }

    /* Porta 3: Fucsia (Imperator) */
    div[data-testid="column"]:nth-child(4) button {
        border-color: #ff00c8 !important;
        box-shadow: 
            0 0 20px rgba(255, 0, 200, 0.4), 
            inset 0 0 20px rgba(255, 0, 200, 0.4), 
            inset 0 0 50px rgba(0,0,0,0.9) !important;
    }
    div[data-testid="column"]:nth-child(4) button strong { 
        color: #ff70d6 !important; 
        text-shadow: 0 0 10px rgba(255, 0, 200, 0.8) !important; 
    }
    div[data-testid="column"]:nth-child(4) button:hover {
        box-shadow: 
            0 0 40px #ff00c8, 
            inset 0 0 30px #ff00c8 !important;
        transform: translateY(-12px);
    }

</style>
"""
st.markdown(euphoria_css, unsafe_allow_html=True)

# --- INIZIALIZZAZIONE STATO DI NAVIGAZIONE ---
if 'level' not in st.session_state:
    st.session_state.level = None

# --- LOBBY CON LE TRE PORTE ---
if st.session_state.level is None:
    
    # Intestazione con titolo centrato
    st.markdown("""
        <div class="title-wrapper">
            <h1 class="neon-title">LUDUS</h1>
            <p class="subtitle">scegli il tuo destino</p>
        </div>
    """, unsafe_allow_html=True)

    # Griglia di colonne per centrare perfettamente gli archi
    _, col1, col2, col3, _ = st.columns([0.5, 2, 2, 2, 0.5])

    with col1:
        if st.button("**DISCIPVLVS**\n\n*beginner*", key="btn_discipulus"):
            st.session_state.level = "Discipulus"
            st.rerun()

    with col2:
        if st.button("**GLADIATOR**\n\n*intermediate*", key="btn_gladiator"):
            st.session_state.level = "Gladiator"
            st.rerun()

    with col3:
        if st.button("**IMPERATOR**\n\n*pro*", key="btn_imperator"):
            st.session_state.level = "Imperator"
            st.rerun()

# --- SCHERMATA DEL LIVELLO ATTIVO (TEST) ---
else:
    # Mostra l'arena del livello selezionato
    st.markdown(f"""
        <div class="title-wrapper">
            <h1 class="neon-title" style="font-size: 4rem;">{st.session_state.level}</h1>
            <p class="subtitle">arena attiva</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Spazio per gli esercizi
    st.info(f"Benvenuto/a nell'arena {st.session_state.level}. Qui inseriremo gli esercizi di latino!")
    
    # Pulsante per tornare alla selezione delle porte
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("← Torna alla selezione"):
        st.session_state.level = None
        st.rerun()
