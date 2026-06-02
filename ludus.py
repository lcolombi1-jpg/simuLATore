import streamlit as st

# ==================================================
# CONFIGURAZIONE
# ==================================================

st.set_page_config(
    page_title="LVDVS",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================================================
# STATO
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = "intro"

# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Montserrat:wght@300;400;500&display=swap');

/* ------------------------------------------------ */
/* ELEMENTI STREAMLIT */
/* ------------------------------------------------ */

#MainMenu,
footer,
header,
[data-testid="stToolbar"]{
    visibility:hidden;
}

/* ------------------------------------------------ */
/* RESPONSIVE */
/* ------------------------------------------------ */

html, body, [class*="css"]{
    width:100%;
    height:100%;
}

.block-container{
    max-width:100vw !important;
    padding-top:1rem !important;
    padding-left:2rem !important;
    padding-right:2rem !important;
}

/* ------------------------------------------------ */
/* SFONDO */
/* ------------------------------------------------ */

.stApp{
    background:
    radial-gradient(
        circle at center,
        #1b0034 0%,
        #0a0015 45%,
        #020004 100%
    );
}

/* ------------------------------------------------ */
/* TITOLI */
/* ------------------------------------------------ */

.hero-title{

    text-align:center;

    font-family:'Cinzel', serif;

    font-size:clamp(3rem, 8vw, 6rem);

    color:white;

    letter-spacing:8px;

    margin-top:3vh;

    text-shadow:
        0 0 10px #ff00ff,
        0 0 30px #ff00ff,
        0 0 60px rgba(255,0,255,.5);
}

.hero-sub{

    text-align:center;

    font-family:'Montserrat', sans-serif;

    color:#00f0ff;

    letter-spacing:6px;

    font-size:clamp(.9rem, 2vw, 1.2rem);

    margin-bottom:4vh;

    text-shadow:
        0 0 10px #00f0ff;
}

/* ------------------------------------------------ */
/* BOTTONI */
/* ------------------------------------------------ */

.stButton > button{

    width:100%;

    transition:.3s ease;

    font-family:'Cinzel', serif;
}

.stButton > button:hover{

    transform:translateY(-4px);
}

/* ------------------------------------------------ */
/* AD MAIORA */
/* ------------------------------------------------ */

.admaiora button{

    height:70px !important;

    font-size:1.3rem !important;

    border:2px solid #00f0ff !important;

    background:transparent !important;

    color:#00f0ff !important;

    box-shadow:
        0 0 10px #00f0ff,
        0 0 30px rgba(0,240,255,.4);
}

/* ------------------------------------------------ */
/* ARCATE */
/* ------------------------------------------------ */

.arch button{

    height:480px !important;

    border-radius:
        220px
        220px
        12px
        12px !important;

    background:transparent !important;

    font-size:1.5rem !important;

    font-weight:700 !important;
}

.arch button:hover{

    transform:translateY(-10px);
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# PAGINA INTRO
# ==================================================

if st.session_state.page == "intro":

    st.markdown(
        "<div class='hero-title'>LVDVS</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='hero-sub'>audaces fortuna iuvat</div>",
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")
    st.write("")

    sx, centro, dx = st.columns([2,1,2])

    with centro:

        st.markdown(
            "<div class='admaiora'>",
            unsafe_allow_html=True
        )

        if st.button("AD MAIORA"):
            st.session_state.page = "lobby"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# LOBBY
# ==================================================

elif st.session_state.page == "lobby":

    st.markdown(
        "<div class='hero-title'>LVDVS</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='hero-sub'>elige gradum tuum</div>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    # DISCIPVLVS

    with col1:

        if st.button(
            "DISCIPVLVS\n\nBEGINNER",
            key="disc"
        ):
            st.session_state.page = "discipulus"
            st.rerun()

    # GLADIATOR

    with col2:

        if st.button(
            "GLADIATOR\n\nINTERMEDIATE",
            key="glad"
        ):
            st.session_state.page = "gladiator"
            st.rerun()

    # IMPERATOR

    with col3:

        if st.button(
            "IMPERATOR\n\nPRO",
            key="imp"
        ):
            st.session_state.page = "imperator"
            st.rerun()

    # COLORI DELLE TRE ARCATE

    st.markdown("""
    <style>

    div[data-testid="column"]:nth-child(1) button{

        border:4px solid #00f0ff !important;

        color:#00f0ff !important;

        text-shadow:0 0 10px #00f0ff;

        height:480px !important;

        border-radius:220px 220px 12px 12px !important;

        box-shadow:
            0 0 15px #00f0ff,
            0 0 50px #00f0ff,
            0 0 100px rgba(0,240,255,.5);
    }

    div[data-testid="column"]:nth-child(2) button{

        border:4px solid #d64dff !important;

        color:#d64dff !important;

        text-shadow:0 0 10px #d64dff;

        height:480px !important;

        border-radius:220px 220px 12px 12px !important;

        box-shadow:
            0 0 15px #d64dff,
            0 0 50px #d64dff,
            0 0 100px rgba(214,77,255,.5);
    }

    div[data-testid="column"]:nth-child(3) button{

        border:4px solid #ff0077 !important;

        color:#ff0077 !important;

        text-shadow:0 0 10px #ff0077;

        height:480px !important;

        border-radius:220px 220px 12px 12px !important;

        box-shadow:
            0 0 15px #ff0077,
            0 0 50px #ff0077,
            0 0 100px rgba(255,0,119,.5);
    }

    </style>
    """, unsafe_allow_html=True)

# ==================================================
# DISCIPVLVS
# ==================================================

elif st.session_state.page == "discipulus":

    st.markdown(
        "<div class='hero-title'>DISCIPVLVS</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='hero-sub'>initium sapientiae</div>",
        unsafe_allow_html=True
    )

    st.info("Qui inserirai il quiz Beginner.")

    if st.button("← Torna alle arcate"):
        st.session_state.page = "lobby"
        st.rerun()

# ==================================================
# GLADIATOR
# ==================================================

elif st.session_state.page == "gladiator":

    st.markdown(
        "<div class='hero-title'>GLADIATOR</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='hero-sub'>virtus in media stat</div>",
        unsafe_allow_html=True
    )

    st.info("Qui inserirai il quiz Intermediate.")

    if st.button("← Torna alle arcate"):
        st.session_state.page = "lobby"
        st.rerun()

# ==================================================
# IMPERATOR
# ==================================================

elif st.session_state.page == "imperator":

    st.markdown(
        "<div class='hero-title'>IMPERATOR</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='hero-sub'>ad astra per aspera</div>",
        unsafe_allow_html=True
    )

    st.info("Qui inserirai il quiz Pro.")

    if st.button("← Torna alle arcate"):
        st.session_state.page = "lobby"
        st.rerun()
