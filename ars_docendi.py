import streamlit as st

st.set_page_config(
    page_title="Ludus",
    page_icon="🏛️",
    layout="wide"
)

if "level" not in st.session_state:
    st.session_state.level = None

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&display=swap');

.stApp{
background:
radial-gradient(circle at center,
#19002f 0%,
#0a0015 50%,
#020004 100%);
}

h1{
text-align:center;
font-family:'Cinzel', serif;
color:white;
font-size:5rem;
}

div.stButton > button{

height:450px;
width:100%;

border-radius:
120px
120px
10px
10px;

background:black;
font-size:2rem;
font-family:'Cinzel', serif;

transition:.3s;
}

div.stButton > button:hover{
transform:translateY(-8px);
}

</style>
""", unsafe_allow_html=True)

if st.session_state.level is None:

    st.markdown("<h1>LUDUS</h1>", unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)

    with c1:
        if st.button("DISCIPVLVS"):
            st.session_state.level="Discipulus"
            st.rerun()

    with c2:
        if st.button("GLADIATOR"):
            st.session_state.level="Gladiator"
            st.rerun()

    with c3:
        if st.button("IMPERATOR"):
            st.session_state.level="Imperator"
            st.rerun()

else:

    st.title(st.session_state.level)

    st.write("Qui inserirai gli esercizi.")

    if st.button("← Torna"):
        st.session_state.level=None
        st.rerun()
