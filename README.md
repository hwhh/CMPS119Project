# CMPS119Project
Sunworks website - Django
https://github.com/ocastroa/grepthink/blob/master/docs/contribute.md

# Setting up a development environment to contribute

## Step 1: Python Virtual Enviornment

Create a new virtual environment (this will create a new folder with python installed and later django/dependencies)
```bash
$ virtualenv twdev
```
Note: you don't have to call your folder/venv "twdev"

Now cd into twdev (or whatever you named your venv) and activate it
```bash
$ source bin/activate
```

You can always exit the venv with `deactivate`

## Step 2: Cloning the Repo
Clone the project repo. Clone it into the virtual environment folder you just created. 

## Step 3: Make a .env file based on .env.example. Copy the example and change only your URL path
The .env file should be in the twdev (or whatever you named your virtual environment) folder. So above the project folder.

This is so we can keep the secret key hidden. 

It also allows us to use sqlite locally and postgres in production, neat.

You might need to install postgres to be able to start the server.

## Step 4: Install dependencies
Run the requirements.txt script located in the cloned repo.
```bash
$sudo pip install -r requirements.txt
```

## Step 5: Migrate 
`python  manage.py migrate`


## Step 6: Start the server
`python  manage.py runserver`
