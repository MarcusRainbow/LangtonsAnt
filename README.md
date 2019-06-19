# Langtons Ant
Python implementation of Langton's ant.

Langton's ant is a finite-state automaton, which operates on a 2d grid. Here, for convenience, we make it a toroidal space. It ought to be infinite. Each square can be white (false) or black (true). If the ant is on a white square, it turns left. If it is on a black square, it turns right. It always changes the colour of the square it is standing on.

On a white starting grid, the ant starts by painting a small square. However, when it runs into the square it started on, it changes direction. Soon, it appears to be behaving chaotically, though it roughly sticks to its own patch, which it only grows quite slowly. After a while, a repeating consistent pattern emerges.
