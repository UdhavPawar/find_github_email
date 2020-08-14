# Find GitHub Email

GitHub brings together the world's largest community of developers to discover, share, and build better software. GitHub profiles often include an email address, twitter handle, and/or link to a personal website. However, some of the best profiles simply have no contact information apart from a GitHub username. Hence, this python module is targetted for finding almost any GitHub user's email address, so you can easliy network/reach out to your favorite developers :)

## Installation

To install this python package, use the package manager [pip](https://pypi.org/project/find-github-email/).

```bash
pip install find-github-email
```
OR
```bash
python3 -m pip install find-github-email
```

## Usage


```python3
import find_github_email

username = input("Enter GitHub username: ")
response = find_github_email.find(username)

print(response)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change and make sure to update tests as appropriate.

## License
[MIT](https://github.com/UdhavPawar/find_github_email/blob/master/LICENSE)
