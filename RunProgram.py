import fantasypointcategories
import FootballWebsiteDataScripts.websiteaccessors

def main():
	print "hello"
	points = fantasypointcategories.OffensiveProduction()
	points.passingyards = 10
	print points.passingyards

if __name__ == '__main__':
	main()
