import PyQt4
import matplotlib
matplotlib.use('qt4agg')
import matplotlib.pyplot as plt


inputDataFile = open('iris.data','r')

# Attribute Information:
#    1. sepal length in cm
#    2. sepal width in cm
#    3. petal length in cm
#    4. petal width in cm
#    5. class:
#       -- Iris Setosa
#       -- Iris Versicolour
#       -- Iris Virginica

sepal_lens = []
sepal_widths = []
petal_lens = []
petal_widths = []
types = []

for line in inputDataFile:
    line = line.strip('\n')
    if line != "":
        words = line.split(",")
        sepal_lens.append(words[0])
        sepal_widths.append(words[1])
        petal_lens.append(words[2])
        petal_widths.append(words[3])
        types.append(words[4])

#define function to visualize data
def scatterplot(x_data, y_data, x_label="", y_label="", title="", color = "r", yscale_log=False):
    # Create the plot object
    _, ax = plt.subplots()
    # Plot the data, set the size (s), color and transparency (alpha)
    # of the points
    ax.scatter(x_data, y_data, s = 10, color = color, alpha = 0.75)
    if yscale_log == True:
        ax.set_yscale('log')
    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

#show sepal data
scatterplot(sepal_lens,sepal_widths,"x","y","Sepal classification","r")
scatterplot(petal_lens,petal_widths,"x","y","Pepal classification","g")
plt.show()






