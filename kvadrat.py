"""
Hm.
"""

import random
#import matplotlib.pyplot as plt


def razdalja(tocka0, tocka1):
    """
    Izračuna evklidsko razdaljo med danima točkama.
    """
    # potencialno spremeni, da dela v R^n
    dx = tocka0[0] - tocka1[0]
    dy = tocka0[1] - tocka1[1]
    return dx**2 + dy**2


class Kvadrat:
    """
    V enotskem kvadratu generiramo točke in opazujemo drevesa najkrjajših 
    poti v grafih, ki jih razpenjajo.
    """

    def __init__(self, st_tock):
        """
        st_tock = število točk v enotskem kvadratu, 
        razdalja = največja razdalja, da jih vseeno povežemo
        """
        self.st_tock = st_tock
        #self.max_razdalja = max_razdalja
        
        # generiramo vse potrebne točke, shranimo kot seznam naborov
        tocke = []
        for _ in range(st_tock):
            # morda lahko eksperimentiramo z različnimi porazdelitvami
            x, y = random.uniform(0, 1), random.uniform(0, 1)
            tocke.append((x, y))
        self.tocke = tocke

    
    def bliznje(self, max_razdalja):
        """
        Vrne slovar oblike točka: seznam točk, ki so dovolj blizu. To
        hjrati služi kot graf v obliki seznama sosedov.
        """
        bliznje = dict()
        for (x, y) in self.tocke:
            ustrezne = []   # seznam točk, ki so dovolj blizu
            for (a, b) in self.tocke:
                if (x, y) == (a, b):
                    # v seznam ne dodamo točke same
                    pass

                elif razdalja((x, y), (a, b)) <= max_razdalja:
                    ustrezne.append((a, b))
            
            bliznje[(x, y)] = ustrezne
        #self.koreni = list(bliznje.keys())      # grdo, da je to stranski učinek 
        return bliznje



    def drevo_najkrajsih_poti(self, max_razdalja, koren=0):
        """
        Uporabi Dijkstrov algoritem za izračun drevesa najkrajših poti
        od dane točke. 

        koren = začetna točka, podana kot zaporedna številka (začnemo z 0)
        """
        koreni = list(self.bliznje(max_razdalja).keys())
        seznam_sosedov = self.bliznje(max_razdalja)

        try:
            root = koreni[koren]
        except IndexError as e:
            print("Premalo korenov!")
            print(e)
            
        Q = []
        oddaljenost = dict()
        oce = dict()

        for vozlisce in seznam_sosedov:
            oddaljenost[vozlisce] = 1000000        # praktično neskončno za naše namene
            oce[vozlisce] = None
            Q.append(vozlisce)
        oddaljenost[root] = 0

        while Q != []:
            #u = min(oddaljenost, key=oddaljenost.get)    # vozlišče z min razdaljo
            u = min({vozl: razd for (vozl, razd) in oddaljenost.items() if vozl in Q}, key=oddaljenost.get)
            Q.remove(u)                           # odstranimo iz seznama

            for sosed in [nei for nei in seznam_sosedov[u] if nei in Q]:
                # pogledamo vse sosede u, ki so še v Q
                alt = oddaljenost[u] + razdalja(u, sosed)
                if alt < oddaljenost[sosed]:
                    oddaljenost[sosed] = alt
                    oce[sosed] = u

        return oddaljenost, oce




a = Kvadrat(500)
print(a.drevo_najkrajsih_poti(0.5))


# TODO: morda dijkstra na bolj učinkovit način
