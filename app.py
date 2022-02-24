from cmath import sqrt
from collections import Counter
import statistics

errorDumpString = 'Values derived so far from list: {} are as follows.\n mean: {} \n mode: {} \n median: {} \n range: {} \n stadard deviation: {}'

class CalculateStandardDeviation: 
    def __init__(self): 
        print('This application quickly calculates mean, median, mode, range, and standard deviation.')
        print('Enter each number in any order and enter the phrase "end" to calculate data properties.')
        self.list = []
        self.mean = None
        self.mode = None
        self.median = None
        self.range = None
        self.standardDeviation = None
        self.injestNewNumber()
    def injestNewNumber(self): 
        try:
            response = input('Enter next number or "end": ')
            if(response == 'end'):
                print('Ready to calculate values')
                self.calculateValues()
            elif(response == 'exit'):
                print('Ending')
            else:
                 self.list.append(int(response))
                 self.injestNewNumber()
        except: 
            print('You\'ve entered an invalid value please try again.')
            self.injestNewNumber()
    def calculateValues(self):
        try:
            self.list = sorted(self.list)
            print('sorted list: ', self.list)
            self.mean = sum(self.list)/len(self.list)
            print('mean: ', self.mean)
            self.mode = Counter(self.list).most_common()
            print('mode: ', self.mode)
            self.median = statistics.median(self.list)
            print('median: ', self.median)
            self.range = self.list[len(self.list) - 1] - self.list[0]
            print('range: ', self.range)
            self.standardDeviation = statistics.stdev(self.list)
            print('standard deviation: ', self.standardDeviation)
            self.standardDeviationValues = self.calculateStandardDeviationValues()
            print('standard deviation values: ', self.standardDeviationValues)
            self.quartiles = statistics.quantiles(self.list)
            print('quartiles: ', self.quartiles)
            self.interquartileRange = self.quartiles[len(self.quartiles) - 1] - self.quartiles[0]
            print('Interquartile Range: ', self.interquartileRange)
            self.calculateAreaAndZIndex()
        except:
            print('Failure to calculate values beginning dump of values so far')
            print(errorDumpString.format(self.list, self.mean, self.mode, self.median, self.range, self.standardDeviation))
    def calculateStandardDeviationValues(self): 
        try:
            list = [-3, -2, -1, 0, 1, 2, 3]
            vals = []
            for i in list:
                vals.append(self.mean + (i * self.standardDeviation))
            return vals
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise
    # Manually calculates standard deviation instead of using statistics library. Works but sort of unneccessary since the library exists. 
    def calculateStandardDeviation(self):
        squaredResults = []
        for i in self.list:
            squaredResults.append(pow(i - self.mean, 2))

        partialResult = sum(squaredResults)/(len(self.list) - 1)

        stdvar = sqrt(partialResult)

        return stdvar
    def calculateAreaAndZIndex(self):
        try:
            print('Enter the number to find percentile, z-index, left area, and right area.')
            selectedValue = str(input('Enter a number or "exit"'))
            if selectedValue.lower() == 'exit':
                print('Exiting')
            else:
                val = int(selectedValue)

                zIndex = (val-self.mean)/self.standardDeviation
                
                print('z-index: ', zIndex)

                self.calculateAreaAndZIndex()


                
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

CalculateStandardDeviation()

# z=(x-μ)/σ; 