from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")
database = client["Project"]
collection = database["players"]
collection19 = database["players19"]

def query9():
    name = input("Enter player name: ")

    pipeline = [
        {
            u"$match": {
                u"short_name": u""+name
            }
        },
        {
            u"$project": {
                u"short_name": 1.0,
                u"overall": 1.0
            }
        }
    ]

    cursor = collection19.aggregate(
        pipeline,
        allowDiskUse = False
    )
    try:
        for doc in cursor:
            m=(doc["overall"])
    finally:
        client.close()

    pipeline = [
        {
            u"$match": {
                u"short_name": u""+name
            }
        },
        {
            u"$project": {
                u"short_name": 1.0,
                u"overall": 1.0
            }
        }
    ]

    cursor = collection.aggregate(
        pipeline,
        allowDiskUse = False
    )
    try:
        for doc in cursor:
            b=(doc["overall"])
    finally:
        client.close()

    c = m-b

    if c == 0:
        print("\nNo Change in rating")
    elif c > 0:
        print("Rating increased by: ",c)
    else:
        print("Rating decreased by: ", abs(c))

##query9()