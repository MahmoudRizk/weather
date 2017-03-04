from flask import Flask, render_template
import requests
from datetime import datetime
app = Flask(__name__)

forecast_data=[]
r = requests.get("http://api.openweathermap.org/data/2.5/forecast/daily?q=Cairo&appid=7e73695b9106e411858e94e01532d30d")
json_data = r.json()

for i in range(json_data['cnt']):
    tmp={'date_time' : datetime.fromtimestamp(json_data["list"][i]['dt']).strftime("%a, %d"),
         'max_temp'  : int(json_data["list"][i]['temp']['day'] - 273.15),
         'min_temp'  : int(json_data["list"][i]['temp']['night'] - 273.15),
         'status'    : json_data["list"][i]['weather'][0]['description'],
         'icon'      : json_data["list"][i]['weather'][0]['icon'][0:2] + 'd.png'
         }
    forecast_data.append(tmp)


@app.route("/")
def template_test():
    return render_template('weather.html', max=forecast_data[0]['max_temp'],min=forecast_data[0]['date_time'],raw_data=forecast_data)


if __name__ == '__main__':
    app.run(debug=True)
