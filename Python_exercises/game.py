print("Es ist Halloween und du hast noch kein Kostüm.")
print("Nachdem die Panik abebbt, ")

kostüm = input("Was machst du? [zwei Löcher in ein Bettlaken schneiden / zuhause bleiben ]")
if kostüm == "zuhause bleiben":
    print("Du langweiler. Dann gehe halt ins Bett.")
elif kostüm == "zwei Löcher in ein Bettlaken schneiden":
    print("Du ziehst dir den alten Laken an und gehst raus zum Trick or Treaten.")
    print("Auf dem Weg nach draußen siehst du deinen Erzfeind, Kevin.")
    print("Er erkennt dich nicht und läuft an dir vorbei Richtung Park.")
    kevin = input("Was machst du? [Trick or Treaten / Kevin folgen / Kevin beim vorbeigehen schlagen]")
    if kevin == "Trick or Treaten":
        print("Du läufst den ganzen Abend rum und sammelst lauter Süssigkeiten.")
        print("Zuhause isst du sie auf. Dir ist danach schlecht.")
        print("Wie jedes Jahr.")
    elif kevin == "Kevin beim vorbeigehen schlagen":
        print("Kevin schlägt zurück.")
        print("Deine Nase blutet. Dein Kostüm ist ruiniert.")
        print("Jetzt kannst du wieder nach Hause gehen.")
        print("Gewalt ist halt nie eine Lösung, Dummkopf.")
    elif kevin == "Kevin folgen":
        print("Du schleichst hinter Kevin her.")
        print("Plötzlich bleibt Kevin aber stehen.")
        print("Er dreht sich um und schaut dich genau an.")
        print("Dann schreit er: 'Ahhh! Ein Geist!'")
        geist = input("Was machst du? [davon rennen / Booh schreien ]")
        if geist == "davon rennen":
            print("Am nächsten Tag liest du in der Zeitung:")
            print("Mann im Park von Geist zu Tode erschreckt.")
            print("Phew. Da hast du aber noch mal Glück gehabt.")
            print("Deine Feigheit hat dir das Leben gerettet.")
        elif geist == "Booh schreien":
            print("Kevin wird ganz blass und fällt tod um.")
            print("Du hast aber keine Zeit dich zu freuen, denn hinter dir hörst du ein Geräusch.")
            print("Du drehst dich um und siehst das krasseste Geist aller Zeiten.")
            print("In echt.")
        else:
            print("Tja, du hattest wohl so Angst, dass nicht mehr wusstest welche Optionen du hattest.")
            print("Deswegen hat dich der Geist erwischt.")
            print("Jetzt bist du tot.")
            print("Nächstes Mal solltest du besser aufpassen.")
    else:
        print("Das war keine gültige Option.")
        print("Du bleibst also wie ein Blöder stehen.")
        print("Auf immer und ewig.")
else:
    print("Wie du spielst nicht mit? Schade!")
