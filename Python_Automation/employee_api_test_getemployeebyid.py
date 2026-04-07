import requests
import time
import random  # added

BASE_URL = "http://dummy.restapiexample.com/api/v1"

def test_get_employee_by_id(employee_id, retries=5, delay=5):
    url = f"{BASE_URL}/employee/{employee_id}"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, headers=headers, timeout=10)

            # Better delay calculation (only change)
            wait_time = delay * (2 ** (attempt - 1)) + random.uniform(0, 2)

            # Handle 429
            if response.status_code == 429:
                print(f"Attempt {attempt} failed: 429 Too Many Requests. Waiting {wait_time:.2f}s...")
                time.sleep(wait_time)
                continue

            # Handle 406
            if response.status_code == 406:
                print(f"Attempt {attempt} failed: 406 Not Acceptable. Retrying in {wait_time:.2f}s...")
                time.sleep(wait_time)
                continue

            response.raise_for_status()

            data = response.json()

            assert "status" in data, "Missing 'status' key"
            assert data["status"] == "success", f"Expected status 'success', got {data['status']}"
            assert "data" in data, "Missing 'data' key"
            assert isinstance(data["data"], dict), "'data' should be a dictionary"

            print(f"✅ GET EMPLOYEE {employee_id} TEST PASSED")
            return data

        except requests.exceptions.RequestException as e:
            wait_time = delay * (2 ** (attempt - 1)) + random.uniform(0, 2)
            print(f"Attempt {attempt} failed: {e}. Retrying in {wait_time:.2f}s...")
            time.sleep(wait_time)

    print(f"❌ GET EMPLOYEE {employee_id} TEST FAILED")
    return None


if __name__ == "__main__":
    employee_id = 1
    employee = test_get_employee_by_id(employee_id)
    if employee:
        print(f"GET EMPLOYEE {employee_id} SUCCESS:")
        print(employee)
    else:
        print(f"No data received for employee {employee_id}.")