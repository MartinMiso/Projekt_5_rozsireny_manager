"""
main.py: čtvrtý projekt do Engeto Online Python Akademie
##################
---TASK MANAGER---
##################
author: Martin Mišo
email: martin.miso@seznam.cz
"""

"""
Přehled názvů nuik


Tento program slouží jako jednoduchý správce úkolů, který umožňuje uživateli:
- Přidávat nové úkoly s názvem a popisem.
- Zobrazovat seznam všech úkolů ve formě přehledné tabulky.
- Odstraňovat úkoly podle čísla nebo názvu s následným přečíslováním.
- Ukládat seznam úkolů do textového souboru před ukončením programu.
"""

def hlavni_menu():
    """
    Účel: Zobrazení hlavního menu s nadpisem a volbami.
    Chování: Vypíše nadpis, podtržení a nabídku možností
    (1. Přidat úkol,
    2. Zobrazit všechny úkoly,
    3. Odstranit úkol,
    4. Konec programu).
    """
    nadpis = "Správce úkolů - Hlavní menu"
    print(nadpis)
    podtrzeni = (len(nadpis) * "-")
    print(podtrzeni)
    print("1. Přidat úkol",
          "\n2. Zobrazit všechny úkoly",
          "\n3. Odstranit úkol",
          "\n4. Konec programu"
          )


def pridat_ukol():
    """
    Účel: Přidání nového úkolu.
    Vstupy: Uživatel zadá název a popis úkolu.
    Zpracování: Pokud alespoň jeden z údajů není prázdný, vytvoří se slovník s klíči `
    "Číslo"`, `"Název"` a `"Popis"` a úkol se přidá do seznamu `ukoly`.
    Výstup: Informace o přidaném úkolu se vypíše na obrazovku.
    """
    print("Přidání úkolu:")
    while True:
        ukol_nazev = (input("Zadej název úkolu: "))
        ukol_popis = (input("Zadej popis úkolu: "))

        if ukol_nazev != "" and ukol_popis != "":
            id_ukolu = len(ukoly) + 1
            ukol = {"Číslo": id_ukolu, "Název": ukol_nazev, "Popis": ukol_popis}
            ukoly.append(ukol)
            print(f"Úkol '{ukol_nazev}' byl přidán.")
            break
        else:
            print("Nezadal jsi název nebo popis úkolu.")


def zobrazit_ukoly():
    """
    Účel: Zobrazení všech aktuálně přidaných úkolů.
    Zpracování: Pokud je seznam `ukoly` prázdný, vypíše se zpráva o neexistenci úkolů.
    Jinak se vypíše formátovaná tabulka obsahující číslo, název a popis každého úkolu.
    Výstup: Seznam úkolů ve formě tabulky.
    """
    if not ukoly:
        print("Žádné úkoly nejsou přidány.")
        return

    print("\n SEZNAM ÚKOLŮ")
    print("=" * 50)
    print(f"{'Číslo':<5} {'Název':<20} {'Popis'}")
    print("-" * 50)

    for ukol in ukoly:
        print(f"{ukol['Číslo']:<5} {ukol['Název']:<20} {ukol['Popis']}")

    print("=" * 50)

def odstranit_ukol():
    """
    Účel: Odstranění úkolu podle čísla nebo názvu.
    Vstupy: Uživatel zadá číslo nebo název úkolu, který chce odstranit.
    Zpracování: Prohledá se seznam úkolů a pokud se najde shoda, úkol se odstraní a následně se přečíslují zbývající úkoly.
    Výstup: Zpráva o úspěšném odstranění nebo upozornění, že úkol nebyl nalezen.
    """
    ukol_odstraneni = input("Zadej číslo nebo název úkolu k odstranění: ")
    nalezeno = False
    for ukol in ukoly:
        if str(ukol["Číslo"]) == ukol_odstraneni or ukol["Název"] == ukol_odstraneni:
            ukoly.remove(ukol)
            print(f"Úkol {ukol['Název']} byl smazán.")
            nalezeno = True
            break
    if not nalezeno:
        print(f"Úkol '{ukol_odstraneni}' nenalezen.")

    for index, ukol in enumerate(ukoly):
        ukol["Číslo"] = index + 1

def ulozeni_ukolu():
    """
    Účel: Uložení aktuálního seznamu úkolů do souboru.
    Vstupy: Globální proměnná `nazev_souboru` obsahující jméno souboru zadané uživatelem.
    Zpracování: Otevře se textový soubor v režimu zápisu a každý úkol se zapíše na jeden řádek ve formátované podobě.
    Výstup: Soubor s uloženým seznamem úkolů.
    """
    with open(f"{nazev_souboru}.txt", "w", encoding="utf-8") as seznam_ukolu:
        seznam_ukolu.write(f"{'Číslo':<5} {'Název':<20} {'Popis'}\n")
        for ukol in ukoly:
            radek = (f"{ukol['Číslo']:<5} {ukol['Název']:<20} {ukol['Popis']}\n")
            seznam_ukolu.write(radek)

# Hlavní smyčka
"""
 Funkce: Program běží ve smyčce, kde se opakovaně zobrazí hlavní menu a vyčká se na volbu uživatele.
Volby:
 - 1: Spustí se funkce pro přidání úkolu.
 - 2: Spustí se funkce pro zobrazení úkolů.
 - 3: Spustí se funkce pro odstranění úkolu.
 - 4: Vyvolá se vnořený cyklus, který se zeptá, zda má uživatel uložit seznam úkolů před ukončením programu. Podle odpovědi se seznam uloží či ne a následně se hlavní smyčka ukončí.
"""
ukoly = []
zakazane_znaky = ["-", "`", "/", ":", "*", "?", '"', "<", ">", "|", "`"]
if __name__ == '__main__':

    while True:
        hlavni_menu()
        moznost = (input(str("Vyberte možnost (1-4): ")))
        print()
        if moznost == "1":
            pridat_ukol()
            print()
        elif moznost == "2":
            zobrazit_ukoly()
            print()
        elif moznost == "3":
            zobrazit_ukoly()
            print()
            odstranit_ukol()
            print()
        elif moznost == "4":
            while True:
                ukonceni_vstup = input("Ukončuji program. Chceš uložit seznam úkolů? a/n ")
                if ukonceni_vstup == "a":
                    while True:
                        nazev_souboru = str(input("Zadej název souboru: "))
                        platny_nazev = True
                        for znak in zakazane_znaky:
                            if znak in nazev_souboru:
                                print(f"Neplatný název souboru. Název obsahuje zakázaný znak: '{znak}'")
                                platny_nazev = False
                                break
                        if platny_nazev:
                            ulozeni_ukolu()
                            print(f"Seznam úkolů uložen jako '{nazev_souboru}', ukončuji program.")
                            break
                    break
                elif ukonceni_vstup == "n":
                    break
                else:
                    print("Asi chceš seznam uložit, ale zadal jsi špatnou hodnotu. Rozmysli se znovu a zadej 'a' nebo 'b'.")
            break
        else:
            print("Nezadal jsi správnou hodnotu, zadej správnou volbu.")


""" KONEC """