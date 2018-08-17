# SWAPI Container Image

This repo contains the source for the SWAPI docker container, and creates a private API to request information.
To build this container, please follow the instructions below.

NOTE: Main Dockerfile uses CentOS, and image ends up being over 600MB. Use the Alpine Linux Dockerfile if you wish to install the bare minimum, resulting in a ~100MB docker image.

Use
---
Once the docker container is running, it will act as an API endpoint.
Try hitting the following URL's once your container is running
- `http://127.0.0.1/ship-people`
- `http://127.0.0.1/films`

Installation Instructions
---

* Clone repository and cd into directory.
  `git clone https://github.com/DivvyPayHQ/devops-danielrich.git`
* Use Dockerfile to build docker image.
  `docker build . --tag swapi_docker`
* Create and run the docker container.
  `docker run --name swapi -p 80:80 swapi_docker`

CONGRADULATIONS! Your docker container is now installed and running on localhost, port 80.
If you wish to change the port, simply change the external port in the docker run command.
- Example:`-p 8005:80`
Try it out in your web browser by going to `http://127.0.0.1/ship-people`

Additional Info
---
The web server is running using chalice, who's primary use is deploying scripts to AWS Lambda's and invoking them through API Gateway's.
web server can also be spun up locally, which is what is done in this docker image.
Chalice: https://github.com/aws/chalice
