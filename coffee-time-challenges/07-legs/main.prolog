#!/usr/bin/swipl -q -t main -f
% In a room there are a mixture of people and dogs.
% There are 72 heads, and 200 legs. How many dogs are in the room?
% (No tricks, no chromosomal abnormalities, no disabilities …)

is_solution(Humans, Dogs) :- between(0, 200, Humans),
                             between(0, 200, Dogs),
                             Legs is 2*Humans + 4*Dogs,
                             Heads is Humans + Dogs,
                             Legs = 200,
                             Heads = 72.

main :-
    is_solution(Humans, Dogs),
    format("There are ~w humans and ~w dogs.\n", [Humans, Dogs]),
    false. % make sure that all solutions get printed