# 📘 The Modern Git & Open Source Guide (2026)
*A comprehensive guide to modern commands, rebasing, and the forking workflow.*

---

## 1. Project Initialization & Setup
| Command | Action |
| :--- | :--- |
| `git init` | Start a new local repository. |
| `git clone <url>` | Clone a remote repository. |
| `git config --global pull.rebase true` | **Best Practice:** Sets rebase as the default for all pulls. |

---

## 2. Modern Branching (The `switch` Command)
Git now uses `switch` instead of `checkout` for moving between branches to avoid confusion.

* **Create and jump to a branch:** `git switch -c feature-name`
* **Switch back to main:** `git switch main`
* **Toggle to previous branch:** `git switch -`



---

## 3. Undoing Mistakes Gracefully
Use `restore` instead of the old `reset` or `checkout` methods for files.

* **Discard unstaged changes:** `git restore <filename>`
* **Unstage a file (keep your code):** `git restore --staged <filename>`
* **The "Clean Slate":** `git reset --hard HEAD` (Wipes all changes since last commit).
* **Delete junk files/folders:** `git clean -fd`

---

## 4. Resolving Merge Conflicts
Conflicts happen when Git doesn't know which version of a line to keep.

### The Workflow:
1.  **Locate the markers:** Look for `<<<<<<< HEAD`, `=======`, and `>>>>>>>`.
    * Everything between `HEAD` and `====` is **your** change.
    * Everything between `====` and the branch name is the **incoming** change.
2.  **Edit the file:** Manually delete the markers and keep the version of the code you want (or combine them).
3.  **Stage it:** `git add <filename>`
4.  **Finish it:**
    * If merging: `git commit`
    * If rebasing: `git rebase --continue`

---

## 5. The Forking Workflow (Working on Open Source)
When you don't have "Write" access to a project, you **Fork** it. This creates your own copy on GitHub.

### Setup (Only do this once):
1.  **Clone your fork:** `git clone <your-fork-url>`
2.  **Add the original repo as "Upstream":**
    `git remote add upstream <original-project-url>`
3.  **Verify:** `git remote -v` (You should see `origin` as yours and `upstream` as the original).



---

## 6. Syncing your Fork
If the original project (`upstream`) adds new features, you need to bring them into your fork (`origin`).

### The Modern Way (Rebase):
1.  **Fetch the latest:** `git fetch upstream`
2.  **Move your work on top:** `git rebase upstream/main`
3.  **Update your GitHub:** `git push origin main --force-with-lease`
    * *Note: Use `--force-with-lease` after rebasing a branch that you've already pushed.*



---

## 7. Conflicts During a Fork Sync
If you edited a line in your fork that was also changed in the `upstream` project, a rebase will pause.

1.  Git will say: *"CONFLICT (content): Merge conflict in <filename>"*.
2.  Open the file and resolve the conflict manually.
3.  Run `git add <filename>`.
4.  Run `git rebase --continue`.
5.  Repeat if necessary, then push: `git push origin HEAD --force-with-lease`.

---

## 8. 🚀 Ultimate Quick-Reference Cheat Sheet

| Category | Task | Command |
| :--- | :--- | :--- |
| **Setup** | Set name/email | `git config --global user.name "Your Name"` |
| **Branching** | Create & move | `git switch -c <name>` |
| **Branching** | Delete branch | `git branch -d <name>` |
| **Saving** | Stage all | `git add .` |
| **Saving** | Commit | `git commit -m "Message"` |
| **Syncing** | Pull latest | `git pull --rebase origin main` |
| **Syncing** | Push to cloud | `git push origin HEAD` |
| **Undo** | Discard edits | `git restore <file>` |
| **Undo** | Unstage file | `git restore --staged <file>` |
| **Open Source** | Link original | `git remote add upstream <url>` |
| **Open Source** | Sync original | `git fetch upstream && git rebase upstream/main` |

---

## 9. Common Scenarios

### "I need to update my branch with main"

```bash
# latest : at branch
git fetch origin main:main      # fetch without switching to main
git rebase main
# ----------- Conflict : rebase paused--------------- #
# ----------- Resolve Conflict via VScode ----------- #
# ----------- After conflict resolved --------------- #
git add <conflicted_file>
git rebase -- continue
git push origin <branch> --force-with-lease
```

```bash
# old command
git checkout main
git pull origin main
git checkout your-branch
git merge main              # Or: git rebase main
```


### "I need to check if my branch is updated with main"


#### 0. basic

`git fetch origin main` : Download teh changes on main without changing you local main
`git fetch origin main:main` : Update local main with the latest update
`git status` : compare the status against main

#### 1. The Visual Comparison (Most Intuitive)

If you want to see which commits exist on one branch but not the other, use the "Double Dot" syntax with the log.

* **To see commits on your branch that are NOT in main:**
`git log main..ds5_update --oneline --graph`
* **To see commits on main that you are MISSING:**
`git log ds5_update..main --oneline --graph`

#### 2. The File-Level Diff

If you don't care about the commit history but want to see the actual **code changes** between the two branches:

* **View all code differences:**
`git diff main..ds5_update`
* **See only a summary of which files changed:**
`git diff main..ds5_update --stat`



#### 3. The "Left-Right" Comparison

This is a powerful "pro" command that shows you both sides of the divergence at once. It tells you which commits are unique to each branch.

`git log --left-right --oneline main...ds5_update`

* Lines starting with `<` are unique to **main**.
* Lines starting with `>` are unique to **your branch**.

---

#### 4. Using VS Code (The "Developer" Way)

Since you are using VS Code on macOS, you don't actually need the terminal for this:

1. Open the **Source Control** tab (shortcut: `Ctrl + Shift + G`).
2. If you have the **GitLens** extension installed (highly recommended for Python devs), look at the **"Branch Comparison"** section.
3. Select `main` as the reference. It will show you a folder-tree view of every line of code that differs.

---

##### Summary of Differences

| Requirement | Command |
| --- | --- |
| **Commit Names** | `git log main..ds5_update --oneline` |
| **Visual Tree** | `git log --graph --all --oneline` |
| **Actual Code** | `git diff main` |
| **Files Changed** | `git diff main --stat` |


---

## ⚠️ The Golden Rule
**Only rebase branches you own (local feature branches).** Never rebase a public branch like `main` if other people are using it, as it will break their history and cause massive conflicts for the team.
