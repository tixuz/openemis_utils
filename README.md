# Openemis Selenium
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
5. Create new Credentials in OpenEMIS Core, copy all from jwtRS256.key.pub to Public Key field
6. Copy Client Id to config.py client_id
7. run get_bearer_token.py