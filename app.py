import requests # for API requests
import time # for measuring execution time

class app(object):
    def __init__(self, username):
        self.gitUserName = username

    def __str__(self):
        return self.checkUserExists()

    # check input github username exists
    def checkUserExists(self):
        githubAPI = f"https://api.github.com/users/{self.gitUserName}"
        status_code = requests.get(githubAPI).status_code
        response = requests.get(githubAPI).json()
        # user exists and github API rate limit is not exceeded
        if status_code == 200:
            start_time = time.time()
            return "\n{} [{:.2f}s]\n".format(self.getEmail(),time.time() - start_time)
        # user exists and github API rate limit is exceeded for the user
        elif str(response["message"]).startswith("API"):
            return f'\n{response["message"]}\n\n{response["documentation_url"]}\n'
        # user does not exist
        else:
            return f'\nProvided github username: "{self.gitUserName}" does not exists.\n'

    # get email address
    def getEmail(self):
        # result
        emails = []
    
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

        if len(emails) != 0:
            return ", ".join(map(str, emails))

        # check user's public commits
        commitsURL = f"https://api.github.com/users/{self.gitUserName}/events/public"
        payloads = requests.get(commitsURL).json()
        for payload in payloads:
            if payload["type"] == "PushEvent":
                data = payload["payload"]
                payload_email = data["commits"][0]["author"]["email"]
                if payload_email not in emails:
                    emails.append(payload_email)

        if len(emails)!= 0:
            return ", ".join(map(str, emails))
        else:
            return f'User: "{self.gitUserName}" has no public commits or a non-forked public repo'

if __name__ == "__main__":
    username = input("\nEnter GitHub username: ")
    print(app(username))
