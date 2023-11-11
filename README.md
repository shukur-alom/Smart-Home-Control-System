# Smart Home Control System

This Django project controls the lights in a smart home using a Raspberry Pi. The project allows users to interact with the lights through a web interface.

## Installation

### Requirements

- Raspberry Pi with Raspbian OS
- Python 3.x
- Django
- RPi.GPIO library

### Setup

1. Clone the repository:

```
   https://github.com/shukur-alom/Home-automation-by-web-application-and-raspberry-pi.git
```

2. Install the required dependencies:
   
```
pip install -r requirements.txt
```

3.Connect the LEDs to the specified GPIO pins on your Raspberry Pi.


```
python manage.py runserver
```

4. Run the Django development server:

```
python manage.py runserver
```

4. Open your web browser and navigate to http://127.0.0.1:8000/ to access the Smart Home Control System.


# Features

* Turn individual lights on and off.

* Get status alerts based on the current state of the lights.
