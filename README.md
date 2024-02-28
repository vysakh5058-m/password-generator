# Password Generator

**To run this application:**

`pip install -r requirements.txt`<br>
`python password-generator.py`

**To run this application in container:**

`docker build -t password-generator:v1 .`<br>
`docker run -d -p 8080:80 password-generator:v1 --name=password-generator`
