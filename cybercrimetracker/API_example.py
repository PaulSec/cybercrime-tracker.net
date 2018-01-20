from cybercrimetracker.cybercrimeTrackerAPI import cybercrimeTrackerAPI
import sys
import json

query = ''
if len(sys.argv) > 1:
   query = sys.argv[1]
# print(json.dumps(cybercrimeTrackerAPI().search(query), indent=2))
print(json.dumps(cybercrimeTrackerAPI().dump(query), indent=2))