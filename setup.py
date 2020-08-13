from setuptools import setup, find_packages

setup(
    name="find_github_email",
    packages=find_packages(),
    version="1.1",
    description="Find any GitHub user’s email address",
    long_description=open('README.md').read(),
    author="Udhav Pawar",
    author_email="upawar78@gmail.com",
    url="https://github.com/UdhavPawar/find_github_email",
    download_url="https://github.com/UdhavPawar/find_github_email/archive/v1.0.tar.gz",
    keywords=["github-profile", "github-email", "python3", "github-api", "github", "email", "pypi", "pypi-package"],
    license="MIT",
    include_package_data = True,
    install_requires=["requests"],
)
