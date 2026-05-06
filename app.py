from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# API endpoint
@app.get("/api/data")
async def get_data():
    return {"message": "Hello from the Python (FastAPI) Backend!"}

# Serve static files (HTML, CSS, JS)
# We assume index.html, style.css, script.js are in the same directory
@app.get("/")
async def read_index():
    return FileResponse("index.html")

# Serve other static files
app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
