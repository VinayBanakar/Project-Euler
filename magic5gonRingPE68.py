# The inner ring elements repeat twice while the outer only once. 
# Using greedy approach solved this in pen and paper. 

[6+7+8+9+10] + 2 * [1+2+3+4+5] = 70
Now 70/5 = 14
Clockwise: Outer to inner
6, 5, 3
10, 3, 1
9, 1, 4
8, 4, 2
7, 2, 5

So each line should sum to 14 when placed. And when placed clockwise and listed as a string. 
We get 6531031914842725

#We can write a brute force method to check if a combination in 10! gives this pattern, 
# but that seems boring, and I didn't find any other intuitive way to code it. 