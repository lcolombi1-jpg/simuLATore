import streamlit as st

# 1. Configurazione della pagina
st.set_page_config(page_title="Legio Latina", page_icon="⚔️", layout="centered")

# 2. CSS per il Look Videogame con contrasto elevato
st.markdown("""
    <style>
    /* Font Times New Roman ovunque */
    html, body, [class*="st-"], .stMarkdown, h1, h2, h3, h4, p, label {
        font-family: "Times New Roman", Times, serif !important;
    }
    /* Sfondo scuro ma scritte bianco ghiaccio per massima leggibilità */
    .stApp {
        background-color: #121212;
        color: #ffffff;
    }
    /* Stile delle opzioni (radio button) per vederle bene */
    .stRadio [data-testid="stMarkdownContainer"] p {
        color: #ffffff !important;
        font-size: 1.1rem;
    }
    /* Riquadri delle domande */
    div[data-testid="stExpander"] {
        background-color: #1e1e1e;
        border: 1px solid #3d3d3d;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar: Status del Miles
with st.sidebar:
    
    st.image("https://share.google/OnOfWzLRXweJcLIIz", width=80)
    st.title("Miles")
    st.markdown("---")
    
    if 'xp' not in st.session_state:
        st.session_state.xp = 0
    
    st.write(f"**Grado:** Discipulus")
    
    
    if 'domande' in st.session_state:
        risposte_date = sum(1 for q in st.session_state.domande if st.session_state.get(f"q_{q['id']}") is not None)
        st.write(f"Missione: {risposte_date}/10")
        st.progress(risposte_date / 10)

# 4. Database Domande
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
        {"id": 10, "testo": "Athenis multas effigies deorum ________ vidi", "opzioni": ["marmor", "marmore", "ex marmore", "marmores"], "corretta": "ex marmore"},
        {"id": 11, "testo": "Pueri _________ verba audient", "opzioni": ["pater", "patres", "patri", "patrum"], "corretta": "patrum"}
    ]

# 5. Header Videogame
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://img.icons8.com/ios/100/ffffff/coliseum.png", width=80)
with col2:
    st.title("LEGIO LATINA")
    st.subheader("La Campagna di Sintassi")

st.markdown("---")

# 6. Area di Battaglia (Domande)
for q in st.session_state.domande:
    with st.expander(f"ORDINE DI BATTAGLIA {q['id']}", expanded=True):
        st.markdown(f"### *{q['testo']}*")
        # Colore radio button forzato per visibilità
        st.radio("Seleziona la tua mossa:", q['opzioni'], key=f"q_{q['id']}", index=None, horizontal=True)

# 7. Risultati
st.markdown("---")
if st.button("CONSEGNA IL RAPPORTO A CESARE ⚔️", use_container_width=True, type="primary"):
    punti = 0
    st.write("## Rapporto Finale:")
    for q in st.session_state.domande:
        risposta = st.session_state.get(f"q_{q['id']}")
        if risposta == q['corretta']:
            punti += 1
            st.success(f"Domanda {q['id']}: Vittoria! ✅")
        else:
            st.error(f"Domanda {q['id']}: Sconfitta. La corretta era '{q['corretta']}' ❌")
    
    st.session_state.xp = punti * 100
    st.divider()
    
    if punti == 10:
        st.balloons()
        st.header("TRIUMPHUS! 🏆")
        st.write("Hai conquistato la gloria eterna. Cesare è fiero di te.")
    elif punti >= 6:
        st.info(f"Hai totalizzato {punti}/10. La legione tiene la posizione.")
    else:
        st.warning(f"Hai totalizzato {punti}/10. Ritirata strategica necessaria.")
