from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the HTML file
@app.get("/", response_class=FileResponse)
def serve_html():
    return FileResponse("login.html")
