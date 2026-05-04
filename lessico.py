import streamlit as st
import random
import re

# --- DATABASE ---
dati_lessico = """
VERBI
amo, -as, -avi, -atum, -are (I con.) = amare
cognosco, -is, cognovi, cognitum, -ere (III con.) conoscere
valeo, -es, -ui, -ere (II con.) = essere forte; essere in buona salute
do, -as, dedi, datum, -are (I con.) = dare
pugno, -as, -avi, -atum, -are (I con.) = combattere
eo, is, ivi, itum, ire andare
facio, -is, feci, factum, -ere = fare
possum, potes, potui, posse (composto di sum) potere
quiesco, -is, quievi, quietum, -ere (III con.) riposare
duco, -is, duxi, dictum, -ere (III con.) = condurre
habeo, -es, -ui, -itum, -ere (II con.) = avere
sum, es, fui, esse = essere
video, -es, vidi, visum, -ere (II con.) vedere
oro, -as, -avi, -atum, -are (I con.) = pregare
vigilo, -as, -avi, -atum, -are (I con.) = vegliare
venio, -is, veni, ventum, -ire (IV con.) = venire
exerceo, -es, -ui, -itum, -ere (II con.) esercitare
gero, -is, gessi, gestum, -ere (III con.) portare
miror, -aris, -atus sum, -ari (I con.; dep.) meravigliarsi
rogo, -as, -avi, -atum, -are (I con.) = chiedere
peto, -is, ivi, -itum, -ere (III con.) = chiedere
suadeo, -es, suasi, suasum, -ere (II con.) = persuadere
constituo, -is, -stitui, -stitutum, -ere (III con.) = decidere
fio, fis, factus sum, fieri essere fatto, accadere, divenire
accido, -is, accidi, -ere (III con.) = accadere
sequor, -eris, secutus sum, sequi (III con.; dep.) = seguire
quaero, -is, quaesivi, quaesitum, -ere (III con.) = chiedere
laudo, -as, -avi, -atum, -are (I con.) = lodare
morior, -eris, mortuus sum, mori (con. mista; dep.) = morire
vinco, -is, vici, victum, -ere (III con.) = vincere
vivo, -is, vixi, victum, -ere (III con.) = vivere
vincio, -is, vinxi, vinctum, -ire (IV con.) legare
cogito, -as, -avi, -atum, -are (I con.) = pensare
respondeo, -es, respondi, responsum, -ere (II con.) = rispondere
audio, -is, -ivi, -itum, -ire (IV con.) = udire
scio, -is, scivi, scitum, -ire (IV con.) = sapere
credo, -is, credidi, creditum, -ere (III con.) = credere
timeo, -es, -ui, -ere (II con.) = temere
erro, -as, -avi, -atum, -are (I con.) = vagare; sbagliare
nego, -as, -avi, -atum, -are (I con.) = negare
invenio, -is, -veni, -ventum, -ire (IV con.) trovare
studeo, -es, -ui, -ere (II con.) = desiderare
disco, -is, didici, -ere (III con.) = imparare
paro, -as, -avi, -atum, -are (I con.) preparare
dico, -is, dixi, dictum, -ere (III con.) = dire
scribo, -is, scripsi, scriptum, -ere (III con.) = scrivere
soleo, -es, solitus sum, -ere (II con.; semidep.) = essere solito
exsisto, -is, -stiti, -ere (III con.) = esistere
nascor, -eris, natus sum, nasci (III con.; dep.) = nascere
censeo, -es, censui, censum, -ere (II con.) giudicare
existimo, -as, -avi, -atum, -are (I con.) stimare
mitto, -is, misi, missum, -ere (III con.) mandare
volo, vis, volui, volle volere
nolo, non vis, nolui, nolle = non volere
malo, mavis, malui, malle preferire
desum, -es, -fui, -esse (composto di sum) = mancare
confiteor, -eris, -fessus sum, -eri (II con.) confessare
oportet, oportuit, -ere (II con.; impersonale) = bisogna
fero, fers, tuli, latum, ferre portare
dono, -as, -avi, -atum, -are (I con.) = donare
pono, -is, posui, positum, -ere (III con.) porre
sumo, -is, sumpsi, sumptum, -ere (III con.) prendere
lego, -is, legi, lectum, -ere (III con.) = leggere
rumpo, -is, rupi, ruptum, -ere (III con.) rompere
obsideo, -er, -sedi, -sessum, -ere (II con.) = assediare
laboro, -as, -avi, -atum, -are (I con.) lavorare, far fatica
teneo, -es, tenui, tentum, -ere (II con.) = tenere
queror, -eris, questus sum, queri (III con.; dep.) = lamentarsi
loquor, -eris, locutus sum, loqui (III con.; dep.) = parlare
dormio, -is, -ivi, -itum, -ire (IV con.) dormire
amitto, -is, -misi, -missum, -ere (III con.) perdere; lasciar andare
moveo, -es, movi, motum, -ere (II con.) = muovere
hortor, -aris, -atus sum, -ari (I con.; dep.) = esortare
capio, -is, cepi, captum, -ere = prendere
pello, -is, pepuli, pulsum, -ere (III con.) spingere; cacciare
proficiscor, -eris, -fectus sum, -ficisci (III con.; dep.) = partire
imitor, -aris, -atus sum, -ari (I con.; dep.) imitare
taceo, -es, -ui, -itum, -ere (II con.) = tacere
consequor, -eris, -secutus sum, -sequi (III con.; dep.) = ottenere
reddo, -is, -didi, -ditum, -ere (III con.) restituire
cerno, -is, crevi, cretum, -ere (III con.) vedere
defendo, -is, -fendi, -fensum, -ere (III con.) difendere
ago, -is, egi, actum, -ere (III con.) = condurre
puto, -as, -avi, -atum, -are (I con.) = pensare
metuo, -is, -ui, -utum, -ere (III con.) = temere

SOSTANTIVI
oppidum, -i (n.; II decl.) = città
custodia, -ae (f.; I decl.) sorveglianza; prigione
bellum, -i (n; II decl.) = guerra
pugna, -ae (f.; I decl.) = battaglia
iniuria, -ae (f.; I decl.) offesa
dux, ducis (m.; III decl.) comandante
hostis, hostis (m.; III decl.) = nemico
exercitus, -us (m.; IV decl.) = esercito
victor, -is (m.; III decl.) vincitore
corpus, -oris (n.; III decl.) = corpo
manus, -us (f.; IV decl.) mano
rostrum, -i (n.; II decl.) rostro
homo, hominis (m; III decl.) = uomo
mos, moris (m.; III decl.) costume, usanza
rex, regis (m.; III decl.) = re
exemplum, -i (n.; II decl.) esempio
multitudo, -inis (f.; III decl.) = folla
res, rei (f.; V decl.) = cosa
patria, -ae (f.; I decl.) = patria
nihil (n.; indeclinabile) niente
urbs, -is (f.; III decl.) = città
solitudo, -inis (f.; III decl.) = solitudine
victoria, -ae (I decl.) vittoria
liber, libri (m.; II decl.) = libro
agricultura, -ae (f.; I decl.) agricoltura
ius, iuris (n.; III decl.) diritto, giustizia
utilitas, -atis (f.; III decl.) utilità
mens, mentis (f.; III decl.) = mente
gloria, -ae (f.; I decl.) = gloria
res publica (sost. f. V decl. + agg.) = stato
Caesar, -is (m.; III decl.) Cesare
equitatus, -us (m.; IV decl.) = cavalleria
iter, itineris (n.; III decl.) viaggio
impetus, -us (m.; IV decl.) impeto
vox, vocis (f.; III decl.) = voce
ferrum, -i (n.; II decl.) ferro; spada
ignis, -is (m.; III decl.) = fuoco
genus, -eris (n.; III decl.) = genere
officium, -i (n.; II decl.) = dovere
epistula, -ae (f.; I decl.) epistola
nox, noctis (f.; III decl.) = notte
imperator, -oris (m.; III decl.) = comandante
miles, -itis (m.; III decl.) soldato
legio, -onis (f.; III decl.) = legione
proelium, -i (n.; II decl.) = battaglia
regnum, -i (n.; II decl.) regno
matrimonium, -i (n.; II decl.) = matrimonio
legatus, -i (II decl.) = ambasciatore
frater, fratris (m.; III decl.) = fratello
consul, -is (m.; III decl.) console
Cicero, -onis (m.; III decl.) = Cicerone
Hannibal, is (m.; III decl.) Annibale
opera, -ae (f.; I decl.) = opera
vir, viri (m.; II decl.) = uomo
verbum, -i (n.; II decl.) = parola
ars, artis (f.; III decl.) arte, tecnica
tempus, -oris (n.; III decl.) tempo
ager, agri (m.; II decl.) = campo
oratio, -onis (f.; III decl.) discorso
virtus, -utis (f.; III decl.) = valore

PRONOMI
ego, mei = io
tu, tui = tu
is, ea, id = egli/lui, ella/lei, esso
hic, haec, hoc = questo
ille, illa, illud = quello
sui, sibi = sè
qui, quae, quod = che/quale
quis, quid chi? che cosa?
nemo, neminis nessuno

AGGETTIVI
facilis, -e (II classe) = facile
omnis, -e (II classe) ogni, tutto
aegrotus, -a, -um (I classe) malato
felix, -icis (II classe) felice, fortunato
bonus, -a, -um (I classe) = buono
dulcis, -e (II classe) = dolce
doctus, -a, -um (I classe) dotto
nullus, -a, -um (agg. pronominale) = nessuno
verus, -a, -um (I classe) = vero
alius, -a, -ud (agg. pronominale) = altro
alter, -a, -um (agg. pronominale) altro (fra due)
Romanus, -a, -um (I classe) romano
multus, -a, -um (I classe) = molto
odiosus, -a, -um (I classe) = odioso
utilis, -e (II classe) = utile
pauper, -eris (II classe) = povero
"""

import streamlit as st
import random
import re

# --- DATABASE ---
dati_lessico = """
[... mantieni qui il database del messaggio precedente ...]
"""

def parse_lessico(testo):
    cards = []
    linee = testo.strip().split('\n')
    categoria_attuale = ""
    for riga in linee:
        riga = riga.strip()
        if not riga: continue
        if riga in ["VERBI", "SOSTANTIVI", "PRONOMI", "AGGETTIVI"]:
            categoria_attuale = riga
            continue
        
        if "=" in riga:
            parti = riga.split("=", 1)
            latino = parti[0].strip()
            italiano = parti[1].strip()
        else:
            parti = re.split(r'\s+(?=[a-zàèéìòù\s]+$)', riga)
            if len(parti) > 1:
                latino = parti[0].strip()
                italiano = parti[1].strip()
            else:
                latino = riga
                italiano = "Traduzione non inserita"

        fronte = latino.replace(",", " ").split()[0]
        cards.append({
            "fronte": fronte.upper(),
            "paradigma": latino,
            "traduzione": italiano,
            "cat": categoria_attuale
        })
    return cards

# --- INTERFACCIA ---
st.set_page_config(page_title="Latino Flashcards", layout="centered")

# CSS per rendere il lemma enorme e la card pulita
st.markdown("""
    <style>
    /* Rimuove i margini superflui dei bottoni di Streamlit per farli sembrare card */
    div.stButton > button {
        height: 350px;
        background-color: #ffffff;
        border: 2px solid #e0e0e0;
        border-radius: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        border-color: #ff4b4b;
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
        background-color: #fffafa;
    }
    /* Stile per il testo del paradigma e traduzione */
    .retro-container {
        text-align: center;
    }
    .retro-paradigma {
        font-size: 24px;
        color: #555;
        margin-bottom: 10px;
    }
    .retro-traduzione {
        font-size: 32px;
        font-weight: bold;
        color: #ff4b4b;
    }
    </style>
""", unsafe_allow_html=True)

# Inizializzazione Session State
if 'mazzo' not in st.session_state:
    st.session_state.mazzo = parse_lessico(dati_lessico)
    random.shuffle(st.session_state.mazzo)
    st.session_state.indice = 0
    st.session_state.mostra_retro = False

# Funzioni
def gira_card():
    st.session_state.mostra_retro = not st.session_state.mostra_retro

def prossima_card():
    st.session_state.indice = (st.session_state.indice + 1) % len(st.session_state.mazzo)
    st.session_state.mostra_retro = False

def mischia():
    random.shuffle(st.session_state.mazzo)
    st.session_state.indice = 0
    st.session_state.mostra_retro = False

# --- LAYOUT ---
st.title("🏛️ Trainer Lessico")

if st.session_state.indice < len(st.session_state.mazzo):
    item = st.session_state.mazzo[st.session_state.indice]
    
    # Info Categoria e Progresso
    col_a, col_b = st.columns([1, 1])
    with col_a:
        st.caption(f"Categoria: **{item['cat']}**")
    with col_b:
        st.markdown(f"<p style='text-align:right; color:gray;'>{st.session_state.indice + 1} / {len(st.session_state.mazzo)}</p>", unsafe_allow_html=True)

    # AREA CARD
    if not st.session_state.mostra_retro:
        # FRONTE: Solo il lemma in grassetto gigante
        st.button(item['fronte'], key="front_btn", use_container_width=True, on_click=gira_card)
        st.markdown(f"<style>#root div[data-testid='stButton'] > button p {{ font-size: 70px !important; font-weight: 800; }}</style>", unsafe_allow_html=True)
    else:
        # RETRO: Paradigma e Traduzione
        contenuto_retro = f"{item['paradigma']}\n\n{item['traduzione'].upper()}"
        st.button(contenuto_retro, key="back_btn", use_container_width=True, on_click=gira_card)
        st.markdown(f"<style>#root div[data-testid='stButton'] > button p {{ font-size: 28px !important; }}</style>", unsafe_allow_html=True)

    st.write("") # Spaziatore

    # Navigazione
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.button("PROSSIMA ➡️", on_click=prossima_card, use_container_width=True)
    with c3:
        st.button("🔀", on_click=mischia, use_container_width=True, help="Mischia il mazzo")
