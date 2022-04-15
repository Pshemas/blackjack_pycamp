# Blackjack - simplified version
my attempt at completing 2nd project for the first edition of Pycamp.pl .

Allowed me to learn more about Pytest and forced me to do as much as possible in OOP.

It is a bit "overdone" - but I've wanted to practice things like dataclasses given the opportunity :) . Again my solution is a bit different from the one proposed by the pycamp organizers - I've decided to assign card values using methos in BlackJack game class, not card / deck class. My thinking was that if I decide to add other card game it would be possible while reusing existing classes.

The readability suffered though. If the time after bootcamp (or in between projects) permits will think about cleaning this one up. But I'm happy that after initial commit I did a refactor that uses exceptions handling to manage scores.
