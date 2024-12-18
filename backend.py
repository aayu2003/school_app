from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. Replace "*" with specific domains if needed.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.).
    allow_headers=["*"],  # Allows all headers.
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve login.html
@app.get("/", response_class=FileResponse)
def serve_login():
    return FileResponse("login.html")

# Serve app.html
@app.get("/principle", response_class=FileResponse)
def serve_principle():
    return FileResponse("app.html")
