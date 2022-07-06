# Description

Dashboard Project


## Installation

#### Virtual Environment

##### Create Virtual Enviroment
```command line
python -m venv .env
```

##### Activate Virtual Enviroment
```command line
.env\Scripts\activate
```

#### Install Libraries
```command line
pip install -r requirements.txt
```
##### Whenever you need to update requirements.txt
```command line
pip freeze > requirements.txt
```

## Use

Run Application
```command line
flask run
```

#### Azure deployment
Make sure you have variable app running with port '0.0.0.0' in your `app.py` file

```python
server.run(host="0.0.0.0") 
```