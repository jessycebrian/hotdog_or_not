# Is your picture a hotdog?
APP that detects if a picture uploaded is a hotdog or not.
Streamlit + OPEN AI's CLIP.


## Virtual Environment

Firt we need to create a virtual environment for the project, to keep track of every dependency, it is also useful to use and explicit version of Python

Install the package for creating a virtual environment:
`$ pip install virtualenv`

Create a new virtual environment
`$ virtualenv venv`

Activate virtual environment
`$ source venv/bin/activate`

## Python packages

Now with the virtual environment we can install the dependencies written in requirements.txt

`$ pip install -r requirements.txt`


## Web application

Finally we can test our web application by running:

`$ uvicorn main:app`

## Docker

Now that we have our web application running, we can use the Dockerfile to create an image for running our web application inside a container

`$ docker build . -t hotdog_or_not`

And now we can test our application using Docker

`$ docker run -p 8000:8000 hotdog_or_not`

## Test!

Test by using the calls in tests/example_calls.txt from the terminal

or run in terminal
`$ cd tests`
`$ python image_request.py`

## Run Streamlit app

`$ streamlit run hotdog_app.py`
and upload a picture to get a prediction.


## Evaluate clip model

### Download images 
To download images for testing there is a python script that allows us to search for a query and obtain images. It can be used from the terminal. 

`$ python get_test_images.py --query "{}" --max_images {}`

### Run evaluation 

`$ python clip_hotdog_evaluation.py`
