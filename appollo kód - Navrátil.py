# =============================================================
# MISE APOLLO 11 - PROGRAMOVACÍ VÝZVA
# =============================================================
# Tvůj kód pro lunární modul Eagle
# =============================================================

def vypocet_vahy(vaha_na_zemi, teleso="mesic"):
    """
    Vypočítá váhu astronauta na jiném tělese.
    Měsíc: 16.5 % váhy na Zemi (koeficient 0.165)
    Mars: 38 % váhy na Zemi (koeficient 0.38)
    """
    # Kontrola záporné váhy
    if vaha_na_zemi < 0:
        print("Varování: Váha nemůže být záporná!")
        return 0
    
    # Výpočet podle konkrétního tělesa
    if teleso == "mesic":
        vysledek = vaha_na_zemi * 0.165
    elif teleso == "mars":
        vysledek = vaha_na_zemi * 0.38
    else:
        print("Neznámé těleso. Vracím pozemskou váhu.")
        vysledek = vaha_na_zemi
        
    return vysledek


def simulator_pristani():
    """
    Simulátor přistání modulu na povrchu Měsíce.
    """
    vyska = 100       # počáteční výška v metrech
    rychlost = 10     # počáteční rychlost klesání (m/s)
    palivo = 50       # jednotky paliva
    gravitace = 2     # kolik rychlosti přibude každou sekundu pádem
    
    print("\n--- ZAČÍNÁ PŘISTÁVACÍ MANÉVR ---")
    
    # Cyklus běží, dokud jsme nad povrchem
    while vyska > 0: 
        print(f"Výška: {vyska}m | Rychlost: {rychlost}m/s | Palivo: {palivo}j")
        
        # Získání vstupu s ochranou proti chybnému zadání (kdyby uživatel napsal text)
        try:
            zazeh = int(input("Síla zážehu (0-10): "))
        except ValueError:
            print("Chyba: Musíš zadat celé číslo!")
            zazeh = 0
            
        # Omezení hodnoty zážehu, aby nedával nesmysly
        if zazeh < 0:
            zazeh = 0
        elif zazeh > 10:
            zazeh = 10
            
        # Ošetření stavu paliva (nesmí jít do mínusu)
        if zazeh > palivo:
            zazeh = palivo
            print("POZOR: Dochází palivo! Byl použit pouze zbytek v nádrži.")
        
        # Odečtení použitého paliva
        palivo -= zazeh
        
        # --- FYZIKÁLNÍ VÝPOČET ---
        # Rychlost se zvyšuje o gravitaci a snižuje o sílu zážehu
        rychlost = rychlost + gravitace - zazeh
        # Výška se snižuje o aktuální rychlost
        vyska -= rychlost
        
        print("-" * 20)

    # --- VYHODNOCENÍ ---
    print(f"\nDopadová rychlost: {rychlost} m/s")
    
    # Podmínka pro úspěch mise
    if rychlost < 5:
        print("Výsledek mise: PŘISTÁNÍ ÚSPĚŠNÉ! Houston, tady základna Tranquility. Orel přistál. 🦅🌔")
    else:
        print("Výsledek mise: KATASTROFA! Modul narazil do povrchu a havaroval. 💥")


# === HLAVNÍ PROGRAM ===
moje_vaha = 80
print(f"Moje váha na Měsíci: {vypocet_vahy(moje_vaha, 'mesic')} kg")
print(f"Moje váha na Marsu: {vypocet_vahy(moje_vaha, 'mars')} kg")

# Odkomentuj řádek níže pro spuštění hry
# simulator_pristani()