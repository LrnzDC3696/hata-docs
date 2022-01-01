import os

from src import app
from dotenv import load_dotenv


load_dotenv()

# We access the variable directly to remind the user to setup .env if forgotten
IS_DEV_MODE = os.environ['DEVMODE'] == 'True'

if __name__ == '__main__':
    app.run(debug=True)
