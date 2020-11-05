from pymongo import MongoClient
#Database functions
class Database:

    #Constructor configures client and db
    def __init__(self):
        self.__client = MongoClient('localhost:27017')
        self.__db = self.__client.TaskManager

    #Add trip history
    def addHistory(self, output):
        self.__db.userHistory.insert_one(output)

    #Retrieve trip history
    def fetchHistory(self):
        docs = self.__db.userHistory.find()
        data = []
        for i in docs:
            data.append(i)
        return data

    #Delete trip history
    def dropHistory(self):
        self.__db.userHistory.drop()
