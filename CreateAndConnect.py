import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27027/")
mydb = myclient["mydatabase"]

