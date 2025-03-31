from fastapi import FastAPI
from app.routes import admin, marketplace

app = FastAPI()

# Include routes
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(marketplace.router, prefix="/marketplace", tags=["Marketplace"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Marketplace API"}
