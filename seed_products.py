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
        products_collection = db["products"]  
        
        result = await products_collection.delete_many({})
        print(f"✓ Cleared {result.deleted_count} existing products")
        sample_products = [
            {
                "name": "Kyocera ECOSYS M2035dn, M2535dn Compatible Black Toner Cartridge TK1140 ", 
                "brand": "Kyocera",
                "description": "New Kyocera TK-1140 black toner for ECOSYS M2035dn/M2535dn delivers up to 7,200 crisp pages. Smart print tech, stable performance and easy installation. Reliable, high‑yield replacement — buy now for value at 575 ZAR (South Africa).",  
                "price": 600.00,
                "originalPrice": 750.00,
                "Tags": " 7200 page black toner, Kyocera M2035 dn M2535 dn toner, TK-1140 compatible toner",  
                "image": "/images/kryocera.jpg",
                "stock": 2,
                "category": " Kyocera ink Cartridges, Kyocera Printer Cartridges, Kyocera Toner Cartridges, Kyocera Toners",
                "createdAt": datetime.now()
            },
            {
                "name": "Kyocera M5526cdn Generic Value Pack Plus Extra Black Toner Cartridges TK-5240",
                "brand": "Kyocera",
                "description": "Kyocera M5526cdn Generic Value Pack Plus Extra Black Toner Cartridges TK-5240, Get a great value for everyday business printing.Help avoid downtime with the legendary quality and reliability of The Cartridge guy Generic Kyocera toner cartridges. Intelligence built into the toner cartridge helps to optimize print quality and reliability. Save space a smaller cartridge and efficient toner use allow for a small printer footprint.",
                "price": 2000.00,
                "originalPrice": 2300.00,
                "Tags": ": Generic Kryocera M5526cdn Value Pack Plus extra black TK-5240",
                "image": "/images/kryocera2.jpg",
                "stock": 5,
                "category": " Kyocera compatible Toners",
                "createdAt": datetime.now()
            },
            {
                "name": "Kyocera M6230cidn, P6230cdn Original Black Toner Cartridge TK-5270 ",
                "brand": "kyocera",
                "description": "Introducing the Kyocera M6230 cidn, P6230 cdn Original Black Toner Cartridge TK-5270, your ultimate solution for high-quality printing. Designed specifically for Kyocera printers, this toner cartridge delivers exceptional performance, ensuring that your documents are sharp and vibrant, page after page.",
                "price": 5050.20,
                "originalPrice": 6070.00 ,
                "Tags": " Kyocera Ecosys Cartridge TK-5270",
                "image": "/images/kryocera3.jpg",
                "stock": 6,
                "category": "kyocera original toner cartridges, kyocera#, Lexmark original toner Cartridges, Toner Cartridges",
                "createdAt": datetime.now()
            },
            {
                "name": "Refilled Toner for Black Kyocera ECOSYS M2040dn/ M2540dn/ M2640idw,7200 pages- TK-1170",
                "brand": "kyocera",
                "description": "Refilled Toner for Black Kyocera ECOSYS M2040dn/ M2540dn/ M2640idw,7200 pages- TK-1170, Refill and Save Money Today. Kyocera Black Toner Refill from The Cartridge Guy, prints the same as the original print volumes.If you are tired of having to buy new Kyocera Toner Cartridges for your printer, you can now save costs by getting our Kyocera TK-1170, which has been fully refilled ready to be used. which will save you thousands of Rands.Compatible with Kyocera ECOSYS M2040dn, M2540dn, M2640idw",
                "price": 370.00,
                "originalPrice": 480.00,
                "Tags": ":Refilled Toner for Black Kyocera ECOSYS TK-1170",
                "image": "/images/krycera4.jpg",
                "stock": 8,
                "category": "Refilled Toner",
                "createdAt": datetime.now()
            },
            
            {
                "name": "Kyocera ECOSYS M3645dn, M3145dn Generic Black Toner TK-3160 ",
                "brand": "kyocera",
                "description": "Introducing the Kyocera ECOSYS M3645 dn, M3145 dn Generic Black Toner TK-3160, a premium compatible toner designed to deliver exceptional print quality while enhancing your productivity. This high-performance toner, branded by Kyocera, is engineered for use with the ECOSYS M3645 dn and M3145 dn printers, ensuring a seamless fit and optimal performance. With a remarkable page yield of up to 12,500 pages, this toner is ideal for high-volume printing, making it a cost-effective solution for businesses and professionals alike. The toner is new and comes in a secure package, ensuring that it maintains its quality until use. It operates efficiently within a storage temperature range of -20 to 40°C, ensuring reliability in various conditions. Priced competitively at R455, discounted from R487, this toner offers outstanding value without compromising on quality. Upgrade your printing experience with the Kyocera ECOSYS M3645 dn, M3145 dn Generic Black Toner TK-3160 and enjoy sharp, clear, and professional-looking documents every time.",
                "price": 602.00,
                "Tags": ": Compatible black toner, Kyocera toner, TK-3160 toner cartridge",
                "image": "/images/kryocera5.jpg",
                "stock": 4,
                "category": " Compatible Kyocera Toners",
                "createdAt": datetime.now()
            },
            {
                "name": "Kyocera P3055DN Compatible Black Toner Cartridge TK-3190",
                "brand": "kyocera",
                "description": "Kyocera P3055DN Compatible Black Toner Cartridge TK-3190,  Help avoid downtime with the legendary quality and reliability of The Cartridge Guy Generic Kyocera LaserJet toner cartridges. Intelligence built into the toner cartridge helps to optimize print quality and reliability. Save space a smaller cartridge and efficient toner use allow for a small printer footprint.",
                "price": 630.00 ,
                "originalPrice": 800.00,
                "Tags": ": Kyocera P3055DN Compatible Black Toner Cartridge TK-3190",
                "image": "/images/kryocera5.jpg",
                "stock": 7,
                "category": "Kyocera compatible Toners",
                "createdAt": datetime.now()
            },
            {
                "name": "Kyocera ECOSYS M2035dn, M2535dn Compatible Black Toner Cartridge TK1140 ",
                "brand": "kyocera",
                "description": "High-performance replacement toner designed for professional environments — the Kyocera ECOSYS M2035 dn / M2535 dn compatible TK-1140 delivers crisp black prints, reliable yields and exceptional value at a sale price of 575 ZAR (regular 599 ZAR).",
                "price": 600.00,
                "Tags": "35 dn M2535 dn toner, TK-1140 compatible toner",
                "image": "/images\kryocera6.jpg",
                "stock": 3,
                "category": " Kyocera ink Cartridges, Kyocera Printer Cartridges, Kyocera Toner Cartridges, Kyocera Toners",
                "createdAt": datetime.now()
            },
            {
                "name": "The Cartridge Depo MP C2503 / DSC1025 Toner Cartridge Set Compatible for Ricoh MP C2003 MP C2503 MP C2004 MP C2504 Printers (1BK / 1C / 1Y / 1M) ",
                "brand": "Ricoh",
                "description": "Compatible toner cartridge set for Ricoh MP C2003 / MP C2503 / MP C2004 / MP C2504 multifunction printers. This premium-quality compatible bundle includes 1 Black, 1 Cyan, 1 Magenta, and 1 Yellow toner cartridge designed to deliver sharp black text and vibrant colour prints for office and business environments.",
                "price": 2210.00,
                "originalPrice": 2450.00,
                "Tags": " Toner Cartridges",
                "image": "/images/ricoh.jpg",
                "stock": 3,
                "category": " Toner Cartridges",
                "createdAt": datetime.now()
            },
                        {
                "name": "Ricoh MP C3503 Black Toner Cartridge (Genuine)",
                "brand": "Ricoh",
                "description": "Ensure peak performance and longevity for your Ricoh MP C3503 with the Genuine Ricoh 841813 (also known as 841817) Black Toner Cartridge. Designed specifically for your Ricoh printer, this toner cartridge delivers crisp, clear black text and graphics, page after page. ",
                "price": 330.00,
                "originalPrice": 430.00,
                "Tags": " Ricoh MP C3503",
                "image": "/images/richo2.jpg",
                "stock": 2,
                "category": " Ricoh MP C3503",
                "createdAt": datetime.now()
            },
            {
                "name": "Ricoh SP, 2501L, MP 2001 Generic Black Toner Cartridge -MP2501 ",
                "brand": "Ricoh",
                "description": "Ricoh SP, 2501L, MP 2001 Generic Black Toner Cartridge -MP2501.  Get a great value for everyday business printing.",
                "price": 230.00,
                "Tags": "2501L, MP 2001 Generic Black Toner Cartridge -MP2501, Ricoh SP",
                "image": "/images/ricoh3.jpg",
                "stock": 5,
                "category": "Ricoh toners",
                "createdAt": datetime.now()
            },
            {
                "name": "Ricoh 410 Series Compatible Black Toner Cartridge 1270D ",
                "brand": "Ricoh",
                "description": "Ricoh 410 Series Compatible Black Toner Cartridge 1270D.  Get a great value for everyday business printing.",
                "price": 260.00,
                "originalPrice": 280.09,
                "Tags": "Ricoh 1270D Compatible Black Toner Cartridge",
                "image": "/images/ricoh4.jpg",
                "stock": 7,
                "category": " Ricoh toners",
                "createdAt": datetime.now()
            },
            {
                "name": "Brother HL-L3210CW, MFC-L3750CDW Generic Black Toner Cartridge TN-277 ",
                "brand": "Brother",
                "description": "Introducing the Brother HL-L3210 CW, MFC-L3750 CDW Generic Black Toner Cartridge TN-277, a reliable and high-performance solution for all your printing needs. Designed to deliver crisp, professional-quality prints, this toner cartridge is perfect for both home and office use, ensuring that your documents stand out with clarity and precision",
                "price": 320.00,
                "originalPrice": 450.00,
                "Tags": " Brother Generic TN-277BK Black Laser Toner Cartridge HLL3210CW, DCPL3551CDW",
                "image": "/images/brother.jpg",
                "stock": 6,
                "category": ": Brother toner cartridges, Toner Cartridges",
                "createdAt": datetime.now()
            },
            
            {
                "name": "Brother TN-469M MFC-8690CDW, MFC-9570CDW Generic Magenta Cartridge TN-469",
                "brand": "Brother",
                "description": "Brother MFC-8690CDW, MFC-9570CDW Generic Magenta Cartridge TN-469. Get a great value for everyday business printing.  Help avoid downtime with the legendary quality and reliability of The Cartridge guy Generic Brother toner cartridges. Intelligence built into the toner cartridge helps to optimize print quality and reliability. Save space a smaller cartridge and efficient toner use allow for a small printer footprint",
                "price": 670.00,
                "originalPrice": 720.00,
                "Tags": " Brother TN-469 Magenta Generic Cartridge",
                "image": "/images/brother2.jpg",
                "stock": 5,
                "category": " Toner Cartridges",
                "createdAt": datetime.now()
            },
            {
                "name": "Brother TN-279 Black Toner Cartridge Original ",
                "brand": "Brother",
                "description": "Brother TN-279BK Black Toner Cartridge 1,500 Pages Original 84GT910K141 Single-pack.  This is an Brother Original Black Laser Toner cartridge with JetIntelligence that may help you to get the most out of your printer – professional documents you may be proud of, more pages at fast speeds, affordable high-yield options and anti-fraud technology.",
                "price": 1500.30,
                "originalPrice": 1736.40,
                "Tags": " Brother TN-279M Black Toner Cartridge 1000 Pages Original 84GT910M141",
                "image": "/images/brother3.jpg",
                "stock": 7,
                "category": "Brother original Toner Cartridges, Brother#, Toner Cartridges",
                "createdAt": datetime.now()
            },
            {
                "name": "Brother TN1000 DCP-1510,1600 Generic Black Toner Cartridge ",
                "brand": "Brother",
                "description": "Brother DCP-1510,1600 Generic Black Toner Cartridge TN-1000.   A High Quality Compatible Generic Replacement Toner Cartridge.",
                "price": 400.00,
                "Tags": "1600 Generic Black Toner TN-1000, Brother DCP-1510",
                "image": "/images/brother4.jpg",  
                "stock": 9,
                "category": " Toner Cartridges",
                "createdAt": datetime.now()
            },
                        {
                "name": "Brother DR1000 MFC-1910W, DCP-1610W Generic Black Drum Unit DR-1000 ",
                "brand": "Brother",
                "description": "Brother MFC-1910W, DCP-1610W Generic Black Drum Unit DR-1000. Get a great value for everyday business printing. Help avoid downtime with the legendary quality and reliability of The Cartridge guy Generic Brother toner cartridges. Intelligence built into the toner cartridge helps to optimize print quality and reliability. Save space a smaller cartridge and efficient toner use allow for a small printer footprint.",
                "price": 410.10,
                "originalPrice": 499.00,
                "Tags": " Generic Brother DR-1000 Black Drum Unit MFC-1910W",
                "image": "/images/brother5.jpg",
                "stock": 6,
                "category": "Drum Units",
                "createdAt": datetime.now()
            },
            {
                "name": "Brother MFC-L2740DW, MFC-L2700DW Compatible Black Toner Cartridge TN-2355",
                "brand": "Brother",
                "description": "Brother MFC-L2740DW, MFC-L2700DW Compatible Black Toner Cartridge TN-2355.  Get a great value for everyday business printing.Help avoid downtime with the legendary quality and reliability of The Cartridge guy Generic Brother toner cartridges. Intelligence built into the toner cartridge helps to optimize print quality and reliability. Save space a smaller cartridge and efficient toner use allow for a small printer footprint.",
                "price": 499.80,
                "originalPrice": 599.80,
                "Tags": " Brother TN-2355 Compatible Black Toner MFC-L2740DW",
                "image": "/images/brother6.jpg",
                "stock": 5,
                "category": "Toner Cartridges",
                "createdAt": datetime.now()
            },
            {
                "name": "Brother HLL2365DW MFCL2700D Generic Black Drum Unit DR-2305 ",
                "brand": "Brother",
                "description": "Brother HLL2365DW MFCL2700D Generic Black Drum Unit DR-2305. A High Quality Compatible Generic Replacement Drum Unit, Print Clear Vivid Images and Text, Easy to Install & Replace, Long Lasting, Money-Wise Printing Solution. Every person and business want to produce professionally looking documents. Because it reflects your image or that of your company. Whether you are printing normal black and white invoices or beautiful full color brochures so at THE Cartridge guy we aim to deliver the right quality at the right price.",
                "price": 420.00,
                "originalPrice": 497.90,
                "Tags": "Brother HLL2365DW MFCL2700D Generic Black Drum Unit DR-2305",
                "image": "/images/brother7.jpg",
                "stock": 6,
                "category": "Brother Generic Toner",
                "createdAt": datetime.now()
            },
               {
                "name": "Brother TN3467 HL-5270 , HL-5250 Generic Black Toner Cartridge TN-3467 ",
                "brand": "Brother",
                "description": "Brother HL-5270 , HL-5250 Generic Black Toner Cartridge TN-3467. Get a great value for everyday business printing. Help avoid downtime with the legendary quality and reliability of The Cartridge guy Generic Brother toner cartridges. Intelligence built into the toner cartridge helps to optimize print quality and reliability. Save space a smaller cartridge and efficient toner use allow for a small printer footprint.",
                "price": 310.00,
                "originalPrice": 400.90,
                "Tags": " Brother TN-3467 Black Generic Toner HL-5240 Series",
                "image": "/images/brother8.jpg",
                "stock": 4,
                "category": "Toner Cartridges",
                "createdAt": datetime.now()
            },
               {
                "name": "Brother DR-3405 Generic Black Drum Unit DR-3405 ",
                "brand": "Brother",
                "description": "Brother DR-3405 Generic Black Drum Unit MFC-L6900DW. Get a great value for everyday business printing.",
                "price": 305.00,
                "originalPrice": 499.90,
                "Tags": "Brother DR-3405 Generic Black Drum Unit MFC-L6900DW",
                "image": "/images/brother9.jpg",
                "stock": 7,
                "category": "Drum Units",
                "createdAt": datetime.now()
            },
                {
                    "name": "Brother MFC-L6900DW Generic Black Toner Cartridge TN-3487 ",
                    "brand": "Brother",
                    "description": "Brother MFC-L6900DW Generic Black Toner Cartridge TN-3487. Get a great value for everyday business printing.Help avoid downtime with the legendary quality and reliability of the Brother Black Generic Toner Cartridge. Intelligence built into the toner cartridge helps to optimize print quality and reliability. Save space a smaller cartridge and efficient toner use allow for a small printer footprint.",
                    "price": 520.00,
                    "originalPrice": 650.00,
                    "Tags": " Brother TN-3487 Black Generic Toner Cartridge MFC-L6900DW",
                    "image": "/images/brother10.jpg",
                    "stock": 5,
                    "category": "Toner Cartridges",
                    "createdAt": datetime.now()
                },

                {
                    "name": "Brother MFC-L6900DW Generic Black Toner Cartridge TN-3487 ",
                    "brand": "Brother",
                    "description": "Brother MFC-L6900DW Generic Black Toner Cartridge TN-3487. Get a great value for everyday business printing.Help avoid downtime with the legendary quality and reliability of the Brother Black Generic Toner Cartridge. Intelligence built into the toner cartridge helps to optimize print quality and reliability. Save space a smaller cartridge and efficient toner use allow for a small printer footprint.",
                    "price": 520.00,
                    "originalPrice": 650.00,
                    "Tags": " Brother TN-3487 Black Generic Toner Cartridge MFC-L6900DW",
                    "image": "/images/brother11.jpg",
                    "stock": 5,
                    "category": "Toner Cartridges",
                    "createdAt": datetime.now()
                },
                 {
                    "name": "Canon CRG-737 Black Toner Cartridge - Compatible ",
                    "brand": "Canon",
                    "description": "Tech Specs Compatible Black Toner Cartridge CRG-737 Page yield: 2400 pages @5% coverage Suitable printers: Canon MF211, Canon MF212w, Canon MF216n, Canon MF217w, Canon MF226dn Canon MF229dw, Canon MF231, Canon MF232w, Canon MF237w, Canon MF247dw Canon MF249dw.",
                    "price": 400.00,
                    "originalPrice": 499.00 ,
                    "Tags": "Canon 737 Black Compatible Toner  ",
                    "image": "/images/canon1.jpg",
                    "stock": 5,
                    "category": "Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "Canon MF641Cw Compatible Magenta Toner Cartridge 054",
                    "brand": "Canon",
                    "description": "Canon MF641Cw Compatible Magenta Toner Cartridge 054. Get a great value for everyday business printing. Help avoid downtime with the legendary quality and reliability of The Cartridge guy Compatible Canon magenta Toner Cartridge. Intelligence built into the toner cartridge helps to optimize print quality and reliability. Save space a smaller",
                    "price": 450.40,
                    "Tags": " Compatible Canon MF641Cw Magenta Toner Cartridge 054",
                    "image": "/images/canon2.jpg",
                    "stock": 5,
                    "category": "Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "Canon 045 Black Toner Cartridge - Compatible ",
                    "brand": "Canon",
                    "description": "Canon MF641Cw Compatible Magenta Toner Cartridge 054. Get a great value for everyday business printing.",
                    "price": 430.00,
                    "originalPrice": 510.00 ,
                    "Tags": "  Compatible Canon MF641Cw Magenta Toner Cartridge 045",
                    "image": "/images/canon5.jpg",
                    "stock": 3,
                    "category": "Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "Compatible Canon 067 Black Toner Cartridge ",
                    "brand": "Canon",
                    "description": "The Compatible Canon 067 Black Toner Cartridge is a premium-quality replacement toner cartridge designed to deliver sharp black text, reliable performance, and professional-quality printing results.",
                    "price": 530.20,
                    "Tags": " LBP631Cw",
                    "image": "/images/canon4.jpg",
                    "stock": 4,
                    "category": "Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "CANON 069 / 069 color toner cartridge - Compatible",
                    "brand": "Canon",
                    "description": "Original Manufacturer Part No: CRG069BK, CRG069C, CRG069M, CRG069Y, Colours: Black, Cyan, Yellow & Magenta. Page yeild Black 2,100 Pages Cyan 1,900 Pages Yellow 1,900 Pages Magenta 1,900 Pages ",
                    "price": 600.80,
                    "Tags": " ",
                    "image": "/images/canon6.jpg",
                    "stock": 3,
                    "category": "Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "Canon C3320i, C3325i Black Generic Toner Cartridge EXV-49",
                    "brand": "Canon",
                    "description": "Canon Black Toner Cartridge EXV-49. ★Compatible Models- Canon C-EXV 49  toner cartridge compatible for Canon imageRUNNER ADVANCE C3020 C3320L C3530 C3525 C3520 C3330 3325 3320 Printer. ★Installation Steps -- Open the waste powder cover to clean the waste powder, Insert the bottle powder funnel into the powder filling hole to add powder, Close the lid and put it in the printer to use.",
                    "price": 950.90,
                    "originalPrice": 1020.90 ,
                    "Tags": " C3325i Black Generic Toner Cartridge EXV-49, Canon C3320i",
                    "image": "/images/canon7.jpg",
                    "stock": 5,
                    "category": "Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "Canon C1325iF, 1335iF Generic Cyan Toner Cartridge EXV-48 ",
                    "brand": "Canon",
                    "description": "Canon has long been a reliable partner in the office to get printing and scanning jobs done. We supply generic and original replacement cartridges for your Canon printer. Moreover some of our customers insist on using the original OEM cartridges and drum units. Use our range of guaranteed generic replacement cartridges and drum units (Canon  Toner), therefore our slogan is to cut costs not corners.",
                    "price": 900.60,
                    "originalPrice": 1570.90 ,
                    "Tags": " 1335iF Cyan Generic Toner Cartridge EXV-48, Canon C1325iF",
                    "image": "/images/canon9.jpg",
                    "stock": 8,
                    "category": " CanonToner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "Pantum P2200, P2500W Generic Black Toner Cartridge PC-210 ",
                    "brand": "Pantum",
                    "description": "Pantum P2200, P2500W Generic Black Toner Cartridge PC-210. Get a great value for everyday business printing. Help avoid downtime with the legendary quality and reliability of The Cartridge guy Generic Pantum toner cartridges. Intelligence built into the toner cartridge helps to optimize print quality and reliability. Save space a smaller cartridge and efficient toner use allow for a small printer footprint.",
                    "price": 601.00,
                    "Tags": "Generic Pantum PC-210 Toner Cartridge P2200",
                    "image": "/images/pantum1.jpg",
                    "stock": 4,
                    "category": "pantum Generic Toner",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "Pantum PC310 Black Original Toner Cartridge – PC 310 ",
                    "brand": "Pantum",
                    "description": "Pantum P3205DN / 3255DN Original Black Toner Cartridge PC-310. This is an original Canon cartridge with JetIntelligence that may help you to get the most out of your printer – professional documents you may be proud of, more pages at fast speeds, affordable high-yield options and anti-fraud technology.",
                    "price": 2200.09,
                    "originalPrice": 2570.00 ,
                    "Tags": " Pantum PC-310 Black Original Toner Cartridge",
                    "image": "/images/pantum2.jpg",
                    "stock": 4,
                    "category": "Pantum Original Toner Cartridges, Pantum supplies, Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "Pantum PC-410 Compatible Toner Cartridge – For Pantum P3010, P3300, M6700, M6800, M7100, M7200 & M7300 Series Printers ",
                    "brand": "Pantum",
                    "description": "Keep your Pantum printer performing at its best with the **Pantum PC-410 Compatible Toner Cartridge**, a reliable and cost-effective alternative to the original cartridge. Designed to deliver sharp black text, professional-quality documents, and consistent print performance, this high-yield toner cartridge is ideal for home offices, small businesses, schools, and corporate environments.",
                    "price": 600.00,
                    "originalPrice": 789.09 ,
                    "image": "/images/pantum3.jpg",
                    "stock": 7,
                    "category": "Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "Pantum P7100DW0 P7200 Generic Black Drum Unit DL-410 ",
                    "brand": "Pantum",
                    "description": "Pantum has been a reliable partner in the office to get printing and scanning jobs done. We supply generic and original replacement cartridges for your Pantum printer. Moreover some of our customers insist on using the original OEM cartridges and drum units. Use our range of guaranteed generic replacement cartridges and drum units (Pantum DL-410 Generic Black Printer Drum)",
                    "price": 770.90,
                    "Tags": "Pantum DL-410 Generic Black Printer Drum",
                    "image": "/images/pantum4.jpg",
                    "stock": 5,
                    "category": "Pantum Printer Drum",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "Hp P1102/M1212 Compatible Black Toner Cartridge CE285A/ 85A ",
                    "brand": "Pantum",
                    "description": "Toner cartridge replacements for 85A CE285A are strictly tested with industry quality control processes. High Quality: Refined toner and high quality accessories to delivery stability and smoothly printing result. Package Contents: 1 Black compatible with 85A CE285A toner cartridge",
                    "price": 485.90,
                    "originalPrice": 570.00 ,
                    "Tags": " Hp P1102/M1212 Compatible 1 Pack Toner Cartridge 85A",
                    "image": "/images/pantum5.jpg",
                    "stock": 6,
                    "category": "Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "Compatible CF283A Toner Cartridge for HP LaserJet Pro M125/M127 – Black – 1,500 Pages",
                    "brand": "HP",
                    "description": "Compatible replacement toner cartridge suitable for selected HP LaserJet Pro printers. Designed to deliver sharp black text, reliable performance, and consistent printing results for office, school, hospital, and home use.",
                    "price": 520.00,
                    "image": "/images/hp1.jpg",
                    "stock": 2,
                    "category": "Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "HP P2035, P2055 Compatible Black Toner Cartridge 05A ",
                    "brand": "HP",
                    "description": "HP P2035, P2055 Compatible Black Toner Cartridge 05A",
                    "price": 502.90,
                    "Tags": " HP P2035, P2055 Compatible Black Toner Cartridge 05A",
                    "image": "/images/hp3.jpg",
                    "stock": 7,
                    "category": "Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "HP MF112/MF113w Generic Black Toner Cartridge CF217A/17A ",
                    "brand": "HP",
                    "description": "Help avoid downtime with the legendary quality and reliability of The Cartridge guy Generic HP toner cartridges. Intelligence built into the toner cartridge helps to optimize print quality and reliability. Save space a smaller cartridge and efficient toner use allow for a small printer footprint.",
                    "price": 550.09,
                    "Tags": " HP Black Toner Cartridge CF217A/17A",
                    "image": "/images/hp2.jpg",
                    "stock": 8,
                    "category": "Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "HP 12A Q2612A Black Compatible Toner Cartridge 12A ",
                    "brand": "HP",
                    "description": "Compatible Models: Hewlett Packard HP Laserjet 1010; 1012; Laserjet 1015; Laserjet 1018; 1020; Laserjet 1022; Laserjet 1022N; 1022NW; Laserjet 3015; Laserjet 3020; HP3030; Laserjet 3050Z; Laserjet 3050; 3052; Laserjet 3055; Laserjet M1005; M1120; Laserjet M1120N; Laserjet M1319F; Laser Jet 1010 / 1012 / 1015 / 1018 / 1020 / 1022",
                    "price": 480.00,
                    "originalPrice": 589.00 ,
                    "Tags": "12A ",
                    "image": "/images/hp4.jpg",
                    "stock": 5,
                    "category": "Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "Hp M2727nf, M2727nfs Compatible Black Toner Cartridge Q7553A/53A ",
                    "brand": "HP",
                    "description": "Hp M2727nf, M2727nfs Compatible Black Toner Cartridge 53A. Get a great value for everyday business printing. Help avoid downtime with the legendary quality and reliability of The Cartridge guy Generic HP LaserJet toner cartridges. Intelligence built into the toner cartridge helps to optimize print quality and reliability. Save space a smaller cartridge and efficient toner use allow for a small printer footprint.",
                    "price": 490.80,
                    "Tags": " Hp 53A Black Compatible Toner Cartridge M2727nf, M2727nfs",
                    "image": "/images/hp6.jpg",
                    "stock": 4,
                    "category": "Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "Hp CF226A Original Black Toner Cartridge 26A ",
                    "brand": "HP",
                    "description": "Introducing the HP CF226A Original Black Toner Cartridge 26A, your ultimate solution for high-quality printing. Designed specifically for HP printers, this toner cartridge ensures crisp, clear, and professional documents every time. Perfect for home offices or businesses, it delivers reliable performance that meets your printing needs.",
                    "price": 3050.00,
                    "originalPrice": 3550.90 ,
                    "Tags": "Hp Original Black Cartridge 26A",
                    "image": "/images/hp7.jpg",
                    "stock": 6,
                    "category": "hp original toner, HP Supplies, Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "HP 30A Black Toner Cartridge 1,600 Pages Original CF230A Single-pack ",
                    "brand": "HP",
                    "description": "Hp MFP M125 M201 Original Black Toner Cartridge 30A. This is an original Hp Toner cartridge with Jet Intelligence that may help you to get the most out of your printer – professional documents you may be proud of, more pages at fast speeds, affordable high-yield options and anti-fraud technology.",
                    "price": 1799.00,
                    "originalPrice": 2609.00 ,
                    "Tags": " Hp MFP M125 M201 Original Black Toner Cartridge 30A",
                    "image": "/images/hp8.jpg",
                    "stock": 4,
                    "category": " hp original toner, Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "Compatible HP CF259A Black Toner Cartridge (59A)",
                    "brand": "HP",
                    "description": "Get exceptional print quality without the high price tag! This Compatible HP CF259A Black Toner Cartridge (59A) is the perfect replacement for your HP LaserJet Pro or Enterprise printer. Engineered to deliver sharp black text and professional results, it matches the performance of the original HP cartridge at a fraction of the cost.",
                    "price": 410.90,
                    "image": "/images/hp10.jpg",
                    "stock": 3,
                    "category": "Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "Hp LaserJet Pro M283, M255 Magenta Compatible Toner Cartridge 207A ",
                    "brand": "HP",
                    "description": "Get a great value for everyday business printing.. Help avoid downtime with the legendary quality and reliability of The Cartridge guy Generic HP LaserJet toner cartridges. Intelligence built into the toner cartridge helps to optimize print quality and reliability. Save space a smaller cartridge and efficient toner use allow for a small printer footprint.",
                    "price": 630.09,
                    "originalPrice": 789.00 ,
                    "Tags": "  Hp LaserJet Pro M283, M255 Magenta Compatible Toner Cartridge 207A",
                    "image": "/images/hp11.jpg",
                    "stock": 5,
                    "category": "Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "p M454 W2030A Original Black Toner Cartridge 415A ",
                    "brand": "HP",
                    "description": "HP 415A Black Toner Cartridge (W2030A). Original HP toner designed for consistent, high-quality printing in colour laser printers ~2,400 Pages. OEM Quality. JetIntelligence. Colour Laser Compatible ",
                    "price": 2600.00,
                    "originalPrice": 2255.00 ,
                    "Tags": "hp 415a black, Hp M454 W2030A Original Black Toner Cartridge 415A",
                    "image": "/images/hp12.jpg",
                    "stock": 9,
                    "category": "hp original toner, Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "HP LaserJet Pro M254,MFP M280 , MFP M281 203A Yellow CF542A Compatible Toner Cartridge ",
                    "brand": "HP",
                    "description": "Hp Pro M254 M280 Compatible Yellow Toner Cartridge 203A. Get a great value for everyday business printing.Help avoid downtime with the legendary quality and reliability of The Cartridge guy Generic HP LaserJet toner cartridges. Intelligence built into the toner cartridge helps to optimize print quality and reliability. Save space a smaller cartridge and efficient toner use allow for a small printer footprint.",
                    "price": 540.09,
                    "originalPrice": 980.09 ,
                    "Tags": " Hp Pro M254 M280 Compatible Yellow Toner Cartridge 203A",
                    "image": "/images/hp13.jpg",
                    "stock": 5,
                    "category": "Toner Cartridges",
                    "createdAt": datetime.now()
                },
                   {
                    "name": "Samsung CLP360 Compatible Cyan Toner Cartridge CLT-C406S ",
                    "brand": "Samsung",
                    "description": "Samsung CLP360 Compatible Cyan Toner Cartridge CLT-C406S. Get a great value for everyday business printing. Help avoid downtime with the legendary quality and reliability of The Cartridge guy Generic Samsung toner cartridges. Intelligence built into the toner cartridge helps to optimize print quality and reliability. Save space a smaller cartridge and efficient toner use allow for a small printer footprint.",
                    "price": 550.90,
                    "originalPrice": 783.90 ,
                    "Tags": "amsung CLP360 Compatible Cyan Toner Cartridge CLT-406S",
                    "image": "/images/samsung.jpg",
                    "stock": 4,
                    "category": "Samsung Generic Toner",
                    "createdAt": datetime.now()
                },
                
             

        ]
        
        result = await products_collection.insert_many(sample_products)
        print(f"✓ Inserted {len(result.inserted_ids)} product placeholders successfully!")
        
        print("\n Products by brand:")
        brands = ["hp", "canon", "epson", "brother", "samsung"]
        for brand in brands:
            count = await products_collection.count_documents({"brand": brand})
            print(f"   {brand.capitalize()}: {count} products")
        
        print(f"\n   Total placeholders: {len(sample_products)} products")
        print("\n Example product update:")
       
    except Exception as e:
        print(f" Error: {e}")
    finally:
        if client:
            client.close()

if __name__ == "__main__":
    asyncio.run(seed_products())