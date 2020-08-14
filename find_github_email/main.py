import requests # for API requests
import time # for measuring execution time

class findGitEmail(object):
    def __init__(self, username):
        self.git_username = username

    def get(self):
        return self.__checkUserExists()

    # check input github username exists
    def __checkUserExists(self):
        githubAPI = f"https://api.github.com/users/{self.git_username}"
        response = requests.get(githubAPI)
        response_json = response.json()

        # user exists and github API rate limit is not exceeded
        if response.status_code == 200:
            start_time = time.time()
            emails = self.__getEmail()
            emails.append("{:.2f}s".format(time.time() - start_time))
            return emails
        # user exists and github API rate limit is exceeded for the user
        elif str(response_json["message"]).startswith("API"):
            return f'{response_json["message"]} Documentation URL: {response_json["documentation_url"]}'
        # user does not exist
        else:
            return f'Provided github username: "{self.git_username}" does not exists.'

    # get email address
    def __getEmail(self):
        # result
        emails = []

        # check user's non-forked public repos
        reposURL = f"https://api.github.com/users/{self.git_username}/repos"
        repos = requests.get(reposURL).json()
        for repo in repos:
            repo_name = repo["name"]
            if repo["fork"] == False:
                commitsURL = f"https://api.github.com/repos/{self.git_username}/{repo_name}/commits"
                commits = requests.get(commitsURL).json()
                for commit in commits:
                    commit_email = commit["commit"]["author"]["email"]
                    if commit_email not in emails:
                        emails.append(commit_email)

        if len(emails) != 0:
            return emails

        # check user's public commits
        commitsURL = f"https://api.github.com/users/{self.git_username}/events/public"
        payloads = requests.get(commitsURL).json()
        for payload in payloads:
            if payload["type"] == "PushEvent":
                data = payload["payload"]
                payload_email = data["commits"][0]["author"]["email"]
                if payload_email not in emails:
                    emails.append(payload_email)

        if len(emails)!= 0:
            return emails
        else:
            return emails.append(f'User: "{self.git_username}" has no public commits or a non-forked public repo')

def find(username):
    finder_response = findGitEmail(username).get()
    if type(finder_response) is list:
        response = {
            'found' : True,
            'execution_time' : finder_response.pop(),
            'email': finder_response
        }
    else:
        response = {
            'found' : False,
            'error_message' : finder_response
        }

    return response
