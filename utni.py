x = {
    "@context": "http://schema.org/",
    "@type": "Product",
    "name": "RAW CLASSIC 20PK KING SIZE CONES -12CT DISPLAY BOX",
    "url": "https:\/\/awswholesale.com\/products\/raw-classic-20pk-king-size-cones-12ct-display-box-106964",
    "image": [
        "https:\/\/awswholesale.com\/cdn\/shop\/products\/106964_1000x.jpg?v=1654722589"
    ],
    "description": "CONTAINS 12 PACKS PER BOX \/ 20 CONES PER PACK",
    "sku": "106964",
    "brand": {"@type": "Thing", "name": "Raw"},
    "offers": [
        {
            "@type": "Offer",
            "sku": "106964",
            "availability": "http://schema.org/InStock",
            "price": 38.25,
            "priceCurrency": "USD",
            "url": "https:\/\/awswholesale.com\/products\/raw-classic-20pk-king-size-cones-12ct-display-box-106964?variant=42900313866462",
        }
    ],
}

y = [
    x["@context"],
    x["@type"],
    x["name"],
    x["url"],
    x["image"][0],
    x["description"],
    x["sku"],
    x["brand"].values(),
    x["offers"][0].values(),
]

print(y)
