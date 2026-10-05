import time 
from functools import wraps

def retry (times=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            intentos=0
            while intentos<times:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    intentos +=1
                    if intentos >= times:
                        raise e
                    print(f"[RETRY] fallo '{func.__name__}'. Reintentando en {delay}s... (intento{intentos}/{times}) ")
                    time.sleep(delay)
        return wrapper
    return decorator