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

security = HTTPBearer()
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here-change-in-production")
ALGORITHM = "HS256"

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

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGODB_URI)
db = client["Rose_db"]
products_collection = db["products"]
Login_collection = db["Login"]  

def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "_id": str(product["_id"]),
        "name": product.get("name", ""),
        "brand": product.get("brand", ""),
        "description": product.get("description", ""),
        "price": product.get("price", 0),
        "image": product.get("image", "https://via.placeholder.com/500"),
        "stock": product.get("stock", 10),
        "category": product.get("category", ""),
        "Tags": product.get("Tags", ""),
        "createdAt": str(product.get("createdAt", "")) if product.get("createdAt") else None,
        "updatedAt": str(product.get("updatedAt", "")) if product.get("updatedAt") else None,
    }

def Login_helper(Login) -> dict:
    return {
        "id": str(Login["_id"]),
        "username": Login.get("username", ""),
        "email": Login.get("email", ""),
        "role": Login.get("role", "Login"),
        "createdAt": str(Login.get("createdAt", "")) if Login.get("createdAt") else None,
    }

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

# Initialize Login user with YOUR credentials
@app.post("/api/Login")
async def setup_Login():
    """
    Setup initial Login user - run this once
    """
    try:
        existing_Login = await Login_collection.find_one({"username": "Rose"})
        if existing_Login:
            return {"success": False, "message": "Login already exists"}
        
        Login_data = {
            "username": "Rose", 
            "email": "Covenantsolutionprint@gmail.com",
            "password": hash_password("rose0308"),  
            "role": "super_Login",
            "createdAt": datetime.now()
        }
        
        result = await Login_collection.insert_one(Login_data)
        return {
            "success": True, 
            "message": "Login created successfully",
            "credentials": {
                "username": "Rose",
                "password": "rose0308"
            }
        }
    except Exception as e:
        return {"success": False, "message": str(e)}

@app.post("/api/Login/login")
async def Login_login(
    username: str = Form(...), 
    password: str = Form(...)
):
    """
    Login login endpoint
    """
    try:
        Login = await Login_collection.find_one({"username": username})
        
        if not Login:
            Login = await Login_collection.find_one({"email": username})
            
        if not Login:
            return {"success": False, "message": "Invalid credentials"}
        
        if not verify_password(password, Login["password"]):
            return {"success": False, "message": "Invalid credentials"}
        
        token = create_access_token({
            "sub": str(Login["_id"]),
            "username": Login["username"],
            "role": Login.get("role", "Login")
        })
        
        return {
            "success": True,
            "token": token,
            "Login": {
                "id": str(Login["_id"]),
                "username": Login["username"],
                "email": Login.get("email", ""),
                "role": Login.get("role", "Login")
            },
            "message": "Login successful"
        }
    except Exception as e:
        return {"success": False, "message": str(e)}


@app.post("/api/Login/create")
async def create_Login(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    role: str = Form("Login"),
    payload: dict = Depends(verify_token)
):
    """
    Create a new Login - only super_Login can do this
    """
    try:
        if payload.get("role") != "super_Login":
            raise HTTPException(status_code=403, detail="Permission denied")
        
        existing = await Login_collection.find_one({"$or": [{"username": username}, {"email": email}]})
        if existing:
            return {"success": False, "message": "Login with this username or email already exists"}
        
        Login_data = {
            "username": username,
            "email": email,
            "password": hash_password(password),
            "role": role,
            "createdAt": datetime.now()
        }
        
        result = await Login_collection.insert_one(Login_data)
        new_Login = await Login_collection.find_one({"_id": result.inserted_id})
        
        return {"success": True, "Login": Login_helper(new_Login)}
    except Exception as e:
        return {"success": False, "message": str(e)}

@app.get("/api/Login/all")
async def get_all_Logins(payload: dict = Depends(verify_token)):
    """
    Get all Logins - only super_Login can do this
    """
    try:
        if payload.get("role") != "super_Login":
            raise HTTPException(status_code=403, detail="Permission denied")
        
        Logins = []
        async for Login in Login_collection.find():
            Login_dict = Login_helper(Login)
            Logins.append(Login_dict)
        
        return {"success": True, "Logins": Logins}
    except Exception as e:
        return {"success": False, "message": str(e)}

@app.get("/api/Login/profile")
async def get_Login_profile(payload: dict = Depends(verify_token)):
    """
    Get current Login profile
    """
    try:
        Login = await Login_collection.find_one({"_id": ObjectId(payload.get("sub"))})
        if not Login:
            return {"success": False, "message": "Login not found"}
        
        return {"success": True, "Login": Login_helper(Login)}
    except Exception as e:
        return {"success": False, "message": str(e)}

@app.post("/api/Login/change-password")
async def change_password(
    old_password: str = Form(...),
    new_password: str = Form(...),
    payload: dict = Depends(verify_token)
):
    """
    Change Login password
    """
    try:
        Login = await Login_collection.find_one({"_id": ObjectId(payload.get("sub"))})
        if not Login:
            return {"success": False, "message": "Login not found"}
        
        # Verify old password
        if not verify_password(old_password, Login["password"]):
            return {"success": False, "message": "Current password is incorrect"}
        
        # Update password
        await Login_collection.update_one(
            {"_id": ObjectId(payload.get("sub"))},
            {"$set": {"password": hash_password(new_password)}}
        )
        
        return {"success": True, "message": "Password changed successfully"}
    except Exception as e:
        return {"success": False, "message": str(e)}

# ==================== PRODUCT ENDPOINTS ====================

@app.post("/api/products/import")
async def import_product(
    name: str = Form(...),
    brand: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    stock: int = Form(...),
    category: str = Form(...),
    Tags: str = Form(""),
    image: UploadFile = File(...),
    payload: dict = Depends(verify_token)  
):
    """
    Import a new product with image upload - Login only
    """
    try:
        if payload.get("role") not in ["Login", "super_Login"]:
            raise HTTPException(status_code=403, detail="Login access required")
        
        file_extension = os.path.splitext(image.filename)[1]
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        image_path = f"images/{unique_filename}"
        
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        
        product_data = {
            "name": name,
            "brand": brand.lower(),
            "description": description,
            "price": price,
            "image": f"/images/{unique_filename}",
            "stock": stock,
            "category": category,
            "Tags": Tags,
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
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
async def get_products(
    brand: Optional[str] = None,
    category: Optional[str] = None,
    limit: int = Query(50, ge=1, le=100),
    skip: int = Query(0, ge=0)
):
    try:
        query = {}
        if brand:
            query["brand"] = {"$regex": f"^{brand}$", "$options": "i"}
        if category:
            query["category"] = {"$regex": f"^{category}$", "$options": "i"}
        
        products = []
        async for product in products_collection.find(query).skip(skip).limit(limit):
            products.append(product_helper(product))
        
        total_count = await products_collection.count_documents(query)
        
        return {
            "success": True, 
            "products": products, 
            "count": len(products),
            "total": total_count
        }
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
    Update a product - Login only
    """
    try:
        if payload.get("role") not in ["Login", "super_Login"]:
            raise HTTPException(status_code=403, detail="Login access required")
        
        product_data["updatedAt"] = datetime.now()
            
        result = await products_collection.update_one(
            {"_id": ObjectId(product_id)},
            {"$set": product_data}
        )
        
        if result.modified_count == 0:
            return {"success": False, "message": "Product not found or no changes made"}
        
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
    Delete a product - Login only
    """
    try:
        if payload.get("role") not in ["Login", "super_Login"]:
            raise HTTPException(status_code=403, detail="Login access required")
            
        result = await products_collection.delete_one({"_id": ObjectId(product_id)})
        if result.deleted_count == 1:
            return {"success": True, "message": "Product deleted"}
        return {"success": False, "message": "Product not found"}
    except Exception as e:
        return {"success": False, "message": str(e)}

@app.get("/api/brands")
async def get_brands():
    try:
        brands = await products_collection.distinct("brand")
        return {"success": True, "brands": sorted(brands)}
    except Exception as e:
        return {"success": False, "message": str(e)}

@app.get("/api/categories")
async def get_categories():
    try:
        categories = await products_collection.distinct("category")
        return {"success": True, "categories": sorted([c for c in categories if c])}
    except Exception as e:
        return {"success": False, "message": str(e)}

# Search products (public)
@app.get("/api/products/search")
async def search_products(q: str = Query(..., min_length=1)):
    try:
        products = []
        async for product in products_collection.find({
            "$or": [
                {"name": {"$regex": q, "$options": "i"}},
                {"description": {"$regex": q, "$options": "i"}},
                {"brand": {"$regex": q, "$options": "i"}},
                {"Tags": {"$regex": q, "$options": "i"}}
            ]
        }):
            products.append(product_helper(product))
        
        return {"success": True, "products": products, "count": len(products)}
    except Exception as e:
        return {"success": False, "message": str(e), "products": []}

# Test endpoint
@app.get("/")
async def root():
    return {"message": "Cartridge Shop API is running!", "status": "active"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)