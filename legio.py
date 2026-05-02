import streamlit as st

# 1. Configurazione della pagina
st.set_page_config(page_title="Ludus Latinus", page_icon="🏛️", layout="centered")

# 2. CSS mirato: Solo estetica, niente che rompa le icone
st.markdown("""
    <style>
    /* Sfondo neutro e riposante */
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* Card per le domande: stile pulito e moderno */
    div.stBox {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 25px;
    }

    /* Titoli più eleganti */
    h1, h2, h3 {
        color: #1E293B;
        font-weight: 700;
    }

    /* Bottone di verifica stile "App" */
    .stButton > button {
        width: 100%;
        background-color: #4F46E5 !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 15px !important;
        font-weight: bold !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar minimale
with st.sidebar:
    st.title("🏛️ Hub Studente")
    st.write("Verifica le tue competenze in sintassi latina.")
    st.divider()
    if 'domande' in st.session_state:
        fatte = sum(1 for q in st.session_state.domande if st.session_state.get(f"ans_{q['id']}") is not None)
        st.write(f"Avanzamento: **{fatte}/10**")
        st.progress(fatte / 10)

# 4. Database Domande
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

# 5. Contenuto Principale
st.title("🎓 Simulatore di Latino")
st.write("Seleziona la forma corretta per completare la frase.")
st.divider()

# Visualizzazione card domande
for q in st.session_state.domande:
    # Usiamo un container per ogni domanda
    with st.container():
        st.subheader(f"Esercizio {q['id']}")
        st.write(f"**{q['t']}**")
        st.radio("Scegli l'opzione:", q['o'], key=f"ans_{q['id']}", index=None)
        st.write("") # Spaziatore
        st.divider()

# 6. Bottone Risultati
if st.button("Verifica il mio livello ✍️"):
    punti = 0
    st.header("Riepilogo Esito")
    
    for q in st.session_state.domande:
        scelta = st.session_state.get(f"ans_{q['id']}")
        if scelta == q['c']:
            punti += 1
            st.success(f"Esercizio {q['id']}: Corretto ✅")
        else:
            st.error(f"Esercizio {q['id']}: Errato (Era '{q['c']}') ❌")
    
    st.divider()
    col1, col2 = st.columns(2)
    col1.metric("Risposte Esatte", f"{punti}/10")
    col2.metric("Voto Finale", f"{punti}/10")

    if punti >= 6:
        st.balloons()
        st.success("Bravo/a! Hai superato la prova. 🏛️")
    else:
        st.warning("Serve un po' di ripasso. Non mollare! 📖")
