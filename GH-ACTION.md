# GitHub Actions

We want to leverage [GitHub Actions](https://docs.github.com/en/actions) to automatically update the [search page](https://audinux.github.io/packages/index.html) when this repo is updated.

> A workflow can be easily disabled: https://docs.github.com/en/actions/managing-workflow-runs/disabling-and-enabling-a-workflow .


## Why

This GitHub repo has an associated Web Site: https://audinux.github.io/ 
and packages can be [search and filtered](https://audinux.github.io/packages/index.html).

Problem: The metadata used for the search are created with a Python script. Without automation, we have to run it and copy files each time the SPECs files are updated.


## How

On git push:
1. the Python script [parse-spec](https://github.com/audinux/parse-spec) 
  - scans all the spec files for specific tags 
  - generates a json file containing metadata about the packages
2. push this file to the web site where it is used in the filters


There are many ways to manages GitHub Actions, but the plan is to:
- create a workflow in this repo
- trigger on push
  - filter on main branch `[ $default-branch ]` https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#onpushpull_requestbranchestags
  - filter on spec file only  https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#onpushpull_requestpaths
- create a machine (https://github.community/t/how-to-setup-github-actions-to-run-my-python-script-on-schedule/18335/2)
  - install Python (see https://github.com/marketplace/actions/setup-python )
  - checkout this repo
  - checkout the Python Script (https://github.com/marketplace/actions/checkout)
  - run the script
    - specify directory to scan
    - specify file to export
  - Push file to Web site https://github.com/audinux/audinux.github.io
    - use https://github.com/marketplace/actions/push-a-file-to-another-repository
    -  or https://docs.github.com/en/actions/guides/storing-workflow-data-as-artifacts


## Where

In this repo, there is a `.github/workflows/search-refresh.yml` file.

See also:

- https://github.com/audinux/fedora-spec/actions 
- https://github.com/audinux/fedora-spec/settings/secrets/actions 


## Security

To push to audinux Web site: (See https://github.com/marketplace/actions/push-a-file-to-another-repository)
1. I created a personal GitHub Access Token (It is NOT the recommended way, but to update another repo via the API, it looks like there is no other way.)
2. It is setup in the `fedora-spec` repo Secrets

It expire in 90 days, will see ...


The Actions do not need to modify the `fedora-spec` repo!  It could be set read only!

https://docs.github.com/en/actions/learn-github-actions/security-hardening-for-github-actions
https://docs.github.com/en/actions/reference/authentication-in-a-workflow#modifying-the-permissions-for-the-github_token


## TODO

- The Json file should be tested (non-empty, valid format, at least 200 packages, ...) before being pushed to the Wbe site repo.
  - A specific step should be added to the job for this, but might be complicated
  - An easy solution is to add the tests to the Python program
- The action is triggered in one repo `fedora-spec`, but pushes to another repo `audinux.github.io`. It is not recommended for security.
  - Could use another action (one that does not use GitHub REST API)
  - Very simply, we could move this workflow to `audinux.github.io` and schedule it daily instead of triggered on push.


