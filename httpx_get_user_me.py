import httpx

payload = {
    "email": "test123@mail.com",
    "password": "test_pass"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

headers = {
    "Authorization": f"{login_response_data["token"]["tokenType"]} {login_response_data["token"]["accessToken"]}"
}

users_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
users_me_response_data = users_me_response.json()

print("User response:", users_me_response_data)
print("Status Code:", users_me_response.status_code)
