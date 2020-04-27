# ab-heartbyte
![ab-heartbyte docker build](https://github.com/bigillu/ab-heartbyte/workflows/ab-heartbyte%20docker%20build/badge.svg?branch=master&event=push)

Web Application using Flask framework.
- The web app is currently hosted on Microsoft Azure Cloud.
- Automated docker builds are setup using Github Actions
- Note: The web-app is only hosted on Azure during deployment tests.

## How to run the application the easy way

**Prerequisites**
- Docker

**Run**
- ```bash
  # Pull the latest ab-heartbyte docker image
  docker pull heartbyte/ab-heartbyte
  # Run it
  docker run --rm -it -p 80:80/tcp heartbyte/ab-heartbyte:latest
  ```    
- The flask app will be running on http://localhost:80/

## For the folks who want to build the docker image themselves

**Run**
- ```bash
  docker build -t ab-heartbyte:master flask/ && \
  docker run --rm -it -p 80:80/tcp ab-heartbyte:master 
  ```    
- The flask app will be running on http://localhost:80/

## Contributing to ab-heartbyte
Refer to [CONTRIBUTING.md](CONTRIBUTING.md)

## Author
* bigillu (Abhimanyu Selvan) is the co-author and maintainer of this application.
  * follow me on [Twitter.](http://www.twitter.com/a_bigillu) 
* gandrein (Andrei Gherghescu) is the co-author.
