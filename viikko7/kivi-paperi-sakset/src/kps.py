from tuomari import Tuomari


class KPS:
    def __init__(self):
        self.tuomari = Tuomari()
        self.ekan_siirto = "k"
        self.tokan_siirto = "k"

    def pelaa(self):
        while self._onko_ok_siirto(self.ekan_siirto) and self._onko_ok_siirto(self.tokan_siirto):
            self.ekan_siirto = self._ensimmaisen_siirto()
            self.tokan_siirto = self._toisen_siirto()
            self.tuomari.kirjaa_siirto(self.ekan_siirto, self.tokan_siirto)
            print(self.tuomari)

        print("Kiitos!")
        print(self.tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
