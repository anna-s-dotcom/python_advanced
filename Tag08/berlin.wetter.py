import requests
from flask import Flask
from flask_restful import Api,Resource

app=Flask(__name__)
api=Api(app)

api_url="http://api.openweathermap.org/data/2.5/weather"
APPID="ae344fafd76de4ffa4df0ec1fcbeeffe"
q="Berlin,deu"

param={
    "q":q,
    "APPID":APPID,
    "units":"metric"

}

class Weather(Resource):

    def get(self):
        r=requests.get(api_url,params=param)
        j=r.json()
        return f"temp:{j['main']['temp']},{j['weather'][0]['description']}",200


api.add_resource(Weather,"/")

if __name__=="__main__":
    app.run(debug=True)
