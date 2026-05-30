import requests

try:
    print("Fetching data from API...\n")

    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    response.raise_for_status()

    users = response.json()

    print("===== ALL USERS =====\n")

    for user in users:
        print(f"Name : {user['name']}")
        print(f"Email: {user['email']}")
        print(f"City : {user['address']['city']}")
        print("-" * 35)

    # Search Feature
    print("\n===== SEARCH USER BY CITY =====")

    city_name = input("Enter city name: ")

    found = False

    for user in users:
        if user["address"]["city"].lower() == city_name.lower():
            print("\nUser Found:")
            print(f"Name : {user['name']}")
            print(f"Email: {user['email']}")
            print(f"City : {user['address']['city']}")
            found = True

    if not found:
        print("No user found in that city.")

except requests.exceptions.RequestException as e:
    print("API Error:", e)

except Exception as e:
    print("Unexpected Error:", e)