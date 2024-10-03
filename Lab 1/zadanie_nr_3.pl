% Fakty
kobieta(anna).
kobieta(monika).
mezczyzna(jan).
mezczyzna(piotr).

% Negacja - sprawdzenie czy ktoœ nie jest kobiet¹
nie_kobieta(X) :- not(kobieta(X)).

% Nierównoœæ - sprawdzenie czy dwie osoby s¹ ró¿ne
nie_tacy_sami(X, Y) :- X \= Y.

% Ciêcie - przyk³ad sprawdzania wieku, które po znalezieniu wyniku koñczy przeszukiwanie
wiek(jan, 30).
wiek(anna, 25).

sprawdz_wiek(X, Wiek) :- wiek(X, Wiek), !.

% Ci¹g dalszy przetwarzania, gdy pierwsza regu³a dla wieku nie by³a spe³niona
sprawdz_wiek(_, 'wiek nieznany').
