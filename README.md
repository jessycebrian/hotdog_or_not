# CLIP + FastAPI + Docker
Deployment of CLIP model  FastAPI + Docker


# Virtual Environment

Firt we need to create a virtual environment for the project, to keep track of every dependency, it is also useful to use and explicit version of Python

Install the package for creating a virtual environment:
`$ pip install virtualenv`

Create a new virtual environment
`$ virtualenv venv`

Activate virtual environment
`$ source venv/bin/activate`

# Python packages

Now with the virtual environment we can install the dependencies written in requirements.txt

`$ pip install -r requirements.txt`

# Train

After we have install all the dependencies we can now run the script in code/train.py, this script takes the input data and outputs a trained model and a pipeline for our web service.

`$ python code/train.py`

# Web application

Finally we can test our web application by running:

`$ uvicorn main:app`

# Docker

Now that we have our web application running, we can use the Dockerfile to create an image for running our web application inside a container

`$ docker build . -t sklearn_fastapi_docker`

And now we can test our application using Docker

`$ docker run -p 8000:8000 sklearn_fastapi_docker`

# Test!

Test by using the calls in tests/example_calls.txt from the terminal
