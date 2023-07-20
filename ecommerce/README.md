
# Features
* User Registration and Authentication: 
    * Implement user registration functionality.
    * Allow users to log in and log out.
    * Allows guest viewing 
    * Use Django's built-in authentication system.

* Product Management:
    * Allow administrators to add, edit, and delete products.
    * Include features like product images, descriptions, category, and prices.
    * Full featured shopping cart

* Quotation Form:
    * Enable users to add products to their quotation form.
    * Allow users to update and remove items from the quotation form.
    * Implement a “checkout” process (with checkout details of the customer).
    * Updates the cart item number icon wherever you are in the website.

* Quotation Management:
    * Enable administrators to view and manage orders.
    * User profile with orders
    * Allow users to view their quotations history.
    * Implement features like quotation updates and notifications.

# Download & Setup Instructions
* 1 - Clone project: git clone https://github.com/reddigetsetgo/ITMGT-25.05-.git
* 2 - cd ecommerce
* 3 - Create virtual environment: virtualenv myenv
* 4 - myenv\scripts\activate
* 5 - pip install -r requirements.txt
* 6 - python manage.py runserver

# Admin Login
* 1 - cd ecommerce
* 2 - python3 manage.py createsuperuser
* 3 - fill out the needed credentials (Username, Email Address, Password)
* 4 - You can log in to your admin dashboard by adding “admin” to your link. 
* 5 - (http://127.0.0.1:8000/admin).
