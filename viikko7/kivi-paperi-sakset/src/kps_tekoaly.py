from kps import KPS


class KPSTekoaly(KPS):
    def __init__(self, tekoaly):
        super().__init__()
        self.tekoaly = tekoaly

    def _toisen_siirto(self):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self.tekoaly.aseta_siirto(self.ekan_siirto)
        return siirto
