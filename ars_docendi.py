import streamlit as st

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="LUDUS",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# SESSION STATE
# =====================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Montserrat:wght@300;400&display=swap');

header,
footer,
#MainMenu,
[data-testid="stToolbar"]{
    visibility:hidden;
}

.block-container{
    max-width:100%;
    padding-top:0rem !important;
    padding-bottom:0rem !important;
}

/* ------------------------------------------------ */
/* SFONDO */
/* ------------------------------------------------ */

.stApp{
    background:
    radial-gradient(
        circle at center,
        #1a0033 0%,
        #090012 45%,
        #020004 100%
    );

    overflow:hidden;
}

/* ------------------------------------------------ */
/* TITOLO */
/* ------------------------------------------------ */

.title-wrapper{
    text-align:center;
    margin-top:5px;
}

.main-title{

    font-family:'Cinzel', serif;

    font-size:5.5rem;

    letter-spacing:10px;

    color:white;

    margin-bottom:0;

    text-shadow:
        0 0 10px #ff00ff,
        0 0 30px #ff00ff,
        0 0 60px rgba(255,0,255,.6);
}

.subtitle{

    color:#00eaff;

    text-align:center;

    font-family:'Montserrat', sans-serif;

    letter-spacing:8px;

    margin-bottom:40px;

    text-shadow:
        0 0 10px #00eaff;
}

/* ------------------------------------------------ */
/* ARCHI */
/* ------------------------------------------------ */

div.stButton > button{

    width:100% !important;

    height:500px !important;

    background:transparent !important;

    border-radius:
        220px
        220px
        10px
        10px !important;

    font-family:'Cinzel', serif !important;

    font-size:2rem !important;

    font-weight:700 !important;

    transition:0.3s !important;

    color:white !important;
}

/* Hover */

div.stButton > button:hover{

    transform:translateY(-10px);
}

/* ------------------------------------------------ */
/* PORTA 1 */
/* ------------------------------------------------ */

[data-testid="column"]:nth-child(1) button{

    border:4px solid #00eaff !important;

    color:#00eaff !important;

    text-shadow:
        0 0 10px #00eaff,
        0 0 20px #00eaff !important;

    box-shadow:
        0 0 10px #00eaff,
        0 0 30px #00eaff,
        0 0 60px rgba(0,234,255,.8),
        0 0 120px rgba(0,234,255,.4) !important;
}

/* ------------------------------------------------ */
/* PORTA 2 */
/* ------------------------------------------------ */

[data-testid="column"]:nth-child(2) button{

    border:4px solid #c442ff !important;

    color:#d56bff !important;

    text-shadow:
        0 0 10px #d56bff,
        0 0 20px #d56bff !important;

    box-shadow:
        0 0 10px #c442ff,
        0 0 30px #c442ff,
        0 0 60px rgba(196,66,255,.8),
        0 0 120px rgba(196,66,255,.4) !important;
}

/* ------------------------------------------------ */
/* PORTA 3 */
/* ------------------------------------------------ */

[data-testid="column"]:nth-child(3) button{

    border:4px solid #ff006e !important;

    color:#ff4ca0 !important;

    text-shadow:
        0 0 10px #ff4ca0,
        0 0 20px #ff4ca0 !important;

    box-shadow:
        0 0 10px #ff006e,
        0 0 30px #ff006e,
        0 0 60px rgba(255,0,110,.8),
        0 0 120px rgba(255,0,110,.4) !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HOME
# =====================================================

if st.session_state.page == "home":

    st.markdown("""
    <div class="title-wrapper">
        <div class="main-title">LUDUS</div>
    </div>

    <div class="subtitle">
        scegli il tuo destino
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "DISCIPVLVS\n\nBEGINNER",
            key="disc"
        ):
            st.session_state.page = "discipulus"
            st.rerun()

    with col2:

        if st.button(
            "GLADIATOR\n\nINTERMEDIATE",
            key="glad"
        ):
            st.session_state.page = "gladiator"
            st.rerun()

    with col3:

        if st.button(
            "IMPERATOR\n\nPRO",
            key="imp"
        ):
            st.session_state.page = "imperator"
            st.rerun()

# =====================================================
# DISCIPULUS
# =====================================================

elif st.session_state.page == "discipulus":

    st.markdown("""
    <div class="title-wrapper">
        <div class="main-title">DISCIPVLVS</div>
    </div>
    """, unsafe_allow_html=True)

    st.info("Qui andranno gli esercizi beginner.")

    if st.button("← Torna"):
        st.session_state.page = "home"
        st.rerun()

# =====================================================
# GLADIATOR
# =====================================================

elif st.session_state.page == "gladiator":

    st.markdown("""
    <div class="title-wrapper">
        <div class="main-title">GLADIATOR</div>
    </div>
    """, unsafe_allow_html=True)

    st.info("Qui andranno gli esercizi intermediate.")

    if st.button("← Torna"):
        st.session_state.page = "home"
        st.rerun()

# =====================================================
# IMPERATOR
# =====================================================

elif st.session_state.page == "imperator":

    st.markdown("""
    <div class="title-wrapper">
        <div class="main-title">IMPERATOR</div>
    </div>
    """, unsafe_allow_html=True)

    st.info("Qui andranno gli esercizi avanzati.")

    if st.button("← Torna"):
        st.session_state.page = "home"
        st.rerun()
