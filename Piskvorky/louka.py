barva_travy = "zelena"
pocet_kotatek = 28

def popis_stav():
    return "trava je {barva}. Prohani se po ni {pocet} kotatek.".format(
        barva=barva_travy, pocet=pocet_kotatek)
