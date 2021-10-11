# Google Retail Search
## Python code samples
The code here demonstartes how to consume Google Retail Search API in Python

### Authorization
In order to authenticate and authorize the client place a JSON file with authorization token to your cloudshell project and refer environment variable `GOOGLE_APPLICATION_CREDENTIALS` to it (use full path to file):

```
export GOOGLE_APPLICATION_CREDENTIALS="/home/<use_name>/cloudshell_open/grs-samples-python/token.json"
```
### Setup your virtual environment
Use terminal to install Google packages with commannds:
```
pip install virtualenv
virtualenv <your-env>
source <your-env>/bin/activate
pip install google
pip install google-cloud-retail
```
### Run code samples
To run the chosen code sample open a terminal and execute command:
```
cd cloudshell_open/grs-samples-python
python search_with_boost_spec.py 
```
