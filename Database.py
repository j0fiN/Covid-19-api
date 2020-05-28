import pymongo
import os
import scraper
import dotenv
dotenv.load_dotenv()
pas = os.getenv('PASSWORD')

def update_database():
    client = pymongo.MongoClient(f'mongodb+srv://Jofin:{pas}@cluster0-e29hp.mongodb.net/test?retryWrites=true&w=majority')
    data = scraper.scrape()
    cluster = client['birthday']
    coll = cluster['COVID-19']
    coll.delete_many({})
    coll.insert_many(data)
    print('done')

if __name__=="__main__":
    update_database()
