from datetime import datetime
def get_timestamp():
    ahora= datetime.now()
    return ahora.strftime("%Y-%m-%d %H:%M:%S")
print(get_timestamp())
