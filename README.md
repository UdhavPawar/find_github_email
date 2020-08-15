<!-- Header -->
<h1 align="center">Find GitHub Email</h1>

<!-- Labels -->
<p align="center">
    <img src="https://img.shields.io/badge/package-pip-blue.svg?style=flat">
    <img src="https://img.shields.io/badge/version-1.2.2-blueviolet.svg?style=flat">
    <img src="https://img.shields.io/badge/code-python-orange.svg?style=flat">
    <img src="https://img.shields.io/badge/code-python3-yellow.svg?style=flat">
    <img src="https://img.shields.io/badge/build-passing-green.svg?style=flat">
    <img src="https://img.shields.io/badge/license-MIT-ff69b4.svg?style=flat">
</p>

<!-- Jumpers -->
<p align="center">
  <a href="#application">Application</a> •
  <a href="#installation">Installation</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#contributing">Contribute</a> •
  <a href="#package">Package</a>
</p>

## Application

- GitHub brings together the world's largest community of developers to discover, share, and build better software. 
- GitHub profiles often include an email address, twitter handle, and/or link to a personal website. 
- However, some of the best profiles simply have no contact information apart from a GitHub username. 
- Hence, this python package is targetted for finding almost any GitHub user's email address, so you can easliy network/reach out to your favorite developers :bowtie::bow:

## Installation

Install package use the package manager [pip](https://pypi.org/project/find-github-email/).

> python2

![python](./svgs/py2install.svg)
```bash
pip install find-github-email
```
OR
```bash
python -m pip install find-github-email
```
> python3

![python3](./svgs/py3install.svg)

```bash
pip3 install find-github-email
```
OR
```bash
python3 -m pip install find-github-email
```
> Facing an issue? Check the [Issues](https://github.com/UdhavPawar/find_github_email/issues) section or open a new issue.


## How To Use

![example](./svgs/run.svg)

> python2 run.py
```python
# python sample code to use "find_github_email" package

# import package
import find_github_email

# read GitHub username from user
username = raw_input("\nEnter GitHub username: ")

response = find_github_email.find(username)
print "\n",response,"\n"
```
> python3 run.py
```python3
# python3 sample code to use "find_github_email" package

# import package
import find_github_email

# read GitHub username from user
username = input("\nEnter GitHub username: ")

response = find_github_email.find(username)
print(f"\n{response}\n")
```
> Facing an issue? Check the [Issues](https://github.com/UdhavPawar/find_github_email/issues) section or open a new issue.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change/fix.

## Package
[PyPi](https://pypi.org/project/find-github-email/)

## License
[MIT](https://github.com/UdhavPawar/find_github_email/blob/master/LICENSE)
