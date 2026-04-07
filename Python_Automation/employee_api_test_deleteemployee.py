import requests
import time

BASE_URL = "http://dummy.restapiexample.com/api/v1"

def test_delete_employee(employee_id, retries=5, delay=5):
    """
    Automate deleting an employee and verify the response.
    """
    url = f"{BASE_URL}/delete/{employee_id}"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    for attempt in range(1, retries + 1):
        try:
            response = requests.delete(url, headers=headers, timeout=10)

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

            # Assertions for automation
            assert "status" in result, "Missing 'status' key in response"
            assert result["status"] == "success", f"Expected status 'success', got {result['status']}"
            assert "data" in result, "Missing 'data' key in response"

            print(f"✅ DELETE EMPLOYEE {employee_id} TEST PASSED")
            return result

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt} failed: {e}")
            time.sleep(delay)

    print(f"❌ DELETE EMPLOYEE {employee_id} TEST FAILED")
    return None


if __name__ == "__main__":
    employee_id = 1  # Employee id 1 is deleted
    result = test_delete_employee(employee_id)
    if result:
        print(f"DELETE EMPLOYEE {employee_id} SUCCESS:")
        print(result)
    else:
        print(f"Failed to delete employee {employee_id}.")