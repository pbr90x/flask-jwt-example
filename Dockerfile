# this is an official Python runtime, used as the parent image
FROM python:3-slim

# set the working directory in the container to /app
WORKDIR /app

# build the Python environment
COPY requirements.txt /app
RUN pip install --no-cache-dir --requirement /app/requirements.txt

# add the app files to the container as /app
COPY app.py create_*.sh start.sh setup.sh /app/

# unblock port 443 for the Flask app to run on
EXPOSE 443

# create certs/keys and execute the Flask app
ENTRYPOINT ["/app/start.sh"]
