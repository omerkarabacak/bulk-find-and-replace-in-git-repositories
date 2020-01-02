# Bulk Find and Replace in multiple files in multiple Git Repositories

## Area of use for this script
This script is useful when you want to change multiple part of multiple files in multiple git repositories in bulk.
Script is creating a new branch from the given base branch and committing changes into it. Maybe push to remote also can be added with small change.

*I used this script for changing the auto scaling config inside the Cloudformation templates for multiple micro services in our project.*

## What to configure before run?

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

## How to run?
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

## Which Python version?
Tested with 3.6.8