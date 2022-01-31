from flask import Flask, request
#from datetime import datetime, timezone
import datetime, sqlite3, getpass

app = Flask(__name__)



@app.route('/', methods=['GET']) 
def testSensor():
    return "Hello world"

@app.route('/', methods=['POST'])
def getSensor():
    

    conn = sqlite3.connect('/var/www/API/FlaskApp/capteur.db')                # Connexion à la DB
    try:
        # initialisation d'un curseur pour la DB
        cur = conn.cursor()
    except Exception as ex:
        return "could not connect to db"

    print("Connected to SQLite DB as {}".format(getpass.getuser()))

    #get current time
    #currentDateTime = datetime.now#timezone.utc)
    currentDateTime = datetime.datetime.now()
    print("current time is {}".format(currentDateTime))
    
    json_dict = request.json

    #get station sensor data array
    sensor_array = json_dict['sensor_array']
    json_station = json_dict['station']
    MAC = json_station['MAC']
    
    print("Station {} reporting in\n".format(MAC))
    print("Detected {} sensors".format(len(sensor_array)))
    for i, sensor in enumerate(sensor_array):
        print("***Sensor {}***".format(i+1))
        print("sensor_id    : {}".format(sensor['id']))
        print("sensor_type  : {}".format(sensor['type']))
        print("value        : {}".format(sensor['val']))

        query = '''
        INSERT INTO SensorReading 
        (`SensorID`,`DateAdded`,`Value`) 
        VALUES(?,?,?);
        '''
        #execute changes locally
        cur.execute(query, (sensor['id'], currentDateTime, sensor['val'])) 

    #commit db changes
    f = conn.commit()                                 
    cur.close()
    conn.close()
    print("Connection to SQLite DB closed\n")

    #send an acknowledgement message to station
    return "Transfer Success"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
