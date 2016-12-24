Python Program: Created by Cory Sollberger 3/4/16

The following program simulates a non-deterministic finite state automaton with epsilon transitions.
Epsilon transitions are state changes that require no input.

2) NFA that recognizes the language {ab, bc, aac}, assuming the alphabet {a,b,c}
4) A NFA+e defined by the table below, "->" representing the starting state, "*" representing the final state(s)
 ______________________________
|______|__e__|__a__|__b__|__c__|
|__->p_|{q,r}|__0__|_{q}_|_{r}_|
|____q_|__0__|_{p}_|_{r}_|{p,q}|
|___*r_|__0__|__0__|__0__|__0__|

5) A program that takes in an alphabet A, a regular expression that is appropriate to that alphabet,
an integer n which generates n strings that in Lr. A regular expression is given that contains a set of strings
over {0,1} that contains at most one pair of consecutive 1's. The program generates 10 non-trivial instances of said
strings.