# local
import helpers
# init
import json
# extermal
from dotenv import load_dotenv

# LOADING .env
load_dotenv()

# REQUEST
response = helpers.makeRequest()

# PARSE HTML
result = helpers.parseWeek(response.text)

# TO JSON
with open("output.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(result, indent=2, ensure_ascii=False))