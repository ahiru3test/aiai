import json

with open("Sample2.json", "r", encoding="utf-8") as f:
  data=json.load(f)
  print(data)
# f.close()
