import jwt, os
from dotenv import load_dotenv
from datetime import datetime


def encodeJWT(data)->str:
    try:
        load_dotenv()
        result = jwt.encode(
            data, 
            os.environ.get("JWT_KEY"), 
            algorithm=os.environ.get("JWT_ALGO"),
            # {"exp": datetime.now(tz=timezone.) + datetime.timedelta(seconds=30)}
        )
        return result
    except Exception as ex:
        raise ex

def decodeJWT(jwtStr: str)->str:
    try:
        load_dotenv()
        result = jwt.decode(jwtStr, os.environ.get("JWT_KEY"), algorithms=[os.environ.get("JWT_ALGO")])
        return result
    except jwt.ExpiredSignatureError:
        return 'Expired'
