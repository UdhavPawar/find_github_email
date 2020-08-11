import requests

class app(object):
    def __init__(self, username):
        self.gitUserName = username

    def __str__(self):
        return self.checkUserExists()

    # check provided github username exists
    def checkUserExists(self):
        status_code = requests.get(f"https://api.github.com/users/{self.gitUserName}").status_code
        if status_code == 200:
            return self.getEmail()
        else:
            return f'\nProvided github username: "{self.gitUserName}" does not exists.\n'

    # get email address
    def getEmail(self):
        # check user's public commits
        commitsURL, email = f"https://api.github.com/users/{self.gitUserName}/events/public", None

        payloads = requests.get(commitsURL).json()
        for payload in payloads:
            if payload["type"] == "PushEvent":
                # print(payload["id"])
                data = payload["payload"]
                if email is None:
                    email = data["commits"][0]["author"]["email"]
                    return f"\n{email}\n"

        # email not found due to
        return f'\nUser: "{self.gitUserName}" has no public commits or a non-forked public repo\n'

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    print(app(username))
