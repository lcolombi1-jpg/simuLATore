import streamlit as st

# 1. Configurazione della pagina
st.set_page_config(page_title="Certamen", page_icon="🏛️", layout="wide")

# 2. Stile personalizzato per un look pulito
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stRadio > label { font-weight: bold; color: #1a1a1a; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar con il BUSTO DI CESARE
with st.sidebar:
    # Icona stilizzata di Giulio Cesare (Nera)
    st.image("https://img.icons8.com/ios/100/000000/julius-caesar.png", width=80)
    st.title("Ave, Discipule!")
    st.markdown("---")
    st.info("Giulio Cesare osserva i tuoi progressi. Non deluderlo!")
    
    if 'domande' in st.session_state:
        risposte_date = sum(1 for q in st.session_state.domande if st.session_state.get(f"q_{q['id']}") is not None)
        st.write(f"Progresso: {risposte_date}/10")
        st.progress(risposte_date / 10)

# 4. Inizializzazione Database (dati forniti dall'utente)
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
st.caption("Esercitazione interattiva di sintassi e morfologia")
st.markdown("---")

# Visualizzazione quesiti in box eleganti
for q in st.session_state.domande:
    with st.container(border=True):
        col_testo, col_scelta = st.columns([2, 1])
        
        with col_testo:
            st.markdown(f"**Esercizio {q['id']}**")
            st.markdown(f"### *{q['testo']}*")
        
        with col_scelta:
            st.radio(
                "Seleziona la forma:",
                q['opzioni'],
                key=f"q_{q['id']}",
                index=None
            )

# 6. Correzione finale
st.markdown("---")
if st.button("Consegna a Cesare ✍️", use_container_width=True, type="primary"):
    punti = 0
    st.header("Esito del Ludus")
    
    for q in st.session_state.domande:
        risposta = st.session_state.get(f"q_{q['id']}")
        
        if risposta == q['corretta']:
            punti += 1
            st.success(f"Quesito {q['id']}: Ottimo! ✅")
        else:
            st.error(f"Quesito {q['id']}: Errato. La forma corretta era '{q['corretta']}' ❌")

    st.divider()
    st.metric("Punteggio Finale", f"{punti}/10")
    
    if punti == 10:
        st.balloons()
        st.success("Veni, vidi, vici! Hai completato il test perfettamente! 🎓")
    elif punti >= 6:
        st.info("Buon lavoro, ma puoi affinare ancora la tua tecnica. 📖")
    else:
        st.warning("Per aspera ad astra: ripassa e riprova! ⚔️")
