## Part 1: Mastering Git Reset
Think of git reset as a way to "rewind" your project's timeline. Depending on which "flavor" of reset you use, you decide how much of your recent work you want to keep.
The Three Stages of Git
To understand resets, you must visualize where your code lives:
 * HEAD (Commit History): Your saved snapshots.
 * Index (Staging Area): Changes prepared for the next snapshot.
 * Working Directory: The actual files you are editing.
Reset Types Comparison
| Command | Moves HEAD? | Keeps Staging? | Keeps File Changes? | Best Use Case |
|---|---|---|---|---|
| --soft | Yes | Yes | Yes | Redoing a commit message or "squashing" many small commits into one. |
| --mixed (Default) | Yes | No | Yes | Unstaging files you didn't mean to include in a commit. |
| --hard | Yes | No | No | Nuclear Option: Deleting all work since the last commit to start over. |
> Analogy: > * Soft: You undo the "Save" on a document but keep the text on the screen.
>  * Mixed: You undo the "Save" and close the file, but the file is still on your desk.
>  * Hard: You throw the document in the paper shredder.
>
Part 2: Managing Releases & Pre-releases
Once your code is stable (or almost stable), you use GitHub Releases to package it for users.
What is a Pre-release?
A pre-release is a public version of your code labeled as "Alpha," "Beta," or "Release Candidate (RC)." It tells users: "This is available for testing, but don't use it for critical production tasks yet."
Step-by-Step Workflow
 * Drafting: In your GitHub sidebar, go to Releases > Draft a new release.
 * Tagging: Create a tag (e.g., v1.2.0-beta.1).
 * The Toggle: Check the box "This is a pre-release". This prevents it from being marked as the "Latest" version of your software.
 * Assets: Attach any compiled binaries or .zip files of your code.
Part 3: Professional Versioning (SemVer)
When assigning tags for your resets and releases, follow Semantic Versioning to keep your history clean.
 * MAJOR: Significant changes that break previous versions.
 * MINOR: Adding new features without breaking old ones.
 * PATCH: Small bug fixes.
For Pre-releases: Always append a suffix like -alpha or -beta so automated tools know it isn't a final version.
Summary Checklist
 * Use git reset --soft HEAD~1 to fix a commit without losing work.
 * Use Pre-releases to get feedback on new features without risking user stability.
 * Never use git reset --hard unless you are 100% sure you want to delete your progress.
> Source: Git SCM - Reset and GitHub Documentation - About Releases.
>
