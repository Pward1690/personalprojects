import requests
import json

while True:
    year = input("Enter the year (1900-1993): ")
    if year.isnumeric() and int(year) in range(1900, 2100):
        break
    print("Invalid input. Please enter a valid year between 1900 and 1993.")

url = f"https://statsapi.mlb.com/api/v1/standings?leagueId=104&season={year}&standingsTypes=regularSeason"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for a bad response status code
except requests.exceptions.RequestException as e:
    print("Error: Could not retrieve data from API.")
    print(e)
    exit()

try:
    data = json.loads(response.text)
    for team in data["records"][0]["teamRecords"]:
        if team["team"]["name"] == "Chicago Cubs":
            wins = team["wins"]
            losses = team["losses"]
            break
    else:
        print("Error: No data found for the Chicago Cubs.")
        exit()
except (KeyError, IndexError, json.JSONDecodeError) as e:
    print("Error: Could not parse data from API.")
    print(e)
    exit()

print(f"The Chicago Cubs' record in {year} was {wins}-{losses}")
