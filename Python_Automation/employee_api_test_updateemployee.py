import requests
import time

BASE_URL = "http://dummy.restapiexample.com/api/v1"

def test_update_employee(employee_id, name=None, salary=None, age=None, retries=5, delay=5):
    """
    Automate updating an employee and verify response.
    Only fields provided (name, salary, age) will be updated.
    """
    url = f"{BASE_URL}/update/{employee_id}"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    data = {}
    if name is not None:
        data["name"] = name
    if salary is not None:
        data["salary"] = salary
    if age is not None:
        data["age"] = age

    for attempt in range(1, retries + 1):
        try:
            response = requests.put(url, headers=headers, json=data, timeout=10)

            # Handle 429 Too Many Requests
            if response.status_code == 429:
                print(f"Attempt {attempt} failed: 429 Too Many Requests. Waiting longer...")
                time.sleep(delay * attempt)
                continue

            # Handle 406 Not Acceptable
            if response.status_code == 406:
                print(f"Attempt {attempt} failed: 406 Not Acceptable. Retrying after {delay} seconds...")
                time.sleep(delay)
                continue

            response.raise_for_status()
            result = response.json()

            # automate using assert
            assert "status" in result, "Missing 'status' key in response"
            assert result["status"] == "success", f"Expected status 'success', got {result['status']}"
            assert "data" in result, "Missing 'data' key in response"
            assert isinstance(result["data"], dict), "'data' should be a dictionary"

            print(f"✅ UPDATE EMPLOYEE {employee_id} TEST PASSED")
            return result

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt} failed: {e}")
            time.sleep(delay)

    print(f"❌ UPDATE EMPLOYEE {employee_id} TEST FAILED")
    return None


if __name__ == "__main__":
    employee_id = 1
    # Example updated data
    name = "John Smith"
    salary = 60000
    age = 31

    employee = test_update_employee(employee_id, name=name, salary=salary, age=age)
    if employee:
        print(f"UPDATE EMPLOYEE {employee_id} SUCCESS:")
        print(employee)
    else:
        print(f"Failed to update employee {employee_id}.")