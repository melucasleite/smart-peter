from datetime import datetime, date
from app import app
import json


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))

# set default jinja filter tojson to use our handy json_serial
@app.template_filter('tojson')
def tojson(string):
    return json.dumps(string, default=json_serial)
