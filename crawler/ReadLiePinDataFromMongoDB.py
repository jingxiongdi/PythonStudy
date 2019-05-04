import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.LiePinData
data = db.android
result = data.find()

allKeys = data.find_one().keys()
for key in allKeys:
    for r in result:
        print(r[key])

