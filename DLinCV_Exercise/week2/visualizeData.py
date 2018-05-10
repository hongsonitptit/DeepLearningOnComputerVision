# import PyQt4
# import matplotlib
# matplotlib.use('qt4agg')
import matplotlib.pyplot as plt

inputDataFile = open('iris.data','r')

# Attribute Information:
#    1. sepal length in cm
#    2. sepal width in cm
#    3. petal length in cm
#    4. petal width in cm
#    5. class:
#       -- Iris-setosa
#       -- Iris-versicolor
#       -- Iris-virginica

class Flower:
    sepal_length = 0
    sepal_width = 0
    petal_length = 0
    petal_width = 0
    type = "unknown"

    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, type):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.type = type

setosaArr = []
versicoArr = []
virginArr = []

flowerType = ["Iris-setosa","Iris-versicolor","Iris-virginica"]

setosaSepalLength = []
setosaSepalWidth = []
versicoSepalLength = []
versicoSepalWidth = []
virginSepalLength = []
virginSepalWidth = []
setosaPetalLength = []
setosaPetalWidth = []
versicoPetalLength = []
versicoPetalWidth = []
virginPetalLength = []
virginPetalWidth = []

for line in inputDataFile:
    line = line.strip('\n')
    if line != "":
        attrs = line.split(",")
        flower = Flower(attrs[0],attrs[1],attrs[2],attrs[3],attrs[4])
        if flower.type == flowerType[0]:
            setosaArr.append(flower)
            setosaSepalLength.append(attrs[0])
            setosaSepalWidth.append(attrs[1])
            setosaPetalLength.append(attrs[2])
            setosaPetalWidth.append(attrs[3])
        elif flower.type == flowerType[1]:
            versicoArr.append(flower)
            versicoSepalLength.append(attrs[0])
            versicoSepalWidth.append(attrs[1])
            versicoPetalLength.append(attrs[2])
            versicoPetalWidth.append(attrs[3])
        elif flower.type == flowerType[2]:
            virginArr.append(flower)
            virginSepalLength.append(attrs[0])
            virginSepalWidth.append(attrs[1])
            virginPetalLength.append(attrs[2])
            virginPetalWidth.append(attrs[3])


fig = plt.figure()

# 1 rows, 2 columns, subplot 1 -> 121

plt.subplot("121")
plt.scatter(setosaSepalLength, setosaSepalWidth, c="r",label=flowerType[0])
plt.scatter(versicoSepalLength, versicoSepalWidth, c="g",label=flowerType[1])
plt.scatter(virginSepalLength, virginSepalWidth, c="b",label=flowerType[2])

plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.legend(loc=2)

# 1 rows, 2 columns, subplot 2 -> 122
plt.subplot("122")
plt.scatter(setosaPetalLength, setosaPetalWidth, c="r",label=flowerType[0])
plt.scatter(versicoPetalLength, versicoPetalWidth, c="g",label=flowerType[1])
plt.scatter(virginPetalLength, virginPetalWidth, c="b",label=flowerType[2])

plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.legend(loc=2)

plt.show()












