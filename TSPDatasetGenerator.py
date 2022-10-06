import random

def generator(numCities, width, height, filename):
    
    datasetFile = open(filename, 'w')
    
    for itr in range(numCities):
        x = random.uniform(0, width)
        y = random.uniform(0, height)
        coordinate = [x, y]
        datasetFile.write(str(itr)+","+str(x)+","+str(y)+"\n")
        
    datasetFile.close()

generator(40, 800, 800, 'TSP-Open-dataset.csv')
generator(40, 800, 800, 'TSP-Closed-dataset.csv')