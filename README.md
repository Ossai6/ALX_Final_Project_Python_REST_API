FindMyDish API Documentation

FindMyDish API allows users to manage recipes, including creating, retrieving, updating, and deleting recipes, as well as rating them. The API supports various features, including ingredient management and advanced search functionality.

Models
Ingredient
Fields:
id: (Integer) Unique identifier for the ingredient.
name: (String) Name of the ingredient (max length: 255).

Recipe
Fields:
id: (Integer) Unique identifier for the recipe.
title: (String) Title of the recipe (max length: 255, optional).
description: (String) Short description of the recipe (max length: 500, optional).
instructions: (Text) Cooking instructions (max length: 500, optional).
cooking_time: (String) Cooking time (max length: 500, optional).
difficulty_level: (String) Difficulty level (max length: 500, optional).
date_created: (Date) Date the recipe was created (auto-set).
author: (ForeignKey) User who created the recipe (optional).
ingredients: (List of Strings) List of ingredient names associated with the recipe.

Rating
Fields:
id: (Integer) Unique identifier for the rating.
recipe: (ForeignKey) Associated recipe.
user: (ForeignKey) User who provided the rating.
rating: (Integer) Rating value (1 to 5).
review: (Text) Optional review text.
created_at: (DateTime) Date and time the rating was created (auto-set).


Endpoints
1. Create a Recipe
Endpoint: POST /recipe/
Request Body:
json
Copy code
{
    "title": "Chocolate Cake",
    "description": "Delicious chocolate cake.",
    "instructions": "Mix ingredients and bake.",
    "cooking_time": "30 minutes",
    "difficulty_level": "Medium",
    "author": 1,  // User ID of the author
    "ingredients": ["flour", "sugar", "cocoa powder"] 
}
Response:
Success (200):
json
{
    "status": 200,
    "response": "Data posted successfully",
    "data": {
        "id": 1,
        "title": "Chocolate Cake",
        "description": "Delicious chocolate cake.",
        "instructions": "Mix ingredients and bake.",
        "cooking_time": "30 minutes",
        "difficulty_level": "Medium",
        "date_created": "2024-11-05",
        "author": 1,
        "ingredients": ["flour", "sugar", "cocoa powder"]
    }
}
Error (400):
json
{
    "status": 400,
    "error": {
        "ingredients": ["This field is required."]
    }
}


2. Retrieve All Recipes
Endpoint: GET /recipe/all/
Response:
Success (200):
json
{
    "status": 200,
    "response": "Data retrieved successfully",
    "data": [
        {
            "id": 1,
            "title": "Chocolate Cake",
            "description": "Delicious chocolate cake.",
            "instructions": "Mix ingredients and bake.",
            "cooking_time": "30 minutes",
            "difficulty_level": "Medium",
            "date_created": "2024-11-05",
            "author": 1,
            "ingredients": ["flour", "sugar", "cocoa powder"]
        }
        // More recipes...
    ]
}


3. Retrieve a Single Recipe
Endpoint: GET /recipe/<id>/
Response:
Success (200):
json
{
    "status": 200,
    "data": {
        "id": 1,
        "title": "Chocolate Cake",
        "description": "Delicious chocolate cake.",
        "instructions": "Mix ingredients and bake.",
        "cooking_time": "30 minutes",
        "difficulty_level": "Medium",
        "date_created": "2024-11-05",
        "author": 1,
        "ingredients": ["flour", "sugar", "cocoa powder"]
    }
}
Error (404):
json
{
    "status": 404,
    "message": "Recipe with the specified ID does not exist"
}


4. Update a Recipe
Endpoint: PUT /recipe/update/<id>/
Request Body:
json
{
    "title": "Updated Chocolate Cake",
    "description": "Delicious chocolate cake with extra chocolate.",
    "instructions": "Mix ingredients and bake at 350F.",
    "cooking_time": "35 minutes",
    "difficulty_level": "Medium",
    "ingredients": ["flour", "sugar", "cocoa powder", "extra chocolate"]  // Updated ingredient list
}
Response:
Success (202):
json
{
    "status": 202,
    "message": "Recipe updated successfully",
    "data": {
        "id": 1,
        "title": "Updated Chocolate Cake",
        "description": "Delicious chocolate cake with extra chocolate.",
        "instructions": "Mix ingredients and bake at 350F.",
        "cooking_time": "35 minutes",
        "difficulty_level": "Medium",
        "date_created": "2024-11-05",
        "author": 1,
        "ingredients": ["flour", "sugar", "cocoa powder", "extra chocolate"]
    }
}
Error (400):
json
{
    "status": 400,
    "message": "Invalid data",
    "errors": {
        "title": ["This field may not be blank."]
    }
}


5. Delete a Recipe
Endpoint: DELETE /recipe/delete/<id>/
Response:
Success (202):
json
{
    "status": 202,
    "message": "Recipe deleted successfully"
}
Error (404):
json
{
    "status": 404,
    "message": "Recipe not found"
}


6. Advanced Search for Recipes
Endpoint: GET /search/?title=<title>
Response:
Success (200):
json
{
    "status": 200,
    "response": "Data retrieved successfully",
    "data": [
        {
            "id": 1,
            "title": "Chocolate Cake",
            "description": "Delicious chocolate cake.",
            "instructions": "Mix ingredients and bake.",
            "cooking_time": "30 minutes",
            "difficulty_level": "Medium",
            "date_created": "2024-11-05",
            "author": 1,
            "ingredients": ["flour", "sugar", "cocoa powder"]
        }
    ]
}


7. List Ratings
Endpoint: GET /ratings/
Response:
Success (200):
json
{
    "status": 200,
    "data": [
        {
            "id": 1,
            "recipe": 1,
            "user": "username",
            "rating": 5,
            "review": "Excellent!",
            "created_at": "2024-11-05T12:34:56Z"
        }
    ]
}


8. Retrieve, Update, or Delete a Rating
Endpoint: GET/PUT/DELETE /ratings/<id>/
Response:
Success (200 for GET):
json
{
    "status": 200,
    "data": {
        "id": 1,
        "recipe": 1,
        "user": "username",
        "rating": 5,
        "review": "Excellent!",
        "created_at": "2024-11-05T12:34:56Z"
    }
}
Error (404):
json
{
    "status": 404,
    "message": "Rating not found"
}


9. Rate a Recipe
Endpoint: POST /recipe/<recipe_id>/ratings/
Request Body:
json
{
    "user": 1,  
    "rating": 5,
    "review": "Best recipe ever!"
}
Response:
Success (201):
json
{
    "status": 201,
    "message": "Rating created successfully"
}
Error (400):
json
{
    "status": 400,
    "error": {
        "rating": ["This field is required."]
    }
}


Error Handling
All responses include a status code and a descriptive message. Common HTTP status codes used include:

200 OK: The request was successful.
201 Created: The resource was created successfully.
202 Accepted: The request has been accepted for processing.
400 Bad Request: The request was invalid.
404 Not Found: The requested resource was not found.


This documentation provides a comprehensive overview of the Recipe API, detailing each endpoint's functionality and expected request/response formats. Users are encouraged to follow the guidelines to ensure smooth integration and usage of the API.
