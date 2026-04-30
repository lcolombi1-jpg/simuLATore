import streamlit as st

# Configurazione della pagina
st.set_page_config(page_title="Latin Quiz", page_icon="🏛️")

st.title("🏛️ Esercitazione di Latino")
st.write("Completa le frasi scegliendo l'opzione corretta.")

# Database delle domande con nuovo ordine richiesto
if 'domande' not in st.session_state:
    st.session_state.domande = [
        {
            "id": 1,
            "testo": "Tota provincia _____________ occupata erat",
            "opzioni": ["Ab hostes", "Ad hostes", "Ab hostibus", "Hostibus"],
            "corretta": "Ab hostibus"
        },
        {
            "id": 2,
            "testo": "_____________ poetarum lecta sunt",
            "opzioni": ["carminis", "carmen", "carmina", "carmines"],
            "corretta": "carmina"
        },
        {
            "id": 3, 
            "testo": "Hannibal fratrem Hasdrubalem in Italiam cum omnibus ______ copiis vocavit",
            "opzioni": ["suum", "suus", "eius"],
            "corretta": "eius"
        },
        {
            "id": 4,
            "testo": "Pietatis ac fortitudinis exempla _________ ad virtutem ducunt",
            "opzioni": ["hominum", "hominibus", "homines", "homini"],
            "corretta": "homines"
        },
        {
            "id": 5,
            "testo": "Hannibal fratrem _______ Hasdrubalem in Italiam vocavit",
            "opzioni": ["suum", "suus", "eius"],
            "corretta": "suum"
        },
        {
            "id": 6,
            "testo": "_____________ mansi",
            "opzioni": ["Romā", "In Romā", "Romam", "Romae"],
            "corretta": "Romae"
        },
        {
            "id": 7,
            "testo": "Postquam bellum confectum est, consul ad hostes legatos misit _______ agentes",
            "opzioni": ["de pacem", "de pace", "ob pacem", "propter pacem"],
            "corretta": "de pace"
        },
        {
            "id": 8,
            "testo": "Domina armillas ____________ ancillis donabat",
            "opzioni": ["eximia pulchritudo", "eximiae pulchritudines", "eximiae pulchritudinis", "eximiam pulchritudinem"],
            "corretta": "eximiae pulchritudinis"
        },
        {
            "id": 9,
            "testo": "Athenis multas effigies deorum ________ vidi",
            "opzioni": ["marmor", "marmore", "ex marmore", "marmores"],
            "corretta": "ex marmore"
        },
        {
            "id": 10,
            "testo": "Pueri _________ verba audient",
            "opzioni": ["pater", "patres", "patri", "patrum"],
            "corretta": "patrum"
        }
    ]

# Visualizzazione domande
for q in st.session_state.domande:
    st.subheader(f"Domanda {q['id']}")
    
    st.radio(
        f"Scegli la forma corretta per: {q['testo']}",
        q['opzioni'],
        key=f"q_{q['id']}",
        index=None
    )
    st.divider()

# Bottone per correggere
if st.button("Invia e Verifica Risultati", type="primary"):
    punti = 0
    st.write("### Risultati:")
    
    for q in st.session_state.domande:
        risposta_studente = st.session_state.get(f"q_{q['id']}")
        
        if risposta_studente == q['corretta']:
            punti += 1
            st.success(f"Domanda {q['id']}: Esatto! ✅")
        elif risposta_studente is None:
            st.warning(f"Domanda {q['id']}: Non hai risposto. La corretta era '{q['corretta']}'. ⚠️")
        else:
            st.error(f"Domanda {q['id']}: Errato. La risposta corretta era '{q['corretta']}'. ❌")
    
    st.divider()
    st.metric("Punteggio Finale", f"{punti}/{len(st.session_state.domande)}")
    
    if punti == len(st.session_state.domande):
        st.balloons()
        st.success("Optime! Conoscenza perfetta della lingua latina! 🏛️")
