class OffensiveFantasyPointValues:
	points_per_passing_yards = 1/25 #floor; not a continuous value 
	points_per_passing_touchdowns = 4
	points_per_interceptions = -1
	points_per_rushing_yards = 1/10
	points_per_rushing_touchdowns = 6
	points_per_reception_yards = 1/10
	points_per_reception_touchdowns = 6
	points_per_return_touchdowns = 6
	points_per_two_point_conversions = 2
	points_per_fumbles_lost = -2
	points_per_offensive_fumble_return_TD = 6

class DefensiveProduction:
	points_per_sack = 1
	points_per_interception = 2
	points_per_fumble_recovery = 2
	points_per_touchdown = 6
	points_per_safety = 2
	points_per_block_kick = 2
	points_per_kickoff_PR_touchdowns = 6

	def create_defensive_points_allowed_array(self):
		create_defensive_points_allowed_array = [None] * 35
		for x in range(0, 36):
			if (x == 0): 
				create_defensive_points_allowed_array[x] = 10
			if (x > 0 and x < 7):
				create_defensive_points_allowed_array[x] = 7
			if (x > 6 and x < 14):
				create_defensive_points_allowed_array[x] = 4
			if (x > 13 and x < 21):
				create_defensive_points_allowed_array[x] = 1
			if (x > 20 and x < 28): 
				create_defensive_points_allowed_array[x] = 0
			if (x > 27 and x < 35):
				create_defensive_points_allowed_array[x] = -1
			if (x > 27 and x < 35):
				create_defensive_points_allowed_array[x] = -4


	points_per_points_allowed = create_defensive_points_allowed_array

class KickingProduction:

	def create_field_goal_point_array(self):
		field_goal_lengths = [None] * 51
		for x in range(0, 51):
			if (x < 39):
				field_goal_lengths[x] = 3
			elif (x > 39 and x <50):
				field_goal_lengths[x] = 4
			elif (x > 49):
				field_goal_lengths[x] = 5

		return field_goal_lengths

	points_per_PAT_made = 1

	field_goal_lengths = create_field_goal_point_array

