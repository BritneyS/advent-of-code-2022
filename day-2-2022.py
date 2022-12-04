# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.

# Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide 
# (your puzzle input) that they say will be sure to help you win Rock, Paper, Scissors. 
# "The first column is what your opponent is going to play: 
# A for Rock, B for Paper, and C for Scissors. 
# The second column--" Suddenly, the Elf is called away to help with someone's tent.

# The second column, you reason, must be what you should play in response: 
# X for Rock, Y for Paper, and Z for Scissors. 
# Winning every time would be suspicious, so the responses must have been carefully chosen.

# The winner of the whole tournament is the player with the highest score. 
# Your total score is the sum of your scores for each round. 
# The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

# What would your total score be if everything goes exactly according to your strategy guide?

def score_rock_paper_scissors(file_path):
    opponent_choice_cipher = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
    your_choice_cipher = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
    choice_score = {'rock': 1, 'paper': 2, 'scissors': 3}
    win_score = {'lose': 0, 'draw': 3, 'win': 6}
    opponent_total_score = 0
    your_total_score = 0

    round = []

    with open(file_path) as file:
        for line in file:
            round = line.strip().split()
            round[0] = opponent_choice_cipher[round[0]]
            round[1] = your_choice_cipher[round[1]]

            if round[0] == 'rock':
                opponent_total_score += choice_score['rock']

                if round[1] == 'rock':
                    your_total_score += choice_score['rock']
                    
                    your_total_score += win_score['draw']
                    opponent_total_score += win_score['draw']

                if round[1] == 'paper':
                    your_total_score += choice_score['paper']

                    your_total_score += win_score['win']
                    opponent_total_score += win_score['lose']

                if round[1] == 'scissors':
                    your_total_score += choice_score['scissors']

                    your_total_score += win_score['lose']
                    opponent_total_score += win_score['win']

            if round[0] == 'paper':
                opponent_total_score += choice_score['paper']

                if round[1] == 'rock':
                    your_total_score += choice_score['rock']
                    
                    your_total_score += win_score['lose']
                    opponent_total_score += win_score['win']

                if round[1] == 'paper':
                    your_total_score += choice_score['paper']

                    your_total_score += win_score['draw']
                    opponent_total_score += win_score['draw']

                if round[1] == 'scissors':
                    your_total_score += choice_score['scissors']

                    your_total_score += win_score['win']
                    opponent_total_score += win_score['lose']

            if round[0] == 'scissors':
                opponent_total_score += choice_score['scissors']

                if round[1] == 'rock':
                    your_total_score += choice_score['rock']
                    
                    your_total_score += win_score['win']
                    opponent_total_score += win_score['lose']

                if round[1] == 'paper':
                    your_total_score += choice_score['paper']

                    your_total_score += win_score['lose']
                    opponent_total_score += win_score['win']

                if round[1] == 'scissors':
                    your_total_score += choice_score['scissors']

                    your_total_score += win_score['draw']
                    opponent_total_score += win_score['draw']

    return your_total_score

print(score_rock_paper_scissors('input/day-2-input.txt'))

# --- Part Two ---
# The Elf finishes helping with the tent and sneaks back over to you. 
# "Anyway, the second column says how the round needs to end: 
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
# Good luck!"

# The total score is still calculated in the same way, but now you need to figure out 
# what shape to choose so the round ends as indicated.

# Following the Elf's instructions for the second column, 
# what would your total score be if everything goes exactly according to your strategy guide?

def score_rock_paper_scissors(file_path):
    opponent_choice_cipher = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
    your_choice_cipher = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
    choice_score = {'rock': 1, 'paper': 2, 'scissors': 3}
    win_score = {'lose': 0, 'draw': 3, 'win': 6}
    opponent_total_score = 0
    your_total_score = 0

    round = []

    with open(file_path) as file:
        for line in file:
            round = line.strip().split()
            round[0] = opponent_choice_cipher[round[0]]
            round[1] = your_choice_cipher[round[1]]

            if round[0] == 'rock':
                opponent_total_score += choice_score['rock']

                if round[1] == 'lose':
                    your_total_score += choice_score['scissors']
                    
                    your_total_score += win_score['lose']
                    opponent_total_score += win_score['win']

                if round[1] == 'draw':
                    your_total_score += choice_score['rock']

                    your_total_score += win_score['draw']
                    opponent_total_score += win_score['draw']

                if round[1] == 'win':
                    your_total_score += choice_score['paper']

                    your_total_score += win_score['win']
                    opponent_total_score += win_score['lose']

            if round[0] == 'paper':
                opponent_total_score += choice_score['paper']

                if round[1] == 'lose':
                    your_total_score += choice_score['rock']
                    
                    your_total_score += win_score['lose']
                    opponent_total_score += win_score['win']

                if round[1] == 'draw':
                    your_total_score += choice_score['paper']

                    your_total_score += win_score['draw']
                    opponent_total_score += win_score['draw']

                if round[1] == 'win':
                    your_total_score += choice_score['scissors']

                    your_total_score += win_score['win']
                    opponent_total_score += win_score['lose']

            if round[0] == 'scissors':
                opponent_total_score += choice_score['scissors']

                if round[1] == 'lose':
                    your_total_score += choice_score['paper']
                    
                    your_total_score += win_score['lose']
                    opponent_total_score += win_score['win']

                if round[1] == 'draw':
                    your_total_score += choice_score['scissors']

                    your_total_score += win_score['draw']
                    opponent_total_score += win_score['draw']

                if round[1] == 'win':
                    your_total_score += choice_score['rock']

                    your_total_score += win_score['win']
                    opponent_total_score += win_score['lose']

    return your_total_score
    
print(score_rock_paper_scissors('input/day-2-input.txt'))

                
            