# https://docs.docker.com/engine/reference/builder/

# get nodejs
FROM node:8.17.0-alpine3.9

# Set the working directory to /app
# The WORKDIR instruction sets the working directory (inside the container) 
# for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that 
# follow it in the Dockerfile. 
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# npm install packages
RUN npm install

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run python app.py when the container launches
# This happens if no command is specified
CMD ["node", "server.js"]
