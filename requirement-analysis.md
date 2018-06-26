# Analysis of requirements

## Django models
- User
- Robot

## Robot model
**Robot class**
contructor method():
	`started` and `status ` are initialized
**Attributes**
started = datetime()
finished = datetime()
status = String
reponse = JSON

## derived class (Child class)

### robot_1
**Methods:**
process(*inputs):
    The status changes at start
    Whend finished, calls `reponse` attribute sending the procressed
respond(Results)L:
    Change status from the sender (Error or finished)
    Stablish execute time(Finished)
    set response

### robot_2
### robot_3
