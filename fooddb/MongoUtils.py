import pymongo

class MongoDBConnection:
    def __init__(self,dbName , collName ,dbUrl,userName = None , passwd=None):
        self.__dbName = dbName
        self.__collName = collName
        self.__user_name = userName
        self.__password = passwd
        self.__dbURL = dbUrl
        self.mydb = None
        self.mycoll = None
    
    def create_connection(self):
        try:
            client = pymongo.MongoClient(self.__dbURL) #client connection

            if self.__dbName in client.list_database_names():
                self.mydb = client[self.__dbName] # creates db object.

                if self.__collName in self.mydb.list_collection_names():
                    self.mycoll = self.mydb[self.__collName] #creates coll object
                    print(f'Connection successfull : {self.__dbName} : {self.__collName}')
                    return self.mycoll 
                else:
                    raise Exception('Collection not found with given name , please check..')

            else:
                raise Exception(' database not found with given name , please check ...')
        except Exception as e:
            print(f'Exception occured while making client connection {e}')


# dbObj = MongoDBConnection('ProjectDB','todolist_coll','mongodb://localhost:27017/') 
# print(dbObj)

# coll = dbObj.create_connection()
# print(coll)
