"""This is a public API which is used to fetch data from MongoDB host"""

import json
import pymongo
from flask import Flask, request
import re
app = Flask(__name__)

def db_connection():
    client = pymongo.MongoClient("mongodb+srv://pasta:pasta_qwerty@pythoncluster.zqoyn8m.mongodb.net/?retryWrites=true&w=majority")
    db = client["NewsDatabase"]
    col = db["Articles"]
    return col  #collection return


def search(text):
    collection = []
    
    for data in db_connection().aggregate([{'$search': {'index': 'default_index','text': {'query': text,'path': {'wildcard': '*'}}}}]):                                                        
        
        data['_id'] = str(data['_id']) 
        collection.append(data)
    return collection

@app.route('/search', methods = ['GET'])
def search_api():
    if (request.method == 'GET'):
        keyword = request.args.get('search')
        store = search(keyword)
        
        if keyword.isalpha():  
            return json.dumps(store)
        return ''

if __name__ == '__main__':
    app.run(port=3001, debug = True)
