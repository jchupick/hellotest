import json
import time
import copy
import psutil
from flask import Flask

app = Flask(__name__)

START_TIME = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
_VER = '1.0.0'

json_out =  {
                "status"  : 'OK', 
                "version" : _VER, 
                "uptime"  : 'up since ' + START_TIME 
            }

@app.route('/')
def return_index():
    return 'Hello!'
  
@app.route('/healthz')
def return_healthz():
    return json.dumps(json_out, indent=4)

@app.route('/healthz-full')
def return_healthz_full():
    json_out_full = copy.deepcopy(json_out)
    json_out_full.update( {'memory' : dict(psutil.virtual_memory()._asdict())} )
    json_out_full.update( {'disk'   : dict(psutil.disk_usage('/')._asdict())} )
    
    return json.dumps(json_out_full, indent=4)

@app.route('/version')
def return_version():
    return 'Version is ' + _VER

@app.route('/mem')
def return_mem():
    return json.dumps(dict(psutil.virtual_memory()._asdict()), indent=4)

@app.route('/disk')
def return_disk():
    return json.dumps(dict(psutil.disk_usage('/')._asdict()), indent=4)

@app.route('/help')
def return_help():
    return 'Help here...'

# Invokation from Docker image starts from here
if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 8080, debug = True)
