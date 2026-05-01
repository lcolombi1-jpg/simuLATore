import streamlit as st

# 1. Configurazione della pagina - Game Mode
st.set_page_config(page_title="Legio Latina", page_icon="⚔️", layout="centered")

# 2. CSS Avanzato per risolvere i difetti di visualizzazione
st.markdown("""
    <style>
    /* Forza il font Times New Roman su ogni elemento */
    @import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,700;1,400&display=swap');
    
    html, body, [class*="st-"], .stMarkdown, h1, h2, h3, h4, p, label {
        font-family: "Times New Roman", Times, serif !important;
    }

    /* Sfondo nero profondo e testo bianco per contrasto videogame */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }

    /* Rende le etichette delle risposte (radio buttons) bianche e leggibili */
    div[data-testid="stWidgetLabel"] p {
        color: #ffffff !important;
        font-size: 1.2rem !important;
    }
    
    label[data-testid="stWidgetLabel"] {
        color: #ffffff !important;
    }

    /* Stile per i contenitori delle domande */
    .stExpander {
        background-color: #1a1c23 !important;
        border: 1px solid #3e4452 !important;
        border-radius: 10px !important;
    }
    
    /* Bottone primario stile "Battle" */
    .stButton>button {
        background-color: #ff4b4b !important;
        color: white !important;
        border-radius: 5px;
        border: none;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar - Il Castrum (Quartier Generale)
with st.sidebar:
    # Icona Busto Romano (Nero/Bianco stilizzato)
    st.image("https://img.icons8.com/ios-filled/100/ffffff/roman-buste.png", width=80)
    st.title("CASTRUM")
    st.markdown("---")
    
    if 'xp' not in st.session_state:
        st.session_state.xp = 0
    
    st.write(f"**Status Militis:** Recluta")
    st.write(f"**XP Totali:** {st.session_state.xp}")
    
    # Progresso missione
    if 'domande' in st.session_state:
        risposte_date = sum(1 for q in st.session_state.domande if st.session_state.get(f"q_{q['id']}") is not None)
        st.write(f"Conquista: {risposte_date}/10")
        st.progress(risposte_date / 10)

# 4. Database Domande (Controllato per errori di sintassi)
if 'domande' not in st.session_state:
    st.session_state.domande = [
        {"id": 1, "testo": "Tota provincia _____________ occupata erat", "opzioni": ["Ab hostes", "Ad hostes", "Ab hostibus", "Hostibus"], "corretta": "Ab hostibus"},
        {"id": 2, "testo": "_____________ poetarum lecta sunt", "opzioni": ["carminis", "carmen", "carmina", "carmines"], "corretta": "carmina"},
        {"id": 3, "testo": "Hannibal fratrem Hasdrubalem in Italiam cum omnibus ______ copiis vocavit", "opzioni": ["suum", "suus", "eius"], "corretta": "eius"},
        {"id": 4, "testo": "Pietatis ac fortitudinis exempla _________ ad virtutem ducunt", "opzioni": ["hominum", "hominibus", "homines", "homini"], "corretta": "homines"},
        {"id": 5, "testo": "Hannibal fratrem _______ Hasdrubalem in Italiam vocavit", "opzioni": ["suum", "suus", "eius"], "corretta": "suum"},
        {"id": 6, "testo": "_____________ mansi", "opzioni": ["Romā", "In Romā", "Romam", "Romae"], "corretta": "Romae"},
        {"id": 7, "testo": "Postquam bellum confectum est, consul ad hostes legatos misit _______ agentes", "opzioni": ["de pacem", "de pace", "ob pacem", "propter pacem"], "corretta": "de pace"},
        {"id": 8, "testo": "Domina armillas ____________ ancillis donabat", "opzioni": ["eximia pulchritudo", "eximiae pulchritudines", "eximiae pulchritudinis", "eximiam pulchritudinem"], "corretta": "eximiae pulchritudinis"},
        {"id": 9, "testo": "Athenis multas effigies deorum ________ vidi", "opzioni": ["marmor", "marmore", "ex marmore", "marmores"], "corretta": "ex marmore"},
        {"id": 10, "testo": "Pueri _________ verba audient", "opzioni": ["pater", "patres", "patri", "patrum"], "corretta": "patrum"}
    ]

# 5. Header Campagna
col_img, col_tit = st.columns([1, 4])
with col_img:
    st.image("https://img.icons8.com/ios/100/ffffff/coliseum.png", width=80)
with col_tit:
    st.title("LEGIO LATINA")
    st.subheader("La Campagna di Sintassi")

st.markdown("---")

# 6. Esecuzione Missioni (Domande)
for q in st.session_state.domande:
    with st.expander(f"⚜️ SFIDA {q['id']}", expanded=True):
        st.markdown(f"### *{q['testo']}*")
        st.radio(
            "Scegli la tua mossa:", 
            q['opzioni'], 
            key=f"q_{q['id']}", 
            index=None, 
            horizontal=True
        )

# 7. Esito della Battaglia
st.markdown("---")
if st.button("INVIA RAPPORTO A CESARE ⚔️"):
    punti = 0
    st.write("## 📜 Esito dello Scontro")
    for q in st.session_state.domande:
        risposta = st.session_state.get(f"q_{q['id']}")
        if risposta == q['corretta']:
            punti += 1
            st.success(f"Sfida {q['id']}: Vittoria Schiacciante! ✅")
        else:
            st.error(f"Sfida {q['id']}: Sconfitta. La tattica era '{q['corretta']}' ❌")
    
    st.session_state.xp = punti * 100
    st.divider()
    
    if punti == 10:
        st.balloons()
        st.header("TRIUMPHUS! 🏆")
        st.write("Hai conquistato Roma. Cesare ti attende per l'alloro.")
    elif punti >= 6:
        st.info(f"Hai ottenuto {punti}/10. La Legione resiste.")
    else:
        st.warning(f"Solo {punti}/10. Ritirati nel Castrum per studiare le tattiche.")
