# stochastic-fairness
This repo applies differential privacy to the decisions made by an outside algorithm and computes change in overall accuracy. The purpose of this algorithm is to modify the outside algorithm so it is more "fair." The idea of this algorithm is to flips two coins. If the first coin lands on heads this algorithm's output would be the same as some outside algorithms output. However, if the first coin lands on tails this algorithm's output is determined by the outcome of the second coin flip (yes if heads, no if tails). \\
The program allows the user to use their an outside algorithms output and expected output or to generate a random one for testing. The user can then run a simulation to see how the accuracy changes given the percentage of the entries they wish to add noise to and the percentage of positive noise (which gives the percentage of negative noise). After the simulation is run the code will overall accuracy, overall false positives, and overall false negatives as percentages. The user can run as many simulations as they want on the data. 

# setup
Install requirements:\\
pip install -r requirements.txt\\
Run main:\\
python main.py \\

# thanks
This repo was inspired by Dr. Brunelle's amazing Ethics in Computer Science class at the University of Washington. Thank you for creating an environment to share our thoughts and opinions about what ethics looks like in this age of algorithms. Additionally, Thank you to the authors of the book, "The Ethical Algorithm" which taught me differential privacy. \\ \\

Link to google doc additional reasoning for why this algorithm might be useful and a couple of problems the current version has: https://docs.google.com/document/d/1wXf-f7NOfAquErEhskjMsYyjzOKMq64zQMQ7txrOFWI/edit?usp=sharing