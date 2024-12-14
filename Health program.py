from statistics import fmean 

class SchoolClass:
    ages = []
    heights = []
    weights = []

    def fillData(self, type, data):
        if type == 'age':
            self.ages = data
        elif type == 'height':
            self.heights = data
        else:
            self.weights = data

    def getMean(self, type):
        if type == 'age':
            return fmean(self.ages)
        elif type == 'height':
            return fmean(self.heights)
        else:
            return fmean(self.weights)

types = ["age", "height", "weight"]
classA = SchoolClass()
classB = SchoolClass()

count_a = int(input())
for i in range(0, 3):
    classA.fillData(types[i], list(map(float, input().split()))[0:count_a])

count_b = int(input())
for i in range(0, 3):
    classB.fillData(types[i], list(map(float, input().split()))[0:count_b]) 


for type in types:
    print(classA.getMean(type))

for type in types:
    print(classB.getMean(type))

if classA.getMean("height") > classB.getMean("height"):
    print("A")
elif classA.getMean("height") < classB.getMean("height"):
    print("B")
elif classA.getMean("weight") < classB.getMean("weight"):
    print("A")
elif classA.getMean("weight") > classB.getMean("weight"):
    print("B")
else:
    print("Same")
