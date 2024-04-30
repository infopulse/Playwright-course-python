# Workflow example and guide
How to configure workflow in a product repo to trigger tests in a pytest-playwright repo.  

## Steps
1. Check the GitHub REST API documentation: [Create a repository dispatch event](https://docs.github.com/en/rest/reference/repos#create-a-repository-dispatch-event)
2. Goto **GitHub -> Settings -> Developer settings -> Personal access tokens -> Generate new token**
   1. Set the token name
   2. Select the expiration date
   3. Select the `Resource owner` (for personal account leave it as is, for organization select the organization. If you don't see the organization, you need to enable token access in the organization settings)
   4. Select the `Repository access` (all or for specific projects)
   5. Select the `Repository Permission`: **contents:write**
   6. Click `Generate token` button
   7. Copy the token. ⚠️ You will not be able to see it again
3. Go to the product **repo -> Settings -> Secrets -> New repository secret** 
    1. Set the secret name: REPO_ACCESS_TOKEN
    2. Paste the token from step 2
    3. Click `Add secret` button

## Examples
Product repo workflow example. Should be updated:
- `owner: 'infopulse'` to your organization name or your account name
- `repo: 'Playwright-course-python'` to your test repo name
- `event_type: 'on-demand-test'` should be the same as in the test repo workflow in `repository_dispatch` types
- `REPO_ACCESS_TOKEN` should have same name as a created secret in the product repo
```yaml
name: build-workflow

on:
  workflow_dispatch:
  push:
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
      
    # your build steps here
    
    - name: Trigger workflow in another repo
      uses: actions/github-script@v7
      with:
        script: |
          const clientPayload = { event_type: 'build_completed' };

          const response = await github.rest.repos.createDispatchEvent({
            owner: 'infopulse', 
            repo: 'Playwright-course-python',
            event_type: 'on-demand-test',
            client_payload: {build : 'ok'},
          });

          console.log(response);
        github-token: ${{ secrets.REPO_ACCESS_TOKEN }}
```

Playwright repo workflow example:
```yaml
name: playwright-general
on:
  repository_dispatch:
    types: [ on-demand-test ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        
      # your test steps here
```