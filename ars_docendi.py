```python
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
# CSS
# =====================================================

st.markdown("""
<style>

/* -------------------------------------------------- */
/* FONT */
/* -------------------------------------------------- */

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Montserrat:wght@300;500&display=swap');

/* -------------------------------------------------- */
/* STREAMLIT CLEAN */
/* -------------------------------------------------- */

header,
footer,
#MainMenu,
[data-testid="stToolbar"],
[data-testid="stDecoration"]{
    display:none !important;
}

.block-container{
    padding-top:0.5rem !important;
    padding-bottom:0rem !important;
    max-width:100% !important;
}

/* -------------------------------------------------- */
/* PAGINA */
/* -------------------------------------------------- */

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

/* -------------------------------------------------- */
/* TITOLO */
/* -------------------------------------------------- */

.title-wrapper{

    text-align:center;

    margin-top:10px;
    margin-bottom:20px;
}

.main-title{

    font-family:'Cinzel', serif;

    font-size:4.8rem;

    color:white;

    letter-spacing:12px;

    margin:0;

    text-shadow:
        0 0 10px #b537f2,
        0 0 25px #b537f2,
        0 0 55px #ff00c8;
}

.subtitle{

    margin-top:6px;

    color:#00f0ff;

    font-family:'Montserrat', sans-serif;

    letter-spacing:8px;

    text-transform:uppercase;

    text-shadow:
        0 0 10px #00f0ff;
}

/* -------------------------------------------------- */
/* PORTE */
/* -------------------------------------------------- */

.gates-row{

    display:flex;

    justify-content:center;

    gap:50px;

    margin-top:20px;

    flex-wrap:nowrap;
}

.gate{

    width:240px;

    height:340px;

    border-radius:
        120px
        120px
        10px
        10px;

    background:#000;

    display:flex;

    flex-direction:column;

    justify-content:center;

    align-items:center;

    text-align:center;

    transition:0.3s ease;
}

.gate:hover{

    transform:translateY(-8px);
}

/* -------------------------------------------------- */
/* TESTI */
/* -------------------------------------------------- */

.gate-title{

    font-family:'Cinzel', serif;

    font-size:2rem;

    letter-spacing:3px;

    margin-bottom:18px;
}

.gate-sub{

    font-family:'Montserrat', sans-serif;

    text-transform:uppercase;

    letter-spacing:5px;

    color:rgba(255,255,255,0.45);

    font-size:0.85rem;
}

/* -------------------------------------------------- */
/* DISCIPVLVS */
/* -------------------------------------------------- */

.cyan{

    border:3px solid #00eaff;

    box-shadow:
        0 0 5px #00eaff,
        0 0 15px #00eaff,
        0 0 35px rgba(0,234,255,.8),
        0 0 70px rgba(0,234,255,.4);
}

.cyan .gate-title{

    color:#00eaff;

    text-shadow:
        0 0 10px #00eaff,
        0 0 20px #00eaff;
}

/* -------------------------------------------------- */
/* GLADIATOR */
/* -------------------------------------------------- */

.violet{

    border:3px solid #b537f2;

    box-shadow:
        0 0 5px #b537f2,
        0 0 15px #b537f2,
        0 0 35px rgba(181,55,242,.8),
        0 0 70px rgba(181,55,242,.4);
}

.violet .gate-title{

    color:#d884ff;

    text-shadow:
        0 0 10px #b537f2,
        0 0 20px #b537f2;
}

/* -------------------------------------------------- */
/* IMPERATOR */
/* -------------------------------------------------- */

.pink{

    border:3px solid #ff00c8;

    box-shadow:
        0 0 5px #ff00c8,
        0 0 15px #ff00c8,
        0 0 35px rgba(255,0,200,.8),
        0 0 70px rgba(255,0,200,.4);
}

.pink .gate-title{

    color:#ff70d6;

    text-shadow:
        0 0 10px #ff00c8,
        0 0 20px #ff00c8;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# TITOLO
# =====================================================

st.markdown("""
<div class="title-wrapper">

    <div class="main-title">
        LUDUS
    </div>

    <div class="subtitle">
        scegli il tuo destino
    </div>

</div>
""", unsafe_allow_html=True)

# =====================================================
# PORTE
# =====================================================

st.markdown("""
<div class="gates-row">

    <div class="gate cyan">

        <div class="gate-title">
            DISCIPVLVS
        </div>

        <div class="gate-sub">
            Beginner
        </div>

    </div>

    <div class="gate violet">

        <div class="gate-title">
            GLADIATOR
        </div>

        <div class="gate-sub">
            Intermediate
        </div>

    </div>

    <div class="gate pink">

        <div class="gate-title">
            IMPERATOR
        </div>

        <div class="gate-sub">
            Pro
        </div>

    </div>

</div>
""", unsafe_allow_html=True)
```
