import requests

response=requests.get(url="http://localhost:5020/animals")
response_heads=requests.get(url="http://localhost:5020/animals/head/?head_type=snake")
response_legs=requests.get(url="http://localhost:5020/animals/legs/?leg_num=6")

print(response.status_code)
print(response.json())
print(response.headers)

print(response_heads.status_code)
print(response_heads.json())
print(response_heads.headers)

print(response_legs.status_code)
print(response_legs.json())
print(response_legs.headers)



