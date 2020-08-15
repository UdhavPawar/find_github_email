# python sample code to use "find_github_email" package

# import package
import find_github_email

# read GitHub username from user
username = raw_input("\nEnter GitHub username: ")

response = find_github_email.find(username)
print "\n",response,"\n"
