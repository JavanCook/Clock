Clock Solitaire Game
==============

A simple Tkinter based UI written in Python that plays clock solitaire until it wins. The UI counts the number of rounds played until the game is won.

Clock solitaire is a chanced based game where the outcome of the game is determined once the deck has been shuffled.
The top card from the central stack is turned over and then moved to the stack at the  position on the clock corresponding to that card's value.
The card at the bottom of that stack is then turned over and this process continues until either the lose condition is met or all the cards have been revealed.

The game is lost if all four Kings are revealed before all the cards in the deck are exposed.
As such, it is only possible to win if the last card revealed is a King.

The card image file comes from [Milefoot.com Mathematics](http://www.milefoot.com/math/discrete/counting/cardfreq.htm), the original source appears to have been lost.

## Requirements
This code requires you to have the [Tkinter module](https://wiki.python.org/moin/TkInter) installed to run.
