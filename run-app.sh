#! /bin/bash

# Script to run the application locally(for dev and test purpose)
cd app/ 

function run(){
    pip install -r requirements.txt && 
    export FLASK_APP=application.py && 
    flask run
}

echo "Note: Run the app in your own virtual environment(venv)!
      Example:  python3 -m venv heartbyte-venv
                source heartbyte/bin/activate"
if { python3 --version | grep -q "^Python[[:space:]]*[3]\.[[:digit:]]*[\.]*[[:digit:]]*$"; } then
    run;
else
    echo "Install Python 3!";
fi

