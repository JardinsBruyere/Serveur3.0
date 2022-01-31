from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/', methods=['POST']) 
def foo():
    print(request.headers)

    json_dict = request.json

    #Printing json string in a pretty way
    #print("type : {}\nprinting data :\n>>>\n{}\n<<<\nend".format(type(json_dict),json_dict))
    json_string = json.dumps(json_dict) #convert broken dict to string
    #print("type : {}\nprinting data :\n>>>\n{}\n<<<\nend".format(type(json_string),json_string))
    parsed = json.loads(json_string) #convert string to working dict
    #print("type : {}\nprinting data :\n>>>\n{}\n<<<\nend".format(type(parsed),parsed))
    print(json.dumps(parsed, indent=4, sort_keys=True)) #convert working dict to nice string
    #print("type : {}\nprinting data :\n>>>\n{}\n<<<\nend".format(type((json.dumps(parsed, indent=4, sort_keys=True))),(json.dumps(parsed, indent=4, sort_keys=True))))
    
    return "Transfer Success"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
