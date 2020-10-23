# Standard Python
import json
from datetime import datetime, timedelta
from copy     import deepcopy

# pip installs
import psutil
import humanize

from flask import Flask

app = Flask(__name__)

START_TIME     = datetime.now()
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
    now    = datetime.now()
    uptime = now - START_TIME
    human_uptime = humanize.naturaldelta(uptime)

    json_out_full = deepcopy(json_out)
    json_out_full.update( {'uptime' : human_uptime } )
    json_out_full.update( {'memory' : dict(psutil.virtual_memory()._asdict())} )

    disk_dict = psutil.disk_usage('/')._asdict()

    disk_dict["total"] = humanize.naturalsize(disk_dict["total"], binary=True)
    disk_dict["used"]  = humanize.naturalsize(disk_dict["used"],  binary=True)
    disk_dict["free"]  = humanize.naturalsize(disk_dict["free"],  binary=True)

    json_out_full.update( {'disk': dict(disk_dict)} )
    
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
    app.run(host ='0.0.0.0', debug = False)
