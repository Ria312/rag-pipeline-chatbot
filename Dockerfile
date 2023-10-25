# Use the official Python image as the base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the poetry files
COPY pyproject.toml poetry.lock /app/
RUN ls
# Install poetry
RUN pip install poetry

# Install project dependencies
RUN poetry lock
RUN poetry install

# Copy the .env file
COPY .env .env

# Copy the rest of the application code
COPY . .

# RUN poetry add chainlit
# # Extract data for app
# RUN poetry run ploomber build

# Expose the port that the app runs on
EXPOSE 80

COPY chainlit.md chainlit.md

# Execute the script when the container starts
# CMD ["poetry", "run", "uvicorn", "hack-chat.src.app:app", "--host", "0.0.0.0", "--port", "8000"]
#ENTRYPOINT ["chainlit", "run", "app.py", "--host=0.0.0.0", "--port=80", "--headless"]
CMD ["poetry", "run", "chainlit", "run", "app.py", "--port", "80"]



