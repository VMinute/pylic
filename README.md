# pylic
This is a very simple Python script that can be used to download licenses of modules used in a Python project that uses pip and virtualenv.  
This is a simple script that can be used to generate a list of the licenses used by your application and download individual licenses for the packages you installed.  
Tested with python 3.7 (should work with all 3.x releases).  
  
Usage:  

```
python pylic.py <requirements_file> <env_path>  
```

- requirements_file is the path of requirements.txt for the project you want to analyze
- env_path is the path of the root folder of your virtual environment

When the script starts it will output something like this:

```
Processing packages in requirements.txt
Using environment .\env
processing altgraph
skipped, not in package list
processing asn1crypto
License downloaded.
processing astroid
skipped, not in package list
processing autopep8
skipped, not in package list
processing bcrypt
License downloaded.
processing certifi
processing cffi
processing chardet
License downloaded.
...
processing urllib3
processing websocket-client
License downloaded.
processing Werkzeug
processing wheel
skipped, not in package list
processing wrapt
skipped, not in package list
```

The script with create a subfolder in current dir named "licenses" and a file named licenses.txt with a list of licenses from individual packages information:

```
asn1crypto 0.24.0 MIT https://github.com/wbond/asn1crypto (license: https://raw.githubusercontent.com/wbond/asn1crypto/master/LICENSE)
bcrypt 3.1.4 Apache License, Version 2.0 https://github.com/pyca/bcrypt/ (license: https://raw.githubusercontent.com/pyca/bcrypt/master/LICENSE)
certifi 2018.8.24 MPL-2.0 http://certifi.io/
...
urllib3 1.24.1 MIT https://urllib3.readthedocs.io/
websocket-client 0.54.0 BSD https://github.com/websocket-client/websocket-client.git (license: https://raw.githubusercontent.com/websocket-client/websocket-client/master/LICENSE)
Werkzeug 0.14.1 BSD https://www.palletsprojects.org/p/werkzeug/
```
It will report license type (as described [here](https://www.python.org/dev/peps/pep-0314/#license)), the package homepage URL and the URL of the license file if it managed to download it correctly.  
Since pip packages don't have a field for a license URL the script will try to find a valid URL appending most common license names to the base URL (with some adjustments if the homepage is a github repo).  
Obviously this script is just meant to automate the work required to collect licenses and can't grant that the information provided is accurate.
