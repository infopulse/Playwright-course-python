# Example of pytest playwright test automation project

## About
Materials to help you get started with test automation using pytest and playwright.  
Software to be tested is a https://coffee-cart.app/

## Installation
1. Install python 3.11 or higher
2. activate virtual environment 
3. install poetry `pip install poetry`
4. run `poetry install` to install all dependencies
5. install Playwright browsers `playwright install`

## Run tests
- Check test configuration in [pyproject.toml](pyproject.toml) file 
  - Make sure tests are running in headless mode
  - Make sure tests are running in parallel
- run `pytest` to run all tests in the project
- run `pytest -m mobile` to run mobile tests only
- run `pytest -m quality_gate` to run QG tests only

