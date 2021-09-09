# GitHub Actions

We want to leverage [GitHub Actions](https://docs.github.com/en/actions) to automatically update the [search page](https://audinux.github.io/packages/index.html) when this repo is updated.


## Why

This GitHub repo has an associated Web Site: https://audinux.github.io/ 
and packages can be [search and filtered](https://audinux.github.io/packages/index.html).

Problem: The metadata used for the search are created with a Python script. We have to run it and copy files each time the SPECs files are updated.


## How

On git push:
1. the Python script [parse-spec](https://github.com/audinux/parse-spec) 
  - scans all the spec files for specific tags 
  - generates a json file containing metadata about the packages
2. push this file to the web site where it is used in the filters


There are many ways to manages GitHub Actions, but the plan is to:
- create a workflow in this repo
- trigger on push
  - ideally filter on main branch, filter on spec file changes only
- create a machine
  - install Python (see https://github.community/t/how-to-setup-github-actions-to-run-my-python-script-on-schedule/18335/2)
  - checkout this repo
  - checkout the Python Script
    - or use a Composite Action?  See https://docs.github.com/en/actions/creating-actions/creating-a-composite-action
  - run the script
    - specify directory to scan
    - specify file to export
  - Push file to Web site https://github.com/audinux/audinux.github.io

## Project planning

- Nothing is done yet. 
- The work is in branch `gh_action`
- It will be tested
- Then merged