from fastapi import APIRouter

router = APIRouter()

@router.get("/products")
def get_products():
    return {"products": ["Product 1", "Product 2", "Product 3"]}