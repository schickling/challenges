#!/usr/bin/swipl -q -t main -f

main :-
    format("~0f x ~0f", [2**10, 5**10]), nl, fail.