# Bulk Find and Replace in multiple files in multiple Git Repositories

## Area of use for this script
This script is useful when you want to change multiple part of multiple files in multiple git repositories in bulk.
Script is creating a new branch from the given base branch and committing changes into it. Maybe push to remote also can be added with small change.

*I used this script for changing the auto scaling config inside the Cloudformation templates for multiple micro services in our project.*

## How to run the script?
First clone repository
```ssh
git clone https://github.com/omerkarabacak/bulk-find-and-replace-in-git-repositories.git
```
### What to do before run?
In config.json file, change these;

* Add your new branch names and repositories in **repository_list**
* Add texts to find and replace **find_and_replace_list**
* Add files to check in **file_list**
* Change commit message **commit_message**
* Change base branch **base_branch**
* Change repository directory if needed **repositories_directory**
* Change author name **repository_author.name**
* Change author email **repository_author.email**
* Change SSH key path if you need something specific **ssh_key**

You are ready to go!
### How to run with Docker?
There are 2 options.
You can build your Docker image with Dockerfile or use ready public Docker image from Docker Hub.

#### Option 1: Build your own Docker image and use it
Build Docker image:
```ssh
docker build -t bulk-find-and-replace-in-git-repositories:1.1 .
```
Run with built local Docker image:
```ssh
docker run --rm -v $(pwd)/config.json:/app/config.json -v $(pwd)/repositories:/app/repositories -v ~/.ssh/id_rsa:/root/.ssh/id_rsa bulk-find-and-replace-in-git-repositories:1.1
```
#### Option 2: Use public Docker image hosted on Docker Hub
Run with public Docker image:
```ssh
docker run --rm -v $(pwd)/config.json:/app/config.json -v $(pwd)/repositories:/app/repositories -v ~/.ssh/id_rsa:/root/.ssh/id_rsa ghcr.io/omerkarabacak/bulk-find-and-replace-in-git-repositories:1.1
```
### How to run with Python virtual environment?
First create virtual environment
```ssh
python3 -m venv env
```
Enter virtual environment
```ssh
source env/bin/activate
```
Install dependencies
```ssh
pip install -r requirements.txt
```
Run script
```ssh
python findandreplace.py
```

#### Which Python version?
Tested with 3.6.8