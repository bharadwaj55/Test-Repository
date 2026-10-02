# Test-Repository

A practice repository demonstrating a basic Git workflow: clone, branch, commit and push.

## Steps Followed

### 1. Clone the repository

```bash
git clone https://github.com/bharadwaj55/Test-Repository.git
```

### 2. Create and check out the `feature-1` branch from `main`

```bash
git checkout -b feature-1
```

### 3. Work done

Added the Python task files (`strings.py`, `lists.py`, `dictionaries.py`, `functions.py`), made changes to them, then staged, committed and pushed.

### 4. Git commands used

```bash
git status
git add .
git commit -m "<commit message>"
git push origin <branch-to-push>
```

### 5. Commits made

Command used to list them (newest first):

```bash
git log --oneline
```

Combined output:

```text
f14741f (HEAD -> feature-1, origin/feature-1)
        feature-1 added function to check and return if given number is even or not in functions.py file
65c630e feature-1 added operations to find even numbers, sum, min, max from lists in lists.py file
ac1cb67 feature-1 added palindrome check in strings.py file
d01f8b1 feature-1 added multiply function in functions.py file
7bbf2e1 feature-1 added subtract function in functions.py file
23ec295 feature-1 added python task files
f196ba7 (origin/main, origin/HEAD, main)
        Initial commit
```

Explanation of each commit:

| #   | Commit    | Description                                                            |
|-----|-----------|------------------------------------------------------------------------|
| 7   | `f14741f` | Added function to check if a number is even in `functions.py`          |
| 6   | `65c630e` | Added even numbers, sum, min and max operations on lists in `lists.py` |
| 5   | `ac1cb67` | Added palindrome check in `strings.py`                                 |
| 4   | `d01f8b1` | Added `multiply` function in `functions.py`                            |
| 3   | `7bbf2e1` | Added `subtract` function in `functions.py`                            |
| 2   | `23ec295` | Added Python task files                                                |
| 1   | `f196ba7` | Initial commit (on `main`)                                             |

Branch pointers: `feature-1` and `origin/feature-1` are at `f14741f`. `main`, `origin/main` and `origin/HEAD` are at `f196ba7`.

### 6. Git reflog

Output of `git reflog`, showing the sequence of actions in the local repository:

```text
f14741f (HEAD -> feature-1, origin/feature-1) HEAD@{0}: commit: feature-1 added function to check and return if given number is even or not in functions.py file
65c630e HEAD@{1}: commit: feature-1 added operations to find even numbers, sum, min, max from lists in lists.py file
ac1cb67 HEAD@{2}: commit: feature-1 added palindrome check in strings.py file
d01f8b1 HEAD@{3}: commit: feature-1 added multiply function in functions.py file
7bbf2e1 HEAD@{4}: commit: feature-1 added subtract function in functions.py file
23ec295 HEAD@{5}: commit: feature-1 added python task files
f196ba7 (origin/main, origin/HEAD, main) HEAD@{6}: checkout: moving from main to feature-1
f196ba7 (origin/main, origin/HEAD, main) HEAD@{7}: clone: from https://github.com/bharadwaj55/Test-Repository.git
```

### 7. Pull request

After pushing `feature-1` to GitHub, a pull request (PR) was raised to merge the changes from `feature-1` into `main`.

1. Opened the repository on GitHub and click **Compare & pull request** for `feature-1`.
2. Set the base branch to `main` and the compare branch to `feature-1`.
3. Added the title "Added python task files", then click **Create pull request**.
4. Review the changes and click **Merge pull request** to merge `feature-1` into `main`.
