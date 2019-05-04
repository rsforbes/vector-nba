import re

def translate_playbyplay(text):
    #  "Vonleh 26' 3PT Jump Shot (3 PTS) (Knox 1 AST)"
    #  "Vonleh 26 foot. 3 point Jump Shot. Knox assist"
    text = text.replace("'"," foot")
    text = text.replace("PT", " point")
    text = text.replace("AST", " assist")
    text = text.replace("BLK", " assist")
    text = text.replace("P.Foul", "personal foul")
    text = text.replace("S.Foul", "shooting foul")
    text = text.replace("SUB", "substitution")
    text = text.replace("STL", " steals")
    #text = text.replace("MISS", "")

    print(text)
    return text
