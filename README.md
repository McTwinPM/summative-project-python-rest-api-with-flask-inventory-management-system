# summative-project-python-rest-api-with-flask-inventory-management-system


Python Inventory CLI Tool




To setup, make sure the directory is wherever the "summative-project-python-rest-api-with-flask-inventory-management-system" folder is installed by cloneing the repository with

"git clone summative-project-python-rest-api-with-flask-inventory-management-system"


run "pip install -r requirements.txt" to install the necessary packages

CLI commands: 

First, start up the external API server with 

"python3 API/server.py"

presently, this will fetch info and from the OpenFoodFacts.org API, while also adding many random foods into the simulated inventory.

In another terminal, run:

'python3 Main.py'

This will tell the tool to activate the main function (remember to keep spaces between each command)

Here's an example command: "python3 main.py product list" This command will display a list of all products in the form of a table, along with itentifying information.

If you ever forget what command you need, you can use the "-h" or "--help" command to show you a list of commands in the directory. If you ever type a wrong command, read the error message that displays and start over.

For your third command (i.e. the third word) you will type one of several commands, depending on which function you need access to. 
1. list - list all products in the table
2. add - adds a product
3. remove - removes a product
4. update - updates a product
5. Search - searches for product

Product Management 

The product commands are as follows:

'add' (add a product) To add a product, you will need : Barcode, name, brand, ingredients, integer of stock

remove (remove a product) To remove a product, you will need to type the product ID given to the product when the product was added to the system

list (list all products) This will display all products in the inventory

update (update the status of a product) To update the status of a product: product_id, what you want to update (stock quantity, price, )


