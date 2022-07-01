# Description

Dashboard Project


## Installation

#### Virtual Environment

##### Create Virtual Enviroment

```command line
python -m venv .[name of enviroment]
```

##### Activate Virtual Enviroment

```command line
.[name of enviroment]\Scripts\activate
```

#### Install Libraries

```command line
python install -r requirements.txt
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

## Observartions

When running the server in the `app.py`, please run it with host 0.0.0.0

```python
if __name__ == '__main__':
    server.run(host="0.0.0.0")
```