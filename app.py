import requests

class app(object):
    def __init__(self, username):
        self.gitUserName = username

    def __str__(self):
        return self.checkUserExists()

    # check input github username exists
    def checkUserExists(self):
        try:
            return self.getEmail()
        except:
            return "User does not exist"

    # get email address
    def getEmail(self):
        # f"string" is a literal string, prefixed with 'f', which contains expressions inside braces.
        URL = f"https://api.github.com/users/{self.gitUserName}/events/public"

        response = requests.get(URL).json()
        email = response[0]["payload"]["commits"][0]["author"]["email"]
        return email

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    print(app(username))
