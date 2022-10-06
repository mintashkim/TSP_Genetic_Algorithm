from TravelingSalesmanProblem import *

#data_mode = 'Random'
data_mode = 'Load'
csvfile = "TSP1.csv"
height = 500
width = 700
cities = 15
mutationFactor = 0.2
time = 10

tsp = TravelingSalesmanProblem(data_mode,csvfile,cities,height, width, time)
routes, utility, distance, elapsedTime = tsp.performEvolution(100, 70, 100, mutationFactor)

currentCity = 0
route = ''
for itr in range(len(routes.keys())):
    route = route + '->' + str(currentCity)
    currentCity = routes[currentCity]
print ("===== 20100072, Student =====")
print ("Routes : %s" %(route))
print ("Distance : ", distance)
print ("Elapsed time : ", elapsedTime, "secs")
