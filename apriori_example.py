import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

data = pd.read_csv('store_data.csv', header=None)
# data = pd.read_csv('teams.csv', header=None)
data.head()

# Data preprocessing

records = []
print(len(data))
for i in range(len(data)):
    records.append([str(data.values[i,j]) for j in range(0, 20)])
    # records.append([str(data.values[i,j]) for j in range(0, 6)])

# for item in records:
#     print(item)

association_rules = apriori(records, min_support=0.0045, min_confidence=0.5, min_lift=3, min_length=2)
association_results = list(association_rules)

# print(len(association_results))
# print(association_results[0])

for item in association_results:
    # print(item)
    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")