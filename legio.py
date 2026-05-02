import streamlit as st

# 1. Configurazione della pagina
st.set_page_config(page_title="Legio Latina", page_icon="⚔️", layout="centered")

# 2. CSS Ultra-Aggressivo per i colori
st.markdown("""
    <style>
    /* Font Times New Roman */
    html, body, [class*="st-"], h1, h2, h3, h4, p, label, span {
        font-family: "Times New Roman", Times, serif !important;
    }
    
    /* Sfondo nero */
    .stApp {
        background-color: #121212 !important;
    }
    
    /* FORZA IL TESTO BIANCO SULLE RISPOSTE (RADIO BUTTONS) */
    .stRadio p, .stRadio label, .stRadio span, div[role="radiogroup"] p {
        color: #ffffff !important;
        font-size: 1.15rem !important;
    }

    /* Colore bianco anche per il testo delle domande */
    .stMarkdown p, .stMarkdown h3 {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Castrum / Base)
with st.sidebar:
    # Busto Romano stilizzato bianco per risaltare sul nero
    st.image("https://img.icons8.com/ios-filled/100/ffffff/roman-buste.png", width=80)
    st.title("Castrum")
    st.markdown("---")
    
    if 'xp' not in st.session_state:
        st.session_state.xp = 0
        
    st.write(f"**Grado:** Legionario")
    st.write(f"**Esperienza:** {st.session_state.xp} XP")

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

# 5. Intestazione Principale
col_img, col_testo = st.columns([1, 4])
with col_img:
    # Schizzo del Colosseo stilizzato
    st.image("https://img.icons8.com/ios/100/ffffff/coliseum.png", width=80)
with col_testo:
    st.title("LEGIO LATINA")
    st.subheader("Campagna di Sintassi")
st.markdown("---")

# 6. Area di Gioco (Domande in formato scheda semplice)
for q in st.session_state.domande:
    st.markdown(f"### ⚔️ Sfida {q['id']}")
    st.markdown(f"**{q['t']}**")
    # Menu di scelta semplice (ho rimosso "horizontal=True" per non accavallare i testi sui telefoni)
    st.radio("Seleziona:", q['o'], key=f"ans_{q['id']}", index=None)
    st.markdown("---")

# 7. Valutazione
if st.button("TERMINA LA BATTAGLIA 🛡️", use_container_width=True, type="primary"):
    punti = 0
    st.markdown("## 📜 Rapporto di Battaglia")
    
    for q in st.session_state.domande:
        risposta_data = st.session_state.get(f"ans_{q['id']}")
        
        if risposta_data == q['c']:
            punti += 1
            st.success(f"Sfida {q['id']}: VITTORIA! Hai scelto correttamente '{q['c']}'. ✅")
        elif risposta_data is None:
            st.warning(f"Sfida {q['id']}: NON AFFRONTATA. La tattica giusta era '{q['c']}'. ⚠️")
        else:
            st.error(f"Sfida {q['id']}: SCONFITTA. Hai scelto '{risposta_data}', ma era '{q['c']}'. ❌")
            
    st.session_state.xp = punti * 100
    st.divider()
    st.metric("Punteggio XP", f"{st.session_state.xp}")
    
    if punti == 10:
        st.balloons()
        st.success("TRIUMPHUS! 🏆 Hai annientato gli errori. Cesare ti onora.")
    elif punti >= 6:
        st.info("La legione avanza. Hai superato la prova, ma non abbassare la guardia.")
    else:
        st.warning("Gravi perdite. Torna agli accampamenti e ripassa i manuali.")
