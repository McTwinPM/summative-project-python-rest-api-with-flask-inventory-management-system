# summative-project-python-rest-api-with-flask-inventory-management-system


Instructions from Canvas

Scenario
You have been hired by a small retail company to develop an inventory management system. This system will allow employees to add, edit, view, and delete inventory items. Additionally, the system will fetch real-time product data from an external API (e.g., OpenFoodFacts API) to supplement product details.
You are tasked with creating an administrator portal for an e-commerce website which will include.
•	A Flask-based REST API with CRUD operations for managing inventory.

•	An external API integration to fetch product details by barcode or name.

•	A CLI-based interface to interact with the API.

•	Unit tests to validate functionality and interactions.
Tools and Resources
•	Development Tools: A text editor or IDE (e.g., VS Code), browser developer tools, Node.js, and GitHub.
•	OpenFoodFacts APILinks to an external site.



Task 1
•	Analyze and plan each necessary route.
•	Build a user interface to interact with each route.
•	Build flask endpoints to trigger upon user action.
•	Connect to OpenFoodFacts api to get specific data from the database.
•	Update simulated data storage by updating an array.

Task 2
For each planned route determine the necessary route inputs as well as the output of each route.
•	Determine what it will change in regards to the data given.
•	Determine when each route will be triggered within CLI application
•	Utilizing OpenFoodFacts database, build a mock database in an array.
 The data should resemble what the OpenFoodFacts API may contain: 
{
  "status": 1,
  "product": {
    "product_name": "Organic Almond Milk",
    "brands": "Silk",
    "ingredients_text": "Filtered water, almonds, cane sugar, ..."
    // Additional product information
  }
It is up to you to determine what data you may want to store store, ensure each item in your database array contains an ID.

Task 3
	Step 1
•	Initialize or clone new python project. 
o	Install necessary python installs like flask.
o	Use Github. 

	Step 2
•	Define API endpoints following RESTful conventions:

o	GET /inventory → Fetch all items
o	GET /inventory/<id> → Fetch a single item
o	POST /inventory → Add a new item
o	PATCH /inventory/<id> → Update an item
o	DELETE /inventory/<id> → Remove an item
•	Implement Flask routing and request handling.
•	Update temporary array to simulate storage.

	Step 3
•	Use the OpenFoodFacts API to fetch product details.
•	Implement a function that queries the external API using a barcode or product name.
•	Enhance stored inventory data with additional details from the API.

	Step 4
•	Develop a CLI tool to interact with the API.
•	Allow users to:

o	Add new inventory items.
o	View inventory details.
o	Update item prices or stock levels.
o	Delete products.
o	Find item on api.
•	Ensure error handling for invalid inputs and API failures.

Task 4
1.	Write unit tests for:
    •	API endpoints (GET, POST, PATCH, DELETE)
    •	CLI commands
    •	External API interactions
2.	Use pytest and unittest.mock to simulate API responses.
3.	Debug with Flask Debug Mode and Postman for API validation.

Task 5
•	Write a README.md with:
o	Installation and setup instructions
o	API endpoint details
o	Example usage of CLI commands
o	Ensure clear code comments and maintainability.
•	Push the project to GitHub with a structured repository.

Submission and Grading Criteria
1.	Review the rubric below as a guide for how this lab will be graded.

2.	Complete your assignment using your preferred IDE.

3.	When you are ready, push your final script to GitHub.

4.	Your GitHub repository should include:
    •	Complete source code.

    •	A README.md file with project details and instructions.

    •	Mock-up references or additional documentation if applicable.
5.	To submit your assignment, share the link to your GitHub repo below. 


Summative Lab: Python REST API with Flask- Inventory Management System
Summative Lab: Python REST API with Flask- Inventory Management System
Criteria	Ratings	Points
Flask Routing	Excelled
Route for CRUD actions and additional helper routes built with Flask
20 pts
Met Expectations
Route for CRUD actions built with flask
16 pts
Attempted
1 route built with flask
8 pts
No Attempt
No routes built with flask
0 pts	/20 pts
CRUD	Excelled
Read, create, update (patch) and delete requests completed.
20 pts
Met Expectations
Read and create (post) request completed.
16 pts
Attempted
Read (get) request completed.
8 pts
No Attempt
No CRUD
0 pts	/20 pts
External API	Excelled
User interface built to get from external api and add it to database array.
20 pts
Met Expectations
User interface built to get from external api
16 pts
Attempted
Database array built with external api
8 pts
No Attempt
No utilization of external api.
0 pts	/20 pts
Git Management	Excelled
Git utilized, branches used, pull requests merged, and branches cleared.
20 pts
Met Expectations
Git utilized, branches used for separate features
16 pts
Attempted
Git utilized, no branches used
8 pts
No Attempt
No git utilized.
0 pts	/20 pts
Testing	Excelled
Testing suite built for each feature created.
20 pts
Met Expectations
Thorough testing suit built.
16 pts
Attempted
Minimal testing suit built.
8 pts
No Attempt
No testing.
0 pts	/20 pts

