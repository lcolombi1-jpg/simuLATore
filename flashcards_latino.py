import re
import random

# Inseriamo una parte del testo che hai fornito come esempio
# In un caso reale, potresti leggere questo testo da un file .txt
testo_lessico = """
(20) ācer -acris -acre agg. [*hek- "punta"]: acuto, acre, pungente
ăcẽo -cũi -ēre 2 intr. [*h2ek- "punta"]: essere acido
ăciēs -ēi f. [*h2ek- "punta"]: punta, spada, acutezza
ăcus' -ūs f. [acer²]: ago
ăcūtus-a-um agg. [acuo]: aguzzo, acuto, pungente
"""

def crea_flashcards(testo):
    flashcards = []
    
    # Questa espressione regolare cerca:
    # 1. Il lemma e il paradigma (tutto ciò che precede la parentesi quadra '[')
    # 2. Salta l'etimologia tra parentesi quadre
    # 3. Prende la traduzione dopo i due punti ':'
    schema = re.compile(r"([^(]+)\s+\[.*?\]:\s+(.*)")

    linee = testo.strip().split('\n')
    
    for linea in linee:
        # Pulizia: rimuoviamo i numeri tra parentesi come (20) all'inizio
        linea_pulita = re.sub(r"\(\d+\)", "", linea).strip()
        
        match = schema.search(linea_pulita)
        if match:
            info_latina = match.group(1).strip() # Es: "ācer -acris -acre agg."
            traduzione = match.group(2).strip() # Es: "acuto, acre, pungente"
            
            # Dividiamo la parte latina per isolare il primo elemento
            parti_latine = info_latina.split()
            fronte = parti_latine[0] # Il primo elemento (nominativo o prima persona)
            retro = f"{info_latina} | Traduzione: {traduzione}"
            
            flashcards.append({"fronte": fronte, "retro": retro})

    # Mescoliamo l'ordine in modo casuale
    random.shuffle(flashcards)
    return flashcards

# Esecuzione del programma
lista_flashcards = crea_flashcards(testo_lessico)

print(f"--- GENERATORE DI FLASHCARDS LATINE ---")
print(f"Trovate {len(lista_flashcards)} parole.\n")

for i, card in enumerate(lista_flashcards, 1):
    print(f"FLASHCARD {i}")
    print(f"FRONTE: {card['fronte']}")
    print(f"RETRO: {card['retro']}")
    print("-" * 30)
