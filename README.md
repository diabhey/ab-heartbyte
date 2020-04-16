# ab-heartbyte
Web Application using Flask framework.
- The web app is currently hosted on Microsoft Azure Cloud.
- Github -> Microsoft Azure Cloud CD(Continous Deployment) pipeline has been setup.
- Automated docker builds are setup using Github Actions
- Note: The web-app is only hosted on Azure during deployment tests.

## How to run the application the easy way

**Prerequisites**
- Docker

**Run**
- ```bash
  # At the moment, only the contributors can access the registry(private)
  # Pull the latest ab-heartbyte docker image
  docker pull heartbyte/ab-heartbyte
  # Run it
  docker run --rm -it  -p 5001:5001/tcp heartbyte/ab-heartbyte:latest
  ```    
- The flask app will be running on http://localhost:5001/

## For the folks who want to build the docker image

**Run**
- ```bash
  docker build -t ab-heartbyte:master flask/ && \
  docker run --rm -it -p 5001:5001/tcp ab-heartbyte:master 
  ```    
- The flask app will be running on http://localhost:5001/

## Contributing to ab-heartbyte
Refer to [CONTRIBUTING.md](CONTRIBUTING.md)

## Author
* bigillu (Abhimanyu Selvan) is the co-author and maintainer of this application.
  * follow me on [Twitter.](http://www.twitter.com/a_bigillu) 
* gandrein (Andrei Gherghescu) is the co-author.
