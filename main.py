# main.py
from app.api import app  # import your FastAPI app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
