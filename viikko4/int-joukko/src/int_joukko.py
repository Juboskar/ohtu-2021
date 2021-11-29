
class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                return True
        return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            
            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.ljono)
            return True

        return False

    def poista(self, n):
        if self.kuuluu(n):
            self.ljono.remove(n)
            self.alkioiden_lkm -= 1
            return True
        return False



    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm
        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]
        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        for i in a.to_int_list() + b.to_int_list(): x.lisaa(i) 
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        s = f"{list(filter(lambda i: i !=0, self.ljono))}"
        return f"{{{s[1:-1]}}}"
