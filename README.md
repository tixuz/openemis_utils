# Openemis Selenium
## How To Install Requered Libraries

Run
```
pip -r requerements.txt
```

## How To Run Selenium

1. Please write necessary information into config.py

2. If the "chromedriver" file in this folder is incompatible with your version of Chrome, download the compatible version and change path to it in config.py

3. Run open_core_chrome.py

## How To Get API Bearer token

4. Create key pair
```
ssh-keygen -t rsa -b 4096 -m PEM -f jwtRS256.key
# Don't add passphrase
openssl rsa -in jwtRS256.key -pubout -outform PEM -out jwtRS256.key.pub
cat jwtRS256.key
cat jwtRS256.key.pub
```

5.
    a) Create new Credentials in OpenEMIS Core;
    b) copy all from jwtRS256.key.pub to Public Key field
    c) Copy Client Id from Credentials and paste it to config.py iss variable value

### Example

```
iss = "1661365366-d6277c12d6e9f67a.app"
```

7. run get_core_assertion.py

8. you can try if the assertion works, using postman or running get_institutions_via_api.py

## Examples of API requests to OpenEMIS Core
```
//curl -i -X GET http://localhost/school/api/restful/v2/Users.json
//curl -i -X GET http://localhost/school/api/restful/v2/Users.json?_contain=Genders
//curl -i -X GET http://localhost/school/api/restful/v2/Users.json?_fields=username,Genders.name&_contain=Genders
//curl -i -X GET http://localhost/school/api/restful/v2/Users.json?_order=-first_name,last_name
//curl -i -X GET http://localhost/school/api/restful/v2/Users.json?_limit=10&_page=2
```
