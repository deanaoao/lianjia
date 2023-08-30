
from fastapi.responses import Response as R
import  json
class Response(R):
    def __init__(self, content, code, msg, error=None):
        if msg:
            content['msg'] = msg
        if error:
            content['error'] = error
        super().__init__(
            content=json.dumps(content),
            media_type="application/json",
            status_code=code
        )
