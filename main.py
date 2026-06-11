from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from bson import ObjectId
import os
from typing import Optional, List

load_dotenv()

app = FastAPI(title="Cartridge Shop API")

# CORS middleware - allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGODB_URI)
db = client["Rose_db"]
products_collection = db["products"]

# Helper function to convert MongoDB document to JSON serializable format
def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "_id": str(product["_id"]),
        "name": product.get("name", ""),
        "brand": product.get("brand", ""),
        "description": product.get("description", ""),
        "price": product.get("price", 0),
        "originalPrice": product.get("originalPrice", 0),
        "discount": product.get("discount", 0),
        "image": product.get("image", "https://via.placeholder.com/500"),
        "compatiblePrinters": product.get("compatiblePrinters", ""),
        "stock": product.get("stock", 10),
        "category": product.get("category", ""),
        "createdAt": str(product.get("createdAt", "")) if product.get("createdAt") else None,
    }

@app.get("/")
async def root():
    return {"message": "Cartridge Shop API is running!", "status": "active"}

@app.get("/api/products")
async def get_products(brand: Optional[str] = None):
    """
    Get all products or filter by brand
    """
    try:
        query = {}
        if brand:
            # Case-insensitive brand search
            query["brand"] = {"$regex": f"^{brand}$", "$options": "i"}
        
        products = []
        async for product in products_collection.find(query):
            products.append(product_helper(product))
        
        return {"success": True, "products": products, "count": len(products)}
    except Exception as e:
        print(f"Error fetching products: {e}")
        return {"success": False, "message": str(e), "products": []}

@app.get("/api/products/{product_id}")
async def get_product(product_id: str):
    """
    Get single product by ID
    """
    try:
        product = await products_collection.find_one({"_id": ObjectId(product_id)})
        if product:
            return {"success": True, "product": product_helper(product)}
        return {"success": False, "message": "Product not found"}
    except Exception as e:
        return {"success": False, "message": str(e)}

@app.post("/api/products")
async def create_product(product_data: dict):
    """
    Add a new product (for admin use)
    """
    try:
        result = await products_collection.insert_one(product_data)
        new_product = await products_collection.find_one({"_id": result.inserted_id})
        return {"success": True, "product": product_helper(new_product)}
    except Exception as e:
        return {"success": False, "message": str(e)}

@app.put("/api/products/{product_id}")
async def update_product(product_id: str, product_data: dict):
    """
    Update a product (for admin use)
    """
    try:
        await products_collection.update_one(
            {"_id": ObjectId(product_id)},
            {"$set": product_data}
        )
        updated_product = await products_collection.find_one({"_id": ObjectId(product_id)})
        return {"success": True, "product": product_helper(updated_product)}
    except Exception as e:
        return {"success": False, "message": str(e)}

@app.delete("/api/products/{product_id}")
async def delete_product(product_id: str):
    """
    Delete a product (for admin use)
    """
    try:
        result = await products_collection.delete_one({"_id": ObjectId(product_id)})
        if result.deleted_count == 1:
            return {"success": True, "message": "Product deleted"}
        return {"success": False, "message": "Product not found"}
    except Exception as e:
        return {"success": False, "message": str(e)}

# Get unique brands
@app.get("/api/brands")
async def get_brands():
    """
    Get all unique brands
    """
    try:
        brands = await products_collection.distinct("brand")
        return {"success": True, "brands": sorted(brands)}
    except Exception as e:
        return {"success": False, "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)