from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from tekoaly_parannettu import TekoalyParannettu
from tekoaly import Tekoaly


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            peli = KPSPelaajaVsPelaaja()
        elif vastaus.endswith("b"):
            peli = KPSTekoaly(Tekoaly())
        elif vastaus.endswith("c"):
            peli = KPSTekoaly(TekoalyParannettu(10))
        else:
            break
        peli.pelaa()
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")


if __name__ == "__main__":
    main()
