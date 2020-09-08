import json
import datetime
import copy
import psutil

from flask import Flask

app = Flask(__name__)

START_TIME     = datetime.datetime.now()
START_TIME_STR = START_TIME.strftime('%Y-%m-%d %H:%M:%S')
_VER = '1.0.0'

json_out =  {
                "status"    : 'OK', 
                "version"   : _VER, 
                "starttime" : 'up since ' + START_TIME_STR 
            }

print('__name__ is ', __name__)

@app.route('/')
def return_index():
    return 'Hello!'
  
@app.route('/healthz')
def return_healthz():
    return json.dumps(json_out, indent=4)

@app.route('/healthz-full')
def return_healthz_full():
    now    = datetime.datetime.now()
    uptime = now - START_TIME

    json_out_full = copy.deepcopy(json_out)
    json_out_full.update( {'uptime' : str(uptime.total_seconds()) + ' seconds' } )
    json_out_full.update( {'memory' : dict(psutil.virtual_memory()._asdict())} )
    json_out_full.update( {'disk'   : dict(psutil.disk_usage('/')._asdict())} )
    
    return json.dumps(json_out_full, indent=4)

@app.route('/version')
@app.route('/ver')
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
    return """Available endpoints:
           
           /
           /healthz
           /healthz-full
           /version
           /disk
           /mem
           /help"""

# Invokation from Docker image starts from here
if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 8080, debug = False)
