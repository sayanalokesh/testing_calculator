import subprocess
import csv

def run_pytest():
    # Run pytest and capture the test results
    result = subprocess.run(['pytest'], capture_output=True, text=True)
    test_output = result.stdout

    # Check if all test cases passed
    if "failed" not in test_output.lower():
        # Save test results to a CSV file
        with open('test_results.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Test Case', 'Status'])
            test_cases = test_output.strip().split('\n')
            for test_case in test_cases:
                test_name = test_case.strip()
                writer.writerow([test_name, 'Passed'])

        # Merge the test branch to the deployment branch
        subprocess.run(['git', 'checkout', 'deployment'])
        subprocess.run(['git', 'merge', 'test'])
        subprocess.run(['git', 'push', 'origin', 'deployment'])
        print("All test cases passed. Test branch merged to deployment branch.")
    else:
        print("Some test cases failed. Skipping merge.")

if __name__ == "__main__":
    run_pytest()
