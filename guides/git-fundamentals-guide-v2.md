# Git Fundamentals
### A Practical Guide for Beginners
*From Download to Pull Request — with Real Code Examples*

---

## Table of Contents

- [Part 1 — Setting Up Your Project](#part-1--setting-up-your-project)
  - [1.1 Download the Repository as a ZIP](#11-download-the-repository-as-a-zip)
  - [1.2 Unzip and Clean the src Folder](#12-unzip-and-clean-the-src-folder)
  - [1.3 Set Up the Project with uv](#13-set-up-the-project-with-uv)
  - [1.4 Initialise a Git Repository](#14-initialise-a-git-repository)
  - [1.5 Add README.md and .gitignore](#15-add-readmemd-and-gitignore)
  - [1.6 Publish to GitHub with VS Code](#16-publish-to-github-with-vs-code)
- [Part 2 — Feature Branches and Pull Requests](#part-2--feature-branches-and-pull-requests)
  - [2.1 Create a Feature Branch](#21-create-a-feature-branch)
  - [2.2 Write Code — BMI Calculator](#22-write-code--bmi-calculator)
  - [2.3 Test the Code Locally](#23-test-the-code-locally)
  - [2.4 Commit and Push the Branch](#24-commit-and-push-the-branch)
  - [2.5 Create a Pull Request and Merge](#25-create-a-pull-request-and-merge)
- [Part 3 — Introducing a Bug (Intentionally)](#part-3--introducing-a-bug-intentionally)
- [Part 4 — Fetching and Pulling Changes](#part-4--fetching-and-pulling-changes)
- [Part 5 — Rolling Back with git revert and git reset](#part-5--rolling-back-with-git-revert-and-git-reset)
  - [5.5 Fix the Bug and Commit a Proper Patch](#55-fix-the-bug-and-commit-a-proper-patch)
- [Part 6 — Tagging Releases with git tag](#part-6--tagging-releases-with-git-tag)
- [Quick Reference Cheat Sheet](#quick-reference-cheat-sheet)
- [Common Scenarios](#common-scenarios)
  - [Scenario 1 — Discard Everything and Restore to a Clean Clone State](#scenario-1--discard-everything-and-restore-to-a-clean-clone-state)
  - [Scenario 2 — Create a Branch, Make Changes, PR, Merge, and Delete](#scenario-2--create-a-branch-make-changes-pr-merge-and-delete)
  - [Scenario 3 — Update Your Branch with the Latest from Main Using Rebase](#scenario-3--update-your-branch-with-the-latest-from-main-using-rebase)
  - [Scenario 4 — Forked Repo: Sync Upstream → Forked Main → Working Branch](#scenario-4--forked-repo-sync-upstream--forked-main--working-branch)

---

## Part 1 — Setting Up Your Project

### 1.1 Download the Repository as a ZIP

If you don't have git installed yet, you can still download a copy of any GitHub repository as a plain ZIP file.

1. Open the repository page on GitHub in your browser.
2. Click the green **Code** button near the top-right of the file list.
3. Select **Download ZIP** from the dropdown menu.
4. Save the ZIP file to a convenient location (e.g. your Desktop or Downloads folder).

> 💡 **Tip:** You won't have any git history in this downloaded copy — that is intentional. You will create a fresh git repository in the next steps.

---

### 1.2 Unzip and Clean the src Folder

After extracting the archive you need to remove all files inside the `src` folder so you can start with a clean slate.

#### On Windows (File Explorer)

1. Right-click the ZIP file and choose **Extract All…**
2. Choose a destination folder and click **Extract**.
3. Open the extracted folder, navigate into `src`, select all files (`Ctrl+A`) and press `Delete`.

#### On macOS / Linux (Terminal)

```bash
# Unzip the archive
unzip repo-main.zip -d my-project

# Navigate into the project
cd my-project

# Remove everything inside src (keep the folder itself)
rm -rf src/*
```

---

### 1.3 Set Up the Project with uv

`uv` is a modern, extremely fast Python package and project manager. It replaces `pip`, `venv`, and `pip-tools` with a single tool. Install it once, then use it for every project.

#### Install uv

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

> 💡 **Tip:** Restart your terminal after installing so the `uv` command is available on your PATH.

#### Initialise the project

Run this from inside your project root (the folder that contains `src/`):

```bash
uv init
```

`uv init` creates the following files if they don't already exist:

```
my-project/
├── pyproject.toml   ← project metadata and dependencies
├── .python-version  ← pins the Python version for this project
└── hello.py         ← sample file (you can delete this)
```

You can safely delete `hello.py` — it is just a placeholder.

#### Add pytest as a development dependency

Development dependencies (like test tools) are only needed locally and should not be shipped with the application. Add pytest with the `--dev` flag:

```bash
uv add --dev pytest
```

This updates `pyproject.toml` and creates a `uv.lock` file that pins all dependency versions for reproducible installs.

```bash
# Verify pytest is available inside the uv-managed environment
uv run pytest --version
# pytest 8.x.x
```

> 📝 **Note:** With `uv`, you don't activate a virtual environment manually. Prefix commands with `uv run` and it handles the environment automatically.

Your project structure should now look like this:

```
my-project/
├── src/
│   └── (empty for now)
├── pyproject.toml
├── uv.lock
└── .python-version
```

---

### 1.4 Initialise a Git Repository

Open a terminal (or Git Bash on Windows), navigate to your project root, and run:

```bash
# Make sure you are in the project root
cd path/to/my-project

# Initialise git
git init

# Expected output:
# Initialized empty Git repository in .../my-project/.git/
```

> 📝 **Note:** `git init` creates a hidden `.git` folder. This folder stores every version of your project — do not delete it.

---

### 1.5 Add README.md and .gitignore

The repository you downloaded already includes a `README.md` and a `.gitignore`. Open them in VS Code and confirm they exist — there is no need to create them from scratch.

Your `README.md` should already describe the project. If you want to personalise it, open it and edit the content directly in VS Code.

Your `.gitignore` should already cover common Python and OS files. Check that it includes the following lines — add any that are missing:

```
# Python
__pycache__/
*.py[cod]
.env

# uv
.venv/
uv.lock

# macOS / Windows
.DS_Store
Thumbs.db
```

> 📝 **Note:** It is common to commit `uv.lock` so that teammates get identical dependency versions. Some teams choose to gitignore it. For this guide, we commit it.

Once you're happy with both files, stage and commit them along with the `uv` project files:

```bash
git add README.md .gitignore pyproject.toml uv.lock .python-version
git commit -m "chore: initialise project with uv and add README"
```

---

### 1.6 Publish to GitHub with VS Code

VS Code has built-in git and GitHub integration — no CLI needed for this step.

1. Open the project folder in VS Code (**File → Open Folder…**).
2. Click the **Source Control** icon in the left sidebar (the branch icon).
3. Click **Publish to GitHub** at the top of the Source Control panel.
4. Sign in with your GitHub account if prompted.
5. Choose a repository name and visibility (public or private).
6. VS Code pushes your initial commit and opens the repository page in your browser.

> 💡 **Tip:** If you don't see 'Publish to GitHub', make sure the **GitHub Pull Requests and Issues** extension is installed.

---

## Part 2 — Feature Branches and Pull Requests

### 2.1 Create a Feature Branch

Always develop new features on a separate branch — never directly on `main`.

#### Modern command: `git switch`

Git 2.23 (released 2019) introduced `git switch` as a clearer, more focused replacement for `git checkout` when working with branches. Prefer it for all branch operations going forward.

```bash
# Create a new branch and switch to it immediately
git switch -c feature/bmi-calculator

# Equivalent old command (still works, but less clear):
# git checkout -b feature/bmi-calculator

# Verify you are on the new branch
git branch
# * feature/bmi-calculator
#   main
```

| Command | What it does |
|---|---|
| `git switch -c <name>` | Create a new branch and switch to it |
| `git switch <name>` | Switch to an existing branch |
| `git switch -` | Switch back to the previous branch |
| `git switch main` | Switch to the main branch |
| `git branch` | List all local branches |
| `git branch -d <name>` | Delete a local branch (safe — warns if unmerged) |

> 📝 **Note:** `git switch` only handles branch switching. Use `git restore` (also introduced in 2.23) to discard file changes instead of the old `git checkout -- <file>`.

---

### 2.2 Write Code — BMI Calculator

Create the file `src/main.py` with the following content:

```python
# src/main.py

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg: Weight in kilograms.
        height_m:  Height in metres.

    Returns:
        BMI as a float rounded to 2 decimal places.
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than zero.")
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def bmi_category(bmi: float) -> str:
    """Return the WHO BMI category label."""
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

---

### 2.3 Test the Code Locally

Before committing, verify that the function produces the correct output.

#### Quick sanity check in the terminal

```bash
# Run from the project root
uv run python -c "
import sys
sys.path.insert(0, 'src')
from main import calculate_bmi, bmi_category

result = calculate_bmi(70, 1.75)
print(f'BMI: {result}')           # Expected: 22.86
print(bmi_category(result))        # Expected: Normal weight
"
```

#### Create a test file

Create a new folder called `tests/` at the project root, then copy and paste the code below into a new file named `tests/test_main.py`:

```
my-project/
├── src/
│   └── main.py
└── tests/
    └── test_main.py    ← create this file
```

**Copy and paste this into `tests/test_main.py`:**

```python
# tests/test_main.py

import sys
import os

# Allow imports from the src folder
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import calculate_bmi, bmi_category


# ── BMI calculation tests ────────────────────────────────────────

def test_normal_bmi():
    assert calculate_bmi(70, 1.75) == 22.86

def test_underweight():
    assert calculate_bmi(50, 1.75) == 16.33

def test_overweight():
    assert calculate_bmi(90, 1.75) == 29.39

def test_obese():
    assert calculate_bmi(100, 1.75) == 32.65

def test_zero_height_raises():
    try:
        calculate_bmi(70, 0)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_zero_weight_raises():
    try:
        calculate_bmi(0, 1.75)
        assert False, "Expected ValueError"
    except ValueError:
        pass


# ── BMI category tests ───────────────────────────────────────────

def test_category_underweight():
    assert bmi_category(17.0) == "Underweight"

def test_category_normal():
    assert bmi_category(22.86) == "Normal weight"

def test_category_overweight():
    assert bmi_category(27.5) == "Overweight"

def test_category_obese():
    assert bmi_category(32.0) == "Obese"


# ── Run manually ─────────────────────────────────────────────────
# You can also run this file directly without pytest:
#   uv run python tests/test_main.py

if __name__ == "__main__":
    tests = [
        test_normal_bmi,
        test_underweight,
        test_overweight,
        test_obese,
        test_zero_height_raises,
        test_zero_weight_raises,
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

#### Run the tests

```bash
# Run with pytest (uses uv to manage the environment)
uv run pytest tests/ -v

# Or run the file directly with plain Python — no pytest needed
uv run python tests/test_main.py
```

You should see all tests passing before you commit.

> 💡 **Tip:** Running tests before every commit is a good habit. If any test fails, fix the code first — don't commit broken work.

---

### 2.4 Commit and Push the Branch

```bash
# Stage the new files
git add src/main.py tests/test_main.py

# Commit with a descriptive message
git commit -m "feat: add BMI calculator with category labels"

# Push the branch to GitHub
git push -u origin feature/bmi-calculator

# -u sets the upstream so future pushes only need: git push
```

---

### 2.5 Create a Pull Request and Merge

1. Go to your GitHub repository in the browser.
2. You will see a banner: *"feature/bmi-calculator had recent pushes"*. Click **Compare & pull request**.
3. Add a clear title (e.g. `feat: BMI calculator`) and a brief description of your changes.
4. Click **Create pull request**.
5. Review the diff, then click **Merge pull request → Confirm merge**.
6. Click **Delete branch** to clean up the remote branch.

Sync your local repo:

```bash
# Switch back to main using the modern command
git switch main

# Pull the merged changes
git pull origin main

# Delete the local branch
git branch -d feature/bmi-calculator
```

---

## Part 3 — Introducing a Bug (Intentionally)

This section demonstrates a common real-world mistake: code that passes all tests but produces wrong results because the test cases were also wrong.

### 3.1 Create a Bug Branch

```bash
git switch -c feature/bmi-imperial-input
```

### 3.2 Add the Buggy Code

Replace the contents of `src/main.py` with the version below. The user enters weight in pounds, but the conversion to kilograms is **missing** — so the formula silently receives the wrong value.

```python
# src/main.py  ← BUGGY VERSION

def calculate_bmi(weight_lb: float, height_m: float) -> float:
    """
    Calculate BMI from weight in POUNDS and height in metres.
    BUG: weight is never converted from lb to kg!
    """
    # Missing: weight_kg = weight_lb * 0.453592
    bmi = weight_lb / (height_m ** 2)   # ← uses lb directly — WRONG
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

### 3.3 The Misleading Test

Copy and paste the test below into `tests/test_main.py`, **replacing** the previous content. Notice that the expected value was calculated using the same buggy formula — so pytest reports a pass, but the answer is completely wrong:

```python
# tests/test_main.py  ← TESTS THAT PASS BUT ARE WRONG

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import calculate_bmi


def test_bmi_with_pounds():
    # A person weighing 154 lb at 1.75 m should have a BMI of ~22.86
    # But because the code never converts lb → kg, the result is 50.32
    # This test was written to match the broken output — so it passes!
    assert calculate_bmi(154, 1.75) == 50.32   # WRONG expected value


if __name__ == "__main__":
    try:
        test_bmi_with_pounds()
        print("PASS  test_bmi_with_pounds")
    except AssertionError as e:
        print(f"FAIL  test_bmi_with_pounds  →  {e}")
```

Run it to confirm it passes (incorrectly):

```bash
uv run pytest tests/ -v
# or
uv run python tests/test_main.py
```

> ⚠️ **Warning:** Tests that pass are not proof of correctness — the test data must also be verified against real-world expectations.

### 3.4 Push, PR, Merge, and Delete

```bash
git add src/main.py tests/test_main.py
git commit -m "feat: accept weight in pounds (WIP)"
git push -u origin feature/bmi-imperial-input
```

Then on GitHub: open a PR, merge into `main`, delete the remote branch, and sync locally as shown in section 2.5.

---

## Part 4 — Fetching and Pulling Changes

This is one of the most important distinctions to understand in Git. There are three similar-looking commands that behave very differently.

### The Three Commands Compared

```bash
git pull                  # (1) fetch + merge in one step
git fetch origin main     # (2) download only — don't touch your branches
git fetch origin main:main  # (3) download AND update your local main branch
```

---

### `git pull`

`git pull` is shorthand for two operations: **fetch** then **merge** (or rebase, depending on config). It downloads new commits from the remote **and immediately merges them into your current branch**.

```bash
git switch main
git pull

# Equivalent to:
git fetch origin
git merge origin/main
```

**When to use it:** When you're on a branch and want to bring it up to date with the remote in one step. This is the most common daily command.

**Potential downside:** If you have local uncommitted changes or unpushed commits, the automatic merge can create merge commits or conflicts. Some teams prefer `git fetch` + manual `git merge` for more control.

---

### `git fetch origin main`

`git fetch origin main` downloads commits from the remote `main` branch into a **remote-tracking reference** called `origin/main`. It does **not** touch your local `main` branch or your working directory at all.

```bash
git fetch origin main

# Your local `main` is unchanged.
# But origin/main is now up to date.

# You can inspect what was fetched before merging:
git log main..origin/main          # commits on remote not yet in local main
git diff main origin/main          # see what changed

# Then merge manually when you're ready:
git merge origin/main
```

**When to use it:** When you want to **see what changed** on the remote without affecting your local work. Safe to run at any time.

---

### `git fetch origin main:main`

`git fetch origin main:main` downloads commits from the remote `main` **and also fast-forwards your local `main` branch** to match — but only if you are **not** currently on `main`.

```bash
# You are on a feature branch
git switch feature/bmi-calculator

# This updates local main without switching branches
git fetch origin main:main

# Now local main is up to date — and you never left your feature branch!
# You can now rebase your feature branch onto the updated main:
git rebase main
```

**When to use it:** When you're working on a feature branch and want to update `main` in the background without switching to it. This is particularly useful before rebasing.

> ⚠️ **Warning:** This command will **fail** if you are currently checked out on `main`, because Git won't update a branch you have checked out via a fetch. Use `git pull` instead in that case.

---

### Side-by-Side Summary

| Command | Downloads new commits | Updates `origin/main` ref | Updates local `main` branch | Merges into current branch |
|---|---|---|---|---|
| `git pull` | ✅ | ✅ | ✅ (if on main) | ✅ automatic |
| `git fetch origin main` | ✅ | ✅ | ❌ | ❌ manual |
| `git fetch origin main:main` | ✅ | ✅ | ✅ (if NOT on main) | ❌ manual |

---

### Practical Workflow Example

```bash
# You're deep in a feature branch and hear that main has been updated.
# You want to rebase your feature on the latest main — without switching branches.

git switch feature/bmi-calculator    # you're here

git fetch origin main:main           # update local main silently

git rebase main                      # rebase feature onto updated main

git push --force-with-lease          # push the rebased branch
```

---

## Part 5 — Rolling Back with git revert and git reset

### 5.1 View Your Commit History

```bash
git log --oneline

# Example output:
# a3f2c1d (HEAD -> main) feat: accept weight in pounds (WIP)
# 7b9e4a2 feat: add BMI calculator with category labels
# 1d0c8f3 chore: add README and .gitignore
```

---

### 5.2 git revert — Safe Undo (Recommended)

`git revert` creates a **new commit** that undoes the changes from a specific commit. This is the safest approach because it preserves the full history and is safe on shared branches.

```bash
# Revert the most recent commit
git revert HEAD

# Revert a specific commit by hash
git revert a3f2c1d

# Revert without opening an editor (uses default commit message)
git revert HEAD --no-edit

# Push the revert
git push
```

> 📝 **Note:** After reverting, `git log` will show both the original commit and the new `Revert "..."` commit. The buggy code is gone from the working tree but still visible in history.

---

### 5.3 git reset — Rewrite History (Use with Caution)

`git reset` moves the branch pointer backwards. Use this **only** on commits that have **not** been pushed, or with extreme care on unshared branches.

```bash
# --soft  →  undo commit, keep changes staged
git reset --soft HEAD~1

# --mixed (default)  →  undo commit, keep changes in working directory (unstaged)
git reset HEAD~1

# --hard  →  DISCARD all changes (cannot be undone easily)
git reset --hard HEAD~1

# After a hard reset on a pushed branch you must force-push
# ⚠️  Never force-push to shared branches!
git push --force-with-lease
```

| Mode | What happens to your changes |
|---|---|
| `--soft` | Kept staged — ready to recommit |
| `--mixed` | Kept but unstaged — review before re-staging |
| `--hard` | Permanently discarded — cannot be recovered easily |

> ⚠️ **Warning:** Avoid `git reset --hard` on commits that teammates have already pulled. Use `git revert` for shared branches.

---

### 5.4 git restore — Discard File Changes (Modern Command)

For discarding changes to individual files, use `git restore` instead of the old `git checkout -- <file>`:

```bash
# Discard unstaged changes to a single file
git restore src/main.py

# Discard all unstaged changes in the working directory
git restore .

# Unstage a file (remove from staging area, keep changes in working dir)
git restore --staged src/main.py

# Old equivalents (still work, but less clear):
# git checkout -- src/main.py
# git reset HEAD src/main.py
```

---

### 5.5 Fix the Bug and Commit a Proper Patch

Rolling back is only half the job. Once `main` is back to a known-good state, create a new branch to implement the **correct** solution and verify it with proper tests before merging.

#### Create a fix branch

```bash
git switch main
git pull                          # make sure you have the latest state after the revert
git switch -c fix/bmi-imperial-conversion
```

#### Write the correct code

Open `src/main.py` and replace it with the fixed version that properly converts pounds to kilograms before calculating:

```python
# src/main.py  ← FIXED VERSION

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg: Weight in kilograms.
        height_m:  Height in metres.

    Returns:
        BMI as a float rounded to 2 decimal places.
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than zero.")
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def pounds_to_kg(weight_lb: float) -> float:
    """Convert pounds to kilograms."""
    return round(weight_lb * 0.453592, 4)


def bmi_category(bmi: float) -> str:
    """Return the WHO BMI category label."""
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

#### Update the tests with correct expected values

Open `tests/test_main.py` and replace its content with the corrected test suite. The key difference: we now convert pounds to kg **before** calling `calculate_bmi`, so the expected value matches reality:

```python
# tests/test_main.py  ← CORRECT TESTS

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import calculate_bmi, bmi_category, pounds_to_kg


def test_normal_bmi_kg():
    assert calculate_bmi(70, 1.75) == 22.86

def test_pounds_to_kg_conversion():
    # 154 lb should convert to approximately 69.85 kg
    assert pounds_to_kg(154) == 69.8532

def test_bmi_from_pounds():
    # 154 lb → 69.8532 kg, height 1.75 m → BMI should be ~22.82 (not 50.32!)
    weight_kg = pounds_to_kg(154)
    assert calculate_bmi(weight_kg, 1.75) == 22.82

def test_category_normal():
    assert bmi_category(22.82) == "Normal weight"

def test_category_obese():
    assert bmi_category(32.0) == "Obese"


if __name__ == "__main__":
    tests = [
        test_normal_bmi_kg,
        test_pounds_to_kg_conversion,
        test_bmi_from_pounds,
        test_category_normal,
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

#### Run tests to confirm everything passes

```bash
uv run pytest tests/ -v
# or
uv run python tests/test_main.py
```

All tests should pass before you commit.

#### Commit, push, and open a PR

```bash
git add src/main.py tests/test_main.py
git commit -m "fix: add pounds-to-kg conversion and correct test expectations"
git push -u origin fix/bmi-imperial-conversion
```

Then on GitHub:

1. Open a PR from `fix/bmi-imperial-conversion` → `main`.
2. Write a short description explaining what was wrong and how you fixed it — this is part of the permanent record.
3. Merge the PR, delete the remote branch, and sync locally:

```bash
git switch main
git pull
git branch -d fix/bmi-imperial-conversion
```

> 📝 **Note:** Your commit history now tells a clear story — you can see the buggy commit, the revert, and the proper fix as three separate events. This is exactly how professional teams handle mistakes.

---

## Part 6 — Tagging Releases with git tag

### 6.1 Why Tags?

Tags mark specific commits as meaningful milestones (`v1.0`, `v2.0-beta`, etc.). Unlike branches, tags do not move when new commits are added — they are **permanent pointers** to a snapshot.

---

### 6.2 Creating Tags

```bash
# Lightweight tag (just a name, no message)
git tag v1.0

# Annotated tag (recommended — includes author, date, message)
git tag -a v1.0 -m "Release v1.0: working BMI calculator with kg input"

# Tag a specific past commit
git tag -a v0.1 7b9e4a2 -m "Initial BMI implementation"

# List all tags
git tag

# Show tag details
git show v1.0
```

---

### 6.3 Push Tags to GitHub

```bash
# Push a single tag
git push origin v1.0

# Push ALL tags at once
git push origin --tags
```

> 📝 **Note:** Tags pushed to GitHub automatically appear under **Releases** on the repository page.

---

### 6.4 Creating a GitHub Release from a Tag

1. Go to your repository on GitHub.
2. Click the **Releases** link in the right sidebar (or the Releases tab).
3. Click **Draft a new release**.
4. Select the tag you just pushed from the dropdown.
5. Add release notes and click **Publish release**.

---

### 6.5 Revert to a Previous Release

To restore your project to the state it was in at a tagged release:

```bash
# Option A: Check out the tag in 'detached HEAD' state (read-only look)
git switch --detach v1.0
# Old equivalent: git checkout v1.0

# Option B: Create a new branch FROM the tag and continue working there (recommended)
git switch -c hotfix/v1.0-patch v1.0
# Old equivalent: git checkout -b hotfix/v1.0-patch v1.0

# Option C: Hard reset main to the tag (rewrites history — be careful!)
git switch main
git reset --hard v1.0
git push --force-with-lease
```

> 💡 **Tip:** Option B is usually the safest choice: you get a full working branch based on the stable release, without destroying the buggy history.

| Goal | Recommended command |
|---|---|
| Undo last commit (keep history) | `git revert HEAD` |
| View repo at old release | `git switch --detach v1.0` |
| Start a hotfix from stable release | `git switch -c hotfix/v1.0-patch v1.0` |
| Permanently roll back main (danger!) | `git reset --hard v1.0` + force push |

---

## Quick Reference Cheat Sheet

### Repository Setup

| Command | Description |
|---|---|
| `git init` | Initialise a new local repository |
| `git clone <url>` | Clone an existing remote repository |
| `git remote add origin <url>` | Link local repo to a remote |
| `git remote -v` | Show remote connections |

---

### Everyday Workflow

| Command | Description |
|---|---|
| `git status` | Show staged/unstaged changes |
| `git add <file>` | Stage a file for commit |
| `git add .` | Stage all changes |
| `git commit -m 'msg'` | Commit staged changes |
| `git push` | Push to remote branch |
| `git pull` | Fetch and merge from remote |
| `git fetch origin main` | Download remote changes, don't merge |
| `git fetch origin main:main` | Update local main while on another branch |
| `git log --oneline` | Compact commit history |

---

### Branches (Modern Commands)

| Command | Description |
|---|---|
| `git switch -c <name>` | Create and switch to new branch |
| `git switch <name>` | Switch to existing branch |
| `git switch -` | Switch back to previous branch |
| `git switch --detach <tag>` | Check out a tag or commit in detached HEAD |
| `git merge <name>` | Merge branch into current |
| `git branch -d <name>` | Delete local branch |
| `git push origin --delete <name>` | Delete remote branch |

---

### Discarding Changes (Modern Commands)

| Command | Description |
|---|---|
| `git restore <file>` | Discard unstaged changes to a file |
| `git restore .` | Discard all unstaged changes |
| `git restore --staged <file>` | Unstage a file |

---

### Undo / History

| Command | Description |
|---|---|
| `git revert HEAD` | Safe undo of last commit (keeps history) |
| `git reset --soft HEAD~1` | Undo commit, keep changes staged |
| `git reset --hard HEAD~1` | Undo commit, discard changes |
| `git diff` | Show unstaged differences |
| `git diff HEAD` | Show all uncommitted changes |

---

### Tags

| Command | Description |
|---|---|
| `git tag -a v1.0 -m 'msg'` | Create annotated tag |
| `git tag` | List all tags |
| `git push origin --tags` | Push all tags to remote |
| `git switch --detach v1.0` | Check out code at a tag |
| `git show v1.0` | Display tag details |

---

### Old vs Modern Command Reference

| Old command | Modern equivalent | Notes |
|---|---|---|
| `git checkout -b <name>` | `git switch -c <name>` | Create and switch branch |
| `git checkout <name>` | `git switch <name>` | Switch branch |
| `git checkout <tag>` | `git switch --detach <tag>` | Detached HEAD |
| `git checkout -- <file>` | `git restore <file>` | Discard file changes |
| `git reset HEAD <file>` | `git restore --staged <file>` | Unstage a file |

---

## Common Scenarios

Each scenario below is a self-contained sequence of commands you can follow step-by-step. Read the **Situation** line first, then run the commands in order.

---

### Scenario 1 — Discard Everything and Restore to a Clean Clone State

**Situation:** You've been experimenting, edited files, staged things, maybe even made commits — and you want to go back to exactly what `git clone` would give you. No traces left.

```bash
# ── Step 1: Discard all unstaged changes in tracked files ──────────
git restore .

# ── Step 2: Unstage everything in the staging area ─────────────────
git restore --staged .

# ── Step 3: Remove all untracked files and directories ─────────────
# -f  = force  |  -d  = include directories  |  -n  = dry-run first
git clean -nd          # preview what would be removed (safe, nothing deleted yet)
git clean -fd          # actually remove untracked files and directories

# ── Step 4: Remove any local commits not on origin/main ────────────
# This resets your local branch pointer to exactly match the remote
git fetch origin
git reset --hard origin/main

# ── Done: your working tree is now identical to a fresh clone ───────
git status
# On branch main
# nothing to commit, working tree clean
```

> ⚠️ **Warning:** `git clean -fd` and `git reset --hard` are **irreversible**. Any uncommitted work is permanently gone. Run the `git clean -nd` dry-run first to review what will be deleted.

| What it removes | Command used |
|---|---|
| Edits to tracked files (unstaged) | `git restore .` |
| Files added to staging area | `git restore --staged .` |
| New untracked files and folders | `git clean -fd` |
| Local commits not on remote | `git reset --hard origin/main` |

---

### Scenario 2 — Create a Branch, Make Changes, PR, Merge, and Delete

**Situation:** You are working alone or as the sole reviewer. You need to go through the full professional workflow: branch → code → commit → push → PR → review → merge → clean up.

```bash
# ── Step 1: Make sure main is up to date before branching ──────────
git switch main
git pull

# ── Step 2: Create and switch to a new feature branch ──────────────
git switch -c feature/my-feature

# ── Step 3: Make your code changes, then verify ────────────────────
# (edit files in src/, update tests/, etc.)
uv run pytest tests/ -v          # all tests must pass before committing

# ── Step 4: Stage and commit ────────────────────────────────────────
git add .
git commit -m "feat: describe what this feature does"

# ── Step 5: Push the branch to GitHub ───────────────────────────────
git push -u origin feature/my-feature

# ── Step 6: Open a Pull Request on GitHub ───────────────────────────
# 1. Go to your repository on GitHub.
# 2. Click "Compare & pull request" on the banner that appears.
# 3. Write a title and description explaining your changes.
# 4. Click "Create pull request".

# ── Step 7: Review the PR (you are also the reviewer) ───────────────
# 1. Click the "Files changed" tab and read through every diff.
# 2. Leave a comment if something looks wrong, or approve if it's good.
# 3. Click "Review changes" → "Approve" → "Submit review".

# ── Step 8: Merge the PR ─────────────────────────────────────────────
# 1. Click "Merge pull request" → "Confirm merge".
# 2. Click "Delete branch" to remove the remote branch immediately.

# ── Step 9: Sync locally and clean up ───────────────────────────────
git switch main
git pull                          # pull the merged commit into local main
git branch -d feature/my-feature  # delete the local branch

# ── Done: main now contains your feature ────────────────────────────
git log --oneline -5
```

> 💡 **Tip:** Even when working alone, always go through a PR. It forces you to review your own diff one more time and keeps a clean audit trail of why each change was made.

---

### Scenario 3 — Update Your Branch with the Latest from Main Using Rebase

**Situation:** You are on a feature branch. While you were working, other commits landed on `main`. You want to bring those changes into your branch and place your commits cleanly on top — then resolve any conflicts along the way.

```bash
# ── Step 1: Confirm where you are ───────────────────────────────────
git branch          # should show * feature/my-feature
git log --oneline -5

# ── Step 2: Fetch the latest main without switching branches ─────────
git fetch origin main:main
# This updates your local main to match origin/main.
# You stay on your feature branch throughout.

# ── Step 3: Start the rebase ────────────────────────────────────────
git rebase main
# Git replays your commits one by one on top of the updated main.
# If there are no conflicts, rebase completes automatically — skip to Step 7.
```

If Git stops with a conflict message like `CONFLICT (content): Merge conflict in src/main.py`, continue below:

```bash
# ── Step 4: Inspect what conflicted ─────────────────────────────────
git status
# Shows:  both modified: src/main.py

# Open the conflicted file in VS Code
code src/main.py
# Look for conflict markers and resolve them:
#
# <<<<<<< HEAD (incoming from main)
# weight_kg = weight_lb * 0.453592
# =======
# weight_kg = weight_lb / 2.205
# >>>>>>> your commit message
#
# Edit the file so it contains only the correct final code.
# Delete all the <<<<<<<, =======, and >>>>>>> lines.

# ── Step 5: Stage the resolved file ─────────────────────────────────
git add src/main.py

# ── Step 6: Continue the rebase to the next commit ──────────────────
git rebase --continue
# Git opens an editor for the commit message — save and close it.
# If another conflict appears, repeat Steps 4–6 until rebase finishes.

# To bail out and undo the entire rebase at any point:
# git rebase --abort
```

Once all conflicts are resolved and rebase completes:

```bash
# ── Step 7: Verify the result ───────────────────────────────────────
git log --oneline -8
# You should see:  main's new commits → then your feature commits on top

uv run pytest tests/ -v           # confirm everything still works

# ── Step 8: Push the rebased branch ─────────────────────────────────
# Because rebase rewrites commit history, a normal push will be rejected.
# Use --force-with-lease (safer than --force: fails if someone else pushed)
git push --force-with-lease

# ── Done: your branch now contains all of main's latest changes ──────
# plus your own commits neatly stacked on top.
```

> ⚠️ **Warning:** Never rebase a branch that other people are also working on — rewriting shared history causes serious problems for teammates. Rebase is safe only on your own private feature branches.

**Rebase conflict flow at a glance:**

```
git rebase main
        │
        ▼
  conflict? ──No──► rebase complete ──► git push --force-with-lease
        │
       Yes
        │
        ▼
  open file, fix markers, save
        │
        ▼
  git add <file>
        │
        ▼
  git rebase --continue
        │
        └──► more conflicts? loop back to "open file"
```

---

### Scenario 4 — Forked Repo: Sync Upstream → Forked Main → Working Branch

**Situation:** You have forked someone else's repository on GitHub. Your local clone points to your fork (`origin`). The original repo is `upstream`. New commits have landed on upstream's `main` and you need them in your fork's `main` and then in your working branch — all from the CLI.

```bash
# ── Step 1: One-time setup — add the upstream remote ────────────────
# Only needed the very first time. Skip if you've done this already.
git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPO.git

# Verify both remotes exist
git remote -v
# origin    https://github.com/YOUR_USERNAME/ORIGINAL_REPO.git (fetch)
# origin    https://github.com/YOUR_USERNAME/ORIGINAL_REPO.git (push)
# upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPO.git (fetch)
# upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPO.git (push)

# ── Step 2: Fetch all new commits from upstream ──────────────────────
git fetch upstream
# Downloads upstream's commits into upstream/main, upstream/dev, etc.
# Nothing in your working tree changes yet.

# ── Step 3: Update your fork's local main ───────────────────────────
git switch main
git merge upstream/main
# Fast-forward merge: moves your local main pointer forward.
# No merge commit is created if your fork's main hasn't diverged.

# ── Step 4: Push the updated main to your fork on GitHub ─────────────
git push origin main
# Your fork on GitHub is now in sync with upstream.

# ── Step 5: Switch back to your working branch ───────────────────────
git switch feature/my-feature

# ── Step 6: Update the working branch with the latest main ───────────
# Option A — Rebase (cleaner history, preferred for feature branches)
git rebase main

# Option B — Merge (keeps history as-is, creates a merge commit)
# git merge main

# ── Step 7: Resolve conflicts if any appear ──────────────────────────
# If rebase pauses with a conflict:

git status                         # see which files conflicted
code src/main.py                   # open and fix the conflict markers

git add src/main.py                # stage the resolved file
git rebase --continue              # resume — repeat for each conflict

# ── Step 8: Push the updated branch to your fork ─────────────────────
# If you used rebase, history was rewritten — force push is required
git push --force-with-lease origin feature/my-feature

# If you used merge instead, a normal push is fine
# git push origin feature/my-feature

# ── Done ────────────────────────────────────────────────────────────
git log --oneline -8
# upstream main commits → your feature commits on top
```

> 💡 **Tip:** Get into the habit of running Steps 2–4 every morning before you start work. Keeping your fork's `main` fresh means smaller, simpler rebases on your feature branches.

**Full sync flow at a glance:**

```
upstream/main  ──fetch──►  upstream/main (local ref)
                                    │
                               merge into
                                    │
                                    ▼
                            local main  ──push──►  origin/main (your fork)
                                    │
                                rebase
                                    │
                                    ▼
                         feature/my-feature  ──force push──►  origin/feature/my-feature
```

| Remote name | Points to |
|---|---|
| `origin` | Your personal fork on GitHub |
| `upstream` | The original repository you forked from |
| `upstream/main` | Local tracking ref for upstream's main branch |
