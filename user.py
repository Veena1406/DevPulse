from database.mongodb import mongo


class User:

    @staticmethod
    def create_user(username, email, password):

        mongo.db.users.insert_one({
            "username": username,
            "email": email,
            "password": password
        })

    @staticmethod
    def find_by_email(email):

        return mongo.db.users.find_one({
            "email": email
        })

    @staticmethod
    def find_by_username(username):

        return mongo.db.users.find_one({
            "username": username
        })