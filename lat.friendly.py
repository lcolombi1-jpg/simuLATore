import streamlit as st

# 1. Configurazione della pagina
st.set_page_config(page_title="Certamen", page_icon="🏛️", layout="wide")

# 2. CSS per forzare il Times New Roman e pulire l'interfaccia
st.markdown("""
    <style>
    /* Forza il font Times New Roman su tutta l'app */
    html, body, [class*="st-"], .stMarkdown, h1, h2, h3, h4, p, label {
        font-family: "Times New Roman", Times, serif !format;
    }
    .main { background-color: #ffffff; }
    /* Rende i testi delle domande un po' più grandi e solenni */
    .stMarkdown h3 {
        font-style: italic;
        color: #1a1a1a;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar con Cesare (Link alternativo più stabile)
with st.sidebar:
    # Ho cambiato l'origine dell'immagine per renderla più compatibile
    st.image("https://img.icons8.com/?size=100&id=23307&format=png&color=000000", width=100)
    st.title("Ave, Discipule!")
    st.markdown("---")
    st.write("Giulio Cesare osserva la tua prova. Sii preciso come un legionario.")
    
    if 'domande' in st.session_state:
        risposte_date = sum(1 for q in st.session_state.domande if st.session_state.get(f"q_{q['id']}") is not None)
        st.write(f"Progresso: {risposte_date}/10")
        st.progress(risposte_date / 10)

# 4. Inizializzazione Database (10 quesiti)[cite: 1]
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

# 5. Interfaccia Principale
st.title("🏛️ Certamen")
st.markdown("---")

for q in st.session_state.domande:
    with st.container():
        st.markdown(f"**Esercizio {q['id']}**")
        st.markdown(f"### {q['testo']}")
        st.radio("Seleziona la risposta:", q['opzioni'], key=f"q_{q['id']}", index=None, horizontal=True)
        st.markdown("---")

# 6. Verifica
if st.button("Consegna il compito ✍️", use_container_width=True, type="primary"):
    punti = 0
    st.subheader("Risultati del Ludus:")
    for q in st.session_state.domande:
        risposta = st.session_state.get(f"q_{q['id']}")
        if risposta == q['corretta']:
            punti += 1
            st.success(f"Quesito {q['id']}: Optime! ✅")
        else:
            st.error(f"Quesito {q['id']}: Errore. La risposta era '{q['corretta']}' ❌")
    
    st.divider()
    st.metric("Punteggio", f"{punti}/10")
    if punti == 10:
        st.balloons()
        st.success("Veni, vidi, vici!")
