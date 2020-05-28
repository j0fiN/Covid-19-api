import requests
import os
import dotenv
def check(a,b):
    dotenv.load_dotenv()
    res = requests.request("GET",url=f'''http://127.0.0.1:5000/api/{os.getenv('API-KEY')}/{a}/{b}''')
    return eval(res.text)

print(type(check('country','India')))