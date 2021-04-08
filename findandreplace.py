import os
import git
import json


class Author:
    name: str
    email: str


with open('config.json') as config_file:
    config = json.load(config_file)

repository_list = config['repository_list']
find_and_replace_list = config['find_and_replace_list']
file_list = config['file_list']
commit_message = config['commit_message']
base_branch = config['base_branch']
repositories_directory = config['repositories_directory']
repository_author = Author
repository_author.name = config['repository_author_name']
repository_author.email = config['repository_author_email']
ssh_key = config['ssh_key']

for repository in repository_list:
    ticket_id = repository[0]
    service_repo = repository[1]
    path_to_repository = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      repositories_directory + ticket_id)
    cloned_repository = git.Repo.clone_from(service_repo, path_to_repository, branch=base_branch,
                                            env={"GIT_SSH_COMMAND": 'ssh -i ' + ssh_key})
    new_branch = cloned_repository.create_head(ticket_id)
    new_branch.checkout()
    for checked_file in file_list:
        path_to_repository_file = os.path.join(path_to_repository, checked_file)
        repo_file = pathlib.Path(path_to_repository_file)
        if repo_file.exists():
            for texts in find_and_replace_list:
                text_to_find = texts[0]
                text_to_replace = texts[1]
                file = open(path_to_repository_file, 'r')
                current_file_data = file.read()
                file.close()
                new_file_data = current_file_data.replace(text_to_find, text_to_replace)
                file = open(path_to_repository_file, 'w')
                file.write(new_file_data)
                file.close()
            cloned_repository.index.add(path_to_repository_file)
        else:
            print("Ignoring "+path_to_repository_file+". Not found")
    cloned_repository.index.commit(commit_message.format(ticket_id), author=repository_author)
    origin = cloned_repository.remote(name='origin')
    origin.push(new_branch)
