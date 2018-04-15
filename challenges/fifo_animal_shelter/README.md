# FIFO ANIMAL fifo_animal_shelter
**Author** : George Ceja
**Version**: 0.1.0


## Overview
FIFO Animal Shelter is a shelter who has a Queue of dogs and cats.
Someone can adopt a cat or dog.


## Challenge
Popping a cat or dog depending on user preference.


## Solution
Initiate a queue with all the animals and initialize another queue that is empty
Dequeue from the filled queue if the customer does not a preference in mind. In
case the user has some preference either a cat or dog then you'd dequeue the
first pet from the filled stack and return it to him if that's his preference if
not enqueue it to the second queue.


## Assets
![pseudocode](assets/fifo_animal_shelter.jpg)


## Architecture
Python 3.6.4


## API
None


## Change log
v0.2 - fixed queue class and fifo_animal_shelter. Revised README.md.
v0.1 - Created FIFO method.
