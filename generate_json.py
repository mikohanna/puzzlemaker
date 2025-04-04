import json
import os

# Example JSON data
data = {
    "puzzle": [[1, 2, 3], [4, 5, 6]]
}

# Save JSON to the /data/ folder
os.makedirs("data", exist_ok=True)
with open("data/puzzle.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("✅ JSON file generated successfully!")
