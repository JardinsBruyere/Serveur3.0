from flask import Flask, request
import json,sqlite3
app = Flask(__name__)

@app.route('/', methods=['POST'])
def getSensor():
    json_dict = request.json

    #get station sensor data array
    sensor_array = json_dict['data']

    conn = sqlite3.connect('/var/www/API/FlaskApp/capteur.db')                # Connexion à la DB
    cur = conn.cursor()                                 # initialisation d'un curseur pour la DB
    print("Connected to SQLite DB")
    

    print("Detected {} sensors".format(len(sensor_array)))
    for i, sensor in enumerate(sensor_array):
        print("***Sensor {}***".format(i+1))
        print("date_added : {}".format(sensor['DateAjout']))
        print("sensor_id  : {}".format(sensor['IdCapteur']))
        print("value      : {}".format(sensor['Valeur']))
        cur.execute("INSERT INTO RelevesCapteurs (`DateAjout`,`IdCapteur`,`Valeur`) VALUES('"+format(sensor['DateAjout'])+"',"+format(sensor['IdCapteur'])+","+format(sensor['Valeur'])+");")
    f = conn.commit()                                   #On insert les données dans la DB
    cur.close()
    conn.close()
    print("Connection to SQLite DB closed")

    #send an acknowledgement message to station
    return "Transfer Success"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
