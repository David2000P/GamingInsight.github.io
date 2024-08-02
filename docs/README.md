 # Projekt GamingInsight

## Steps to execute the app
Step 1: set up and activate a Python Virtual Environment. Gehen Sie rechts danach auf Code danach auf kopiere den Link vom Reposity dann öffnen Sie Visual Studio und gehen Sie auf Clone Git Reposity und fügen Sie den kopierten Link ein.

Step 2: install the required Python packages from the terminal with the command pip install -r requirements.txt:

(venv) C:\Users\me\projects\webapp> pip install -r requirements.txt
I created the file 📄requirements.txt with this command: pip freeze > requirements.txt

Step 3 (optional at tag location sqlalchemy): initialize the app's SQLite database via flask init-db:

(venv) PS C:\Users\me\projects\webapp> flask init-db
Database has been initialized.
Step 4: start the web server via flask run --reload:

(venv) PS C:\Users\me\projects\webapp> flask run --reload
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
Step 5: visit http://127.0.0.1:5000/insert/sample to populate the app's database with some sample data.

Step 6: visit http://127.0.0.1:5000/ to view the landing page
