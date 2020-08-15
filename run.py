# python3 sample code to use "find_github_email" package

# import package
import find_github_email

# read GitHub username from user
username = input("\nEnter GitHub username: ")

response = find_github_email.find(username)
print(f"\n{response}\n")
