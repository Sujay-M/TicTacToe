# TicTacToe
Tic Tac Toe game with a gist of machine learning


In 1959, Arthur Samuel defined machine learning as a
"Field of study that gives computers the ability to learn without being explicitly programmed".
He wrote a checkers program that learned by playing against itself and used that data when it played against a human.

#Approach
Initially i was biased towards applying supervised learning (since i am following coursera Machine learning course).
I used classification (logistic regression and also neural networks) to model if the next move leads to win or loss.
But even though tictactoe has finite number of states and is deterministic there is no one optimal move for a perticular state.(atleast not initially) 
I didn't get the results i hoped for (maybe my model was not too good) and i wanted the program to learn the moves for which it would lose. So reinforcement learning came to my aid and i used temporal difference to solve my problem.

Temporal difference is essentially dynamic programming and greedy algorithm approach.(Both of which i knew)
But since i restricted myself to applying machine learning concepts (biased towards supervised learning) i was blinded and couldn't bring myself to even think about those algorithms. 

#About Code

(Code is now a little messy.) 
Havent tested it thoroughly but seems to work pretty well.(better than my previous approaches)

suggestions are very much appreciated.( email : sujaym.sujaym@gmail.com)
#Acknowledgement
Thanks to coursera for such a great course on Machine Learning and thanks to Prof.Andrew Ng for teaching it. 
