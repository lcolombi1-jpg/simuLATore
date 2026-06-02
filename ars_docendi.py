import streamlit as st

# ==========================================================
# CONFIG
# ==========================================================

st.set_page_config(
    page_title="LVDVS",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================================
# SESSION STATE
# ==========================================================

if "page" not in st.session_state:
    st.session_state.page = "intro"

# ==========================================================
# CSS GLOBALE
# ==========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Montserrat:wght@300;400;500&display=swap');

header,
footer,
#MainMenu,
[data-testid="stToolbar"]{
    visibility:hidden;
}

.block-container{
    padding-top:0rem !important;
    max-width:100%;
}

/* ================================================= */
/* SFONDO */
/* ================================================= */

.stApp{

    background:
    radial-gradient(
        circle at center,
        #19002f 0%,
        #0a0015 50%,
        #020004 100%
    );

    color:white;
}

/* ================================================= */
/* TITOLI */
/* ================================================= */

.hero-title{

    text-align:center;

    font-family:'Cinzel', serif;

    font-size:6rem;

    letter-spacing:12px;

    margin-top:60px;

    color:white;

    text-shadow:
        0 0 10px #ff00ff,
        0 0 25px #ff00ff,
        0 0 60px rgba(255,0,255,.7);
}

.hero-sub{

    text-align:center;

    font-family:'Montserrat', sans-serif;

    color:#00eaff;

    font-size:1.1rem;

    letter-spacing:8px;

    margin-top:-20px;

    text-shadow:
        0 0 12px #00eaff;
}

/* ================================================= */
/* PULSANTE AD MAIORA */
/* ================================================= */

div.stButton > button {

    transition:0.3s ease;
}

.intro-button button{

    font-family:'Cinzel', serif !important;

    font-size:1.3rem !important;

    height:70px !important;

    border:2px solid #00eaff !important;

    color:#00eaff !important;

    background:transparent !important;

    box-shadow:
        0 0 10px #00eaff,
        0 0 25px rgba(0,234,255,.6) !important;
}

.intro-button button:hover{

    transform:scale(1.04);

    box-shadow:
        0 0 20px #00eaff,
        0 0 50px rgba(0,234,255,.8) !important;
}

/* ================================================= */
/* ARCATE */
/* ================================================= */

.arch-button button{

    width:100% !important;

    height:480px !important;

    background:transparent !important;

    border-radius:
        240px
        240px
        12px
        12px !important;

    font-family:'Cinzel', serif !important;

    font-size:1.8rem !important;

    letter-spacing:1px !important;

    transition:0.3s ease !important;
}

.arch-button button:hover{

    transform:translateY(-8px);
}

/* ================================================= */
/* ARCATA CIANO */
/* ================================================= */

.cyan button{

    border:4px solid #00eaff !important;

    color:#00eaff !important;

    text-shadow:
        0 0 10px #00eaff !important;

    box-shadow:
        0 0 10px #00eaff,
        0 0 30px #00eaff,
        0 0 60px rgba(0,234,255,.7),
        0 0 120px rgba(0,234,255,.35) !important;
}

/* ================================================= */
/* ARCATA VIOLA */
/* ================================================= */

.violet button{

    border:4px solid #c442ff !important;

    color:#d56bff !important;

    text-shadow:
        0 0 10px #d56bff !important;

    box-shadow:
        0 0 10px #c442ff,
        0 0 30px #c442ff,
        0 0 60px rgba(196,66,255,.7),
        0 0 120px rgba(196,66,255,.35) !important;
}

/* ================================================= */
/* ARCATA ROSA */
/* ================================================= */

.pink button{

    border:4px solid #ff006e !important;

    color:#ff4ca0 !important;

    text-shadow:
        0 0 10px #ff4ca0 !important;

    box-shadow:
        0 0 10px #ff006e,
        0 0 30px #ff006e,
        0 0 60px rgba(255,0,110,.7),
        0 0 120px rgba(255,0,110,.35) !important;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# PAGINA INTRO
# ==========================================================

if st.session_state.page == "intro":

    st.markdown(
        """
        <div class="hero-title">LVDVS</div>
        <div class="hero-sub">audaces fortuna iuvat</div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")
    st.write("")
    st.write("")

    c1, c2, c3 = st.columns([2,1,2])

    with c2:

        st.markdown('<div class="intro-button">', unsafe_allow_html=True)

        if st.button("AD MAIORA"):
            st.session_state.page = "lobby"
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================================
# LOBBY
# ==========================================================

elif st.session_state.page == "lobby":

    st.markdown(
        """
        <div class="hero-title" style="font-size:4.5rem;">LVDVS</div>
        <div class="hero-sub">elige gradum tuum</div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            '<div class="arch-button cyan">',
            unsafe_allow_html=True
        )

        if st.button(
            "DISCIPVLVS\n\nBEGINNER",
            key="disc"
        ):
            st.session_state.page = "discipulus"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:

        st.markdown(
            '<div class="arch-button violet">',
            unsafe_allow_html=True
        )

        if st.button(
            "GLADIATOR\n\nINTERMEDIATE",
            key="glad"
        ):
            st.session_state.page = "gladiator"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    with col3:

        st.markdown(
            '<div class="arch-button pink">',
            unsafe_allow_html=True
        )

        if st.button(
            "IMPERATOR\n\nPRO",
            key="imp"
        ):
            st.session_state.page = "imperator"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================================
# DISCIPVLVS
# ==========================================================

elif st.session_state.page == "discipulus":

    st.markdown(
        """
        <div class="hero-title">DISCIPVLVS</div>
        <div class="hero-sub">initium sapientiae</div>
        """,
        unsafe_allow_html=True
    )

    st.info("Qui inserirai il quiz Beginner.")

    if st.button("← Torna alle arcate"):
        st.session_state.page = "lobby"
        st.rerun()

# ==========================================================
# GLADIATOR
# ==========================================================

elif st.session_state.page == "gladiator":

    st.markdown(
        """
        <div class="hero-title">GLADIATOR</div>
        <div class="hero-sub">virtus in media stat</div>
        """,
        unsafe_allow_html=True
    )

    st.info("Qui inserirai il quiz Intermediate.")

    if st.button("← Torna alle arcate"):
        st.session_state.page = "lobby"
        st.rerun()

# ==========================================================
# IMPERATOR
# ==========================================================

elif st.session_state.page == "imperator":

    st.markdown(
        """
        <div class="hero-title">IMPERATOR</div>
        <div class="hero-sub">ad astra per aspera</div>
        """,
        unsafe_allow_html=True
    )

    st.info("Qui inserirai il quiz Pro.")

    if st.button("← Torna alle arcate"):
        st.session_state.page = "lobby"
        st.rerun()
