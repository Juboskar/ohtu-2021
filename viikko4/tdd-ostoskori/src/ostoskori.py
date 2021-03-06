from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.__ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return sum([o.lukumaara() for o in self.__ostokset])
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return sum([o.hinta() for o in self.__ostokset])
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        for o in self.__ostokset:
            if o.tuotteen_nimi() == lisattava.nimi():
                o.muuta_lukumaaraa(1)
                break
        else:
            self.__ostokset.append(Ostos(lisattava))
        # lisää tuotteen
        

    def poista_tuote(self, poistettava: Tuote):
        for o in self.__ostokset:
            if o.tuotteen_nimi() == poistettava.nimi():
                o.muuta_lukumaaraa(-1) if o.lukumaara() > 1 else self.__ostokset.remove(o)
                break

    def tyhjenna(self):
        self.__ostokset = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.__ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
