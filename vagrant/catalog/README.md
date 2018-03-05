# Item catalog project

An example web application to practice the CRUD pattern.
It displays a fictional catalog of products and allows the following actions:

* adding new products
* editing existing items
* deleting existing items

Adding, editing and deleting is only permitted when the user has been logged in.

Log in is possible with a Google account.

Furthermore it offers two endpoints to retrieve the product data in JSON format:

* Single product: [http://localhost:5000/api/v1/product/1](http://localhost:5000/api/v1/product/1) (where 1 is the product id)
* All products: [http://localhost:5000/api/v1/products](http://localhost:5000/api/v1/products)

## Database setup

* Bring up the Vagrant-based virtual machine by running
    
        cd vagrant
        vagrant up
        
* SSH into the virtual machine

        vagrant ssh
        
* Run the database setup script and import example data

        cd /vagrant/catalog
        python database_setup.py
        python addExampleData.py
        
## Run the server

    python flaskServer.py
    
You can now access the web application at [http://localhost:5000](http://localhost:5000) 
