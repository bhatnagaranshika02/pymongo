import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
myquery = {"address":{"$regex":"^S"}
mycol.delete_many(myquery)
print(x.deleted_count,"document deleted")
mycol.delete_many({}) #Delete all
