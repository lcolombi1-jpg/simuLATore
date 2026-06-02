import streamlit as st

# =====================================================
# CONFIG PAGINA
# =====================================================

st.set_page_config(
    page_title="Ludus",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# SESSION STATE
# =====================================================

if "level" not in st.session_state:
    st.session_state.level = None

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Montserrat:wght@300;500&display=swap');

header, footer, #MainMenu {
    visibility:hidden;
}

/* ---------------------------------- */
/* SFONDO */
/* ---------------------------------- */

.stApp{
    background:
    radial-gradient(
        circle at center,
        #1d0036 0%,
        #0b0017 45%,
        #020004 100%
    );

    color:white;
}

/* ---------------------------------- */
/* TITOLO */
/* ---------------------------------- */

.main-title{
    text-align:center;
    margin-top:40px;
}

.main-title h1{

    font-family:'Cinzel', serif;

    font-size:6rem;

    letter-spacing:14px;

    margin-bottom:0;

    color:white;

    text-shadow:
        0 0 10px #b537f2,
        0 0 25px #b537f2,
        0 0 60px #ff00c8;
}

.main-title p{

    font-family:'Montserrat', sans-serif;

    color:#00f0ff;

    letter-spacing:8px;

    text-transform:uppercase;

    margin-top:8px;

    text-shadow:
        0 0 10px #00f0ff;
}

/* ---------------------------------- */
/* CONTENITORE ARCHI */
/* ---------------------------------- */

.arch-space{
    margin-top:30px;
}

/* ---------------------------------- */
/* ARCHI */
/* ---------------------------------- */

.arch-preview{

    width:270px;
    height:460px;

    margin:auto;

    border-radius:
        135px
        135px
        10px
        10px;

    background:
        rgba(0,0,0,0.97);

    display:flex;

    flex-direction:column;

    justify-content:center;

    align-items:center;

    text-align:center;
}

.arch-title{

    font-family:'Cinzel', serif;

    font-size:2.1rem;

    letter-spacing:3px;

    margin-bottom:18px;
}

.arch-sub{

    font-family:'Montserrat', sans-serif;

    font-size:0.9rem;

    letter-spacing:6px;

    text-transform:uppercase;

    color:rgba(255,255,255,.45);
}

/* ---------------------------------- */
/* CIANO */
/* ---------------------------------- */

.cyan{

    border:3px solid #00eaff;

    box-shadow:
        0 0 6px #00eaff,
        0 0 15px #00eaff,
        0 0 35px rgba(0,234,255,.9),
        0 0 80px rgba(0,234,255,.55),
        0 0 130px rgba(0,234,255,.25);
}

.cyan .arch-title{

    color:#00eaff;

    text-shadow:
        0 0 10px #00eaff,
        0 0 25px #00eaff;
}

/* ---------------------------------- */
/* VIOLA */
/* ---------------------------------- */

.violet{

    border:3px solid #b537f2;

    box-shadow:
        0 0 6px #b537f2,
        0 0 15px #b537f2,
        0 0 35px rgba(181,55,242,.9),
        0 0 80px rgba(181,55,242,.55),
        0 0 130px rgba(181,55,242,.25);
}

.violet .arch-title{

    color:#d884ff;

    text-shadow:
        0 0 10px #b537f2,
        0 0 25px #b537f2;
}

/* ---------------------------------- */
/* FUCSIA */
/* ---------------------------------- */

.pink{

    border:3px solid #ff00c8;

    box-shadow:
        0 0 6px #ff00c8,
        0 0 15px #ff00c8,
        0 0 35px rgba(255,0,200,.9),
        0 0 80px rgba(255,0,200,.55),
        0 0 130px rgba(255,0,200,.25);
}

.pink .arch-title{

    color:#ff70d6;

    text-shadow:
        0 0 10px #ff00c8,
        0 0 25px #ff00c8;
}

/* ---------------------------------- */
/* BOTTONI */
/* ---------------------------------- */

div.stButton > button{

    width:270px !important;

    margin-top:20px;

    border-radius:8px !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HOME
# =====================================================

if st.session_state.level is None:

    st.markdown("""
    <div class="main-title">
        <h1>LUDUS</h1>
        <p>Scegli il tuo destino</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="arch-space"></div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    # -----------------------------------
    # DISCIPVLVS
    # -----------------------------------

    with c1:

        st.markdown("""
        <div class="arch-preview cyan">
            <div class="arch-title">
                DISCIPVLVS
            </div>

            <div class="arch-sub">
                Beginner
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("ENTRA", key="disc"):
            st.session_state.level = "Discipulus"
            st.rerun()

    # -----------------------------------
    # GLADIATOR
    # -----------------------------------

    with c2:

        st.markdown("""
        <div class="arch-preview violet">
            <div class="arch-title">
                GLADIATOR
            </div>

            <div class="arch-sub">
                Intermediate
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("ENTRA", key="glad"):
            st.session_state.level = "Gladiator"
            st.rerun()

    # -----------------------------------
    # IMPERATOR
    # -----------------------------------

    with c3:

        st.markdown("""
        <div class="arch-preview pink">
            <div class="arch-title">
                IMPERATOR
            </div>

            <div class="arch-sub">
                Pro
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("ENTRA", key="imp"):
            st.session_state.level = "Imperator"
            st.rerun()

# =====================================================
# PAGINA LIVELLO
# =====================================================

else:

    st.markdown(f"""
    <div class="main-title">
        <h1 style="font-size:4rem;">
            {st.session_state.level}
        </h1>

        <p>Arena Attiva</p>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        f"Benvenuto nell'arena {st.session_state.level}. "
        "Qui verranno mostrati gli esercizi."
    )

    st.write("")

    if st.button("← Torna alle porte"):
        st.session_state.level = None
        st.rerun()
