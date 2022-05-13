<img src ="https://prod-discovery.edx-cdn.org/media/course/image/3a31db71-de8f-45f1-ae65-11981ed9d680-b801bb328333.small.png" width="100"> <br/>
# Project Harvard CS50AI <br/>
![Harvard CS50AI](https://certificates.cs50.io/d39904b5-94a6-434b-88e5-813da08a54e5.png?size=letter) <br/>
###  My projects & solutions for CS50's Introduction to Artificial Intelligence with Python (CS50AI) course <br/>
### My CS50AI Project certificate : [CS50AI certificate](https://certificates.cs50.io/d39904b5-94a6-434b-88e5-813da08a54e5.pdf?size=letter) [Verified Certificate](https://courses.edx.org/certificates/b96f09744e39472196a39e47faf09f58) <br/>
### Before visiting the projects, please carefully read about [CS50 Academic Honesty](https://cs50.harvard.edu/x/2020/honesty/#:~:text=Unless%20otherwise%20specified%2C%20collaboration%20on,doing%20your%20work%20for%20you.). <br/>

## Course Information:
Link to the course : [CS50AI on Harvard's website ](https://cs50.harvard.edu/ai/2020/ "CS50AI on Harvard's website ") or [CS50AI on Edx](https://learning.edx.org/course/course-v1:HarvardX+CS50AI+1T2020/home "CS50AI on Edx") <br/>
[CS50AI](https://learning.edx.org/course/course-v1:HarvardX+CS50AI+1T2020/home "CS50AI") course is taught by David J. Malan and Brian Yu. <br/>
The nominally 7-week course comprised 12 practical tasks covering key methods in both conventional deterministic AI and more current approaches such as deep neural networks and natural language processing. This repository contains my solutions to the assignments for future reference. The course had a total of 19 tasks, including 7 quizzes and 12 programming assignments.

[========]

## Week 0  : Search 
The first week discussed standard methods for finding preferrably optimum or near-optimal ways to complete a job that can be reduced to a problem of "finding a path between two places with the least amount of cost incurred." <br/>

**The algorithm and theory covered:** <br/>
**1. Depth-First Search.** <br/> 
Depth-First Search is a search algorithm that exhausts each direction before trying another. <br/>

**2. Breadth-First Search.** <br/>
Breadth-First Search is a search algorithm that will take one step in each possible direction before taking the second step in each direction at the same time.

**3. Greedy best-first search.** <br/>
Greedy best-first search is a search algorithm that extends the node closest to the target, as defined by a heuristic function h(n). The function, as the name implies, calculates how close the next node is to the goal, although it is vulnerable to errors. The greedy best-first algorithm's efficiency is determined by the quality of the heuristic function. <br/>

**4. A * search** <br/>
A variant of the greedy best-first method, takes into account not only h(n), the estimated cost from the current position to the goal, but also g(n), the cost incurred up to the current location. By integrating these numbers, the algorithm can more accurately calculate the value of the solution and optimise its quick decisions. The algorithm keeps track of (cost of path until now + estimated cost to goal), and if it exceeds the estimated cost of some previous option, it will abandon the current path and return to the previous option, preventing itself from taking a long, inefficient path that h(n) incorrectly marked as best. <br/>

**5. MiniMax** <br/>
Minimax is an adversarial search method that depicts victory circumstances as (-1) for one side and (+1) for the other. These conditions will drive subsequent actions, with the minimising side attempting to get the lowest score and the maximizer attempting to achieve the maximum score.

**6. Alpha-Beta Pruning** <br/>
Alpha-Beta Pruning, a method for optimising Minimax, avoids some of the unpleasant recursive calculations. Following the establishment of the value of one action, if there is preliminary evidence that the following action can bring the opponent to a higher score than the previously established action, there is no need to investigate this action further because it will be decidedly less favourable than the previously established one. <br/>

**7. Depth-Limited Minimax** <br/>
Depth-limited Minimax algorithm examines just a certain number of moves before stopping, never reaching a terminal state. However, because the end of the hypothetical games has not been reached, this does not provide an exact value for each action. Depth-limited Minimax addresses this issue by relying on an evaluation function that calculates the predicted utility of the game from a given state, or, in other words, assigns values to states. <br/>
 
- **Project 0a : Degree** <br/>
The first project makes use of the breadth-first search technique to determine the "degrees of separation" between two actors, commonly known as the "Six Degrees of Kevin Bacon." <br/> 
Link to full assignment on Harvard website : [Degree ](https://cs50.harvard.edu/ai/2020/projects/0/degrees/ "Degree ") <br/>
Link to my project : [Project 0a : Degree](https://github.com/Lim-Calculus/Project-CS50AI/tree/main/Week%200%20:%20Search/Project%200a%20:%20Degree) <br/>

- **Project 0b : Tic-Tac-Toe** <br/>
This project demonstrating a simple game of Tic-Tac-Toe with an AI opponent employs the minimax Alpha-Beta pruning algorithm to determine the best strategy. <br/>
Link to full assignment on Harvard website : [Tic-Tac-Toe](https://cs50.harvard.edu/ai/2020/projects/0/tictactoe "Tic-Tac-Toe") <br/>
Link to my project : [Project 0b : Tic-Tac-Toe](https://github.com/Lim-Calculus/Project-CS50AI/tree/main/Week%200%20:%20Search/Project%200b%20:%20Tic-Tac-Toe "Project 0b : Tic-Tac-Toe") <br/>
Video to my project : [Presentation of Project 0b : Tic-Tac-Toe](https://www.youtube.com/watch?v=ToK0P4cTvAc "Presentation of Project 0b : Tic-Tac-Toe") <br/>


[========]

## Week 1  :  Knowledge  <br/>
This week works with knowledge representation and logical reasoning in a machine-readable manner, algorithmically addressing logically deductive issues. <br/>
**The algorithms and theory covered : **
1. Knowledge-base agents
2. Propositional Logic
3.	Inference algorithms
4. Truth table
5. Model Checking
6. Knowledge Engineering
7. Inference rules
8. De Morgan’s Law
9. Conjunctive normal form
10. Inference by resolution
11. First-Order Logic

- **Project 1a: Knights**
The goal of this project is to develop an AI that can use inference to rationally deduce answers to numerous classic "Knights and knaves" issues. <br/>
Link to full assignment on Harvard website : [Knights](https://cs50.harvard.edu/ai/2020/projects/1/knights/ "Knights") <br/>
Link to my project : [Project 1a : Knights](https://github.com/Lim-Calculus/Project-CS50AI/tree/main/Week%201%20:%20Knowledge/Project%201a%20:%20Knights "Project 1a : Knights")

- **Project 1b: Minesweeper**
This project integrates artificial intelligence to the popular Windows game Minesweeper. It operates by making safe moves based on field information and, if no safe moves are available, producing a random one. <br/>
Link to full assignment on Harvard website : [Minesweeper](https://cs50.harvard.edu/ai/2020/projects/1/minesweeper/) <br/>
Link to my project : [Project 1b : Minesweeper](https://github.com/Lim-Calculus/Project-CS50AI/tree/main/Week%201%20:%20Knowledge/Project%201b%20:%20Minesweeper)


[========]
## Week 2 : Uncertainty 
Due to numerous constraints, the AI, like us, may not always be aware of all of the knowledge available within the problem at any given time. As a result, the issues revolve around building AI to operate with probabilistic reasoning.

**The algorithm and theory covered:**
1. Unconditional probability
2. Conditional probability
3. Random Variable
4. Joint probability
5. Probability Rule
6. Bayesian Network
7. Bayes’ Rule
8. Inference by enumeration
10. Inference by approximation
11. Sampling
12. Markov Model

- **Project 2a: PageRank**
This project simulates Google's algorithm for ranking websites based on their relevance <br/>
Link to full assignment on Harvard Website : [PageRank](https://cs50.harvard.edu/ai/2020/projects/2/pagerank/) <br/>
Link to my project : [Project 2a : Pagerank](https://github.com/Lim-Calculus/Project-CS50AI/tree/main/Week%202%20:%20Uncertainty/Project%202a%20:%20Pagerank) <br/>


- **Project 2b: Heredity**
This project implements an AI algorithm that estimates a hidden attribute of having a damaged gene based on a visible impairment, in this instance, hearing loss. <br/>
Link to full assignment on Harvard Website : [Heredity](https://cs50.harvard.edu/ai/2020/projects/2/heredity/) <br/>
Link to my project : [Project 2b : Heredity](https://github.com/Lim-Calculus/Project-CS50AI/tree/main/Week%202%20:%20Uncertainty/Project%202b%20:%20Heredity)

[========]

## Week 3 : Optimization <br/>
This week discusses the topic that can be handled by an AI determining the optimal solution among a set of options. <br>

**The algorithm and theory covered:** <br>
1. Local search
2. Hill Climbing
3. Simulated Annealing
4. Linear Programming
5. Constraint Satisfaction
6. Node Consistency
7. Arc Consistency
8. Backtracking Search

- **Project 3 : Crossword** <br>
The goal of this project is to build an AI that generates crossword puzzles from a template and a word dictionary. <br>
Link to full assignment descripment on Harvard website : [Crossword](https://cs50.harvard.edu/ai/2020/projects/3/crossword/) <br/>
Link to my project : [Project 3: Crossword](https://github.com/Lim-Calculus/Project-CS50AI/tree/main/Week%203%20:%20Optimization/Project%203%20:%20Crossword)

[========]

## Week 4 : Learning <br>
This week introduces the chapters on machine learning, which is the development of AI that can reach conclusions without direct human intervention. <br/>

**The algorithm and theory covered:** <br>
1. Machine Learning
2. Supervised Learning
3. Nearest - Neighbor Classification 
4. Perceptron Learning
5. Support Vector Machines
6. Regression
7. Loss Functions
8. Overfitting
9. Regularization
10. Reinforcement Learning
11. Markov Descision Processes
12. Q - learning
13. Unsupervised Learning
14. k-means Clustering
15. Scikit-learn framework

- **Project 4a : Shopping** <br/>
This project implements an AI to predict whether or not internet shoppers will complete a purchase. <br/>
Link to full assignment on Harvard website : [Shopping](https://cs50.harvard.edu/ai/2020/projects/4/shopping/) <br/>
Link to my project : [Project 4a : Shopping](https://github.com/Lim-Calculus/Project-CS50AI/tree/main/Week%204%20:%20Learning/Project%204a%20:%20Shopping) <br/>

- **Project 4b : Nim** <br/>
This project implements an AI that learns to play the NIM game, in which two players remove rings from several towers, with the last person to take a ring losing. <br/>
Link to full assignment on Harvard website : [Nim](https://cs50.harvard.edu/ai/2020/projects/4/nim/) <br/>
Link to my project : [Project 4b : Nim](https://github.com/Lim-Calculus/Project-CS50AI/tree/main/Week%204%20:%20Learning/Project%204b%20:%20Nim) <br/>

[========]

## Week 5: Neural Networks <br/>
This week discusses the now immensely popular notion of neural networks, which was developed in the 1970s but is only being used now because of decreasing processing costs.<br/>
**The algorithm and theory covered:** <br/>
1. Neural Networks
2. Activation Functions
3. Neural Network Structure
4. Gradient Descent
5. Multilayer Neural Networks
6. Backpropagation
7. Overfitting
8. TensorFlow
9. Computer Vision
10. Image Convolution
11. Convolutional Neural Networks
12. Recurrent Neural Networks

- **Project 5: Traffic** <br/>
This project is to develop a rudimentary computer vision neural network that recognizes traffic signs in preparation for automated driving. <br/> 
Link to full assignment descriptions on Harvard website : [Traffic](https://cs50.harvard.edu/ai/2020/projects/5/traffic/) <br/>
Link to my project : [Project 5 : Traffic](https://github.com/Lim-Calculus/Project-CS50AI/tree/main/Week%205%20:%20Neural%20Networks/Project%205%20:%20Traffic) <br/> 

[========]
## Week 6 : Natural Language Processing










