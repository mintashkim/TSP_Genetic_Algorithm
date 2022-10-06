import abc

class GeneticAlgorithmProblem:
    
    @abc.abstractmethod
    def fitness(self, instance):
        pass

    @abc.abstractmethod
    def getPotentialGenes(self):
        pass

    @abc.abstractmethod
    def performEvolution(self):
        pass

    @abc.abstractmethod
    def selection(self):
        pass
    
    @abc.abstractmethod
    def crossover(self):
        pass
    
    @abc.abstractmethod
    def mutation(self):
        pass
    
class GeneticAlgorithmInstance:
    
    phenotype = 0;
    genotype = [];
        
    def getGenotype(self):
        if type(self.genotype) is list:
            currentCity = 0
            path = {}
            for itr in range(len(self.genotype)):
                nextCity = self.genotype[currentCity]
                path[currentCity] = nextCity
                currentCity = nextCity
            self.genotype = path
        return self.genotype
    
    def setPhenotype(self, phenotype):
        self.phenotype = phenotype
    
    def getPhenotype(self):
        return self.phenotype
    
    def setGenotype(self, genotype):
        self.genotype = genotype
    
        
    