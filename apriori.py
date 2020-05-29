# Support(A->B) = (Teams containing A&&B)/(Total Teams)
# Confidence(A->B) = (Teams containing A&&B)/(Teams containing A)
# Lift(A->B) = (Support(A->B)/Support(A)*Support(B))

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

csvFile = 'store_data' + '.csv'
store_data = pd.read_csv(csvFile, header=None)
# print(store_data.head())

num_records = len(store_data)

print(num_records)
records = []
for i in range (0,num_records):
  records.append([str(store_data.values[i,j]) for j in range(0,6)])

# string_num = store_data.str.count()
association_rules = apriori(records,min_support=0.05,min_confidence=0.2,min_length=2)
association_results = list(association_rules)
print(len(association_results))

results = []
for item in association_results:
  pair = item[0]
  items = [x for x in pair]
  if(len(items) > 1):
    value0 = str(items[0])
    value1 = str(items[1])
    value2 = str(item[1])[:7]
    value3 = str(item[2][0][2])[:7]
    value4 = str(item[2][0][3])[:7]

    rows = (value0, value1, value2, value3, value4)
    results.append(rows)
    Labels = ['Title1', 'Title2', 'Support', 'Confidence', 'Lift']
  
    suggestion = pd.DataFrame.from_records(results,columns=Labels)
    print(suggestion)
  