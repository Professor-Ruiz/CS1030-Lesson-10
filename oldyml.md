
name: Build and Test

on:
  push:
    # This workflow will only execute when there is a push to the student solution file or the testing script
    # This workflow will not execute when a repo is first created (cloned, assigned, forked, etc)
    # https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions
    paths: 
      - 'tests/test_exercise.py'      # testing script
      - 'src/exercise.py'             # student solution file

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
      # By using 'Python 3.x' syntax below, the runner will use the newest release of Python 3 available
      # https://docs.github.com/en/actions/guides/building-and-testing-python
    - name: Set up Python 3.x
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest flake8
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        python -m pytest