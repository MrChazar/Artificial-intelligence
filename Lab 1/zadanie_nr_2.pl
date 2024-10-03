% Pierwszy ci¹g: f(n+1) = f(n) + f(n-1), f(0) = 1, f(1) = 1
f1(0, 1).  % f(0) = 1
f1(1, 1).  % f(1) = 1
f1(N, F) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    f1(N1, F1),
    f1(N2, F2),
    F is F1 + F2.

% Drugi ci¹g: f(n) = f(n+1) + f(n-2), f(0) = f(1) = f(2) = 2
f2(0, 2).  % f(0) = 2
f2(1, 2).  % f(1) = 2
f2(2, 2).  % f(2) = 2
f2(N, F) :-
    N > 2,
    N1 is N + 1,
    N2 is N - 2,
    f2(N1, F1),
    f2(N2, F2),
    F is F1 + F2.

% Trzeci ci¹g: f(n+2) = f(n) * n, f(0) = 2, f(1) = 3
f3(0, 2).  % f(0) = 2
f3(1, 3).  % f(1) = 3
f3(N, F) :-
    N > 1,
    N2 is N - 2,
    f3(N2, F2),
    F is F2 * N.
