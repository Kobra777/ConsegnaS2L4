import math


def calcolaPerimetri():
    print("Scegli la figura geometrica per calcolare il perimetro:")
    print("1. Quadrato")
    print("2. Cerchio")
    print("3. Rettangolo")

    scelta = input("scelta: ")

    match scelta:
        case "1":
            lato = float(input("Inserisci il lato del quadrato: "))
            perimetro = lato * 4
            print(f"Il perimetro del quadrato è: {perimetro}")

        case "2":
            raggio = float(input("Inserisci il raggio del cerchio: "))
            perimetro = 2 * math.pi * raggio
            print(f"La circonferenza del cerchio è: {perimetro}")

        case "3":
            base = float(input("Inserisci la base del rettangolo: "))
            altezza = float(input("Inserisci l'altezza del rettangolo: "))
            perimetro = 2 * (base + altezza)
            print(f"Il perimetro del rettangolo è: {perimetro}")

        case _:
            print("Scelta non valida. Riprova.")

calcolaPerimetri()
