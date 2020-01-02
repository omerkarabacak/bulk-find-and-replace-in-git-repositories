import fileinput
import os
import git


class Author:
    name: str
    email: str


repository_list = [
    [
        'JIRA-id-1111',
        'git@gitlab.example.com:micro-services/example-service-1.git'
    ],
    [
        'JIRA-id-1112',
        'git@gitlab.example.com:micro-services/example-service-2.git'
    ]
]
find_and_replace_list = [
    [
        'cron(0 0 5 1/1 * ? *)',
        'cron(0 0 5 ? * MON,TUE,WED,THU,FRI *)'
    ],
    [
        'cron(0 0 20 1/1 * ? *)',
        'cron(0 0 20 ? * MON,TUE,WED,THU,FRI *)'
    ]
]
file_list = [
    'infrastructure/stack-scaling-dev.yml',
    'infrastructure/stack-scaling-int.yml',
    'infrastructure/stack-scaling-test.yml'
]
commit_message = '{} Changed autoscaling schedule for dev, int and test environments'
base_branch = 'develop'
repositories_directory = 'repositories/'

repository_author = Author
repository_author.name = 'Omer Karabacak'
repository_author.email = 'email@example.com'
ssh_key = '~/.ssh/id_rsa'

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
        for texts in find_and_replace_list:
            text_to_find = texts[0]
            text_to_replace = texts[1]
            with fileinput.FileInput(path_to_repository_file, inplace=True) as file:
                for line in file:
                    line.replace(text_to_find, text_to_replace)
        cloned_repository.index.add(path_to_repository_file)
    cloned_repository.index.commit(commit_message.format(ticket_id), author=repository_author)
