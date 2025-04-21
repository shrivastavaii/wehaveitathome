# wehaveitathome

# wehaveitathome


To run current code, download Postman software on desktop. run app through terminal, then set to POST, put local host link\suggest into URL (example: http://127.0.0.1:5050/suggest). go to body and select json, input raw data (example {
  "ingredients": ["bread", "egg", "milk"],
  "method": "fuzzy",
  "dietary": "vegetarian",
  "max_time": 15
}
 )

 and then test. 

 should get output like this (example {
    "recipes": [
        [
            "French Toast",
            1.0
        ]
    ]
})
