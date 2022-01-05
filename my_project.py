import pygit2

commit1='3e5307d'
commit2='66f416b'

rep='/home/saeedeh/Work/codean_job/interview-challenge-saeedeh-baneshi/test-repository.git'
rep='/home/saeedeh/Work/codean_job/test_repo'
repository = pygit2.Repository(rep)
tree_from = repository.revparse_single(commit1)
tree_to = repository.revparse_single(commit2)

# Calculate the difference between them
patches = repository.diff(tree_from, tree_to)
patches.find_similar()


# Go through all patches
for patch in patches:
    blob_old = patch.delta.old_file
    blob_new = patch.delta.new_file


    # Go through all patch hunks
    for hunk in patch.hunks:

        # Now we can finally go through all lines
        for line in hunk.lines:
            print(line.content)
            # We can skip all contextual lines
            if line.origin == " ":
                continue
print(patches[0].hunks[0].lines[0].content)