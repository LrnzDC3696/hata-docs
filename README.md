# hata-docs

Documentation website for hata.

## Setting Up Instructions

### 1.setup the files

```bash
# Clone the repo
git clone https://github.com/m0nk3ybraindead/hata-docs.git

# cd to the project
cd hata-docs

# make .env file
touch .env

# setup your .env file ( you could use an editor to edit this file btw )
nano .env
```

#### sample layout of `.env` file

```python
DEVMODE='True'
```

### 2.setup virtual environment

```bash
# For installing the virtual environment
pip install pipenv

# Now setup pipenv (add --dev if you will be developing code)
pipenv install --dev

# Start the shell
pipenv shell

# Start the code
python run.py
```

you are not ready to edit the code!
