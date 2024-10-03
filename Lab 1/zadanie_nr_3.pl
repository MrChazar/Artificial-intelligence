% Fakty
kobieta(anna).
kobieta(monika).
mezczyzna(jan).
mezczyzna(piotr).

% Negacja - sprawdzenie czy kto� nie jest kobiet�
nie_kobieta(X) :- not(kobieta(X)).

% Nier�wno�� - sprawdzenie czy dwie osoby s� r�ne
nie_tacy_sami(X, Y) :- X \= Y.

% Ci�cie - przyk�ad sprawdzania wieku, kt�re po znalezieniu wyniku ko�czy przeszukiwanie
wiek(jan, 30).
wiek(anna, 25).

sprawdz_wiek(X, Wiek) :- wiek(X, Wiek), !.

% Ci�g dalszy przetwarzania, gdy pierwsza regu�a dla wieku nie by�a spe�niona
sprawdz_wiek(_, 'wiek nieznany').
