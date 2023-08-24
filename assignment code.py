class Match:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

matches = [
    Match("Mumbai", "India", "Sri Lanka", "DAY"),
    Match("Delhi", "England", "Australia", "DAY-NIGHT"),
    Match("Chennai", "India", "South Africa", "DAY"),
    Match("Indore", "England", "Sri Lanka", "DAY-NIGHT"),
    Match("Mohali", "Australia", "South Africa", "DAY-NIGHT"),
    Match("Delhi", "India", "Australia", "DAY")
]

def search_matches_by_team(team):
    results = []
    for match in matches:
        if team in [match.team1, match.team2]:
            results.append(match)
    return results

def search_matches_by_location(location):
    results = []
    for match in matches:
        if match.location == location:
            results.append(match)
    return results

def search_matches_by_timing(timing):
    results = []
    for match in matches:
        if match.timing == timing:
            results.append(match)
    return results

# User input
choice = int(input("Choose the search parameter: \n1. List of all the matches of a Team\n2. List of Matches on a Location\n3. List of Matches based on timing\n"))

if choice == 1:
    team = input("Enter the team name: ")
    results = search_matches_by_team(team)
elif choice == 2:
    location = input("Enter the location: ")
    results = search_matches_by_location(location)
elif choice == 3:
    timing = input("Enter the timing: ")
    results = search_matches_by_timing(timing)
else:
    print("Invalid choice")

# Print the results
print("Search results:")
for result in results:
    print(f"Match Location: {result.location}")
    print(f"Team 01: {result.team1}")
    print(f"Team 02: {result.team2}")
    print(f"Timing: {result.timing}")
    print()