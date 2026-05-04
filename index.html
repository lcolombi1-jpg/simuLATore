<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Programmatore Flash Cards Latino</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; flex-direction: column; align-items: center; background-color: #f0f2f5; padding: 20px; }
        .counter { margin-bottom: 15px; font-size: 1.1rem; color: #555; font-weight: bold; }
        
        /* Contenitore card */
        .card { width: 380px; height: 280px; perspective: 1000px; cursor: pointer; }
        .card-inner {
            position: relative; width: 100%; height: 100%; text-align: center;
            transition: transform 0.6s; transform-style: preserve-3d;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2); border-radius: 15px;
        }
        .card.flipped .card-inner { transform: rotateY(180deg); }
        
        .front, .back {
            position: absolute; width: 100%; height: 100%; backface-visibility: hidden;
            display: flex; align-items: center; justify-content: center;
            padding: 30px; box-sizing: border-box; border-radius: 15px;
        }
        .front { background-color: #ffffff; font-size: 2.5rem; color: #1a73e8; font-weight: bold; }
        .back { background-color: #e8f0fe; transform: rotateY(180deg); flex-direction: column; font-size: 1.2rem; }
        
        .controls { margin-top: 40px; display: flex; gap: 15px; flex-wrap: wrap; justify-content: center; }
        button {
            padding: 15px 30px; font-size: 1rem; cursor: pointer; border: none;
            border-radius: 50px; background-color: #1a73e8; color: white; transition: 0.3s;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        button:hover { background-color: #1557b0; transform: translateY(-2px); }
        .btn-shuffle { background-color: #34a853; }
        .btn-prev { background-color: #70757a; }
    </style>
</head>
<body>

    <h1>Lessico Latino</h1>
    <div class="counter" id="counter">Caricamento...</div>
    
    <div class="card" id="flashcard" onclick="this.classList.toggle('flipped')">
        <div class="card-inner">
            <div class="front" id="card-front">...</div>
            <div class="back" id="card-back">...</div>
        </div>
    </div>

    <div class="controls">
        <button class="btn-prev" onclick="prevCard()">Indietro</button>
        <button onclick="nextCard()">Prossima</button>
        <button class="btn-shuffle" onclick="shuffleAndReset()">Mescola e Ricomincia</button>
    </div>

    <script>
        // Database completo dal tuo documento
        let vocaboli = [
            // VERBI
            { p: "amo, -as, -avi, -atum, -are (I con.)", t: "amare" },
            { p: "cognosco, -is, cognovi, cognitum, -ere (III con.)", t: "conoscere" },
            { p: "valeo, -es, -ui, -ere (II con.)", t: "essere forte; essere in buona salute" },
            { p: "do, -as, dedi, datum, -are (I con.)", t: "dare" },
            { p: "pugno, -as, -avi, -atum, -are (I con.)", t: "combattere" },
            { p: "eo, is, ivi, itum, ire", t: "andare" },
            { p: "facio, -is, feci, factum, -ere", t: "fare" },
            { p: "possum, potes, potui, posse", t: "potere" },
            { p: "quiesco, -is, quievi, quietum, -ere (III con.)", t: "riposare" },
            { p: "duco, -is, duxi, ductum, -ere (III con.)", t: "condurre" },
            { p: "habeo, -es, -ui, -itum, -ere (II con.)", t: "avere" },
            { p: "sum, es, fui, esse", t: "essere" },
            { p: "video, -es, vidi, visum, -ere (II con.)", t: "vedere" },
            { p: "oro, -as, -avi, -atum, -are (I con.)", t: "pregare" },
            { p: "vigilo, -as, -avi, -atum, -are (I con.)", t: "vegliare" },
            { p: "venio, -is, veni, ventum, -ire (IV con.)", t: "venire" },
            { p: "exerceo, -es, -ui, -itum, -ere (II con.)", t: "esercitare" },
            { p: "gero, -is, gessi, gestum, -ere (III con.)", t: "portare" },
            { p: "miror, -aris, -atus sum, -ari (I con.; dep.)", t: "meravigliarsi" },
            { p: "rogo, -as, -avi, -atum, -are (I con.)", t: "chiedere" },
            { p: "peto, -is, ivi, -itum, -ere (III con.)", t: "chiedere" },
            { p: "suadeo, -es, suasi, suasum, -ere (II con.)", t: "persuadere" },
            { p: "constituo, -is, -stitui, -stitutum, -ere (III con.)", t: "decidere" },
            { p: "fio, fis, factus sum, fieri", t: "essere fatto, accadere, divenire" },
            { p: "accido, -is, accidi, -ere (III con.)", t: "accadere" },
            { p: "sequor, -eris, secutus sum, sequi (III con.; dep.)", t: "seguire" },
            { p: "quaero, -is, quaesivi, quaesitum, -ere (III con.)", t: "chiedere" },
            { p: "laudo, -as, -avi, -atum, -are (I con.)", t: "lodare" },
            { p: "morior, -eris, mortuus sum, mori (con. mista; dep.)", t: "morire" },
            { p: "vinco, -is, vici, victum, -ere (III con.)", t: "vincere" },
            { p: "vivo, -is, vixi, victum, -ere (III con.)", t: "vivere" },
            { p: "vincio, -is, vinxi, vinctum, -ire (IV con.)", t: "legare" },
            { p: "cogito, -as, -avi, -atum, -are (I con.)", t: "pensare" },
            { p: "respondeo, -es, respondi, responsum, -ere (II con.)", t: "rispondere" },
            { p: "audio, -is, -ivi, -itum, -ire (IV con.)", t: "udire" },
            { p: "scio, -is, scivi, scitum, -ire (IV con.)", t: "sapere" },
            { p: "credo, -is, credidi, creditum, -ere (III con.)", t: "credere" },
            { p: "timeo, -es, -ui, -ere (II con.)", t: "temere" },
            { p: "erro, -as, -avi, -atum, -are (I con.)", t: "vagare; sbagliare" },
            { p: "nego, -as, -avi, -atum, -are (I con.)", t: "negare" },
            { p: "invenio, -is, -veni, -ventum, -ire (IV con.)", t: "trovare" },
            { p: "studeo, -es, -ui, -ere (II con.)", t: "desiderare" },
            { p: "disco, -is, didici, -ere (III con.)", t: "imparare" },
            { p: "paro, -as, -avi, -atum, -are (I con.)", t: "preparare" },
            { p: "dico, -is, dixi, dictum, -ere (III con.)", t: "dire" },
            { p: "scribo, -is, scripsi, scriptum, -ere (III con.)", t: "scrivere" },
            { p: "soleo, -es, solitus sum, -ere (II con.; semidep.)", t: "essere solito" },
            { p: "exsisto, -is, -stiti, -ere (III con.)", t: "esistere" },
            { p: "censeo, -es, censui, censum, -ere (II con.)", t: "giudicare" },
            { p: "existimo, -as, -avi, -atum, -are (I con.)", t: "stimare" },
            { p: "mitto, -is, misi, missum, -ere (III con.)", t: "mandare" },
            { p: "nascor, -eris, natus sum, nasci (III con.; dep.)", t: "nascere" },
            { p: "volo, vis, volui, volle", t: "volere" },
            { p: "nolo, non vis, nolui, nolle", t: "non volere" },
            { p: "malo, mavis, malui, malle", t: "preferire" },
            { p: "desum, -es, -fui, -esse", t: "mancare" },
            { p: "confiteor, -eris, -fessus sum, -eri (II con.)", t: "confessare" },
            { p: "oportet, oportuit, -ere (II con.; impersonale)", t: "bisogna" },
            { p: "fero, fers, tuli, latum, ferre", t: "portare" },
            { p: "dono, -as, -avi, -atum, -are (I con.)", t: "donare" },
            { p: "pono, -is, posui, positum, -ere (III con.)", t: "porre" },
            { p: "sumo, -is, sumpsi, sumptum, -ere (III con.)", t: "prendere" },
            { p: "lego, -is, legi, lectum, -ere (III con.)", t: "leggere" },
            { p: "rumpo, -is, rupi, ruptum, -ere (III con.)", t: "rompere" },
            { p: "obsideo, -er, -sedi, -sessum, -ere (II con.)", t: "assediare" },
            { p: "laboro, -as, -avi, -atum, -are (I con.)", t: "lavorare, far fatica" },
            { p: "teneo, -es, tenui, tentum, -ere (II con.)", t: "tenere" },
            { p: "queror, -eris, questus sum, queri (III con.; dep.)", t: "lamentarsi" },
            { p: "loquor, -eris, locutus sum, loqui (III con.; dep.)", t: "parlare" },
            { p: "dormio, -is, -ivi, -itum, -ire (IV con.)", t: "dormire" },
            { p: "amitto, -is, -misi, -missum, -ere (III con.)", t: "perdere; lasciar andare" },
            { p: "moveo, -es, movi, motum, -ere (II con.)", t: "muovere" },
            { p: "hortor, -aris, -atus sum, -ari (I con.; dep.)", t: "esortare" },
            { p: "capio, -is, cepi, captum, -ere", t: "prendere" },
            { p: "pello, -is, pepuli, pulsum, -ere (III con.)", t: "spingere; cacciare" },
            { p: "proficiscor, -eris, -fectus sum, -ficisci (III con.; dep.)", t: "partire" },
            { p: "imitor, -aris, -atus sum, -ari (I con.; dep.)", t: "imitare" },
            { p: "taceo, -es, -ui, -itum, -ere (II con.)", t: "tacere" },
            { p: "consequor, -eris, -secutus sum, -sequi (III con.; dep.)", t: "ottenere" },
            { p: "reddo, -is, -didi, -ditum, -ere (III con.)", t: "restituire" },
            { p: "cerno, -is, crevi, cretum, -ere (III con.)", t: "vedere" },
            { p: "defendo, -is, -fendi, -fensum, -ere (III con.)", t: "difendere" },
            { p: "ago, -is, egi, actum, -ere (III con.)", t: "condurre" },
            { p: "puto, -as, -avi, -atum, -are (I con.)", t: "pensare" },
            { p: "metuo, -is, -ui, -utum, -ere (III con.)", t: "temere" },
            
            // SOSTANTIVI
            { p: "oppidum, -i (n.; II decl.)", t: "città" },
            { p: "custodia, -ae (f.; I decl.)", t: "sorveglianza; prigione" },
            { p: "bellum, -i (n; II decl.)", t: "guerra" },
            { p: "pugna, -ae (f.; I decl.)", t: "battaglia" },
            { p: "iniuria, -ae (f.; I decl.)", t: "offesa" },
            { p: "dux, ducis (m.; III decl.)", t: "comandante" },
            { p: "hostis, hostis (m.; III decl.)", t: "nemico" },
            { p: "exercitus, -us (m.; IV decl.)", t: "esercito" },
            { p: "victor, -is (m.; III decl.)", t: "vincitore" },
            { p: "corpus, -oris (n.; III decl.)", t: "corpo" },
            { p: "manus, -us (f.; IV decl.)", t: "mano" },
            { p: "rostrum, -i (n.; II decl.)", t: "rostro" },
            { p: "homo, hominis (m; III decl.)", t: "uomo" },
            { p: "mos, moris (m.; III decl.)", t: "costume, usanza" },
            { p: "rex, regis (m.; III decl.)", t: "re" },
            { p: "exemplum, -i (n.; II decl.)", t: "esempio" },
            { p: "multitudo, -inis (f.; III decl.)", t: "folla" },
            { p: "res, rei (f.; V decl.)", t: "cosa" },
            { p: "patria, -ae (f.; I decl.)", t: "patria" },
            { p: "nihil (n.; indeclinabile)", t: "niente" },
            { p: "urbs, -is (f.; III decl.)", t: "città" },
            { p: "solitudo, -inis (f.; III decl.)", t: "solitudine" },
            { p: "victoria, -ae (I decl.)", t: "vittoria" },
            { p: "liber, libri (m.; II decl.)", t: "libro" },
            { p: "agricultura, -ae (f.; I decl.)", t: "agricoltura" },
            { p: "ius, iuris (n.; III decl.)", t: "diritto, giustizia" },
            { p: "utilitas, -atis (f.; III decl.)", t: "utilità" },
            { p: "mens, mentis (f.; III decl.)", t: "mente" },
            { p: "gloria, -ae (f.; I decl.)", t: "gloria" },
            { p: "res publica", t: "stato" },
            { p: "Caesar, -is (m.; III decl.)", t: "Cesare" },
            { p: "equitatus, -us (m.; IV decl.)", t: "cavalleria" },
            { p: "iter, itineris (n.; III decl.)", t: "viaggio" },
            { p: "impetus, -us (m.; IV decl.)", t: "impeto" },
            { p: "vox, vocis (f.; III decl.)", t: "voce" },
            { p: "ferrum, -i (n.; II decl.)", t: "ferro; spada" },
            { p: "ignis, -is (m.; III decl.)", t: "fuoco" },
            { p: "genus, -eris (n.; III decl.)", t: "genere" },
            { p: "officium, -i (n.; II decl.)", t: "dovere" },
            { p: "epistula, -ae (f.; I decl.)", t: "epistola" },
            { p: "nox, noctis (f.; III decl.)", t: "notte" },
            { p: "imperator, -oris (m.; III decl.)", t: "comandante" },
            { p: "miles, -itis (m.; III decl.)", t: "soldato" },
            { p: "legio, -onis (f.; III decl.)", t: "legione" },
            { p: "proelium, -i (n.; II decl.)", t: "battaglia" },
            { p: "regnum, -i (n.; II decl.)", t: "regno" },
            { p: "matrimonium, -i (n.; II decl.)", t: "matrimonio" },
            { p: "legatus, -i (II decl.)", t: "ambasciatore" },
            { p: "frater, fratris (m.; III decl.)", t: "fratello" },
            { p: "consul, -is (m.; III decl.)", t: "console" },
            { p: "Cicero, -onis (m.; III decl.)", t: "Cicerone" },
            { p: "Hannibal, is (m.; III decl.)", t: "Annibale" },
            { p: "opera, -ae (f.; I decl.)", t: "opera" },
            { p: "vir, viri (m.; II decl.)", t: "uomo" },
            { p: "verbum, -i (n.; II decl.)", t: "parola" },
            { p: "ars, artis (f.; III decl.)", t: "arte, tecnica" },
            { p: "tempus, -oris (n.; III decl.)", t: "tempo" },
            { p: "ager, agri (m.; II decl.)", t: "campo" },
            { p: "oratio, -onis (f.; III decl.)", t: "discorso" },
            { p: "virtus, -utis (f.; III decl.)", t: "valore" },

            // PRONOMI
            { p: "ego, mei", t: "io" },
            { p: "tu, tui", t: "tu" },
            { p: "is, ea, id", t: "egli/lui, ella/lei, esso" },
            { p: "hic, haec, hoc", t: "questo" },
            { p: "ille, illa, illud", t: "quello" },
            { p: "sui, sibi", t: "sè" },
            { p: "qui, quae, quod", t: "che / quale" },
            { p: "quis, quid", t: "chi? che cosa?" },
            { p: "nemo, neminis", t: "nessuno" },

            // AGGETTIVI
            { p: "facilis, -e (II classe)", t: "facile" },
            { p: "omnis, -e (II classe)", t: "ogni, tutto" },
            { p: "aegrotus, -a, -um (I classe)", t: "malato" },
            { p: "felix, -icis (II classe)", t: "felice, fortunato" },
            { p: "bonus, -a, -um (I classe)", t: "buono, migliore, ottimo" },
            { p: "dulcis, -e (II classe)", t: "dolce" },
            { p: "doctus, -a, -um (I classe)", t: "dotto" },
            { p: "nullus, -a, -um", t: "nessuno" },
            { p: "verus, -a, -um (I classe)", t: "vero" },
            { p: "alius, -a, -ud", t: "altro (fra molti)" },
            { p: "alter, -a, -um", t: "altro (fra due)" },
            { p: "Romanus, -a, -um", t: "romano" },
            { p: "multus, -a, -um (I classe)", t: "molto" },
            { p: "odiosus, -a, -um (I classe)", t: "odioso" },
            { p: "utilis, -e (II classe)", t: "utile" },
            { p: "pauper, -eris (II classe)", t: "povero" }
        ];

        let indice = 0;

        // Funzione per mescolare l'array
        function shuffle(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
        }

        function aggiorna() {
            const card = document.getElementById('flashcard');
            card.classList.remove('flipped');
            
            const current = vocaboli[indice];
            // Prendi solo la prima parola prima della virgola
            const fronte = current.p.split(',')[0].trim();
            
            document.getElementById('card-front').innerText = fronte;
            document.getElementById('card-back').innerHTML = `
                <div style="font-size: 0.9rem; color: #666; margin-bottom: 10px;">Paradigma:</div>
                <strong>${current.p}</strong>
                <hr style="width: 60%; margin: 15px auto;">
                <div style="color: #1a73e8; font-style: italic;">${current.t}</div>
            `;
            
            document.getElementById('counter').innerText = `Card ${indice + 1} di ${vocaboli.length}`;
        }

        function nextCard() {
            indice = (indice + 1) % vocaboli.length;
            aggiorna();
        }

        function prevCard() {
            indice = (indice - 1 + vocaboli.length) % vocaboli.length;
            aggiorna();
        }

        function shuffleAndReset() {
            shuffle(vocaboli);
            indice = 0;
            aggiorna();
        }

        // Inizio: mescola subito all'apertura e mostra la prima
        shuffle(vocaboli);
        aggiorna();
    </script>
</body>
</html>
