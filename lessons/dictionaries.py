"""Demonstarations of dictionary capabilities."""

# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has ~{schools['UNC']} undergrads")

# Remove a key-value pair from a dictionary
# By its key
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# Update / Reassign a key-value pair
schools["UNC"] = 20_000
schools["NCSU"] += 200
print(schools)

# ALternatively, initialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

# print(schools["UNCC"])

# Example of looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")

print(type(school))


