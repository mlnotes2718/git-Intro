# Git Fundamentals — Hands-On Tutorial

*A step-by-step tutorial that teaches Git by doing, using a real Python project.*

---

## Table of Contents

- [What is Git and GitHub?](#what-is-git-and-github)
- [Step 1 — Install Git](#step-1--install-git)
- [Step 2 — Install VS Code](#step-2--install-vs-code)
- [Step 3 — Download and Rename the Project](#step-3--download-and-rename-the-project)
- [Step 4 — Clean the Project Folder](#step-4--clean-the-project-folder)
- [Step 5 — README and .gitignore](#step-5--readme-and-gitignore)
- [Step 6 — git init](#step-6--git-init)
- [Step 7 — git add](#step-7--git-add)
- [Step 8 — First Commit and Push to GitHub](#step-8--first-commit-and-push-to-github)
- [Step 9 — Working with Folders and Files](#step-9--working-with-folders-and-files)
- [Step 10 — Understanding .gitignore](#step-10--understanding-gitignore)
- [Step 11 — .gitignore in Action](#step-11--gitignore-in-action)
- [Step 12 — Tracking Changes with git log](#step-12--tracking-changes-with-git-log)
- [Step 13 — Simulating a Remote Change](#step-13--simulating-a-remote-change)
- [Step 14 — git fetch, git diff, git merge vs git pull](#step-14--git-fetch-git-diff-git-merge-vs-git-pull)
- [Step 15 — Set Up a Python Environment with uv](#step-15--set-up-a-python-environment-with-uv)
- [Step 16 — Create a Feature Branch and Write the BMI Calculator](#step-16--create-a-feature-branch-and-write-the-bmi-calculator)
- [Step 17 — Push the Branch, Open a PR, and Merge](#step-17--push-the-branch-open-a-pr-and-merge)
- [Step 18 — Introduce a Bug (No Tests)](#step-18--introduce-a-bug-no-tests)
- [Step 19 — Undo One Commit with git revert](#step-19--undo-one-commit-with-git-revert)
- [Step 20 — Introduce the Same Bug Across Two Commits](#step-20--introduce-the-same-bug-across-two-commits)
- [Step 21 — Undo Multiple Commits with git reset](#step-21--undo-multiple-commits-with-git-reset)
- [Step 22 — revert vs reset: When to Use Which](#step-22--revert-vs-reset-when-to-use-which)
- [Step 23 — Discard Before Committing with git restore and git clean](#step-23--discard-before-committing-with-git-restore-and-git-clean)
- [Step 24 — Tag the Good Code as a Release](#step-24--tag-the-good-code-as-a-release)
- [Step 25 — Introduce the Bug Again, PR and Merge](#step-25--introduce-the-bug-again-pr-and-merge)
- [Step 26 — Roll Back to the Release Tag with git reset](#step-26--roll-back-to-the-release-tag-with-git-reset)
- [Step 27 — Redo the Bug Fix with Proper Tests](#step-27--redo-the-bug-fix-with-proper-tests)
- [Step 28 — Amend, Commit, Push, and Tag v1.0.1](#step-28--amend-commit-push-and-tag-v101)

---

## What is Git and GitHub?

**Git** is a version control system. It records every change you make to your code, lets you travel back in time to any previous state, and lets multiple people work on the same project without overwriting each other's work.

**GitHub** is a cloud hosting service for Git projects. You store your code there so it is backed up, shareable, and accessible from any machine.

Think of it this way: Git is the tool you run on your computer; GitHub is the website where you keep a copy.

---

## Step 1 — Install Git

### macOS

macOS does not ship with Git pre-installed, but it provides the easiest possible way to trigger the installation. Open **Terminal** and type:

```bash
git --version
```

If Git is not installed, macOS will immediately pop up a dialog asking you to install the **Xcode Command Line Tools** — click **Install** and wait for it to finish. This installs Git along with other developer tools.

After installation, confirm it worked:

```bash
git --version
# git version 2.x.x
```

### Linux

Git is installed by default on most Linux distributions. Verify with:

```bash
git --version
```

If it is missing (rare), install it with your package manager:

```bash
# Debian / Ubuntu
sudo apt install git

# Fedora / RHEL
sudo dnf install git
```

### Configure Git (all platforms — do this once)

Tell Git who you are. These details are attached to every commit you make:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Set VS Code as the default editor (optional but recommended)
git config --global core.editor "code --wait"

# For macOS user you may need the following:
git config --global http.postBuffer 524288000

# Confirm your settings
git config --list
git config --global --list
```

---

## Step 2 — Install VS Code

Visual Studio Code is a free code editor with excellent built-in Git support.

Download it from **https://code.visualstudio.com** and follow the installer for your operating system.

After installing, open VS Code and install the following extension:

- **GitHub Pull Requests and Issues** — adds a "Publish to GitHub" button directly in the Source Control panel, which you will use in Step 8.

To install an extension: press `Ctrl+Shift+X` (or `Cmd+Shift+X` on Mac), search for the extension name, and click **Install**.

---

## Step 3 — Download and Rename the Project

### Download the starter repository

We are going to use a sample repository as a starting point. Download it as a ZIP file — **not** by cloning — because we want to start with a clean history of our own.

1. Open **https://github.com/mlnotes2718/git_intro** in your browser.
2. Click the green **Code** button.
3. Select **Download ZIP**.
4. Save the ZIP to your Desktop or Downloads folder.

> 💡 **Tip:** Downloading as ZIP gives you the files without any git history attached. That is intentional — you are about to create your own fresh repository from these files.

### Extract and rename the folder

Extract the ZIP. You will get a folder named something like `git_intro-main`. **Rename it** to your chosen project name before you do anything else.

#### Why the folder name matters

When you run `git init` inside a folder, Git uses that **folder name** as the local project name. When you later push to GitHub, the repository will be created with that same name. So:

- `my-bmi-app` → GitHub repo will be `my-bmi-app`
- `git_intro-main` → GitHub repo will be `git_intro-main` (messy name, avoid this)

Choose a short, lowercase name with hyphens instead of spaces. For example: `bmi-project`.

```
# Example on macOS / Linux:
mv ~/Downloads/git_intro-main ~/Desktop/bmi-project

# Or just rename the folder in Windows Explorer / macOS Finder
```

After renaming, open the folder in VS Code:

```bash
cd ~/Desktop/bmi-project
code .
```

---

## Step 4 — Clean the Project Folder

Now tidy up the downloaded files so you start with only what you need.

### Keep `.gitkeep` in src and tests folder, remove everything else inside src

The `src` folder is where your Python source code will live. It currently contains example files — delete them all, but **keep the `.gitkeep` file**.

> 📝 **What is `.gitkeep`?**  Git does not track empty folders. If `src/` has no files in it, git will simply not include it when you push. The `.gitkeep` file is a convention — an empty placeholder file that forces Git to remember the folder exists. Its name is not special; any file would work, but `.gitkeep` makes the intention clear.

#### On macOS / Linux (Terminal):

```bash
cd ~/Desktop/bmi-project

# Delete everything in src EXCEPT .gitkeep
find src -type f ! -name '.gitkeep' -delete
# Delete everything in tests EXCEPT .gitkeep
find tests -type f ! -name '.gitkeep' -delete
# Open the file .gitignore and remove the last entry secret.json
# Mac Users can use the command below
sed -i '' '/secrets.json/d' .gitignore
```

### Remove the docs folder entirely

The downloaded repo may include a `docs` folder with example content. Delete the entire folder — you will recreate it from scratch in Step 9.

```bash
rm -rf docs
```

Your project should now look like this:

```
bmi-project/
├── guides/. # various guide related to git including a textbook
│   ├── ...
│   └── progit.pdf
├── src/
│   └── .gitkeep
├── tests/
│   └── .gitkeep
├── .gitignore
├── .python-version
├── git-fundamentals-tutorial.md
├── pyproject.toml
└── README.md
└── uv.lock
```

---

## Step 5 — README and .gitignore

The repository you downloaded already includes a `README.md` and a `.gitignore`. **Use these as-is** — no need to create new ones.

### README.md

Open `README.md` in VS Code. It describes the project. Feel free to personalize the title and description to match your project name.

### .gitignore

Open `.gitignore`. This file tells Git which files and folders to never track. Confirm it contains at least these entries (add any that are missing):

```
# .gitignore
## Source : https://github.com/github/gitignore

## Python.gitignore
## Source : https://github.com/github/gitignore/blob/main/Python.gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[codz]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
...
...
# Recycle Bin used on file shares
$RECYCLE.BIN/

# Windows Installer files
*.cab
*.msi
*.msix
*.msm
*.msp

# Windows shortcuts
*.lnk
```

You will learn more about `.gitignore` in Step 10.

---

## Step 6 — git init

Now you will turn the project folder into a Git repository. Open a terminal, navigate to your project root, and run:

```bash
cd ~/Desktop/bmi-project

git init
```

Expected output:

```
Initialized empty Git repository in /Users/you/Desktop/bmi-project/.git/
```

### What just happened?

`git init` created a hidden folder called `.git` inside your project. This is Git's database — it stores every version of every file, all commit messages, branch information, and configuration. **Never delete or edit the `.git` folder manually.**

To see it:

```bash
ls -la
# You should see .git listed
```

> 📝 **Note:** A project is "a git repository" the moment `.git` exists inside it. The folder name of the project is the name Git (and GitHub) will use for the repo.

---

## Step 7 — git add

Before Git can save (commit) any files, you need to **stage** them — tell Git exactly which changes should go into the next commit. This two-step process (stage → commit) gives you precise control over what gets saved.

```bash
git add .
```

The `.` means "add everything in the current folder and all subfolders." After running this, Git knows about all your files and is ready to commit them.

### Check what is staged

```bash
git status
```

You will see something like:

```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .gitignore
        new file:   README.md
        new file:   src/.gitkeep
```

Everything listed under "Changes to be committed" is staged and ready.

### git add . vs git add filename

| Command | What it stages |
|---|---|
| `git add .` | Every new, modified, and deleted file in the project |
| `git add src/main.py` | Only that specific file |
| `git add src/` | Everything inside the `src` folder |

Use `git add .` when all your changes belong in the same commit. Use individual file paths when you want to group only certain changes together.

---

## Step 8 — First Commit and Push to GitHub

### Commit

A commit is a permanent snapshot of your staged files, stamped with your name, email, timestamp, and a message.

```bash
git commit -m "chore: initial project setup with README and gitignore"
```

The `-m` flag lets you write the commit message inline. Always write a short, meaningful message — future-you will thank present-you.

> 💡 **Good commit message habits:**
> - Start with a category: `feat:`, `fix:`, `chore:`, `docs:`
> - Use the present tense: "add file" not "added file"
> - Keep it under 72 characters

### Push to GitHub using VS Code (Recommended)

1. Open VS Code. Make sure your project folder is open (**File → Open Folder…**).
2. Click the **Source Control** icon in the left sidebar (looks like a branch).
3. Click **Publish to GitHub**.
4. Sign in to GitHub if prompted.
5. Choose a name for the repository and set it to **Public** or **Private**.
6. VS Code pushes your commit and opens the GitHub repository page in your browser.

> 💡 **Tip:** If you don't see "Publish to GitHub", make sure the **GitHub Pull Requests and Issues** extension is installed (see Step 2).

### Alternative: Push using the CLI

If VS Code cannot connect to GitHub, create the repository manually:

**On GitHub:**
1. Click the **+** icon (top right) → **New repository**.
2. Enter the repository name (use the same name as your project folder).
3. **Do not** tick "Initialize with README" — your local copy already has one.
4. Click **Create repository**.
5. Copy the repository URL shown (e.g. `https://github.com/yourusername/bmi-project.git`).

**In your terminal:**

```bash
# Link your local repo to the GitHub repo
git remote add origin https://github.com/yourusername/bmi-project.git

# Push to GitHub and set origin as the default remote
git push -u origin main
```

The `-u` flag sets `origin main` as the default, so from now on you only need to type `git push`.

### Clone back (optional but educational)

Once the project is on GitHub, try this: copy the web address of your GitHub repo, then delete your local project folder entirely. Then clone it back:

```bash
# In VS Code: click "Clone Git Repository" in the Source Control panel
# Or from the terminal:
git clone https://github.com/yourusername/bmi-project.git
```

Notice that the cloned folder name matches your GitHub repository name exactly. This is the relationship between folder name and project name in action.

---

## Step 9 — Working with Folders and Files

### Create an empty docs folder

Create a new folder called `docs` in the project root. You can do this in VS Code's file explorer, Windows Explorer, Finder, or the terminal:

```bash
mkdir docs
```

Now try to commit it:

```bash
git add .
git commit -m "add empty docs folder"
```

Git will respond with:

```
On branch main
nothing to commit, working tree clean
```

**Git completely ignores empty folders.** It tracks files, not directories. The `docs` folder does not appear in `git status` at all because there is nothing inside it.

### The `.gitkeep` convention

To force Git to remember a folder, add a placeholder file:

```bash
# Navigate into docs and create the placeholder
touch docs/.gitkeep
```

> 📝 **Note:** Always run git commands from the project root (the folder that contains `.git`). Running `git push` from inside a subfolder may only push changes in that subfolder.

Now Git can see the folder:

```bash
git status
# new file: docs/.gitkeep

git add .
git commit -m "chore: add docs folder with .gitkeep"
git push
```

### Add a text file

Create a file called `mytext.txt` inside the `docs` folder and write a few lines in it:

```bash
touch docs/mytext.txt
```

Open `docs/mytext.txt` in VS Code and write something, for example:

```
This is my first text file tracked by Git.
Git records every change I make to this file.
```

Save the file, then commit and push:

```bash
git add .
git commit -m "docs: add mytext.txt with personal notes"
git push
```

Open your GitHub repository in the browser — you can see the `docs` folder and the new file. The commit message is visible next to each file, showing exactly when and why it was added.

> 💡 **Good practice:**
> - Commit often — each commit should cover one logical task
> - Write meaningful messages so that months later you can understand what each commit was for

---

## Step 10 — Understanding .gitignore

### What it does

`.gitignore` is a plain text file that tells Git to completely ignore certain files or folders. Ignored files will never appear in `git status` and will never be committed.

### What to ignore and why

| Category | Examples | Why ignore |
|---|---|---|
| Python cache | `__pycache__/`, `*.pyc` | Auto-generated, changes constantly, not needed by others |
| Virtual environments | `.venv/`, `venv/` | Recreated from `pyproject.toml`; huge and system-specific |
| OS files | `.DS_Store`, `Thumbs.db` | Clutter created by macOS and Windows |
| Secrets and credentials | `.env`, `secrets.json` | **Never commit passwords or API keys**, especially to public repos |
| Large data files | `*.csv`, `data/` | GitHub has a 100 MB file limit |

### The `.gitignore` syntax

```
# This is a comment — ignored by Git

# Ignore a specific file
secrets.json

# Ignore all .log files anywhere in the project
*.log

# Ignore an entire folder
.venv/

# Ignore a folder only at the root level
/node_modules/

# Exception: track this file even though *.log is ignored
!important.log
```

---

## Step 11 — .gitignore in Action

Let's see it work. Create a file that should be ignored:

```bash
touch docs/secrets.json
```

Check git status — it should appear as an untracked file:

```bash
git status
# Untracked files:
#   docs/secrets.json
```

Now open `.gitignore` in VS Code and add this line at the bottom:

```
secrets.json
```

Save `.gitignore` and run `git status` again:

```bash
git status
# Changes not staged for commit:
#   modified: .gitignore
#
# (secrets.json is no longer listed!)
```

`secrets.json` has disappeared from the status output. Git is now ignoring it completely. Commit the updated `.gitignore`:

```bash
git add .gitignore
git commit -m "chore: ignore secrets.json"
git push
```

> ⚠️ **Important:** `.gitignore` only prevents **untracked** files from being added. If you already committed a file and then added it to `.gitignore`, git will **still track it**. To stop tracking a file that was already committed:
> ```bash
> git rm --cached docs/secrets.json
> git commit -m "chore: stop tracking secrets.json"
> ```

---

## Step 12 — Tracking Changes with git log

Every commit you make is stored permanently. Use `git log` to see the history:

```bash
git log --oneline
```

Example output:

```
4a1d2f3 (HEAD -> main, origin/main) chore: ignore secrets.json
9c3e1b2 docs: add mytext.txt with personal notes
7f2a0c1 chore: add docs folder with .gitkeep
1e8b3d4 chore: initial project setup with README and gitignore
```

Each line shows:
- The **short commit hash** (7-character ID) — unique fingerprint for that commit
- The **commit message** you wrote
- Where `HEAD` is pointing (your current position)

### Useful log variations

```bash
# Show full details for each commit
git log

# Show which files changed in each commit
git log --oneline --stat

# Show a visual branch graph
git log --oneline --graph --all

# Show only the last 5 commits
git log --oneline -5
```

---

## Step 13 — Simulating a Remote Change

In a real team, someone else will push changes to GitHub while you are working locally. You need a way to get their updates. Let's simulate this.

### Make a change directly on GitHub

1. Go to your GitHub repository in the browser.
2. Navigate to `docs/mytext.txt`.
3. Click the **pencil icon** (Edit this file) in the top-right of the file view.
4. Add a new line at the bottom, for example: `This line was added directly on GitHub.`
5. Scroll down to **Commit changes**, write a short message, and click **Commit changes**.

The change now exists on GitHub — but your local copy does not know about it yet.

Open VS Code. Look at `docs/mytext.txt`. The new line is **not there**. Your local copy is behind.

---

## Step 14 — git fetch, git diff, git merge vs git pull

### The difference between fetch and pull

| Command | What it does |
|---|---|
| `git fetch` | Downloads changes from GitHub — does **not** modify your local files |
| `git diff` | Shows the difference between two states |
| `git merge` | Applies the downloaded changes to your local branch |
| `git pull` | `fetch` + `merge` in a single command |

Fetch first when you want to **look before you leap**. Pull when you just want the latest changes and trust what's on the remote.

### Step-by-step: fetch, inspect, then merge

```bash
# Step 1: download the remote changes (nothing in your files changes yet)
git fetch origin main

# Step 2: see what is different between your local main and the remote
git diff main origin/main
```

The `git diff` output will show the line you added on GitHub, prefixed with `+` (added lines are green, removed lines are red in most terminals):

```diff
+ This line was added directly on GitHub.
```

If you are happy with what you see:

```bash
# Step 3: apply the downloaded changes to your local branch
git merge origin/main
```

Open `docs/mytext.txt` in VS Code — the new line is now there.

### The shortcut: git pull

`git pull` does Steps 1 and 3 together, skipping the inspection step:

```bash
git pull
```

Practice by making another change on the GitHub website and then running `git pull` to bring it down in one step.

### When to use each

- Use **`git fetch` + `git diff` + `git merge`** when you want to review changes before applying them — useful in a team where you don't always know what others have pushed.
- Use **`git pull`** for your own solo repositories or when you trust the remote and just want to stay up to date quickly.

---

## Step 15 — Set Up a Python Environment with uv

`uv` is a modern, fast Python package manager. It handles virtual environments automatically — you never need to activate one manually.

### Install uv

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Restart your terminal, then confirm it installed:

```bash
uv --version
```

### Pin a Python version

Confirm that there is a file `.python-version`. If not, you can use the following command to install and pin a python version.

```bash
# Install Python 3.12 (managed by uv, no system Python needed)
uv python install 3.12

# Pin this project to Python 3.12
uv python pin 3.12
```

Anyone who opens this project gets the same Python version.

Your project now looks like:

```
bmi-project/
├── docs/
│   ├── .gitkeep
│   ├── mytext.txt
│   └── secrets.json
├── guides/. # various guide related to git including a textbook
│   ├── ...
│   └── progit.pdf
├── src/
│   └── .gitkeep
├── tests/
│   └── .gitkeep
├── .gitignore
├── .python-version
├── git-fundamentals-tutorial.md
├── pyproject.toml
└── README.md
└── uv.lock
```


Run the following command to install the files:

```bash
uv sync
```

> 📝 **Note:** With `uv`, run Python scripts and tools with `uv run <command>`. There is no need to activate a virtual environment — `uv` handles it automatically.

Check if there is anything to commit:
```bash
git status
```

If the return is `nothing to commit`, then you can skipped the section below, otherwise please follow teh command below to commit the changes:

```bash
git add .
git commit -m "chore: initialize uv Python environment"
git push
```

---

## Step 16 — Create a Feature Branch and Write the BMI Calculator

From now on, never write code directly on `main`. Always create a **branch** first.

### Why branches?

A branch is an independent line of development. Changes on your branch do not affect `main` until you deliberately merge them. This means:

- `main` always contains working, stable code
- You can experiment freely without breaking anything
- Multiple people can work on different features at the same time

### Create the branch

```bash
# Make sure you are on a clean main first
git switch main
git pull

# Create and switch to the feature branch
git switch -c feature/bmi-calculator
```

`git switch -c` is the modern command for creating and switching to a new branch in one step.

Confirm you are on the right branch:

```bash
git branch
# * feature/bmi-calculator
#   main
```

The `*` shows your current branch.

### Write the BMI calculator

Create `src/main.py` and copy in this code:

```python
# src/main.py

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg: Weight in kilograms.
        height_m:  Height in metres.

    Returns:
        BMI as a float, rounded to 2 decimal places.
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than zero.")
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def bmi_category(bmi: float) -> str:
    """Return the WHO BMI category for a given BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"


if __name__ == "__main__":
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in metres: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi} — {bmi_category(bmi)}")
```

### Run it to verify

```bash
uv run python src/main.py
# Enter your weight in kg: 70
# Enter your height in metres: 1.75
# Your BMI is 22.86 — Normal weight
```

> 💡 **Tip:** Always run your code at least once before committing. Catching a typo before it hits Git saves you an extra commit.

---

## Step 17 — Push the Branch, Open a PR, and Merge

### Commit the code

```bash
git add src/main.py
git commit -m "feat: add BMI calculator with kg input and category labels"
```

### Push the branch to GitHub

```bash
git push -u origin feature/bmi-calculator
```

The `-u` flag links your local branch to the remote branch. After this, you only need `git push` for future commits on this branch.

### Open a Pull Request on GitHub

1. Go to your GitHub repository in the browser.
2. You will see a yellow banner: *"feature/bmi-calculator had recent pushes"* — click **Compare & pull request**.
3. Write a title: `feat: BMI calculator` if it did not auto populate
4. In the description, briefly explain what you built and why.
5. Click **Create pull request**.

### Review and merge

The Pull Request shows a **diff** — a side-by-side view of exactly what changed. In a team, a colleague would review this and either approve or request changes. For now, you are both author and reviewer.

Click the **Files changed** tab and review your own diff. When you are satisfied:

1. Click **Submit review**. You cannot approve your own pull request, so you can just comment and click **Submit review**
2. Click **Merge pull request** → **Confirm merge**.
3. Click **Delete branch** to remove the remote branch.

> 📝 **Note:** In a real team, the person who wrote the code should **not** be the one who merges it. A team lead or designated reviewer should approve and merge. This is a safeguard against errors reaching `main`.

### Sync your local repository

```bash
# Switch back to main
git switch main

# Pull the merged changes
git pull

# Delete the local branch (it is no longer needed)
git branch -d feature/bmi-calculator
```

Run `git log --oneline` to confirm the merge commit is in your history.

---

## Step 18 — Introduce a Bug (No Tests)

Now we deliberately break things — this is how you learn to fix them.

### Create a new branch

```bash
git switch main
git pull
git switch -c feature/bmi-imperial
```

### Write the buggy code

Open `src/main.py` and **replace** the entire content with this version. The user inputs their weight in **pounds**, but the code never converts pounds to kilograms before calculating — so the result is wrong by a factor of roughly 2.2.

```python
# src/main.py  ← BUGGY VERSION

def calculate_bmi(weight_lb: float, height_m: float) -> float:
    """
    BUG: parameter says lb but we forget to convert lb → kg.
    The formula receives the wrong unit and silently produces a wrong answer.
    """
    bmi = weight_lb / (height_m ** 2)   # ← weight_lb used directly — WRONG
    return round(bmi, 2)


def bmi_category(bmi: float) -> str:
    if bmi < 18.5:   return "Underweight"
    elif bmi < 25.0: return "Normal weight"
    elif bmi < 30.0: return "Overweight"
    else:            return "Obese"


if __name__ == "__main__":
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in metres: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi} — {bmi_category(bmi)}")
```

Run it to see the wrong result:

```bash
uv run python src/main.py
# Enter your weight in pounds: 154
# Enter your height in metres: 1.75
# Your BMI is 50.29 — Obese   ← completely wrong (should be ~22.86)
```

### Commit, push, PR, and merge

Pretend you didn't notice the bug and push it through to `main`:

```bash
git add src/main.py
git commit -m "feat: add imperial (pounds) input support"
git push -u origin feature/bmi-imperial
```

On GitHub Extension: open a PR, merge it to `main`, delete the branch remotely and locally. Then:

```bash
git pull
```

Check the log to see where you are:

```bash
git log --oneline
# 7c7adc2 (HEAD -> main, origin/main, origin/HEAD) Merge pull request #2 from mlnotes2718:feature/bmi-imperial
# 62e095f feat: add imperial (pounds) input support
# ...
```

---

## Step 19 — Undo One Commit with git revert

The bug is on `main`. `git revert` is the right tool here — it creates a **new commit** that undoes a specific commit without erasing any history. It is safe to use on `main` because it does not rewrite history.

```bash
# View the log to identify the buggy commit
git log --oneline

# Revert the most recent commit (the buggy one)
git revert HEAD -m 1 --no-edit
```

`--no-edit` skips the editor and uses the default "Revert" message. Without it, git opens your editor so you can write a custom message.

```bash
# Push the revert commit to GitHub
git push
```

Check the log:

```bash
git log --oneline
# a1b2c3d (HEAD -> main, origin/main) Revert "feat: add imperial (pounds) input support"
# e7f3a21 feat: add imperial (pounds) input support
# 2b4c1d8 feat: add BMI calculator with kg input and category labels
```

Notice that the buggy commit is still in the history — `git revert` never erases commits. The bad code has been **reversed** by the new revert commit, but the full story is preserved.

Run the code to confirm the original working version is back:

```bash
uv run python src/main.py
# Enter your weight in kg: 70
# Enter your height in metres: 1.75
# Your BMI is 22.86 — Normal weight  ✓
```

---

## Step 20 — Introduce the Same Bug Across Two Commits

Now we make things more complex: the same problem is introduced across **two separate commits**. You will need to undo both.

### Create a branch and make two bad commits

```bash
git switch main
git pull
git switch -c feature/bmi-imperial-v2
```

**First bad commit** — change the function signature to accept pounds:

```python
# src/main.py — FIRST CHANGE: rename parameter to suggest lb input
def calculate_bmi(weight_lb: float, height_m: float) -> float:
    bmi = weight_lb / (height_m ** 2)   # still no conversion
    return round(bmi, 2)

def bmi_category(bmi: float) -> str:
    if bmi < 18.5:   return "Underweight"
    elif bmi < 25.0: return "Normal weight"
    elif bmi < 30.0: return "Overweight"
    else:            return "Obese"

if __name__ == "__main__":
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in metres: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi} — {bmi_category(bmi)}")
```

```bash
git add src/main.py
git commit -m "refactor: rename parameter to weight_lb"
```

**Second bad commit** — add a prompt message change:

Open `src/main.py` and change the last `print` line to:

```python
    print(f"BMI (from pounds input): {bmi} — {bmi_category(bmi)}")
```

```bash
git add src/main.py
git commit -m "feat: update output message for pounds input"
```

### Push, PR, merge

```bash
git push -u origin feature/bmi-imperial-v2
```

On GitHub: PR → merge → delete remote and local branch. Locally:

```bash
git pull
```

Check the log:

```bash
git log --oneline
# 247f866 feat: update output message for pounds input
# 1a9d37b refactor: rename parameter to weight_lb
# 5f6d02f Revert "Merge pull request #2 from mlnotes2718:feature/bmi-imperial"
# 7c7adc2 Merge pull request #2 from mlnotes2718:feature/bmi-imperial
# 62e095f feat: add imperial (pounds) input support
# 38ec5cd Merge pull request #1 from mlnotes2718/feature/bmi-calculator
# afc7e05 feat: add BMI calculator with kg input and category labels
```

Both bad commits are on `main`. `git revert` can handle this but requires running it twice. `git reset` handles it in one move — see Step 21.

---

## Step 21 — Undo Multiple Commits with git reset

`git reset` moves the branch pointer backwards to a specific commit, effectively erasing everything that came after it from the branch's perspective.

### Choose how far back to go

From the log above, the last good commit is `2b4c1d8` (the original BMI calculator). We want to go back there, removing the two bad commits **and** the earlier revert attempt.

```bash
# --hard erases the commits and all the file changes
git reset --hard 38ec5cd
```

Replace `38ec5cd` with the actual hash from your log.

Verify:

```bash
git log --oneline
# 38ec5cd (HEAD -> main) Merge pull request #1 from mlnotes2718/feature/bmi-calculator
```

The two bad commits (and the old revert) are gone from the local history. The files on disk are back to the clean BMI calculator.

```bash
uv run python src/main.py
# Enter your weight in kg: 70   → 22.86 — Normal weight  ✓
```

### Force-push to GitHub

Because you rewrote history, a normal `git push` will be rejected. Use `--force-with-lease` (safer than `--force`: it refuses to push if someone else has pushed in the meantime):

```bash
git push --force-with-lease
```

> ⚠️ **Warning:** Only use `git reset` + force-push on branches where **you are the only contributor**, or when the entire team has agreed. Force-pushing to `main` on a shared project causes serious problems for everyone else.

---

## Step 22 — revert vs reset: When to Use Which

| | `git revert` | `git reset` |
|---|---|---|
| **What it does** | Adds a new commit that reverses an old one | Moves the branch pointer backwards |
| **History** | Preserved — the bad commit stays visible | Erased — commits after the target are gone |
| **Safe on shared branches?** | ✅ Yes — does not rewrite history | ⚠️ No — requires force-push, breaks teammates |
| **Best for** | Undoing a commit on `main` or any shared branch | Cleaning up local commits before pushing |
| **Recovery** | Easy — just revert the revert | Hard — erased commits are difficult to recover |

**Rule of thumb:**
- Already pushed to a shared branch → use **`git revert`**
- Not pushed yet, or only you use the branch → **`git reset`** is fine

---

## Step 23 — Discard Before Committing with git restore and git clean

Sometimes you make changes and realize they are wrong **before** you commit. There is no need to reset or revert — you can simply discard the changes.

### Set up: introduce the bug again, but don't commit

Make sure you are on `main` with the good code:

```bash
git switch main
git status   # should be clean
```

Open `src/main.py` and introduce the same bug (no lb→kg conversion). Save the file. **Do not run git add or git commit.**

Check the status:

```bash
git status
# modified: src/main.py
```

And optionally create a stray untracked file:

```bash
touch src/temp_notes.txt
```

```bash
git status
# modified:   src/main.py
# Untracked files:
#   src/temp_notes.txt
```

### Discard changes to a tracked file

```bash
# Restore src/main.py to its last committed state
git restore src/main.py
# OR if you make many changes at many places but you want to discard all
git restore .
```

Open `src/main.py` — it is back to the correct version.

### Remove untracked files with git clean

`git restore` only works on files Git is already tracking. Untracked files (like `temp_notes.txt`) need `git clean`:

```bash
# -n = dry run: show what WOULD be deleted (nothing deleted yet)
git clean -n
# Would remove src/temp_notes.txt

# -f = force: actually delete
# -d = also delete untracked directories
git clean -fd
```

After this, `git status` shows a completely clean working tree.

> ⚠️ **`git clean -fd` is permanent.** There is no undo. Always run `git clean -n` first to preview what will be removed.

---

## Step 24 — Tag the Good Code as a Release

Now that `main` is clean and the BMI calculator works correctly, mark this point as version `v1.0`. A **tag** is a permanent, named pointer to a specific commit. Unlike branches, tags never move.

```bash
# Confirm you are on main and it is clean
git switch main
git status

# Create an annotated tag (recommended — includes your name, date, and message)
git tag -a v1.0 -m "Release v1.0: working BMI calculator with kg input"

# Check the tag
git show v1.0
```

### Push the tag to GitHub

Tags are not pushed automatically with `git push`. You must push them explicitly:

```bash
git push origin v1.0
```

### Create a GitHub Release

1. Go to your GitHub repository.
2. Click **Releases** in the right sidebar.
3. Click **Draft a new release**.
4. Select `v1.0` from the **Choose a tag** dropdown.
5. Add a title (`v1.0 — BMI Calculator`) and release notes.
6. Click **Publish release**.

Your release is now permanently tied to the `v1.0` tag. Anyone can download the exact code from this release, even years from now.

---

## Step 25 — Introduce the Bug Again, PR and Merge

We are going to do the imperial bug one more time — this time on a branch, going all the way through to a merged PR — to set up the next rollback exercise.

```bash
git switch main
git pull
git switch -c feature/imperial-broken
```

Open `src/main.py` and replace the full content with the buggy version from Step 18 (pounds input, no conversion). Then:

```bash
git add src/main.py
git commit -m "feat: add imperial input — WIP (contains bug)"
git push -u origin feature/imperial-broken
```

On GitHub: open PR → merge to `main` → delete branch remotely and locally. Locally:

```bash
git pull
```

The bug is back on `main`. The log now looks something like:

```bash
git log --oneline
# a565c51 (HEAD -> main, origin/main, origin/HEAD) Merge pull request #4 from mlnotes2718:feature/imperial-broken
# 67c6768 feat: add imperial input — WIP (contains bug)
# 38ec5cd (tag: v1.0) Merge pull request #1 from mlnotes2718/feature/bmi-calculator
```

---

## Step 26 — Roll Back to the Release Tag with git reset

You have a release tag `v1.0` pointing at the last known-good commit. Use it to reset `main` back to that exact state.

```bash
# Reset main to the v1.0 tag
git revert -m 1 v1.0..HEAD --no-edit
```

```bash
git revert --continue
```

Verify the reset worked:

```bash
git log --oneline
# d6774ed (HEAD -> main, origin/main, origin/HEAD) Revert "Merge pull request #4 from mlnotes2718:feature/imperial-broken"
# a565c51 Merge pull request #4 from mlnotes2718:feature/imperial-broken
# 67c6768 feat: add imperial input — WIP (contains bug)
# 38ec5cd (tag: v1.0) Merge pull request #1 from mlnotes2718/feature/bmi-calculator

uv run python src/main.py
# Enter your weight in kg: 70 → 22.86 — Normal weight  ✓
```

Force-push to update GitHub:

```bash
git push
```

> 💡 **This is the power of tags.** Without `v1.0`, you would have had to scroll through `git log` to find the right hash. With a tag, you say exactly what you mean: "go back to the v1.0 release."

---

## Step 27 — Redo the Bug Fix with Proper Tests

Now let's do it right. Create a branch, write the **correct** imperial conversion code, and back it up with tests this time.

```bash
git switch main
git pull
git switch -c fix/imperial-with-tests
```

### The correct code

Open `src/main.py` and replace it with the fixed version:

```python
# src/main.py  ← CORRECT VERSION with pounds support

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg: Weight in kilograms.
        height_m:  Height in metres.

    Returns:
        BMI as a float, rounded to 2 decimal places.
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than zero.")
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def pounds_to_kg(weight_lb: float) -> float:
    """Convert pounds to kilograms (1 lb = 0.453592 kg)."""
    return round(weight_lb * 0.453592, 4)


def bmi_category(bmi: float) -> str:
    """Return the WHO BMI category for a given BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"


if __name__ == "__main__":
    unit = input("Enter weight unit (kg / lb): ").strip().lower()
    weight = float(input("Enter your weight: "))
    if unit == "lb":
        weight = pounds_to_kg(weight)
    height = float(input("Enter your height in metres: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi} — {bmi_category(bmi)}")
```

Run it to manually verify:

```bash
uv run python src/main.py
# Enter weight unit (kg / lb): lb
# Enter your weight: 154
# Enter your height in metres: 1.75
# Your BMI is 22.81 — Normal weight  ✓  (no longer 50.32!)
```

### Write the tests

Create a `tests/` folder at the project root and add `tests/test_main.py`. Copy and paste the following:

```python
# tests/test_main.py

import sys
import os

# Allow imports from the src folder without installing the package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import calculate_bmi, bmi_category, pounds_to_kg


# ── Conversion ───────────────────────────────────────────────────

def test_pounds_to_kg():
    assert pounds_to_kg(154) == 69.8532

def test_pounds_to_kg_small():
    assert pounds_to_kg(100) == 45.3592


# ── BMI calculation ──────────────────────────────────────────────

def test_normal_bmi():
    assert calculate_bmi(70, 1.75) == 22.86

def test_bmi_from_pounds():
    # 154 lb converted correctly: 69.8532 kg → BMI 22.82, NOT 50.32
    weight_kg = pounds_to_kg(154)
    assert calculate_bmi(weight_kg, 1.75) == 22.81

def test_zero_height_raises():
    try:
        calculate_bmi(70, 0)
        assert False, "Expected ValueError"
    except ValueError:
        pass


# ── Category ─────────────────────────────────────────────────────

def test_category_underweight():
    assert bmi_category(17.0) == "Underweight"

def test_category_normal():
    assert bmi_category(22.86) == "Normal weight"

def test_category_overweight():
    assert bmi_category(27.5) == "Overweight"

def test_category_obese():
    assert bmi_category(32.0) == "Obese"


# ── Manual runner (no pytest required) ───────────────────────────

if __name__ == "__main__":
    tests = [
        test_pounds_to_kg,
        test_pounds_to_kg_small,
        test_normal_bmi,
        test_bmi_from_pounds,
        test_zero_height_raises,
        test_category_underweight,
        test_category_normal,
        test_category_overweight,
        test_category_obese,
    ]
    passed = 0
    failed = 0
    for t in tests:
        try:
            t()
            print(f"  PASS  {t.__name__}")
            passed += 1
        except Exception as e:
            print(f"  FAIL  {t.__name__}  →  {e}")
            failed += 1
    print(f"\n{passed} passed, {failed} failed")
```

Run the tests:

```bash
# With plain Python (no extra tools needed)
uv run python tests/test_main.py

# Or with pytest if you have it installed via uv add --dev pytest
uv run pytest tests/ -v
```

All tests should pass.

---

## Step 28 — Amend, Commit, Push, and Tag v1.0.1

### Commit the fix and the tests together

```bash
git add src/main.py tests/test_main.py
git commit -m "fix: add pounds_to_kg conversion with tests — closes imperial bug"
```

### Optional: amend the commit message

If you want to improve the commit message before pushing (you can only amend the **most recent** commit):

```bash
git commit --amend -m "fix: correct lb→kg conversion; add tests for imperial input"
```

`--amend` rewrites the last commit in place. It is safe to use **before** pushing. Do not amend commits that have already been pushed to a shared branch.

### Push, PR, and merge

```bash
git push -u origin fix/imperial-with-tests
```

On GitHub: open PR → review the diff → confirm the tests are included → merge → delete branch.

Locally:

```bash
git pull
```

### Tag the new release as v1.0.1

```bash
git tag -a v1.0.1 -m "Release v1.0.1: fix imperial lb input with correct kg conversion"
git push origin v1.0.1
```

On GitHub: go to **Releases** → **Draft a new release** → select `v1.0.1` → add release notes:

```
## What's changed
- Fixed BMI calculation when user enters weight in pounds
- Added `pounds_to_kg()` conversion helper
- Added unit tests covering conversion, BMI calculation, and category labels
```

Click **Publish release**.

### Verify the final log

```bash
git log --oneline
# c9d8e7f (HEAD -> main, tag: v1.0.1, origin/main) fix: correct lb→kg conversion; add tests for imperial input
# 2b4c1d8 (tag: v1.0) feat: add BMI calculator with kg input and category labels
# ...
```

You can now clearly see both release points in history. If a future bug is discovered, you know exactly which tag to roll back to.

---

## Summary: The Git Workflow You Have Learned

```
main (stable) ──────────────────────────────────────────────────────►
                │            │              │                │
          git init      feature branch  git revert       git tag
          git add .     git switch -c   git reset        v1.0.1
          git commit    code → commit
          git push      git push
                        PR → merge
                        git switch main
                        git pull
                        git branch -d
```

### The daily loop (for any new feature or fix)

```bash
git switch main && git pull               # always start fresh
git switch -c feature/my-feature          # new branch
# ... write code, test locally ...
git add .
git commit -m "feat: describe what you did"
git push -u origin feature/my-feature
# open PR on GitHub, get it reviewed, merge
git switch main && git pull
git branch -d feature/my-feature
```

### Key commands reference

| Task | Command |
|---|---|
| Initialise repo | `git init` |
| Stage all changes | `git add .` |
| Commit | `git commit -m "message"` |
| Push | `git push` |
| Create & switch branch | `git switch -c branch-name` |
| Switch branch | `git switch branch-name` |
| See history | `git log --oneline` |
| Download remote changes | `git fetch origin main` |
| Download + apply | `git pull` |
| Safe undo (shared branch) | `git revert HEAD` |
| Erase local commits | `git reset --hard <hash>` |
| Discard file edits | `git restore filename` |
| Remove untracked files | `git clean -fd` |
| Tag a release | `git tag -a v1.0 -m "msg"` |
| Push a tag | `git push origin v1.0` |

### Branch and Prefix Preference

Yes, but commit messages use a colon format instead of a slash. This convention is called **Conventional Commits**.

| Branch prefix | Commit prefix | Example commit message |
|---|---|---|
| `feature/` | `feat:` | `feat: add BMI calculator` |
| `fix/` | `fix:` | `fix: correct lb to kg conversion` |
| `hotfix/` | `fix:` | `fix: prevent divide by zero on zero height` |
| `chore/` | `chore:` | `chore: update dependencies` |
| `docs/` | `docs:` | `docs: add setup instructions` |
| `refactor/` | `refactor:` | `refactor: extract bmi_category to helpers` |
| `test/` | `test:` | `test: add edge cases for zero weight` |
| `release/` | `chore:` | `chore: bump version to v1.1.0` |

Notice `hotfix/` and `fix/` both use `fix:` for commits — the branch name carries the urgency context, the commit type just describes what kind of change it is.

A full conventional commit message looks like this:

```
feat: add imperial pound input with kg conversion

- add pounds_to_kg() helper function
- update __main__ block to accept kg or lb
- validated against WHO BMI ranges
```

The first line is the **subject** (keep it under 72 characters), then a blank line, then an optional **body** with more detail. Most day-to-day commits only need the subject line.

The real benefit of being consistent is that tools like GitHub, changelog generators, and your teammates can instantly understand the nature of every commit just by reading the prefix — without opening the diff.
