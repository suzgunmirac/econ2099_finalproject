## Authors: Mirac Suzgun and Abhishek Anand

import numpy

SIZE = 20
CONSTANT = 38
EPSILON_VALUE = 0.1
EPISODES = 100

def main ():
	# assumption: the team strength of A is proportional to the wealth of A
	team_strength = [0 for i in range (SIZE)]
	winning_ratio = [[0 for i in range (SIZE)] for j in range (SIZE)]

	for i in range (SIZE):
		team_strength [i] = numpy.random.uniform (0,1)
		for j in range (SIZE - i):
			epsilon = numpy.random.uniform (0.0, 0.05) ## randomization part
			sign = numpy.random.uniform(-1, 1) 
			if sign < 0:
				sign = -1
			else:
				sign = 1
			denominator = team_strength [i] + team_strength [j]
			prop_i_wins = (team_strength[i]/denominator) * (1 + sign * epsilon)

			if prop_i_wins >= 1:
				prop_i_wins = 1

			prop_j_wins = 1 - prop_i_wins
			winning_ratio [i][j] = prop_i_wins
			winning_ratio [j][i] = prop_j_wins

	print "INITIAL team_strength: \n"
	initial_team_strength = [0 for i in range (SIZE)]
	for i in range (SIZE):
		initial_team_strength [i] = team_strength[i]

	full_season = []

	for season in range (EPISODES):
		score_board = [0 for i in range (SIZE)]
		# 38 GAMES
		for i in range (SIZE):
			for j in range (SIZE):
				if i != j:
					# also generate a random number
					if winning_ratio [i] [j] > numpy.random.uniform (0, 1):
						score_board[i] += 1
					else:
						score_board[j] += 1

		full_season.append(score_board)
		## Now it is time to give some rewards...

		for i in range (SIZE):
			sign_epsilon = 1
			random_value = numpy.random.uniform (0, 1)
			if random_value < EPSILON_VALUE:
				sign_epsilon = -1
			gradient_range = (1 - team_strength[i])/(score_board[i] + CONSTANT)
			team_strength [i] += sign_epsilon * (numpy.random.uniform (0, gradient_range))

			if team_strength[i] < 0.05:
				team_strength [i] = 0.05


		for i in range (SIZE):
			for j in range (SIZE - i):
				epsilon = numpy.random.uniform (0.0, 0.05) ## randomization part
				sign = numpy.random.uniform(-1, 1) 
				if sign < 0:
					sign = -1
				else:
					sign = 1
				denominator = team_strength [i] + team_strength [j]
				prop_i_wins = (team_strength[i]/denominator) * (1 + sign * epsilon)

				if prop_i_wins >= 1:
					prop_i_wins = 1

				prop_j_wins = 1 - prop_i_wins
				winning_ratio [i][j] = prop_i_wins
				winning_ratio [j][i] = prop_j_wins

	print "FULL SEASON: \n"
	print full_season

	print "FINAL team_strength: \n"
	for i in range (SIZE):
		print team_strength[i] - initial_team_strength[i]

	print team_strength


if __name__ == '__main__':
  main()
