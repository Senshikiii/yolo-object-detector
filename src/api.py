from fastapi import FastAPI

app = FastAPI() # this is a class apparently, we're making an instance to store the class in memory and also storing it in a variable

# this is a decorator, we need it to register the function into the server's routing table?? tf is that?

@app.get("/")
async def root():
    return{"message": "Haii privvi"}


