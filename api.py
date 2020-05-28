from flask import *
import dotenv
import os
import Database
import pymongo
dotenv.load_dotenv()
print(os.getenv('API-KEY'))
api = Flask(__name__)

@api.route('/')
def home():
    return """<p>END POINT:/api/api-key/'category(country or region)'/'data'</p><p>UPDATE:/api/update</p>\n<p>NOTE:type the country name with first letter caps</p>"""

@api.route('/api/update')
def update():
    try:
        Database.update_database()
        return "done"
    except:
        abort(500)


def db():
    client = pymongo.MongoClient(f'''mongodb+srv://Jofin:{os.getenv('PASSWORD')}@cluster0-e29hp.mongodb.net/test?retryWrites=true&w=majority''')
    cluster = client['birthday']
    coll = cluster['COVID-19']
    return coll

@api.route('/api/<string:key>/<string:category>/<string:data>')
def req(key,category,data):
    database = db()
    if key==os.getenv('API-KEY'):
        query = {f'{category}':f'{data}'}
        result = database.find(query)
        if result.count()==0:
            return jsonify({"result":"None"})
        else:
            l = list()
            for i in result:l.append(i)
            return jsonify(l)
    else:
        abort(401)

if __name__ =="__main__":
    api.run(debug=True)