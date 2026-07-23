import requests as r

base_url = "https://pokeapi.co/api/v2/"
def pokemon(name):
    path = f"{base_url}/pokemon/{name}"
    response = r.get(path)
    if response.status_code == 200:
        print("Data retrieved!")
        return response.json()
    else:
        print("Enter an actual pokemon.")
name = input("Enter pokemon name: ")
info = pokemon(name)
if info:
    print(f"Name: {info["name"].capitalize()}")
    print(f"Height: {info["height"]}cm")
    print(f"Weight: {info["weight"]} lbs")
    print(f"ID: {info["id"]}")