from calc_session_assignment import *
import os
import subprocess
import pytest
from git import Repo

def test_add_negative_numbers():
    result =add(-2,0)
    assert result == -2

def test_add_positive_numbers():
    result =add(2,3)
    assert result == 5

def test_add_zero():
    result =add(-2,0)
    assert result == -2

def test_divide_by_numbers():
    result =divide(-2,0)
    assert result == 'infinity'

def run_tests():
    # Run pytest
    result = pytest.main()

    return result

def merge_to_dev():
    # Change to the project directory
    os.chdir("/Users/Lokesh/OneDrive/Desktop/Hero Vired/Devops/Testing/testing_calculator")

    # Check if the tests have passed
    test_result = run_tests()

    # If the tests passed, merge the test branch to the dev branch
    if test_result == pytest.ExitCode.OK:
        repo = Repo()
        dev_branch = repo.heads["dev"]
        test_branch = repo.heads["test"]
        dev_branch.checkout()
        dev_branch.merge(test_branch)
        print("Test branch merged to dev branch successfully!")
    else:
        print("Tests failed. Not merging to dev branch.")

if __name__ == "__main__":
    merge_to_dev()

