import streamlit as st

# 1. Configurazione della pagina
st.set_page_config(page_title="Legio Latina", page_icon="⚔️", layout="centered")

# 2. CSS "Anti-Bug" e Alta Visibilità
st.markdown("""
    <style>
    /* Usiamo Georgia per un look classico ma leggibile, senza rompere le icone */
    h1, h2, h3, h4, .stMarkdown p, .stRadio label {
        font-family: 'Georgia', serif !important;
    }

    /* Sfondo nero profondo */
    .stApp {
        background-color: #0A0A0A !important;
    }

    /* FORZA IL TESTO BIANCO SULLE RISPOSTE (RADIO BUTTONS) */
    /* Questo risolve il problema del testo grigio illeggibile */
    div[data-testid="stMarkdownContainer"] p {
        color: #FFFFFF !important;
        font-size: 1.1rem !important;
        font-weight: 500 !important;
    }

    /* Rende i pallini delle risposte e le etichette più chiari */
    .stRadio label {
        color: #FFFFFF !important;
    }

    /* Box delle domande per dare ordine */
    div.stBox {
        background-color: #1A1A1A;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #333;
        margin-bottom: 20px;
    }
    
    /* Nasconde caption di errore delle immagini */
    [data-testid="stImageCaption"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar - Status Giocatore
with st.sidebar:
    # Icona Elmo Romano (più stabile del busto)
    st.image("https://www.svgrepo.com/show/398188/roman-helmet.svg", width=80)
    st.title("Castrum")
    st.markdown("---")
    
    if 'xp' not in st.session_state:
        st.session_state.xp = 0
    
    st.write(f"**Legionario:** Discipulus")
    st.write(f"**Esperienza:** {st.session_state.xp} XP")
    
    if 'domande' in st.session_state:
        fatte = sum(1 for q in st.session_state.domande if st.session_state.get(f"ans_{q['id']}") is not None)
        st.progress(fatte / 10)
        st.write(f"Avanzamento: {fatte}/10")

# 4. Database Domande (Controllato e Pulito)
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

# 5. Header Campagna
col1, col2 = st.columns([1, 4])
with col1:
    # Schizzo Colosseo SVG (Bianco)
    st.image("https://www.svgrepo.com/show/396030/colosseum.svg", width=80)
with col2:
    st.title("LEGIO LATINA")
    st.subheader("La Conquista della Sintassi")

st.markdown("---")

# 6. Schermata di Battaglia
for q in st.session_state.domande:
    st.markdown(f"### ⚔️ Sfida {q['id']}")
    st.markdown(f"**{q['t']}**")
    # Radio button con chiave unica
    st.radio("Seleziona la mossa:", q['o'], key=f"ans_{q['id']}", index=None)
    st.markdown("---")

# 7. Risultati Finali
if st.button("TERMINA LA BATTAGLIA 🛡️", use_container_width=True, type="primary"):
    punti = 0
    st.markdown("## 📜 Rapporto di Cesare")
    
    for q in st.session_state.domande:
        risp = st.session_state.get(f"ans_{q['id']}")
        if risp == q['c']:
            punti += 1
            st.success(f"Sfida {q['id']}: VITTORIA! ✅")
        else:
            st.error(f"Sfida {q['id']}: DISFATTA. La mossa corretta era '{q['c']}' ❌")
    
    st.session_state.xp = punti * 100
    st.divider()
    st.metric("XP GUADAGNATI", f"{st.session_state.xp}")
    
    if punti == 10:
        st.balloons()
        st.success("TRIUMPHUS! Cesare ti attende a Roma! 🏆")
