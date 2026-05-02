import streamlit as st

# 1. Configurazione della pagina - Look moderno e pulito
st.set_page_config(page_title="Ludus Latinus", page_icon="🏛️", layout="centered")

# 2. CSS Minimale per la leggibilità (Niente che rompa le icone)
st.markdown("""
    <style>
    /* Font moderno e pulito */
    html, body, [class*="st-"] {
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    /* Sfondo chiaro e riposante */
    .stApp {
        background-color: #Fbfffe;
    }
    /* Card delle domande: bianche con ombra leggera (stile Instagram/Notion) */
    div.stButton > button:first-child {
        background-color: #6366f1;
        color: white;
        border-radius: 8px;
    }
    .question-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border: 1px solid #e0e7ff;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar - Progresso e Voto
with st.sidebar:
    st.title("🏛️ Hub Studente")
    st.write("Mettiti alla prova con la sintassi latina.")
    st.divider()
    
    if 'domande' in st.session_state:
        risposte_date = sum(1 for q in st.session_state.domande if st.session_state.get(f"ans_{q['id']}") is not None)
        st.write(f"Completamento: **{risposte_date}/10**")
        st.progress(risposte_date / 10)

# 4. Database Domande (Controllato e robusto)
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

# 5. Interfaccia Principale
st.title("🎓 Simulatore di Latino")
st.write("Scegli l'opzione corretta per completare la frase. *Audentes fortuna iuvat!*")
st.divider()

# Ciclo delle domande
for q in st.session_state.domande:
    # Usiamo st.container per creare l'effetto "card"
    with st.container():
        st.markdown(f"### Esercizio {q['id']}")
        st.markdown(f"**{q['t']}**")
        st.radio("Seleziona la risposta:", q['o'], key=f"ans_{q['id']}", index=None)
        st.markdown("---")

# 6. Bottone Correzione
if st.button("Verifica il mio livello ✍️", use_container_width=True):
    punti = 0
    st.header("Riepilogo Risultati")
    
    for q in st.session_state.domande:
        scelta = st.session_state.get(f"ans_{q['id']}")
        if scelta == q['c']:
            punti += 1
            st.success(f"Domanda {q['id']}: Esatto! ✅")
        else:
            st.error(f"Domanda {q['id']}: Errore. La risposta era '{q['c']}' ❌")
    
    # Calcolo voto in decimi (classico scolastico)
    voto = punti
    st.divider()
    
    col1, col2 = st.columns(2)
    col1.metric("Risposte Corrette", f"{punti}/10")
    col2.metric("Voto Finale", f"{voto}/10")

    if voto >= 6:
        st.balloons()
        st.success("Ottimo lavoro! Hai superato la prova. 🏛️")
    else:
        st.warning("Non mollare! Un po' di ripasso e sarai imbattibile. 📖")
