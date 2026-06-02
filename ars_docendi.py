import streamlit as st

# ==================================================
# CONFIG
# ==================================================

st.set_page_config(
    page_title="Ludus",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================================================
# SESSION STATE
# ==================================================

if "level" not in st.session_state:
    st.session_state.level = None

# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Montserrat:wght@300;500&display=swap');

/* Nasconde elementi Streamlit */

header,
footer,
#MainMenu,
[data-testid="stToolbar"]{
    visibility:hidden;
}

/* Pagina */

.stApp{
    background:
    radial-gradient(
        circle at center,
        #1c0033 0%,
        #0b0016 45%,
        #020004 100%
    );

    overflow:hidden;
}

.block-container{
    padding-top:0.5rem;
    max-width:100%;
}

/* Titolo */

.title-wrapper{
    text-align:center;
    margin-top:5px;
    margin-bottom:25px;
}

.main-title{
    font-family:'Cinzel', serif;
    font-size:4.5rem;
    letter-spacing:12px;
    color:white;

    text-shadow:
        0 0 10px #b537f2,
        0 0 25px #b537f2,
        0 0 60px #ff00c8;

    margin-bottom:0;
}

.subtitle{
    font-family:'Montserrat', sans-serif;
    color:#00f0ff;
    letter-spacing:6px;
    text-transform:uppercase;

    text-shadow:
        0 0 10px #00f0ff;
}

/* ================================= */
/* PORTE */
/* ================================= */

div.stButton > button {

    width:240px !important;
    height:340px !important;

    border-radius:
        120px
        120px
        10px
        10px !important;

    background:#000 !important;

    color:white !important;

    border:3px solid white !important;

    padding:0 !important;

    transition:all .3s ease !important;

    font-family:'Cinzel', serif !important;

    font-size:2rem !important;

    font-weight:700 !important;

    letter-spacing:2px !important;
}

div.stButton > button:hover{
    transform:translateY(-8px);
}

/* Porta 1 */

[data-testid="column"]:nth-of-type(1) button{

    border-color:#00eaff !important;

    color:#00eaff !important;

    box-shadow:
        0 0 5px #00eaff,
        0 0 15px #00eaff,
        0 0 35px rgba(0,234,255,.8),
        0 0 70px rgba(0,234,255,.4) !important;
}

/* Porta 2 */

[data-testid="column"]:nth-of-type(2) button{

    border-color:#b537f2 !important;

    color:#d884ff !important;

    box-shadow:
        0 0 5px #b537f2,
        0 0 15px #b537f2,
        0 0 35px rgba(181,55,242,.8),
        0 0 70px rgba(181,55,242,.4) !important;
}

/* Porta 3 */

[data-testid="column"]:nth-of-type(3) button{

    border-color:#ff00c8 !important;

    color:#ff70d6 !important;

    box-shadow:
        0 0 5px #ff00c8,
        0 0 15px #ff00c8,
        0 0 35px rgba(255,0,200,.8),
        0 0 70px rgba(255,0,200,.4) !important;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HOME
# ==================================================

if st.session_state.level is None:

    st.markdown("""
    <div class="title-wrapper">
        <div class="main-title">LUDUS</div>
        <div class="subtitle">scegli il tuo destino</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("DISCIPVLVS", key="disc"):
            st.session_state.level = "Discipulus"
            st.rerun()

    with col2:
        if st.button("GLADIATOR", key="glad"):
            st.session_state.level = "Gladiator"
            st.rerun()

    with col3:
        if st.button("IMPERATOR", key="imp"):
            st.session_state.level = "Imperator"
            st.rerun()

# ==================================================
# SCHERMATE
# ==================================================

else:

    st.markdown(f"""
    <div class="title-wrapper">
        <div class="main-title" style="font-size:3.5rem;">
            {st.session_state.level}
        </div>
        <div class="subtitle">
            Arena Attiva
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        f"Benvenuto nell'arena {st.session_state.level}. "
        "Qui inserirai gli esercizi di latino."
    )

    st.write("")

    if st.button("← Torna alle porte"):
        st.session_state.level = None
        st.rerun()
