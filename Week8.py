import pymongo
import datetime
from flask import Flask,request

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://restect:pastibisa@cluster.t2gqqht.mongodb.net/?retryWrites=true&w=majority")
db = client['Week8']
my_collections = db['Ibnu']

@app.route('/location',methods = ['GET','POST'])
def location():
    kecepatan = request.args.get('kecepatan')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    if request.method == 'POST' :
        result = my_collections.insert_one({"kecepatan":kecepatan,"latitude":latitude,"longitude":longitude})
        print(result)
        return {
            "output":{
                "kecepatan": kecepatan,
                "latitude":latitude,
                "longitude":longitude,
                "timestamp":datetime.datetime.now()
                    }
            }

if __name__ == '__main__':
    app.run(debug=True)