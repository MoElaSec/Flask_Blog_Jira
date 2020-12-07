# This script shows how to use the client in anonymous mode
# against jira.atlassian.com.
# from flaskblog import my_jira_client
from jira import JIRA
import re

# By default, the client will connect to a Jira instance started from the Atlassian Plugin SDK
# (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
# Override this with the options parameter.
options = {"server": "https://al-addin.atlassian.net"}
jira = JIRA(options, basic_auth=('mohd.debrecen@gmail.com', 'Tf33gXQ83Qa8pc6A2ArD452D'))

# jira = my_jira_client

# Get all projects viewable by anonymous users.
projects = jira.projects()
my_projects = []
for project in projects:
    my_projects.append({ 'Name':project.key, 'Description':project.name })
print(my_projects)
# Sort available project keys, then return the second, third, and fourth keys.
keys = sorted([project.key for project in projects])[2:5]
print(keys)

# Get an issue.
issue = jira.issue("TR-3")

# Find all comments made by Atlassians on this issue.
atl_comments = [
    comment
    for comment in issue.fields.comment.comments
    if re.search(r"@gmail.com$", comment.author.emailAddress)
]

# Add a comment to the issue.
# jira.add_comment(issue, "this is from python")

# Change the issue's summary and description.
# issue.update(
#     summary="I'm different!", description="Changed the summary to be different."
# )

# Change the issue without sending updates
# issue.update(notify=False, description="Quiet summary update.")

# You can update the entire labels field like this
# issue.update(fields={"labels": ["AAA", "BBB"]})

# Or modify the List of existing labels. The new label is unicode with no
# spaces
# issue.fields.labels.append(u"new_text")
# issue.update(fields={"labels": issue.fields.labels})

# Send the issue away for good.
# issue.delete()

# Linking a remote jira issue (needs applinks to be configured to work)
# issue = jira.issue("JRA-1330")
# issue2 = jira.issue("XX-23")  # could also be another instance
# jira.add_remote_link(issue, issue2)