from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

async def seed_products():
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    client = None
    try:
        client = AsyncIOMotorClient(MONGODB_URI)
        db = client["Rose_db"]
        products = db["products"]
        
        # Clear existing products
        result = await products.delete_many({})
        print(f"✓ Cleared {result.deleted_count} existing products")
        
        # Sample products with real image URLs
        sample_products = [
            # HP Products
            {
                "name": "HP 61 Black Ink Cartridge",
                "brand": "hp",
                "description": "Original HP 61 black ink cartridge. High-quality prints with sharp text.",
                "price": 1100,
                "originalPrice": 2800,
                "discount": 61,
                "image": "/hpitem.jpg",
                "compatiblePrinters": "HP Deskjet 1000, 1050, 1510, 2000, 2050",
                "stock": 50,
                "category": "Ink Cartridge",
                "createdAt": datetime.now()
            },
            {
                "name": "HP 61 Tri-color Ink Cartridge",
                "brand": "hp",
                "description": "Original HP 61 tri-color cartridge for vibrant color prints.",
                "price": 1200,
                "originalPrice": 3000,
                "discount": 60,
                "image": "/hpitem2.jpg",
                "compatiblePrinters": "HP Deskjet 1000, 1050, 1510, 2000, 2050",
                "stock": 45,
                "category": "Ink Cartridge",
                "createdAt": datetime.now()
            },
            {
                "name": "HP 62 Black High-Yield Cartridge",
                "brand": "hp",
                "description": "High-yield black ink cartridge for more prints.",
                "price": 1500,
                "originalPrice": 3500,
                "discount": 57,
                "image": "/hpitem3.jpg",
                "compatiblePrinters": "HP Envy 4500, 5540, 5640, OfficeJet 5740",
                "stock": 30,
                "category": "Ink Cartridge",
                "createdAt": datetime.now()
            },
            {
                "name": "HP LaserJet  CF283A",
                "brand": "hp",
                "description": "Black  cartridge for HP LaserJet printers.",
                "price": 899,
                "originalPrice": 1299,
                "discount": 31,
                "image": "/hpitem4.jpg",
                "compatiblePrinters": "HP LaserJet M125, M127, M201, M225",
                "stock": 25,
                "category": "",
                "createdAt": datetime.now()
            },
            
            # Canon Products
            {
                "name": "Canon PG-245 Black Ink Cartridge",
                "brand": "canon",
                "description": "Original Canon black ink cartridge for crisp documents.",
                "price": 1050,
                "originalPrice": 2500,
                "discount": 58,
                "image": "/canonitem1.jpg",
                "compatiblePrinters": "Canon Pixma MG2420, MG2520, MG2920, MX492",
                "stock": 40,
                "category": "Ink Cartridge",
                "createdAt": datetime.now()
            },
            {
                "name": "Canon CL-246 Color Ink Cartridge",
                "brand": "canon",
                "description": "Original Canon color cartridge for vibrant photos.",
                "price": 1150,
                "originalPrice": 2800,
                "discount": 59,
                "image": "/canontem2.jpg",
                "compatiblePrinters": "Canon Pixma MG2420, MG2520, MG2920",
                "stock": 38,
                "category": "Ink Cartridge",
                "createdAt": datetime.now()
            },
            {
                "name": "Canon PG-275 High-Yield Black",
                "brand": "canon",
                "description": "High-yield black cartridge for more prints.",
                "price": 1400,
                "originalPrice": 3200,
                "discount": 56,
                "image": "/canonitem3.jpg",
                "compatiblePrinters": "Canon Pixma TS3120, TS5120, TS6120",
                "stock": 25,
                "category": "Ink Cartridge",
                "createdAt": datetime.now()
            },

               {
                "name": "Canon PG-275 High-Yield Black",
                "brand": "canon",
                "description": "High-yield black cartridge for more prints.",
                "price": 1400,
                "originalPrice": 3200,
                "discount": 56,
                "image": "/canonitem6.jpg",
                "compatiblePrinters": "Canon Pixma TS3120, TS5120, TS6120",
                "stock": 25,
                "category": "Ink Cartridge",
                "createdAt": datetime.now()
            },
            
            
            # Epson Products
            {
                "name": "Epson 220 Black Ink Cartridge",
                "brand": "epson",
                "description": "Original Epson black ink for sharp text.",
                "price": 980,
                "originalPrice": 2300,
                "discount": 57,
                "image": "/epson1.jpg",
                "compatiblePrinters": "Epson Expression XP-330, XP-430, XP-530",
                "stock": 55,
                "category": "Ink Cartridge",
                "createdAt": datetime.now()
            },
            {
                "name": "Epson 220 Color Ink Cartridge",
                "brand": "epson",
                "description": "Original Epson color cartridge.",
                "price": 1080,
                "originalPrice": 2600,
                "discount": 58,
                "image": "/epson22.jpg",
                "compatiblePrinters": "Epson Expression XP-330, XP-430, XP-530",
                "stock": 52,
                "category": "Ink Cartridge",
                "createdAt": datetime.now()
            },
            {
                "name": "Epson EcoTank Ink Bottle Black",
                "brand": "epson",
                "description": "High-capacity ink bottle for EcoTank printers.",
                "price": 450,
                "originalPrice": 699,
                "discount": 36,
                "image": "/epson1.jpg",
                "compatiblePrinters": "Epson EcoTank ET-2720, ET-2760, ET-4750",
                "stock": 100,
                "category": "Ink Bottle",
                "createdAt": datetime.now()
            },
            
            # Brother Products
            {
                "name": "Brother LC3019 Black Ink Cartridge",
                "brand": "brother",
                "description": "Original Brother black ink cartridge.",
                "price": 329,
                "originalPrice": 499,
                "discount": 34,
                "image": "/brother11.jpg",
                "compatiblePrinters": "Brother MFC-J880DW, MFC-J890DW",
                "stock": 35,
                "category": "Ink Cartridge",
                "createdAt": datetime.now()
            },
            {
                "name": "Brother TN-760 High-Yield ",
                "brand": "brother",
                "description": "High-yield  cartridge for Brother printers.",
                "price": 899,
                "originalPrice": 1299,
                "discount": 31,
                "image": "/brother22.jpg",
                "compatiblePrinters": "Brother HL-L2300D, HL-L2340DW, MFC-L2700DW",
                "stock": 40,
                "category": "",
                "createdAt": datetime.now()
            },
                  {
                "name": "Brother TN-760 High-Yield ",
                "brand": "brother",
                "description": "High-yield  cartridge for Brother printers.",
                "price": 899,
                "originalPrice": 1299,
                "discount": 31,
                "image": "/brother22.jpg",
                "compatiblePrinters": "Brother HL-L2300D, HL-L2340DW, MFC-L2700DW",
                "stock": 40,
                "category": "",
                "createdAt": datetime.now()
            },

                  {
                "name": "Brother TN-760 High-Yield ",
                "brand": "brother",
                "description": "High-yield  cartridge for Brother printers.",
                "price": 899,
                "originalPrice": 1299,
                "discount": 31,
                "image": "/brother24.jpg",
                "compatiblePrinters": "Brother HL-L2300D, HL-L2340DW, MFC-L2700DW",
                "stock": 44,
                "createdAt": datetime.now()
            },
            # Samsung Products
            {
                "name": "Samsung MLT-D101S ",
                "brand": "samsung",
                "description": "Black  for Samsung printers.",
                "price": 649,
                "originalPrice": 749,
                "discount": 13,
                "image": "/samsun10.jpg",
                "compatiblePrinters": "Samsung ML-2165W, ML-2160",
                "stock": 25,
                "createdAt": datetime.now()
            },
                {
                "name": "Samsung MLT-D101S ",
                "brand": "samsung",
                "description": "Black  for Samsung printers.",
                "price": 649,
                "originalPrice": 749,
                "discount": 13,
                "image": "/samsung11.jpg",
                "compatiblePrinters": "Samsung ML-2165W, ML-2160",
                "stock": 25,
                "createdAt": datetime.now()
            },
                {
                "name": "Samsung MLT-D101S ",
                "brand": "samsung",
                "description": "Black  for Samsung printers.",
                "price": 649,
                "originalPrice": 749,
                "discount": 13,
                "image": "/samsung.jpg",
                "compatiblePrinters": "Samsung ML-2165W, ML-2160",
                "stock": 25,
                "createdAt": datetime.now()
            }
        ]
        
        # Insert new products
        result = await products.insert_many(sample_products)
        print(f"✓ Inserted {len(result.inserted_ids)} products successfully!")
        
        # Show statistics
        hp_count = await products.count_documents({"brand": "hp"})
        canon_count = await products.count_documents({"brand": "canon"})
        epson_count = await products.count_documents({"brand": "epson"})
        brother_count = await products.count_documents({"brand": "brother"})
        samsung_count = await products.count_documents({"brand": "samsung"})
        
        print("\n📊 Products by brand:")
        print(f"   HP: {hp_count} products")
        print(f"   Canon: {canon_count} products")
        print(f"   Epson: {epson_count} products")
        print(f"   Brother: {brother_count} products")
        print(f"   Samsung: {samsung_count} products")
        print(f"   Total: {len(sample_products)} products")
        
        print("\n✅ Database seeding completed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if client:
            client.close()  # Don't await it, just close

if __name__ == "__main__":
    asyncio.run(seed_products())