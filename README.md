# Monty Hall
Monty Hall Problem is a classic probability problem which is a kind of paradox of the veridical type, which is due to the fact that the solution of this particular problem is so absurd and not following the a standard common sense. The problem started with assuming a game show with the following rules:

- 3 Doors, with 1 door has a car behind it and the other has goats.
- The contestant is given a choice to choose a door.
- The host, who knows which door that has a car, opens another door that has a goat in it.
- The contestant is then given another choice to switch to the remaining door, or keep on with their initial choice.

The response by Vos Savant is shown to show that switching is the right strategy, and it will lead to a higher probability of winning the car. The reason for this is because as the host has shown another door that has a goat in it (and will always do this), then the probability of winning if the contestant switch is equivalent to the probability of initially choosing a goat. This is because as the number of goats are 2, and if one of the goat has been revealed, then there is a $2/3$ chance that the other door that hasn't been revealed to be a car.

### Additional Comments
The given jupyter notebook includes the function to run this show given if the number of doors are more than 1, and the number of opportunity to switch is given more than 1 as well (With caveat that the winning door will always be 1). With two strategies, always switch, or stay in the same door.

<p align = 'center'>
  <img src = 'https://i0.wp.com/statisticsbyjim.com/wp-content/uploads/2017/02/Monty_open_door_blog-300x167.png?resize=300%2C167'>
</p>
