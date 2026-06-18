from fastapi import FastAPI, HTTPException, Query, File, UploadFile, Form, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from bson import ObjectId
import os
import shutil
from datetime import datetime, timedelta
from typing import Optional, List
import uuid
import bcrypt
import jwt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

load_dotenv()

app = FastAPI(title="Cartridge Shop API")

# Security setup
security = HTTPBearer()
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here-change-in-production")
ALGORITHM = "HS256"

# Ensure images directory exists
os.makedirs("images", exist_ok=True)
app.mount("/images", StaticFiles(directory="images"), name="images")

# CORS middleware
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
admin_collection = db["Admin"]  

# Helper functions
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

def admin_helper(admin) -> dict:
    return {
        "id": str(admin["_id"]),
        "username": admin.get("username", ""),
        "email": admin.get("email", ""),
        "role": admin.get("role", "admin"),
        "createdAt": str(admin.get("createdAt", "")) if admin.get("createdAt") else None,
    }

# Create JWT token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=7)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Verify JWT token
async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

# Hash password
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

# Verify password
def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

# Initialize admin user with YOUR credentials
@app.post("/api/admin")
async def setup_admin():
    """
    Setup initial admin user - run this once
    """
    try:
        existing_admin = await admin_collection.find_one({"username": "Rose"})
        if existing_admin:
            return {"success": False, "message": "Admin already exists"}
        
        # Create admin with your credentials
        admin_data = {
            "username": "Rose", 
            "email": "Covenantsolutionprint@gmail.com",
            "password": hash_password("rose0308"),  
            "role": "super_admin",
            "createdAt": datetime.now()
        }
        
        result = await admin_collection.insert_one(admin_data)
        return {
            "success": True, 
            "message": "Admin created successfully",
            "credentials": {
                "username": "Rose",
                "password": "rose0308"
            }
        }
    except Exception as e:
        return {"success": False, "message": str(e)}

# Admin login
@app.post("/api/admin/login")
async def admin_login(username: str = Form(...), password: str = Form(...)):
    """
    Admin login endpoint
    """
    try:
        # Find admin by username
        admin = await admin_collection.find_one({"username": username})
        
        if not admin:
            # Check by email too
            admin = await admin_collection.find_one({"email": username})
            
        if not admin:
            return {"success": False, "message": "Invalid credentials"}
        
        # Verify password
        if not verify_password(password, admin["password"]):
            return {"success": False, "message": "Invalid credentials"}
        
        # Create JWT token
        token = create_access_token({
            "sub": str(admin["_id"]),
            "username": admin["username"],
            "role": admin.get("role", "admin")
        })
        
        return {
            "success": True,
            "token": token,
            "admin": admin_helper(admin),
            "message": "Login successful"
        }
    except Exception as e:
        return {"success": False, "message": str(e)}

@app.post("/api/admin/create")
async def create_admin(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    role: str = Form("admin"),
    payload: dict = Depends(verify_token)
):
    """
    Create a new admin - only super_admin can do this
    """
    try:
        if payload.get("role") != "super_admin":
            raise HTTPException(status_code=403, detail="Permission denied")
        
        existing = await admin_collection.find_one({"$or": [{"username": username}, {"email": email}]})
        if existing:
            return {"success": False, "message": "Admin with this username or email already exists"}
        
        admin_data = {
            "username": username,
            "email": email,
            "password": hash_password(password),
            "role": role,
            "createdAt": datetime.now()
        }
        
        result = await admin_collection.insert_one(admin_data)
        new_admin = await admin_collection.find_one({"_id": result.inserted_id})
        
        return {"success": True, "admin": admin_helper(new_admin)}
    except Exception as e:
        return {"success": False, "message": str(e)}

@app.get("/api/admin/all")
async def get_all_admins(payload: dict = Depends(verify_token)):
    """
    Get all admins - only super_admin can do this
    """
    try:
        if payload.get("role") != "super_admin":
            raise HTTPException(status_code=403, detail="Permission denied")
        
        admins = []
        async for admin in admin_collection.find():
            admin_dict = admin_helper(admin)
            admins.append(admin_dict)
        
        return {"success": True, "admins": admins}
    except Exception as e:
        return {"success": False, "message": str(e)}

# Get current admin profile (protected)
@app.get("/api/admin/profile")
async def get_admin_profile(payload: dict = Depends(verify_token)):
    """
    Get current admin profile
    """
    try:
        admin = await admin_collection.find_one({"_id": ObjectId(payload.get("sub"))})
        if not admin:
            return {"success": False, "message": "Admin not found"}
        
        return {"success": True, "admin": admin_helper(admin)}
    except Exception as e:
        return {"success": False, "message": str(e)}

# Change password (protected)
@app.post("/api/admin/change-password")
async def change_password(
    old_password: str = Form(...),
    new_password: str = Form(...),
    payload: dict = Depends(verify_token)
):
    """
    Change admin password
    """
    try:
        admin = await admin_collection.find_one({"_id": ObjectId(payload.get("sub"))})
        if not admin:
            return {"success": False, "message": "Admin not found"}
        
        # Verify old password
        if not verify_password(old_password, admin["password"]):
            return {"success": False, "message": "Current password is incorrect"}
        
        # Update password
        await admin_collection.update_one(
            {"_id": ObjectId(payload.get("sub"))},
            {"$set": {"password": hash_password(new_password)}}
        )
        
        return {"success": True, "message": "Password changed successfully"}
    except Exception as e:
        return {"success": False, "message": str(e)}

# IMPORT PRODUCT - Protected route
@app.post("/api/products/import")
async def import_product(
    name: str = Form(...),
    brand: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    originalPrice: float = Form(...),
    discount: float = Form(0),
    compatiblePrinters: str = Form(""),
    stock: int = Form(...),
    category: str = Form(...),
    image: UploadFile = File(...),
    payload: dict = Depends(verify_token)  
):
    """
    Import a new product with image upload - Admin only
    """
    try:
        if payload.get("role") not in ["admin", "super_admin"]:
            raise HTTPException(status_code=403, detail="Admin access required")
        
        # Generate unique filename
        file_extension = os.path.splitext(image.filename)[1]
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        image_path = f"images/{unique_filename}"
        
        # Save the image
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        
        # Prepare product data
        product_data = {
            "name": name,
            "brand": brand.lower(),
            "description": description,
            "price": price,
            "originalPrice": originalPrice,
            "discount": discount,
            "image": f"/images/{unique_filename}",
            "compatiblePrinters": compatiblePrinters,
            "stock": stock,
            "category": category,
            "createdAt": datetime.now()
        }
        
        # Insert into MongoDB
        result = await products_collection.insert_one(product_data)
        new_product = await products_collection.find_one({"_id": result.inserted_id})
        
        return {"success": True, "product": product_helper(new_product)}
    except Exception as e:
        print(f"Error importing product: {e}")
        return {"success": False, "message": str(e)}

# Get all products (public)
@app.get("/api/products")
async def get_products(brand: Optional[str] = None):
    try:
        query = {}
        if brand:
            query["brand"] = {"$regex": f"^{brand}$", "$options": "i"}
        
        products = []
        async for product in products_collection.find(query):
            products.append(product_helper(product))
        
        return {"success": True, "products": products, "count": len(products)}
    except Exception as e:
        print(f"Error fetching products: {e}")
        return {"success": False, "message": str(e), "products": []}

# Get single product (public)
@app.get("/api/products/{product_id}")
async def get_product(product_id: str):
    try:
        product = await products_collection.find_one({"_id": ObjectId(product_id)})
        if product:
            return {"success": True, "product": product_helper(product)}
        return {"success": False, "message": "Product not found"}
    except Exception as e:
        return {"success": False, "message": str(e)}

# Update product (protected)
@app.put("/api/products/{product_id}")
async def update_product(
    product_id: str, 
    product_data: dict,
    payload: dict = Depends(verify_token)
):
    """
    Update a product - Admin only
    """
    try:
        if payload.get("role") not in ["admin", "super_admin"]:
            raise HTTPException(status_code=403, detail="Admin access required")
            
        await products_collection.update_one(
            {"_id": ObjectId(product_id)},
            {"$set": product_data}
        )
        updated_product = await products_collection.find_one({"_id": ObjectId(product_id)})
        return {"success": True, "product": product_helper(updated_product)}
    except Exception as e:
        return {"success": False, "message": str(e)}

# Delete product (protected)
@app.delete("/api/products/{product_id}")
async def delete_product(
    product_id: str,
    payload: dict = Depends(verify_token)
):
    """
    Delete a product - Admin only
    """
    try:
        if payload.get("role") not in ["admin", "super_admin"]:
            raise HTTPException(status_code=403, detail="Admin access required")
            
        result = await products_collection.delete_one({"_id": ObjectId(product_id)})
        if result.deleted_count == 1:
            return {"success": True, "message": "Product deleted"}
        return {"success": False, "message": "Product not found"}
    except Exception as e:
        return {"success": False, "message": str(e)}

# Get unique brands (public)
@app.get("/api/brands")
async def get_brands():
    try:
        brands = await products_collection.distinct("brand")
        return {"success": True, "brands": sorted(brands)}
    except Exception as e:
        return {"success": False, "message": str(e)}

# Test endpoint
@app.get("/")
async def root():
    return {"message": "Cartridge Shop API is running!", "status": "active"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)