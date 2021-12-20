from kps import KPS


class KPSPelaajaVsPelaaja(KPS):
    def __init__(self):
        super().__init__()

    def _toisen_siirto(self):
        # metodin oletustoteutus
        return input("Toisen pelaajan siirto: ")
