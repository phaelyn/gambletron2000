# Track and report game state
import game_state as gs

class Runner:

	def __init__(self, home_team, away_team):
		"""
		Create a runner for a single football game
		"""
		self.state = gs.GameState(home_team, away_team)


	def run_game(self):
		# coin toss 
		# loop: game
		# ot?
		# print results
		pass