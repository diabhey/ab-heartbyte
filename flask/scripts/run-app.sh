#! /bin/bash

sourceDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
appDir="/.."

function run(){
    pip install -r "${sourceDir}${appDir}"/requirements.txt &&
    export FLASK_APP="${sourceDir}${appDir}"/application.py &&
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

