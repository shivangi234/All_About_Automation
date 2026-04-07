import subprocess

scripts = [
    "employee_api_test_getallemployees.py",
    "employee_api_test_getemployeebyid.py",
    "employee_api_test_createemployee.py",
    "employee_api_test_updateemployee.py",
    "employee_api_test_deleteemployee.py",
]

for script in scripts:
    print(f"\n===== Running {script} =====")
    try:
        # Run the script using the same Python interpreter
        subprocess.run(["python", script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script}: {e}")