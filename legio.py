import streamlit as st

# 1. Configurazione della pagina (Stile Videogame)
st.set_page_config(page_title="Legio Latina", page_icon="⚔️", layout="centered")

# 2. CSS per eliminare difetti e forzare il Times New Roman
st.markdown("""
    <style>
    /* Forza il font Times New Roman ovunque */
    html, body, [class*="st-"], .stMarkdown, h1, h2, h3, h4, p, label {
        font-family: "Times New Roman", Times, serif !important;
    }
    
    /* Sfondo nero e testo bianco per il contrasto */
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }

    /* Rende le risposte (label dei radio button) bianche e ben visibili */
    div[data-testid="stMarkdownContainer"] p {
        color: #ffffff !important;
        font-size: 1.2rem !important;
    }

    /* Riquadri delle domande stile 'scheda' */
    .stColumn {
        padding: 10px;
    }
    
    /* Nasconde eventuali scritte residue dei widget */
    [data-testid="stImageCaption"] {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Quartier Generale)
with st.sidebar:
    # Usiamo un'immagine con link diretto pulito per evitare scritte "keyboard"
    st.image("https://www.svgrepo.com/show/398188/roman-helmet.svg", width=80)
    st.title("CASTRUM")
    st.markdown("---")
    
    if 'xp' not in st.session_state:
        st.session_state.xp = 0
    
    st.write(f"**Esperienza Totale:** {st.session_state.xp} XP")
    
    if 'domande' in st.session_state:
        risposte_date = sum(1 for q in st.session_state.domande if st.session_state.get(f"ans_{q['id']}") is not None)
        st.progress(risposte_date / 10)
        st.write(f"Conquista: {risposte_date}/10")

# 4. Database Domande (Controllato e Semplificato)
if 'domande' not in st.session_state:
    st.session_state.domande = [
        {"id": 1, "t": "Tota provincia _____________ occupata erat", "o": ["Ab hostes", "Ad hostes", "Ab hostibus", "Hostibus"], "c": "Ab hostibus"},
        {"id": 2, "t": "_____________ poetarum lecta sunt", "o": ["carminis", "carmen", "carmina", "carmines"], "c": "carmina"},
        {"id": 3, "t": "Hannibal fratrem Hasdrubalem in Italiam cum omnibus ______ copiis vocavit", "o": ["suum", "suus", "eius"], "c": "eius"},
        {"id": 4, "t": "Pietatis ac fortitudinis exempla _________ ad virtutem ducunt", "o": ["hominum", "hominibus", "homines", "homini"], "c": "homines"},
        {"id": 5, "t": "Hannibal fratrem _______ Hasdrubalem in Italiam vocavit", "o": ["suum", "suus", "eius"], "c": "suum"},
        {"id": 6, "t": "_____________ mansi", "o": ["Romā", "In Romā", "Romam", "Romae"], "c": "Romae"},
        {"id": 7, "t": "Postquam bellum confectum est, consul ad hostes legatos misit _______ agentes", "o": ["de pacem", "de pace", "ob pacem", "propter pacem"], "c": "de pace"},
        {"id": 8, "t": "Domina armillas ____________ ancillis donabat", "o": ["eximia pulchritudo", "eximiae pulchritudines", "eximiae pulchritudinis", "eximiam pulchritudinem"], "c": "eximiae pulchritudinis"},
        {"id": 9, "t": "Athenis multas effigies deorum ________ vidi", "o": ["marmor", "marmore", "ex marmore", "marmores"], "c": "ex marmore"},
        {"id": 10, "t": "Pueri _________ verba audient", "o": ["pater", "patres", "patri", "patrum"], "c": "patrum"}
    ]

# 5. Header Campagna (Titolo e Schizzo Colosseo)
col_logo, col_titolo = st.columns([1, 4])
with col_logo:
    # Schizzo del Colosseo in bianco (per risaltare sul nero)
    st.image("https://www.svgrepo.com/show/396030/colosseum.svg", width=90)
with col_titolo:
    st.title("LEGIO LATINA")
    st.subheader("La Campagna di Sintassi")

st.markdown("---")

# 6. Esecuzione del Gioco
for q in st.session_state.domande:
    st.markdown(f"#### ⚔️ SFIDA {q['id']}")
    st.markdown(f"**{q['t']}**")
    st.radio("Seleziona la tua arma:", q['o'], key=f"ans_{q['id']}", index=None, horizontal=True)
    st.markdown("---")

# 7. Esito della Battaglia
if st.button("INVIA RAPPORTO A CESARE ✍️", use_container_width=True, type="primary"):
    punti = 0
    st.markdown("### 📜 Esito dello scontro:")
    for q in st.session_state.domande:
        risposta = st.session_state.get(f"ans_{q['id']}")
        if risposta == q['c']:
            punti += 1
            st.success(f"Sfida {q['id']}: Vittoria! ✅")
        else:
            st.error(f"Sfida {q['id']}: Sconfitta. Era '{q['c']}' ❌")
    
    st.session_state.xp = punti * 100
    st.divider()
    st.metric("XP GUADAGNATI", f"{st.session_state.xp}")
    
    if punti == 10:
        st.balloons()
        st.header("TRIUMPHUS! 🏆")
    elif punti >= 6:
        st.info("La Legione resiste. Continua così!")
    else:
        st.warning("Ritirata strategica! Ripassa la sintassi.")
