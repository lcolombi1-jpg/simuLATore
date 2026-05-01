import streamlit as st

# 1. Configurazione base
st.set_page_config(page_title="Legio Latina", page_icon="⚔️")

# 2. CSS Semplificato (evitiamo errori di parsing)
st.markdown("""
    <style>
    /* Font Times New Roman */
    html, body, [class*="st-"], .stMarkdown, h1, h2, h3, h4, p, label {
        font-family: "Times New Roman", Times, serif !important;
    }
    /* Sfondo scuro e testo chiaro per leggibilità videogame */
    .stApp {
        background-color: #111111;
        color: #ffffff;
    }
    /* Forza il colore bianco per le opzioni del radio button */
    div[data-testid="stMarkdownContainer"] p {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Quartier Generale)
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/100/ffffff/roman-buste.png", width=80)
    st.title("Castrum")
    if 'xp' not in st.session_state:
        st.session_state.xp = 0
    st.write(f"Esperienza: {st.session_state.xp} XP")

# 4. Database Domande (Verificato 1 per 1)
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

# 5. Interfaccia
st.title("⚔️ LEGIO LATINA")
st.write("Completa la missione, soldato. Cesare ti osserva.")

for q in st.session_state.domande:
    with st.container():
        st.markdown(f"### Sfida {q['id']}")
        st.write(f"**{q['t']}**")
        st.radio("Scegli:", q['o'], key=f"ans_{q['id']}", index=None, horizontal=True)
        st.markdown("---")

# 6. Conclusione
if st.button("CONSEGNA IL RAPPORTO", type="primary", use_container_width=True):
    punti = 0
    for q in st.session_state.domande:
        risp = st.session_state.get(f"ans_{q['id']}")
        if risp == q['c']:
            punti += 1
            st.success(f"Domanda {q['id']}: Vittoria!")
        else:
            st.error(f"Domanda {q['id']}: Sconfitta. Era '{q['c']}'")
    
    st.session_state.xp = punti * 100
    st.metric("Punteggio", f"{punti}/10")
    if punti == 10: st.balloons()
