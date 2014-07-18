from functools import wraps
import simplejson as json
from flask import Response

def jsonify(f):
    @wraps(f)
    def jsonified(*args, **kwargs):
        data_dict = f(*args, **kwargs)
        resp = Response(response=json.dumps(data_dict), 
                        status=200, 
                        mimetype='application/json')
        return resp
    return jsonified
