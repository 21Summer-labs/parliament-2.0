## Parliament 2.0 web

To run the application:

Install the required packages: 
```pip install flask flask-sqlalchemy```\

Initialize the database by running 
```python init_db.py```

Start the Flask development server by running 
```python app.py```

Open a web browser and go to http://127.0.0.1:5000/ to see the Parliament 2.0 application

This implementation provides a basic structure for the Parliament 2.0 application, including:

A bills page where users can view and add bills, and navigate to a voting page
A causes page where users can view, add, and edit causes
A discussions page where users can view, create, update, and like discussions
A communities page that displays the 47 counties of Kenya

The application uses Flask for the backend, SQLite for the database, and Bootstrap for the frontend styling. The data is separated from the code using SQLAlchemy models, and the routes are organized into separate files for better maintainability.
Remember that this is a basic implementation and would need further development for a production-ready application, including user authentication, more robust error handling, and additional features as specified in the original requirements.
