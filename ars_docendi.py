import streamlit as st

# ==================================================
# CONFIGURAZIONE PAGINA
# ==================================================

st.set_page_config(
    page_title="Ludus",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================================================
# CSS
# ==================================================

css = """
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Montserrat:wght@300;500;700&display=swap');

/* --------------------------------------------------
   PAGINA
-------------------------------------------------- */

.stApp{
    background:
    radial-gradient(
        circle at center,
        #170028 0%,
        #080010 45%,
        #020004 100%
    ) !important;

    color:white;
}

/* Rimuove elementi Streamlit */

header,
footer,
[data-testid="stHeader"]{
    display:none !important;
}

/* --------------------------------------------------
   TITOLO
-------------------------------------------------- */

.title-wrapper{
    text-align:center;
    margin-top:50px;
    margin-bottom:70px;
}

.neon-title{
    font-family:'Cinzel', serif;
    font-size:6rem;
    font-weight:700;
    letter-spacing:16px;

    color:white;

    text-shadow:
        0 0 10px #b537f2,
        0 0 25px #b537f2,
        0 0 60px #ff00c8;

    margin:0;
}

.subtitle{
    margin-top:12px;

    font-family:'Montserrat', sans-serif;
    font-size:1rem;

    color:#00f3ff;

    letter-spacing:8px;
    text-transform:uppercase;

    text-shadow:0 0 10px #00f3ff;
}

/* --------------------------------------------------
   ARCHI
-------------------------------------------------- */

div.stButton{
    display:flex;
    justify-content:center;
}

div.stButton > button{

    width:320px !important;
    height:560px !important;

    background:rgba(0,0,0,0.95) !important;

    border-radius:160px 160px 12px 12px !important;

    border:3px solid transparent !important;

    padding-top:180px !important;
    padding-bottom:40px !important;

    display:flex !important;
    flex-direction:column !important;
    justify-content:flex-start !important;
    align-items:center !important;

    transition:all .35s ease !important;
}

/* testo principale */

div.stButton > button strong{

    font-family:'Cinzel', serif !important;

    font-size:2rem !important;

    letter-spacing:4px;

    margin-bottom:25px;

    display:block;
}

/* sottotitolo */

div.stButton > button em{

    font-family:'Montserrat', sans-serif !important;

    font-style:normal !important;

    text-transform:uppercase;

    letter-spacing:4px;

    font-size:0.9rem;

    color:rgba(255,255,255,0.55);
}

/* --------------------------------------------------
   DISCIPVLVS
-------------------------------------------------- */

div[data-testid="column"]:nth-child(2) button{

    border-color:#00f3ff !important;

    box-shadow:
        0 0 8px #00f3ff,
        0 0 20px rgba(0,243,255,.9),
        0 0 50px rgba(0,243,255,.6),
        0 0 100px rgba(0,243,255,.25) !important;
}

div[data-testid="column"]:nth-child(2) button strong{

    color:#00f3ff !important;

    text-shadow:
        0 0 10px #00f3ff,
        0 0 20px #00f3ff;
}

div[data-testid="column"]:nth-child(2) button:hover{

    transform:translateY(-12px) scale(1.03);

    box-shadow:
        0 0 12px #00f3ff,
        0 0 30px #00f3ff,
        0 0 70px #00f3ff,
        0 0 140px rgba(0,243,255,.4) !important;
}

/* --------------------------------------------------
   GLADIATOR
-------------------------------------------------- */

div[data-testid="column"]:nth-child(3) button{

    border-color:#b537f2 !important;

    box-shadow:
        0 0 8px #b537f2,
        0 0 20px rgba(181,55,242,.9),
        0 0 50px rgba(181,55,242,.6),
        0 0 100px rgba(181,55,242,.25) !important;
}

div[data-testid="column"]:nth-child(3) button strong{

    color:#d884ff !important;

    text-shadow:
        0 0 10px #b537f2,
        0 0 20px #b537f2;
}

div[data-testid="column"]:nth-child(3) button:hover{

    transform:translateY(-12px) scale(1.03);

    box-shadow:
        0 0 12px #b537f2,
        0 0 30px #b537f2,
        0 0 70px #b537f2,
        0 0 140px rgba(181,55,242,.4) !important;
}

/* --------------------------------------------------
   IMPERATOR
-------------------------------------------------- */

div[data-testid="column"]:nth-child(4) button{

    border-color:#ff00c8 !important;

    box-shadow:
        0 0 8px #ff00c8,
        0 0 20px rgba(255,0,200,.9),
        0 0 50px rgba(255,0,200,.6),
        0 0 100px rgba(255,0,200,.25) !important;
}

div[data-testid="column"]:nth-child(4) button strong{

    color:#ff70d6 !important;

    text-shadow:
        0 0 10px #ff00c8,
        0 0 20px #ff00c8;
}

div[data-testid="column"]:nth-child(4) button:hover{

    transform:translateY(-12px) scale(1.03);

    box-shadow:
        0 0 12px #ff00c8,
        0 0 30px #ff00c8,
        0 0 70px #ff00c8,
        0 0 140px rgba(255,0,200,.4) !important;
}

/* --------------------------------------------------
   PAGINA ARENA
-------------------------------------------------- */

.arena-title{
    text-align:center;
    margin-top:70px;
}

</style>
"""

st.markdown(css, unsafe_allow_html=True)

# ==================================================
# STATO
# ==================================================

if "level" not in st.session_state:
    st.session_state.level = None

# ==================================================
# HOME
# ==================================================

if st.session_state.level is None:

    st.markdown(
        """
        <div class="title-wrapper">
            <h1 class="neon-title">LUDUS</h1>
            <div class="subtitle">scegli il tuo destino</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    spacer1, col1, col2, col3, spacer2 = st.columns(
        [0.6, 2, 2, 2, 0.6]
    )

    with col1:
        if st.button(
            "**DISCIPVLVS**\n\n*beginner*",
            key="discipulus"
        ):
            st.session_state.level = "Discipulus"
            st.rerun()

    with col2:
        if st.button(
            "**GLADIATOR**\n\n*intermediate*",
            key="gladiator"
        ):
            st.session_state.level = "Gladiator"
            st.rerun()

    with col3:
        if st.button(
            "**IMPERATOR**\n\n*pro*",
            key="imperator"
        ):
            st.session_state.level = "Imperator"
            st.rerun()

# ==================================================
# ARENA
# ==================================================

else:

    st.markdown(
        f"""
        <div class="arena-title">
            <h1 class="neon-title" style="font-size:4rem;">
                {st.session_state.level}
            </h1>

            <div class="subtitle">
                arena attiva
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### ⚔️ Esercizi in arrivo")

    st.info(
        f"Benvenuto nell'arena {st.session_state.level}. "
        "Qui appariranno gli esercizi di latino."
    )

    st.markdown("<br><br>", unsafe_allow_html=True)

    if st.button("← Torna alla selezione"):
        st.session_state.level = None
        st.rerun()
