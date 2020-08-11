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
        except Exception as error:
            return str(error)

    # get email address
    def getEmail(self):
        # f"string" is a literal string, prefixed with 'f', which contains expressions inside braces.
        URL = f"https://api.github.com/users/{self.gitUserName}/events/public"

        response, email = requests.get(URL).json(), None
        for payload in response:
            if payload["type"] == "PushEvent":
                # print(payload["id"])
                data = payload["payload"]
                if email is None:
                    email = data["commits"][0]["author"]["email"]
                    break
        return email

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    print(app(username))
