import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://emre81:Emre.2021@clusteremre0.mtcnw.mongodb.net/node-app")

mydb = myclient["node-app"]

print(myclient.list_database_names())