import requests

class app(object):
    def __init__(self, username):
        self.gitUserName = username

    def __str__(self):
        return self.checkUserExists()

    # check input github username exists
    def checkUserExists(self):
        status_code = requests.get(f"https://api.github.com/users/{self.gitUserName}").status_code
        if status_code == 200:
            return self.getEmail()
        else:
            return f'\nProvided github username: "{self.gitUserName}" does not exists.\n'


    # get email address
    def getEmail(self):
        # result
        emails = []

        # check user's public commits
        commitsURL = f"https://api.github.com/users/{self.gitUserName}/events/public"
        payloads = requests.get(commitsURL).json()
        for payload in payloads:
            if payload["type"] == "PushEvent":
                data = payload["payload"]
                payload_email = data["commits"][0]["author"]["email"]
                if payload_email not in emails:
                    emails.append(payload_email)

        if len(emails) != 0:
            return "\n" + ", ".join(map(str, emails)) + "\n"

        # check user's non-forked public repos
        reposURL = f"https://api.github.com/users/{self.gitUserName}/repos"
        repos = requests.get(reposURL).json()
        for repo in repos:
            repo_name = repo["name"]
            if repo["fork"] == False:
                commitsURL = f"https://api.github.com/repos/{self.gitUserName}/{repo_name}/commits"
                commits = requests.get(commitsURL).json()
                for commit in commits:
                    commit_email = commit["commit"]["author"]["email"]
                    if commit_email not in emails:
                        emails.append(commit_email)

        if len(emails)!= 0:
            return "\n" + ", ".join(map(str, emails)) + "\n"
        else:
            return f'\nUser: "{self.gitUserName}" has no public commits or a non-forked public repo\n'

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    print(app(username))
