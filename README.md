# ab-heartbyte
Web Application using Flask framework.
- The web app is currently hosted on Microsoft Azure Cloud.
- Github -> Microsoft Azure Cloud CD(Continous Deployment) pipeline has been setup.
- Note: The web-app is only hosted on Azure during deployment tests.

## How to run locally(on Linux)

**Prerequisites**
- Python 3.6 or higher

**Run**
- ```bash
  # Set up your venv
  python3 -m venv hb
  source hb/bin/activate
  ```    
- ```bash
  ./flask/scripts/run-app.sh
  ```
- The flask app will be running on http://localhost:5000/

## How to run the app on Docker(Windows, Linux)

**Prerequisites**
- Docker 

**Run**
- ```bash
  docker build -t ab-heartbyte:master flask/ && \
  docker run --rm -it -p 5001:5001/tcp ab-heartbyte:master 
  ```    
- The flask app will be running on http://localhost:5001/

## Author
* bigillu (Abhimanyu Selvan) is the co-author and maintainer of this application.
  * follow me on [Twitter.](http://www.twitter.com/a_bigillu) 
* gandrein (Andrei Gherghescu) is the co-author.
