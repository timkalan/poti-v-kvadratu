"""
Hm.
"""
# za 3D risanje
from mpl_toolkits.mplot3d import Axes3D 

import random
# osnovna knjižnica za risanje
import matplotlib.pyplot as plt

# prednostna vrsta
from queue import PriorityQueue


# računanje evklidske razdalje, za vsak slučaj dela v R ** n
def razdalja(tocka0, tocka1):
    razdalja = 0
    for i in range(len(tocka0)):
        dx = tocka0[i] - tocka1[i]
        razdalja += dx ** 2

    return razdalja ** (1/2)


class Kvadrat:
    """
    V enotskem kvadratu generiramo točke in opazujemo drevesa najkrjajših 
    poti v grafih, ki jih razpenjajo.
    """

    def __init__(self, st_tock, max_razdalja):
        """
        st_tock = število točk v enotskem kvadratu 
        """
        self.st_tock = st_tock
        self.max_razdalja = max_razdalja
        
        # generiramo vse potrebne točke, shranimo kot seznam naborov
        tocke = []
        for _ in range(st_tock):
            # morda lahko eksperimentiramo z različnimi porazdelitvami
            x, y = random.uniform(0, 1), random.uniform(0, 1)
            tocke.append((x, y))
        self.tocke = tocke

    
    def bliznje(self):
        """
        Vrne slovar oblike {točka: seznam točk, ki so dovolj blizu}. To
        hkrati služi kot graf v obliki seznama sosedov.
        """
        bliznje = dict()
        for koren in self.tocke:
            ustrezne = []   # seznam točk, ki so dovolj blizu
            for sosed in self.tocke:
                if koren == sosed:
                    # v seznam ne dodamo točke same
                    pass

                elif razdalja(koren, sosed) <= self.max_razdalja:
                    ustrezne.append(sosed)
            
            bliznje[koren] = ustrezne
        return bliznje


    def dosezena(self, koren=0):
        pass


    def drevo_najkrajsih_poti(self, koren=0):
        """
        Uporabi Dijkstrov algoritem za izračun drevesa najkrajših poti
        od dane točke. 

        koren = začetna točka, podana kot zaporedna številka (začnemo z 0)
        """
        # za vsako točko dobimo njene sosede
        seznam_sosedov = self.bliznje()
        
        # koreni so vse točke ki so si dovolj blizu
        koreni = list(seznam_sosedov.keys())

        # pogledamo, če smo si izbrali ustrezen koren
        try:
            root = koreni[koren]
            self.root = root         # zabeležimo, kaj je koren (za vizualizacijo)
        except IndexError as e:
            print("Premalo korenov!")
            print(e)
            
        # dejanski začetek Dijkstrovega algoritma - še ni prednostne vrste
        Q = []
        oddaljenost = dict()
        oce = dict()

        for vozlisce in seznam_sosedov:
            oddaljenost[vozlisce] = 1000000        # praktično neskončno za naše namene
            oce[vozlisce] = None
            Q.append(vozlisce)
        oddaljenost[root] = 0

        while Q != []:
            # določimo vozlišče z minimalno oddaljenostjo, ki je še v Q
            u = min({vozl: razd for (vozl, razd) in oddaljenost.items() 
                if vozl in Q}, key=oddaljenost.get)
            Q.remove(u)    # odstranimo iz seznama

            # pregledamo vse sosede opazovanega vozlišča, ki so še v Q
            for sosed in [nei for nei in seznam_sosedov[u] if nei in Q]:
                alt = oddaljenost[u] + razdalja(u, sosed)
                if alt < oddaljenost[sosed]:
                    oddaljenost[sosed] = alt
                    oce[sosed] = u

        return oddaljenost, oce


    def drevo_najkrajsih_poti_hitro(self, koren=0):
        """
        Uporabi Dijkstrov algoritem za izračun drevesa najkrajših poti
        od dane točke. Izvajaje je pohitreno s pomočjo prednostne vrste.

        koren = začetna točka, podana kot zaporedna številka (začnemo z 0)
        """
        # za vsako točko dobimo njene sosede
        seznam_sosedov = self.bliznje()
        
        # koreni so vse točke ki so si dovolj blizu
        koreni = list(seznam_sosedov.keys())

        # pogledamo, če smo si izbrali ustrezen koren
        try:
            root = koreni[koren]
            self.root = root         # zabeležimo, kaj je koren (za vizualizacijo)
        except IndexError as e:
            print("Premalo korenov!")
            print(e)
            
        # dejanski začetek Dijkstrovega algoritma - še ni prednostne vrste
        Q = PriorityQueue()
        oddaljenost = dict()
        oce = dict()

        for vozlisce in seznam_sosedov:
            if vozlisce != root:
                oddaljenost[vozlisce] = 1000000        # praktično neskončno za naše namene
                oce[vozlisce] = None

            prioriteta = oddaljenost.get(vozlisce)
            Q.put((prioriteta, vozlisce))

        oddaljenost[root] = 0

        while not Q.empty():
            # določimo vozlišče z minimalno oddaljenostjo, ki je še v Q
            u = Q.get()   # odstranimo iz seznama in vrnemo najboljšega

            # pregledamo vse sosede opazovanega vozlišča, ki so še v Q
            for sosed in [nei for nei in seznam_sosedov[u] if nei in Q]:
                alt = oddaljenost[u] + razdalja(u, sosed)
                if alt < oddaljenost[sosed]:
                    oddaljenost[sosed] = alt
                    oce[sosed] = u

        return oddaljenost, oce
    
    
################################## VIZUALIZACIJA ########################################
    

    def narisi_tocke(self):
        """
        Nariše naše generirane točke v enotskem kvadratu.
        """
        # *zip(*seznam_parov) pomeni unzip: vrne dva seznama, in ju da kot dva argumenta
        # za plt.scatter -> x in y
        plt.scatter(*zip(*self.tocke))

        
    
    def narisi_bliznje(self, tocka=0):
        """
        Nariše vse dovolj bližnje točke dane točke.
        
        tocka = zaporedno število točke v slovarju sosedov
        """
        bliznje = self.bliznje()          # da ne računamo tega dvakrat
        
        # povedati moramo, katero točko smo si izbrali
        koren = list(bliznje.keys())[tocka]
        
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        try:
            # *zip(*seznam_parov) pomeni unzip: vrne dva seznama, in ju da kot dva argumenta
            # za plt.scatter -> x in y
            plt.scatter(*zip(*bliznje[koren]))
        except:
            print('Nimamo bližnjih točk!')


    def narisi_okolico(self, tocka=0):
        """
        Nariše krožnico, ki predstavlja okolico dane točke, znotraj katere so točke, 
        s katerimi se bo ta povezala.

        tocka = zaporedno število točke v slovarju sosedov
        """
        # naša izbrana točka, v obliki (x, y)
        koren = list(self.bliznje().keys())[tocka]

        # narišemo krog s središčem v korenu in radijem max_razdalja
        plt.gcf().gca().add_artist(plt.Circle(koren, self.max_razdalja, fill=False))
            
    
    def narisi_graf_tocke(self, tocka=0):
        """
        Nariše graf, ki ga generira posamezna točka in njej dovolj bližnje točke.
        """
        # določimo bližnje točke in naš koren
        bliznje = self.bliznje()
        koren = list(bliznje.keys())[tocka]
        
        # pogledamo vse bližnje točke korena
        for x, y in bliznje[koren]:
            x0, x1 = koren[0], x
            y0, y1 = koren[1], y
            plt.plot([x0, x1], [y0, y1], color='black')
            
    
    def narisi_graf(self):
        """
        Nariše graf, ki je generiran s parametrom max_razdalja. To je naša osnova 
        za iskanje drevesa najkrajših poti.
        """
        # sprehodimo se čez vse točke in uporabimo zgornjo funkcijo
        for i in range(len(self.tocke)):
            self.narisi_graf_tocke(i)

    
    def narisi_dosezena(self, koren=0):
        """
        Označi voslišča, ki smo jih dosegli iz našega vozlišča.
        """
        pass
            
            
    def narisi_drevo(self, koren=0):
        """
        Nariše drevo najkrajših poti, ki se začne v izbranem korenu.
        """
        _, oce = self.drevo_najkrajsih_poti(koren)
        
        # narišemo koren - zorder prisili, da je narisan kot vrhnji element grafa
        plt.scatter(self.root[0], self.root[1], marker='s', color='#FF0000', zorder=1000000)
        
        # pregledamo slovar očetov
        for pred, nasl in oce.items():
            # če ima 'sina', ga narišemo
            if nasl != None:
                x0, x1 = pred[0], nasl[0]
                y0, y1 = pred[1], nasl[1]
                plt.plot([x0, x1], [y0, y1], color='#23FF00')



class Kocka(Kvadrat):
    """
    Razred 'Kvadrat' preselimo v tri dimenzije.
    """

    def __init__(self, st_tock, max_razdalja, n_dim=3):
        """
        st_tock = število točk v enotskem kvadratu 
        """
        self.st_tock = st_tock
        self.max_razdalja = max_razdalja
        
        # generiramo vse potrebne točke, shranimo kot seznam naborov
        tocke = []
        for _ in range(st_tock):
            tocka = [random.uniform(0, 1) for _ in range(n_dim)]
            tocke.append(tuple(tocka))
        self.tocke = tocke

    
    def narisi_tocke(self):
        """
        Nariše naše generirane točke v enotskem kvadratu.
        """
        # *zip(*seznam_parov) pomeni unzip: vrne dva seznama, in ju da kot dva argumenta
        # za plt.scatter -> x in y

        fig = plt.figure()
        ax = Axes3D(fig)

        x, y, z = zip(*self.tocke)
        ax.scatter(x, y, z)
    

    #TODO: ne dela for some reason
    def narisi_bliznje(self, tocka=0):
        """
        Nariše vse dovolj bližnje točke dane točke.
        
        tocka = zaporedno število točke v slovarju sosedov
        """
        bliznje = self.bliznje()          # da ne računamo tega dvakrat
        
        # povedati moramo, katero točko smo si izbrali
        koren = list(bliznje.keys())[tocka]

        try:
            # *zip(*seznam_parov) pomeni unzip: vrne dva seznama, in ju da kot dva argumenta
            # za plt.scatter -> x in y
            x, y, z = zip(*self.tocke)
            Axes3D.scatter(x, y, z)
        except:
            print('Nimamo bližnjih točk!')


    def narisi_graf_tocke(self, tocka=0):
        """
        Nariše graf, ki ga generira posamezna točka in njej dovolj bližnje točke.
        """
        # določimo bližnje točke in naš koren
        bliznje = self.bliznje()
        koren = list(bliznje.keys())[tocka]
        
        # pogledamo vse bližnje točke korena
        for x, y, z in bliznje[koren]:
            x0, x1 = koren[0], x
            y0, y1 = koren[1], y
            z0, z1 = koren[2], z
            plt.plot([x0, x1], [y0, y1], [z0, z1], color='black')


    def narisi_drevo(self, koren=0):
        """
        Nariše drevo najkrajših poti, ki se začne v izbranem korenu.
        """
        _, oce = self.drevo_najkrajsih_poti(koren)

        # narišemo koren - zorder prisili, da je narisan kot vrhnji element grafa
        plt.plot(self.root[0], self.root[1], self.root[2], marker='s', color='#FF0000', zorder=1000000)
        
        # pregledamo slovar očetov
        for pred, nasl in oce.items():
            # če ima 'sina', ga narišemo
            if nasl != None:
                x0, x1 = pred[0], nasl[0]
                y0, y1 = pred[1], nasl[1]
                z0, z1 = pred[2], nasl[2]
                plt.plot([x0, x1], [y0, y1], [z0, z1], color='#23FF00')



# TODO: dijkstra na bolj učinkovit način
# TODO: razmisli, če lahko na učinkovit način implemetiraš bliznje
# TODO: morda kakšne animacije, če se to da
# TODO: 3D
# TODO: da se nariše katera vozlišča so dosežena in katera ne - morda računa razmerje
# TODO: oznake na osi