def say_hello(name=None):
    if name:
        return {"message": "Hello %s" %(name)} 
    else:
        return {"message": "Hello API!"}
