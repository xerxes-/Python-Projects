import pickle
import requests

lst = []
nlst = []
i = 0

result = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
src = result.content

with open('downloaded.txt', 'wb') as dw:
    dw.write(src)

with open('downloaded.txt', 'r') as rdw:
    str = rdw.read()
    lst = str.split()

for i in range(len(lst)):
    nlst.append(lst[i].split(','))

file = 'Iris-ML.pkl'

#Pickled Python Object
fileObj = open(file, 'wb')
pickle.dump(nlst, fileObj)
fileObj.close()

#Reading a De-pickled object

fileObj = open(file, 'rb')
dpLst = pickle.load(fileObj)
print(dpLst)
fileObj.close()



