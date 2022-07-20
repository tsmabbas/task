# Python base image.
FROM python:3.10
# Create and set the work directory inside the image named 'task'
WORKDIR /task
ENV SECRET_KEY: $SECRET_KEY
ENV DATABASE_URI: $DATABASE_URI
# Execute a pip install command using the list 'requirements.txt'
RUN pip install Flask Flask_Login flask_sqlalchemy sqlalchemy.sql werkzeug.security
# Copy the app file into the image working directory
COPY . .
# State the listening port for the container. 
# The app's code does not actually specify the port, so it would be useful to include here.
EXPOSE 5000
# Run 'python app.py' on container start-up. This is the main process.
ENTRYPOINT ["python", "app.py"]