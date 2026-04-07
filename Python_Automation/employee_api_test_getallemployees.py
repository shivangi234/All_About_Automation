import requests
import time

BASE_URL = "http://dummy.restapiexample.com/api/v1"


def test_get_all_employees(retries=5, delay=3):
    url = f"{BASE_URL}/employees"
    headers = {
        "Accept": "application/json, text/plain, */*",  # Accept all common content types
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, headers=headers, timeout=10)

            # Handle 406 and retry
            if response.status_code == 406:
                print(f"Attempt {attempt} failed: 406 Not Acceptable. Retrying after {delay} seconds...")
                time.sleep(delay)
                continue

            # Raise for other HTTP errors
            response.raise_for_status()

            data = response.json()

            # Automate using assert
            assert "status" in data, "Missing 'status' key"
            assert data["status"] == "success", f"Expected status 'success', got {data['status']}"
            assert "data" in data, "Missing 'data' key"
            assert isinstance(data["data"], list), "'data' should be a list"

            print("✅ GET ALL EMPLOYEES TEST PASSED")
            return data

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt} failed: {e}")
            time.sleep(delay)

    print("❌ GET ALL EMPLOYEES TEST FAILED")
    return None


if __name__ == "__main__":
    employees = test_get_all_employees()
    if employees:
        print("Employee data fetched successfully.")
    else:
        print("No data received.")