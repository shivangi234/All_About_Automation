import requests
import time

BASE_URL = "http://dummy.restapiexample.com/api/v1"

def test_create_employee(name, salary, age, retries=5, delay=5):

    url = f"{BASE_URL}/create"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    data = {
        "name": name,
        "salary": salary,
        "age": age
    }

    for attempt in range(1, retries + 1):
        try:
            response = requests.post(url, headers=headers, json=data, timeout=10)

            # Handle 429 Too Many Requests with exponential backoff
            if response.status_code == 429:
                print(f"Attempt {attempt} failed: 429 Too Many Requests. Waiting longer...")
                time.sleep(delay * attempt)
                continue

            # Handle 406 Not Acceptable (common with this dummy API)
            if response.status_code == 406:
                print(f"Attempt {attempt} failed: 406 Not Acceptable. Retrying after {delay} seconds...")
                time.sleep(delay)
                continue

            response.raise_for_status()
            result = response.json()

            # Assertions for automation
            assert "status" in result, "Missing 'status' key in response"
            assert result["status"] == "success", f"Expected status 'success', got {result['status']}"
            assert "data" in result, "Missing 'data' key in response"
            assert isinstance(result["data"], dict), "'data' should be a dictionary"

            print("✅ CREATE EMPLOYEE TEST PASSED")
            return result

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt} failed: {e}")
            time.sleep(delay)

    print("❌ CREATE EMPLOYEE TEST FAILED")
    return None


if __name__ == "__main__":
    # Check employee data
    name = "John Doe"
    salary = 50000
    age = 30

    employee = test_create_employee(name, salary, age)
    if employee:
        print("CREATE EMPLOYEE SUCCESS:")
        print(employee)
    else:
        print("Failed to create employee.")