import streamlit as st
import random

# 1. Configurazione della pagina (Layout Wide per dare respiro)
st.set_page_config(page_title="Certamen", page_icon="🏛️", layout="wide")

# 2. Stile personalizzato con CSS per rendere i font più leggibili
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stRadio > label { font-weight: bold; color: #2c3e50; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar per info e progresso
with st.sidebar:
    st.image("https://img.icons8.com/ios/100/2ecc71/coliseum.png", width=100)
    st.title("Statistiche Quiz")
    st.info("Benvenuto! Rispondi a tutte le domande per testare la tua conoscenza del Latino.")
    
    # Calcolo risposte date per la barra di progresso
    if 'domande' in st.session_state:
        risposte_date = sum(1 for q in st.session_state.domande if st.session_state.get(f"q_{q['id']}") is not None)
        st.write(f"Avanzamento: {risposte_date}/10")
        st.progress(risposte_date / 10)

# 4. Inizializzazione del database (manteniamo l'ordine o randomizziamo)
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

# 5. Titolo e Intestazione Principale
st.title("🏛️ Ludus Latinus: La Sfida")
st.markdown("---")

# 6. Visualizzazione Domande con Layout a schede (Contenitori)
for q in st.session_state.domande:
    with st.container(border=True): # Crea un riquadro per ogni domanda
        st.markdown(f"#### Quesito n. {q['id']}")
        st.markdown(f"**Completa la frase:**")
        st.info(f"*{q['testo']}*")
        
        st.radio(
            "Scegli l'opzione corretta:",
            q['opzioni'],
            key=f"q_{q['id']}",
            index=None,
            horizontal=True # Opzioni disposte orizzontalmente per risparmiare spazio
        )

# 7. Bottone Finale e Correzione
st.markdown("---")
if st.button("Concludi il compito ✍️", use_container_width=True, type="primary"):
    punti = 0
    
    # Area risultati
    st.header("Esito della prova")
    
    for q in st.session_state.domande:
        risposta = st.session_state.get(f"q_{q['id']}")
        
        with st.expander(f"Dettaglio Domanda {q['id']}", expanded=False):
            if risposta == q['corretta']:
                punti += 1
                st.success(f"Corretto! ✅ Hai scelto '{risposta}'")
            elif risposta is None:
                st.warning(f"Non hai risposto. ⚠️ La forma corretta è '{q['corretta']}'")
            else:
                st.error(f"Errore ❌ Hai scelto '{risposta}', ma la forma corretta era '{q['corretta']}'")

    # Feedback finale basato sul punteggio
    col_voto, col_messaggio = st.columns(2)
    
    with col_voto:
        st.metric("Punteggio Finale", f"{punti}/10")
    
    with col_messaggio:
        if punti == 10:
            st.balloons()
            st.success("ECCELLENTE! 🏆 Sei un vero esperto di sintassi latina!")
        elif punti >= 6:
            st.success("Bravo! Hai raggiunto la sufficienza, ma puoi ancora migliorare! 📖")
        else:
            st.error("Ripassa bene le regole e riprova. Perseverantia vincit! ⚔️")
