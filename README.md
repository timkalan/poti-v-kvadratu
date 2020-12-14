# Najkrajše poti v enotskem kvadratu

Repozitorij je namenjem projektu pri predmetu Finančni praktikum v povezavi z
Operacijskimi raziskavami.

## Iztočnica

Consider a set P of n points in the unit square. Make a graph with vertex set P
and connecting any two points of P that are at distance at most r, where r is a
parameter. Consider a shortest path tree in the graph from one of the points of
P selected at random; the starting point is called the root. How does the length
of the shortest path tree change as n and/or r changes? How does the sum of the
distances from the root to all other vertices change?
You may consider it also in 3d.

## Struktura

V datoteki `koda/kvadrat.py` se nahaja razred `Kvadrat` v katerem so implemetirane vse 
ključne funkcije. razred `Kocka` si deli večino funkcionalnosti, le da se zadeva 
prestavi v tri dimenzije.

V datoteki `koda/vizualizacija.ipynb` je prikazanih nekaj zmogljivosti razreda `Kvadrat`.
Tam so prikazane vse jederne funkcionalnosti, ki se tičejo vizualizacije - risanja 
točk, grafov, dreves, ... Seveda so demonstrirane tudi funkcionalnosti razreda `Kocka`. 

V datoteki `koda/izracuni.ipynb` so prikazani rezultati eksperimentov. Večina jih je vključena 
tudi v poročilu.

Poročilo ima dve verziji: v `porocilo_dolgo.ipynb` je predstavjeno poročilo, in vsa izvorna koda, 
ki ga poganja. Je bolj nazorna verzija, iz katere lahko pridobimo tudi precej znanja in vpogled v 
celotni kodi. Hkrati to poročilo služi za namene predstavitve na ustnem zagovoru.
To poročilo potem prevedeno v `porocilo_kratko.pdf`, kjer je koda skrita. Poročilo je zato v 
tej verziji bolj strnjeno, a so prisotne tudi morebitne napake, ki so nastajale pri avtomatskem 
procesu prevajanja. Za tovrstne napake se opravičujemo. Prav tako so skriti vsi "nepovprečeni" grafi, 
zato so nekateri komentarji morda na prvi pogled malo čudno strukturirani. Zakritih je tudi nekaj drugih 
grafov, saj se zaradi velike količine vizualizacij nabere kar nekaj strani. Poročilo je vseeno 
nekoliko daljše, to pa je posledica tega, da smo se prvič srečali z izvažanjem Jupyter notebooka.
