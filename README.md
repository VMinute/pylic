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
processing click
processing clickclick
License downloaded.
processing colorama
skipped, not in package list
processing connexion
License downloaded.
processing cryptography
License downloaded.
processing docker
License downloaded.
processing docker-pycreds
License downloaded.
processing Flask
processing future
skipped, not in package list
processing idna
processing inflection
License downloaded.
processing isort
skipped, not in package list
processing itsdangerous
processing Jinja2
processing jsonschema
processing lazy-object-proxy
skipped, not in package list
processing macholib
skipped, not in package list
processing MarkupSafe
processing mccabe
skipped, not in package list
processing openapi-spec-validator
License downloaded.
processing paramiko
License downloaded.
processing pbr
skipped, not in package list
processing pefile
skipped, not in package list
processing pep8
skipped, not in package list
processing pip
skipped, not in package list
processing pipdeptree
skipped, not in package list
processing pyasn1
processing pycodestyle
skipped, not in package list
processing pycparser
License downloaded.
processing PyInstaller
skipped, not in package list
processing pylint
skipped, not in package list
processing PyNaCl
License downloaded.
processing pyOpenSSL
skipped, not in package list
processing pypiwin32
processing pyserial
License downloaded.
processing python-dateutil
processing pywin32
processing pywin32-ctypes
License downloaded.
processing PyYAML
processing requests
processing requirements-parser
skipped, not in package list
processing setuptools
skipped, not in package list
processing six
processing sshtunnel
License downloaded.
processing swagger-spec-validator
License downloaded.
processing swagger-ui-bundle
License downloaded.
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
cffi 1.11.5 MIT http://cffi.readthedocs.org
chardet 3.0.4 LGPL https://github.com/chardet/chardet (license: https://raw.githubusercontent.com/chardet/chardet/master/LICENSE)
click 6.7 UNKNOWN http://github.com/mitsuhiko/click
clickclick 1.2.2 Apache License 2.0 https://github.com/zalando/python-clickclick (license: https://raw.githubusercontent.com/zalando/python-clickclick/master/LICENSE)
connexion 2.0.1 Apache License Version 2.0 https://github.com/zalando/connexion (license: https://raw.githubusercontent.com/zalando/connexion/master/LICENSE.txt)
cryptography 2.3.1 BSD or Apache License, Version 2.0 https://github.com/pyca/cryptography (license: https://raw.githubusercontent.com/pyca/cryptography/master/LICENSE)
docker 3.5.1 Apache License 2.0 https://github.com/docker/docker-py (license: https://raw.githubusercontent.com/docker/docker-py/master/LICENSE)
docker-pycreds 0.3.0 Apache License 2.0 https://github.com/shin-/dockerpy-creds (license: https://raw.githubusercontent.com/shin-/dockerpy-creds/master/LICENSE)
Flask 1.0.2 BSD https://www.palletsprojects.com/p/flask/
idna 2.7 BSD-like https://github.com/kjd/idna
inflection 0.3.1 MIT http://github.com/jpvanhal/inflection (license: http://raw.githubusercontent.com/jpvanhal/inflection/master/LICENSE)
itsdangerous 0.24 UNKNOWN http://github.com/mitsuhiko/itsdangerous
Jinja2 2.10 BSD http://jinja.pocoo.org/
jsonschema 2.6.0 MIT http://github.com/Julian/jsonschema
MarkupSafe 1.0 BSD http://github.com/pallets/markupsafe
openapi-spec-validator 0.2.4 Apache License, Version 2.0 https://github.com/p1c2u/openapi-spec-validator (license: https://raw.githubusercontent.com/p1c2u/openapi-spec-validator/master/LICENSE)
paramiko 2.4.2 LGPL https://github.com/paramiko/paramiko/ (license: https://raw.githubusercontent.com/paramiko/paramiko/master/LICENSE)
pyasn1 0.4.4 BSD https://github.com/etingof/pyasn1
pycparser 2.18 BSD https://github.com/eliben/pycparser (license: https://raw.githubusercontent.com/eliben/pycparser/master/LICENSE)
PyNaCl 1.2.1 Apache License 2.0 https://github.com/pyca/pynacl/ (license: https://raw.githubusercontent.com/pyca/pynacl/master/LICENSE)
pypiwin32 223 UNKNOWN UNKNOWN
pyserial 3.4 BSD https://github.com/pyserial/pyserial (license: https://raw.githubusercontent.com/pyserial/pyserial/master/LICENSE.txt)
python-dateutil 2.7.5 Dual License https://dateutil.readthedocs.io
pywin32 223 PSF https://github.com/mhammond/pywin32
pywin32-ctypes 0.2.0 BSD https://github.com/enthought/pywin32-ctypes (license: https://raw.githubusercontent.com/enthought/pywin32-ctypes/master/LICENSE.txt)
PyYAML 3.13 MIT http://pyyaml.org/wiki/PyYAML
requests 2.20.1 Apache 2.0 http://python-requests.org
six 1.11.0 MIT http://pypi.python.org/pypi/six/
sshtunnel 0.1.4 MIT https://github.com/pahaz/sshtunnel (license: https://raw.githubusercontent.com/pahaz/sshtunnel/master/LICENSE)
swagger-spec-validator 2.4.1 Apache License, Version 2.0 http://github.com/Yelp/swagger_spec_validator (license: http://raw.githubusercontent.com/Yelp/swagger_spec_validator/master/LICENSE.txt)
swagger-ui-bundle 0.0.2 Apache License Version 2.0 https://github.com/dtkav/swagger_ui_bundle (license: https://raw.githubusercontent.com/dtkav/swagger_ui_bundle/master/LICENSE)
urllib3 1.24.1 MIT https://urllib3.readthedocs.io/
websocket-client 0.54.0 BSD https://github.com/websocket-client/websocket-client.git (license: https://raw.githubusercontent.com/websocket-client/websocket-client/master/LICENSE)
Werkzeug 0.14.1 BSD https://www.palletsprojects.org/p/werkzeug/
```
It will report license type (as described [here](https://www.python.org/dev/peps/pep-0314/#license)), the package homepage URL and the URL of the license file.  
Since pip packages don't have a field for a license URL the script will try to find a valid URL appending most common license names to the base URL (with some adjustments if the homepage is a github repo).  
Obviously this script is just meant to automate the work required to collect licenses and can't grant that the information provided is accurate.
