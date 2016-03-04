import FantasyPointCategories
imp.load_source()

def main():
	print "hello"
	points = FantasyPointCategories.OffensiveProduction()
	points.passingyards = 10
	print points.passingyards

if __name__ == '__main__':
	main()	