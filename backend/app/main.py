from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl

# Import our new scraper function
from app.services.scraper_service import fetch_and_extract_text

# --- Pydantic Model for Input Validation ---
class URLRequest(BaseModel):
    """Defines the shape of our input. Expects a JSON with a 'url' key."""
    url: HttpUrl  # HttpUrl ensures we get a valid URL

# --- Create the FastAPI app instance ---
app = FastAPI(
    title="Katalyst API",
    description="The backend engine for the Katalyst project.",
    version="0.1.0"
)

# --- API Endpoints ---
@app.get("/")
def read_root():
    """Root endpoint for a simple health check."""
    return {"message": "Welcome to the Katalyst Backend Engine!"}

@app.post("/api/v1/extract")
def extract_text_from_url(request: URLRequest):
    """
    This endpoint receives a URL, scrapes it, 
    and returns the main extracted text.
    """
    print(f"Received URL: {request.url}")
    
    # Call our service function
    try:
        main_text = fetch_and_extract_text(str(request.url))
        
        if main_text is None:
            # This handles cases where trafilatura failed
            print("Extraction failed or no main content found.")
            raise HTTPException(
                status_code=400, 
                detail="Could not extract main content from the provided URL."
            )
            
        print("Extraction successful.")
        return {"extracted_text": main_text}

    except Exception as e:
        # A general catch-all for other errors (e.g., network issues)
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=f"An internal server error occurred: {e}")