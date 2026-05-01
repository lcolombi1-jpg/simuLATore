import streamlit as st

# 1. Configurazione della pagina (Game Mode)
st.set_page_config(page_title="Legio Latina", page_icon="⚔️", layout="centered")

# 2. CSS per l'effetto Videogame RPG
st.markdown("""
    <style>
    /* Font Times New Roman e Colori Dark RPG */
    html, body, [class*="st-"], .stMarkdown, h1, h2, h3, h4, p, label {
        font-family: "Times New Roman", Times, serif !important;
    }
    .stApp {
        background-color: #1a1a1a;
        color: #e0e0e0;
    }
    /* Box delle domande come "Incontri" */
    .stBox {
        background-color: #262626;
        border: 2px solid #4a4a4a;
        border-radius: 10px;
        padding: 20px;
    }
    /* Barra della Vita / Progresso */
    .stProgress > div > div > div > div {
        background-color: #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar: Status del Giocatore
with st.sidebar:
    st.image("https://img.icons8.com/?size=100&id=23307&format=png&color=ffffff", width=80)
    st.title("🛡️ Status Legio")
    st.markdown("---")
    
    # Inizializzazione punteggio
    if 'xp' not in st.session_state:
        st.session_state.xp = 0
    
    st.write(f"**Soldato:** Discipulus")
    st.write(f"**XP Guadagnati:** {st.session_state.xp}")
    
    # Barra della Salute (basata sul progresso)
    if 'domande' in st.session_state:
        risposte_date = sum(1 for q in st.session_state.domande if st.session_state.get(f"q_{q['id']}") is not None)
        st.write(f"Avanzamento Campagna: {risposte_date}/10")
        st.progress(risposte_date / 10)

# 4. Database Domande[cite: 1]
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

# 5. Schizzo del Colosseo e Titolo
col1, col2 = st.columns([1, 3])
with col1:
    # Schizzo del colosseo (Nero su bianco, ma invertito per dark mode o neutro)
    st.image("https://img.icons8.com/ios/100/ffffff/coliseum.png", width=100)
with col2:
    st.title("LEGIO LATINA")
    st.subheader("La Conquista della Sintassi")

st.markdown("---")
st.write("⚔️ **Missione:** Attraversa le linee nemiche completando correttamente le frasi. Ogni errore ti farà perdere onore di fronte a Cesare!")

# 6. Area di Gioco
for q in st.session_state.domande:
    with st.expander(f"⚜️ SFIDA {q['id']}", expanded=True):
        st.markdown(f"### *{q['testo']}*")
        st.radio("Scegli la tua arma (risposta):", q['opzioni'], key=f"q_{q['id']}", index=None, horizontal=True)

# 7. Conclusione Campagna
if st.button("TERMINA LA BATTAGLIA 🏛️", use_container_width=True, type="primary"):
    punti = 0
    for q in st.session_state.domande:
        risposta = st.session_state.get(f"q_{q['id']}")
        if risposta == q['corretta']:
            punti += 1
            st.success(f"VITTORIA nella Sfida {q['id']}! ✅")
        else:
            st.error(f"SCONFITTA nella Sfida {q['id']}. La tattica corretta era '{q['corretta']}' ❌")
    
    st.session_state.xp = punti * 100
    st.divider()
    
    if punti == 10:
        st.balloons()
        st.header(f"TRIUMPHUS! 🏆")
        st.write(f"Hai ottenuto {st.session_state.xp} XP. Cesare ti nomina Generale!")
    elif punti >= 6:
        st.header(f"VITTORIA PIRRICA 🗡️")
        st.write(f"Hai ottenuto {st.session_state.xp} XP. La legione sopravvive, ma serve più studio.")
    else:
        st.header(f"DISFATTA ☠️")
        st.write(f"Hai ottenuto solo {st.session_state.xp} XP. Ritirati nel castrum a ripassare.")
