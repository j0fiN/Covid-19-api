import pymongo
import scraper
cluster =pymongo.MongoClient('mongodb+srv://Jofin:JT9wYx0RQKObQVvO@cluster0-e29hp.mongodb.net/test?retryWrites=true&w=majority')
database = cluster["birthday"]

collection = database["COVID-19"]

data = scraper.scrape()

collection.insert_many(data)

