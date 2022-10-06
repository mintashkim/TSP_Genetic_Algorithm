# Solving Traveling Salesman Problem with Genetic Algorithm

### 1. Initial population (Related function: createInitialPopulation(), performEvolution())
In the original version of code, we create randomly permutated genotype in the given number of times (numPopulation) and regard it as our initial population. However, during research, I found that k-means clustering performs better because it provides population with genotypes have less total distance. Then, the idea is simple, which is providing better genotypes than randomly selected out of N! (N: number of cities) cases. Hence, I utilized the fitness function to rank each genotype which is randomly created. Create 10 times numPopulation number of genotypes and rank it using the fitness function. Then, return the top numPopulation genotypes as an initial population. This method is simple but strong because we can prevent inferior genotypes which are way too far from the optimal solution.  
  
### 2. Mutation (Related functions: calculateMutationFactor(), mutation(), performEvolution())
In the original version of code, we use a fixed mutation factor, 0.2. However, we need more mutation if the output distance is too large. On the other hand, we need less mutation if the output is sufficiently small. Therefore, I used calculateMutationFactor() function in order to make mutation factor more flexible. First get the total distance(standardTotalDist) of the best solution is prior iteration of evolution. If the best solution of current iteration(totalDist) is larger than 0.9 times standardTotalDist, which means that there was not enough improvement during one iteration, we mutate more. Otherwise, if the improvement is satisfactory, we loosen mutation with less mutation factor. The function that calculates mutation factor is as follows.
I found the function in the last line from this paper: Chunhua Fu, Lijun Zhang, Xiaojing Wang, and Liying Qiao, Solving TSP problem with improved genetic algorithm AIP Conference Proceedings 1967, 040057 (2018); https://doi.org/10.1063/1.5039131, Published Online: 23 May 2018. 
  
I have also tried another version of mutation factor calculation as follows, but it did not work well.  
if totalDist > 2800:  
    maxMutationFactor = 0.3  
    minMutationFactor = 0.2  
elif totalDist <= 2800 and totalDist > standardTotalDist * 2500:  
    maxMutationFactor = 0.2  
    minMutationFactor = 0.15  
else:   
    maxMutationFactor = 0.15  
    minMutationFactor = 0.08  
  
Another modification I tried in mutation procedure is to mutate cities with the longest distance. During the evolution, I found that the cities with the longest distance from each other are one of the main causes of inferior genotype. Therefore, I inserted another mutation procedure designed to mutate cities with the longest distance. In the iteration, we mutate factor number of times and before the original swapping, I inserted new swapping for the max distance cities. The actual code is as follows.  
  
currentCity = 0  
maxDistance = 0.0  
maxCities = {"MaxIdx1": 0, "MaxIdx2": 1}  
for itr in range(len(genotype) - 1):  
    nextCity = genotype[currentCity]  
    current = self.dicLocations[currentCity]  
    next = self.dicLocations[nextCity]  
    if maxDistance < self.calculateDistance(current, next):  
        maxDistance = self.calculateDistance(current, next)  
        maxCities["MaxIdx1"] = currentCity  
        maxCities["MaxIdx2"] = nextCity  
    currentCity = nextCity  
idxSwapMax1, idxSwapMax2 = maxCities.values()  
idxSwap = random.randint(0, len(genotype))  
genotype[idxSwapMax1], genotype[idxSwap] = genotype[idxSwap], genotype[idxSwapMax1]  
  
### 3. Crossover (Related functions: evaluateInheritance(), performEvolution())
Since we are using position-based encoding, there are not many things we can modify. Even we use k-ary encoding and so on, it would require a lot of computation time so it hinders evolution. When we use position-based encoding, the offspring defers from its parents too much after a crossover. Therefore, I created a function which evaluates whether the offspring is well inherited or not. In performEvolution, we check the inheritance rate using evaluateInheritance function below. The actual code is as follows.  
  
for itr in range(numOffsprings):  
    gp1, gp2 = self.selectParents(population)  
    p1 = self.crossoverParents(gp1, gp2)  
    p2 = self.crossoverParents(gp1, gp2)  
    wellInherited = False  
    while wellInherited == False:  
        offspring = self.crossoverParents(p1, p2)  
        wellInherited = self.evaluateInheritance(p1.getGenotype(), p2.getGenotype(), offspring.getGenotype())  
    offsprings[itr] = offspring  
    mutationFactor = self.calculateMutationFactor(population, offsprings[itr], self.calculateTotalDistance(offsprings[itr]), standardTotalDist)  
    factor = int(mutationFactor * len(self.dicLocations.keys()))  
    self.mutation(offsprings[itr], factor)  
  
def evaluateInheritance(self, genotypeP1, genotypeP2, genotypeOff):  
    match1 = 0  
    match2 = 0  
    for itr in range(len(genotypeP1)):  
        if genotypeP1[itr] == genotypeOff[itr]:  
            match1 += 1  
        if genotypeP2[itr] == genotypeOff[itr]:  
            match2 += 1  
    if float(match1)/float(len(genotypeP1)) > 0.1 and float(match2)/float(len(genotypeP1)) > 0.1:  
        return True  
    else:  
        return False  
  
We check whether the ratio of same neighbor between a parent and an offspring is larger than 0.1 (e.g. If the length of a genotype is 15, we check whether offspring has more than 2 same neighbors as its parents). If this evaluation we can avoid totally irrelevant offspring. Surprisingly, the acceptance rate of evaluateInheritance() is approximately 5%. This implies there were so many irrelevant offspring after crossover.  
  
Reference  
Chunhua Fu, Lijun Zhang, Xiaojing Wang, and Liying Qiao, Solving TSP problem with improved genetic algorithm AIP Conference Proceedings 1967, 040057 (2018); https://doi.org/10.1063/1.5039131, Published Online: 23 May 2018
