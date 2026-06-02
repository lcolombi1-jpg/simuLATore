import streamlit as st

# ======================================================
# CONFIG
# ======================================================

st.set_page_config(
    page_title="Ludus",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ======================================================
# SESSION STATE
# ======================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

# ======================================================
# CSS
# ======================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Montserrat:wght@300;500&display=swap');

header,
footer,
#MainMenu,
[data-testid="stToolbar"]{
    display:none !important;
}

.block-container{
    padding-top:0.5rem !important;
    max-width:100% !important;
}

/* ================================================== */
/* SFONDO */
/* ================================================== */

.stApp{

    background:
    radial-gradient(
        circle at center,
        #1c0033 0%,
        #0b0016 45%,
        #020004 100%
    );

    color:white;
}

/* ================================================== */
/* TITOLO */
/* ================================================== */

.title{

    text-align:center;

    margin-top:10px;
    margin-bottom:20px;
}

.title h1{

    font-family:'Cinzel', serif;

    font-size:4.8rem;

    letter-spacing:12px;

    margin-bottom:0;

    color:white;

    text-shadow:
        0 0 10px #b537f2,
        0 0 25px #b537f2,
        0 0 60px #ff00c8;
}

.title p{

    color:#00eaff;

    letter-spacing:7px;

    text-transform:uppercase;

    font-family:'Montserrat', sans-serif;

    text-shadow:
        0 0 12px #00eaff;
}

/* ================================================== */
/* BOTTONI-PORTE */
/* ================================================== */

div.stButton > button{

    width:250px !important;
    height:350px !important;

    border-radius:
        125px
        125px
        12px
        12px !important;

    background:#000 !important;

    font-family:'Cinzel', serif !important;

    font-size:2rem !important;

    font-weight:700 !important;

    transition:0.3s !important;

    border-width:3px !important;
}

div.stButton > button:hover{

    transform:translateY(-8px) scale(1.02);
}

/* ================================================== */
/* CIANO */
/* ================================================== */

button[kind="secondary"]{

    border-color:#00eaff !important;

    color:#00eaff !important;

    text-shadow:
        0 0 10px #00eaff,
        0 0 20px #00eaff,
        0 0 35px #00eaff !important;

    box-shadow:
        0 0 5px #00eaff,
        0 0 15px #00eaff,
        0 0 35px rgba(0,234,255,.9),
        0 0 70px rgba(0,234,255,.6),
        0 0 120px rgba(0,234,255,.4) !important;
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# HOME
# ======================================================

if st.session_state.page == "home":

    st.markdown("""
    <div class="title">
        <h1>LUDUS</h1>
        <p>Scegli il tuo destino</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1,1,1])

    with c1:
        if st.button("DISCIPVLVS", key="disc"):
            st.session_state.page = "discipulus"
            st.rerun()

    with c2:
        if st.button("GLADIATOR", key="glad"):
            st.session_state.page = "gladiator"
            st.rerun()

    with c3:
        if st.button("IMPERATOR", key="imp"):
            st.session_state.page = "imperator"
            st.rerun()

# ======================================================
# DISCIPVLVS
# ======================================================

elif st.session_state.page == "discipulus":

    st.title("DISCIPVLVS")

    st.info("Livello principiante")

    if st.button("← Torna"):
        st.session_state.page = "home"
        st.rerun()

# ======================================================
# GLADIATOR
# ======================================================

elif st.session_state.page == "gladiator":

    st.title("GLADIATOR")

    st.info("Livello intermedio")

    if st.button("← Torna"):
        st.session_state.page = "home"
        st.rerun()

# ======================================================
# IMPERATOR
# ======================================================

elif st.session_state.page == "imperator":

    st.title("IMPERATOR")

    st.info("Livello avanzato")

    if st.button("← Torna"):
        st.session_state.page = "home"
        st.rerun()
