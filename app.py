import requests
import json

class app(object):
    def getEmail(self, username):
        # f"string" is a literal string, prefixed with 'f', which contains expressions inside braces.
        URL = f"https://api.github.com/users/{username}/events/public"

        response = requests.get(URL).json()
        return response

if __name__ == "__main__":
    username = "udhavpawar"
    print(app().getEmail(username))
