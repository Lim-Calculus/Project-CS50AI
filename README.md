# Project CS50AI 
![Harvard CS50AI ](https://certificates.cs50.io/d39904b5-94a6-434b-88e5-813da08a54e5.pdf?size=letter "Harvard CS50AI ")
####  My projects & solutions for CS50's Introduction to Artificial Intelligence with Python (CS50AI) courseMy solutions for CS50's Introduction to Artificial Intelligence with Python (CS50AI) course
Before visiting the projects, please carefully read about [CS50 Academic Honesty](httphttps://cs50.harvard.edu/ai/2020/honesty/:// "CS50 Academic Honesty").

## Course Information:
Link to the course : [CS50AI on Harvard's website ](https://cs50.harvard.edu/ai/2020/ "CS50AI on Harvard's website ") or [CS50AI on Edx](https://learning.edx.org/course/course-v1:HarvardX+CS50AI+1T2020/home "CS50AI on Edx")
[CS50AI](https://learning.edx.org/course/course-v1:HarvardX+CS50AI+1T2020/home "CS50AI") course is taught by David J. Malan and Brian Yu. 
The nominally 7-week course comprised 12 practical tasks covering key methods in both conventional deterministic AI and more current approaches such as deep neural networks and natural language processing. This repository contains my solutions to the assignments for future reference. The course had a total of 19 tasks, including 7 quizzes and 12 programming assignments.

## Week 0  : Search 
The first week discussed standard methods for finding preferrably optimum or near-optimal ways to complete a job that can be reduced to a problem of "finding a path between two places with the least amount of cost incurred."

Algorithm covered :
**1. Depth-First Search. **
Depth-First Search is a search algorithm that exhausts each direction before trying another.

**2. Breadth-First Search.**
Breadth-First Search is a search algorithm that will take one step in each possible direction before taking the second step in each direction at the same time.

**3. Greedy best-first search. **
Greedy best-first search is a search algorithm that extends the node closest to the target, as defined by a heuristic function h(n). The function, as the name implies, calculates how close the next node is to the goal, although it is vulnerable to errors. The greedy best-first algorithm's efficiency is determined by the quality of the heuristic function.

**4. A * search**
A* search, a variant of the greedy best-first method, takes into account not only h(n), the estimated cost from the current position to the goal, but also g(n), the cost incurred up to the current location. By integrating these numbers, the algorithm can more accurately calculate the value of the solution and optimise its quick decisions. The algorithm keeps track of (cost of path until now + estimated cost to goal), and if it exceeds the estimated cost of some previous option, it will abandon the current path and return to the previous option, preventing itself from taking a long, inefficient path that h(n) incorrectly marked as best.

**5. MiniMax**
Minimax is an adversarial search method that depicts victory circumstances as (-1) for one side and (+1) for the other. These conditions will drive subsequent actions, with the minimising side attempting to get the lowest score and the maximizer attempting to achieve the maximum score.

**6. Alpha-Beta Pruning**
Alpha-Beta Pruning, a method for optimising Minimax, avoids some of the unpleasant recursive calculations. Following the establishment of the value of one action, if there is preliminary evidence that the following action can bring the opponent to a higher score than the previously established action, there is no need to investigate this action further because it will be decidedly less favourable than the previously established one.

**7. Depth-Limited Minimax**
Depth-limited Minimax algorithm examines just a certain number of moves before stopping, never reaching a terminal state. However, because the end of the hypothetical games has not been reached, this does not provide an exact value for each action. Depth-limited Minimax addresses this issue by relying on an evaluation function that calculates the predicted utility of the game from a given state, or, in other words, assigns values to states.


