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

V datoteki `kvadrat.py` se nahaja razred `Kvadrat` v katerem so implemetirane vse 
ključne funkcije. razred `Kocka` si deli večino funkcionalnosti, le da se zadeva 
prestavi v tri dimenzije.

V datoteki `vizualizacija.ipynb` je prikazanih nekaj zmogljivosti razreda `Kvadrat`.
Tam so prikazane vse jederne funkcionalnosti, ki so (zaenkrat) implementirane. Seveda
so demonstrirane tudi funkcionalnosti razreda `Kocka`. 

V datoteki `izracuni.ipynb` so prikazani nekateri rezultati eksperimentov.