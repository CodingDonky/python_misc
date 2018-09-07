import json
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

with open('jsonFiles/monsters.json') as f:
    data = json.load(f)

#pprint(data) # Prints out all of the Json File

numMonst = 325;
monstNames = np.chararray((numMonst,1))
monstCRs = np.array((numMonst,1))
#mmatrix = np.zeros((nrows, ncols))
x = data[0]["name"]

for i in range(0,325):
    monstNames[i] = data[i]["name"]
    monstCRs[i] = data[i]["challenge_rating"]
    print(data[i]["challenge_rating"])

randomMonstIndex = np.random.randint(numMonst);

print(data[randomMonstIndex]["name"])
print(data[randomMonstIndex]["challenge_rating"])

print(data[324])

gaussian_numbers = np.random.randn(1000)
plt.hist(monstCRs,10)
plt.title("CR Histogram")
plt.xlabel("CR")
plt.ylabel("Frequency")
plt.show()

#data["maps"][0]["id"]
#data["masks"]["id"]
#data["om_points"]
