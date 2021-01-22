# music-events
API for manage music events

## Prerequirements
Python(3.8), pip(latest)
# How to start
### locally
- Clone git repository:

```
git clone https://github.com/Tabaszczan/music-events.git
```
- In root directory run:

```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
To generate random objects run:

```
python manage.py setup_test_data
```

### with docker
Work In Progress
# TO-DO
- [ ] extract external API reponse to function and handle exceptions 
- [ ] write more tests and fix existing ones (parametrise)
- [ ] setup docker for postgis 
- [ ] change create event endpoint location to something more friendly (longitude, latitude)
- [ ] add some actions (tests, flake8)
- [ ] parametrise objects generator
- [ ] more info on README
- [ ] Documentation

#### If You find any bug, or something will not work contact me or make an issue
Time spent on a task: 16 hours
