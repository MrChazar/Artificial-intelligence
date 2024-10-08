% Fakty
kobieta(anna).
kobieta(monika).
kobieta(ewa).
kobieta(kasia).

mezczyzna(jan).
mezczyzna(piotr).
mezczyzna(marek).

% Przyk³adowo anna jest matka moniki
matka(anna, monika).
matka(ewa, piotr).
matka(kasia, marek).
matka(kasia, ewa).

% Przyk³adowo Jan jest ojcem moniki
ojciec(jan, monika).
ojciec(marek, piotr).
ojciec(piotr, jan).
ojciec(piotr, anna).

% a)
% Regu³y
% Sprawdzi czy X jest córk¹ Y
corka(X, Y) :- kobieta(X), (matka(Y, X); ojciec(Y, X)).
% Sprawdzi czy X jest synem Y
syn(X, Y) :- mezczyzna(X), (matka(Y, X); ojciec(Y, X)).

% b)
% Dziadek to ojciec rodzica:
dziadek(X, Y) :- ojciec(X, Z), (ojciec(Z, Y); matka(Z, Y)).

% Babcia to matka rodzica:
babcia(X, Y) :- matka(X, Z), (ojciec(Z, Y); matka(Z, Y)).

% Wnuk to mê¿czyzna, który jest dzieckiem dziecka:
wnuk(X, Y) :- mezczyzna(X), (ojciec(Y, Z); matka(Y, Z)), (ojciec(Z, X); matka(Z, X)).

% Wnuczka to kobieta, która jest dzieckiem dziecka:
wnuczka(X, Y) :- corka(X, Z), (syn(Z, Y); corka(Z, Y)).


