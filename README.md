# Robots by Dev-LSV
This is a software that helps companies automatize the boring stuff

## index

- Requeriments 
   - Software versions
   - Initial structure
   - Enviroment
   - Persistent data
 - Colaborators
- Models

## Requirements
### Software versions
- python version 3.5
- django version 1.11
- django-rest-framework
- celery 4.2
### Environment
### Persistent data

## project strucutre
```
.
└── robotlsv_container
    ├── apps
    │   └── robotone
    ├── robotlsv
    ├── static
    │   ├── css
    │   ├── img
    │   └── js
    └── templates
        └── robotone

```

## current start process

**set up db**

```
python manage.py makemigrations
python manage.py migrations
python manage.py createsuperuser

```

**run the django app**


**add robot monitor on the admin** on http://localhost:8000/admin

**run celery:**
But make sure you dont clase the windows tha pops up.
```
celery worker -A robotlsv -l info
```

**Go to** http://localhost:8000/robot/1 to execut the robot initialization task.

## UMLs

insert uml here:

## Collaborators
- Pedro Castilla
- Jesus Lemus
- Daniel Nuñez
- Rafael p. Barboza

