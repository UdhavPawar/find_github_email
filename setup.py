from setuptools import setup, find_packages

setup(
    name="find_github_email",
    packages=find_packages(),
    version="1.2.6",
    description="Find any GitHub user’s email address",
    long_description="Some of the best profiles simply have no contact information apart from a GitHub username. Hence, this python package is targetted for finding almost any GitHub user's email address, so you can easliy network/reach out to your favorite developers. Read more about it here: https://blog.udhav.com",
    author="Udhav Pawar",
    author_email="upawar78@gmail.com",
    url="https://github.com/UdhavPawar/find_github_email",
    download_url="https://github.com/UdhavPawar/find_github_email/archive/v1.0.tar.gz",
    keywords=["github-profile", "github-email", "python3", "github-api", "github", "email", "pypi", "pypi-package"],
    license="MIT",
    include_package_data = True,
    install_requires=["requests"],
)
