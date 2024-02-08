# Is your picture a hotdog?
APP that detects if a picture uploaded is a hotdog or not.
Streamlit + OPEN AI's CLIP.

## Virtual Environment

First we need to create a virtual environment for the project, to keep track of every dependency, it is also useful to use and explicit version of Python

Install the package for creating a virtual environment:
`$ pip install virtualenv`

Create a new virtual environment
`$ virtualenv venv`

Activate virtual environment
`$ source venv/bin/activate`

## Python packages

Now with the virtual environment we can install the dependencies written in requirements.txt

`$ pip install -r requirements.txt`


## Run Streamlit app

`$ streamlit run hotdog_app.py`
and upload a picture to get a prediction.

