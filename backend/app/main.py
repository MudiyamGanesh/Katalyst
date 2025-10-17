from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()


@app.get("/")
def read_root():
    """
    This is the main root endpoint.
    It just returns a welcome message.
    """
    return {"message": "Hello, World! This is the Katalyst backend."}