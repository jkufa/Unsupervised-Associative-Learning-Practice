# Generates a dummy dataset for testing purposes
from random import seed
from random import randint
import random

dataset = open("another_test_dataset.csv","w")

# Seed random number
seed(1)

datas = ['wub', 'apple', 'foo', 'bar', 'all', 'wow', 'bar', 'eight', 'meme', 'dog','pupper','gamer','lanturn','sadness','dark','clouds','epic']
test = []

row = []
for i in range(5000):
  column_num = randint(6,6) # Generate between 4 and 6 columms
  row = random.sample(datas,column_num) # Create row
  dataset.write(', '.join(row))
  if(i != 4999):
    dataset.write('\n') 
  row.clear()

dataset.close()