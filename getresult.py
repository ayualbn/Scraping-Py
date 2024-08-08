#The machine learning mechanism
import csv
from sklearn import tree

x = [] #input
y = [] #output
with open ('usedcarsale.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    for _ in range(1):
        next(csvfile)
    for line in data:
        x.append(line[0:2])
        y.append(line[2])

clf = tree.DecisionTreeClassifier() 
clf = clf.fit(x , y)

new_car = str(input("enter the name of your car: "))
new_mile = str(input("enter the miles of your used car: "))
new_data = [new_car , new_mile]
result = clf.predict(new_data)

print(result)