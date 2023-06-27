from datetime import datetime
import json

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat().replace("+00:00", "Z")

        return super().default(o)