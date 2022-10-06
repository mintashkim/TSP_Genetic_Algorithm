from TravelingSalesmanProblem import *
from TravelingSalesmanProblemGUI import *

speed = 1000
data_mode = 'Random'
# data_mode = 'Load'
csvfile = "TSP1.csv"
height = 500
width = 700
cities = 15
mutationFactor = 0.2
time = 180

tsp = TravelingSalesmanProblem(data_mode, csvfile, cities, height, width, time)
gui = TravelingSalesmanProblemGUI(tsp, speed, height, width)
routes, utility, distance, elapsedTime = tsp.performEvolution(100, 49, 50, mutationFactor)

currentCity = 0
route = ''
for itr in range(len(routes.keys())):
    route = route + '->' + str(currentCity)
    currentCity = routes[currentCity]
print ("===== 20190102, Student =====")
print ("Routes : %s" %(route))
print ("Distance : ", distance)
print ("Elapsed time : ", elapsedTime, "secs")
