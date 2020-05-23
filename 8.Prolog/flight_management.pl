% airport(city, airportTax, minSecurityDelay)
airport(london, 75, 80).
airport(toronto, 50, 60).
airport(barcelona, 40, 30).
airport(madrid, 75, 45).
airport(valencia, 40, 20).
airport(malaga, 50, 30).
airport(paris, 50, 60).
airport(toulouse, 40, 30).

% flight(from , airline, to, price, duration)
flight(london, air_canada, toronto, 500, 360).
flight(london, united, toronto, 650, 420).
flight(london, iberia, barcelona, 220, 240).
flight(barcelona, air_canada, madrid, 100, 60).
flight(barcelona, iberia, madrid, 120, 65).
flight(barcelona, iberia, valencia, 110, 75).
flight(valencia, iberia, madrid, 40, 50).
flight(madrid, air_canada, toronto, 900, 480).
flight(madrid, united, toronto, 950, 540).
flight(madrid, iberia, toronto, 800, 480).
flight(madrid, iberia, malaga, 50, 60).
flight(valencia, iberia, malaga, 50, 30).
flight(paris, united, toulouse, 35, 120).

isflight(X, Y) :-
	(flight(X, _, Y, _, _) ; flight(Y, _, X, _, _)) ->
	write('There is a flight') ; write('There is no flight').

ischeap(A, B, C) :-
	airport(A, X, _) , airport(B, V, _), (flight(A, C, B, L, _) ; flight(B, C, A, L, _)), X + L + V < 400 ->
	write('Flight is cheap. ') ; write('Flight is not cheap. ').

istwopossible(A, B) :-
	(flight(A, _, C, _, _) , flight(C, _, B, _, _)) ; (flight(B, _, C, _, _) , flight(C, _, A, _, _)) ->
	write('Two flights are possible') ;  write('Two flights are not possible').

ispreferable(A, B, C) :-
	((airport(A, X, _) , airport(B, V, _), (flight(A, C, B, L, _) ; flight(B, C, A, L, _)), X + L + V < 400) ; C == air_canada) ->
	write('The flight is preferred') ; write('Flight is not preferred').

ifunithencan(A, B) :-
	(flight(A, united, B, _, _) ; flight(B, united, A, _, _)) , (flight(A, air_canada, B, _, _) ; flight(B, air_canada, A, _, _)) ->
	write('True') ; write('false').
