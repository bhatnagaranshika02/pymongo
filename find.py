import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27071")
mydb = myclient["mydatabase"]
mycol = mydb["student"]
x=mycol.find_one()
print(x)
for i in mycol.find():
    print(i)

for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)

for x in mycol.find({},{ "name": 1, "address": 0 }):
  print(x) 
