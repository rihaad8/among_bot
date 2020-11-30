from UserHandling import User
import csv
class UserList(object):
    """docstring forUserList."""

    users = []

    def __init__(self):
        super(UserList, self).__init__()

    def addUser(self, User):
        self.users.append(User)

    def getNameList(self):
        nameList =[]
        for user in self.users:
            nameList.append(user.name)
        return nameList

    def saveListToFile(self, fileName = "users.csv"):
        with open(fileName, 'w', newline='') as usersFile:
            writer = csv.writer(usersFile)
            writer.writerow(vars(self.users[0]))
            for user in self.users:
                writer.writerow(user.toList())

    def loadListFromFile(self, fileName = "users.csv"):
        with open(fileName, 'r') as usersFile:
            reader = csv.reader(usersFile)
            firstLine = True
            for row in reader:
                if(firstLine):
                    firstLine = False
                    continue
                self.addUser(User.User(str(row[0]), str(row[1]), str(row[2]), str(row[3]), int(row[4])))
