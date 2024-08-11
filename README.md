# Project Startup Instructions

This document contains instructions on how to start a project using Docker. Before you start, make sure you have the following tools installed: [Docker](https://www.docker.com/) version 20.10.0 or higher.

### Steps to start a project

1. Clone the repository with the project to your local machine using the command:
   `git clone https://github.com/DIprooger/gRPC-enabled-microservices-.git`.
   Navigate to the project directory:
   `cd mydockerproject`.

2. Build the Docker image using the following command. Replace `mydockerproject` with the name of your image:
   `docker build -t mydockerproject .`

3. Run the Docker container using the following command:
   `docker run -d mydockerproject`.
   This command starts the container in the background. 

### Testing

Tests are run with the command:
   ` python3 -m unittest test.py`.
To run tests for user, go to services/user; for order, go to services/order.

### Usage

After starting the container you can access the microservice with already written clients, to run the client you need to start it with the command:
   `python3 client.py`.
   The console will output the result of the microservices.

### Licence

This project is distributed under the MIT Licence. Details can be found in the [LICENSE](LICENSE) file.
