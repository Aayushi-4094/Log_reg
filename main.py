from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Define the routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register", response_class=HTMLResponse)
async def register(request: Request, username: str = Form(...), email: str = Form(...), password: str = Form(...), confirm_password: str = Form(...)):
    # Validate the registration form data
    if len(username) < 4:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Username must be at least 4 characters long."})
    if len(password) < 6:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Password must be at least 6 characters long."})
    if password != confirm_password:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Passwords do not match."})
    
    # Add the new user to the database
    # (replace this with your own database logic)
    # ...
    
    # Redirect the user to the login page
    return templates.TemplateResponse("index.html", {"request": request, "success": "Registration successful. Please log in."})

@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    # Validate the login form data
    if username != "example_user" or password != "example_password":
        return templates.TemplateResponse("index.html", {"request": request, "error": "Invalid username or password."})
    
    # Redirect the user to the dashboard
    return templates.TemplateResponse("dashboard.html", {"request": request})
