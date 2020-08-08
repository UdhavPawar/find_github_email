import requests
import json

class app(object):
    def getEmail(self, username):
        # f"string" is a literal string, prefixed with 'f', which contains expressions inside braces.
        URL = f"https://api.github.com/users/{username}/events/public"

        response = requests.get(URL).json()
        email = response[0]["payload"]["commits"][0]["author"]["email"]
        return email

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    print(app().getEmail(username))
