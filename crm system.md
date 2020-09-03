# **Simple CRM project with login page**

My task was create the request form which keeps the customers problems for their further treatment.

This app has a login system with request form that sending emails to customers  and saving all requests in dedicated table. This table can update requests data or delete them. The app also has a search bar, so we can find the specific data about customers complaints/requests.

My app using the Flask app factory pattern with blueprints. It has one blueprint that handles everything auth related, and another for regular routes, which include the index and the protected profile page. 

There are main packages that I used for this project:

- Flask
- Flask-Login: to handle the user sessions after authentication
- Flask-SQLAlchemy: to represent the user model and interface with  database
- Flask-Mail: to send email messages
- Flask-WTF: to provide an alternative way of designing forms

I used SQLite to avoid having to install any extra dependencies for the database.

The problem I faced was how I can send the request form and display it on another route. For it solving I needded to build the right connections between database, forms, models and configurations.







