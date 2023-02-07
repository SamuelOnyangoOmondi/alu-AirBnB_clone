# AirBnB clone - The console
![airbnb](https://user-images.githubusercontent.com/106454335/215355859-58381dbc-f59b-4400-861e-e01428cec17a.png)

## Project Description:
This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

## Command Interpreter Description:
### Functions of the Command Interpreter:

Create a new object (ex: a new User or a new Place)

Retrieve an object from a file, a database etc…

Do operations on objects (count, compute stats, etc…)

Update attributes of an object

Destroy an object

### How to start the Command Interpreter:

To use this project:
Clone
https://github.com/yeungegs/AirBnB_clone.git
On your machine, navigate (cd) to the newly created directory
cd AirBnb_clone

### How to use the command Interpreter:

This console works in interactive mode:

$ ./console.py
(hbnb) help

####Documented commands:

EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
This console also works in non-interactive mode:

$ ./console.py
(hbnb) help

####Built-in commands

EOF: Quit the program.
quit: Quit the program.
all: Prints all string representation of all instances based.
all <class name>: Print all the string representation of all instances of one class.
help: list all the commands in this console.
help <command>: Provide the document of the command.
<class name> count: retrieve the number of instances of a class.
create <class name>: Creates a new instance of the class, saves it (to the JSON file) and prints the id.
destroy <class name> <id>: Deletes an instance based on the class name and id (save the change into the JSON file).
show <class name> <id>: Prints the string representation of an instance based on the class name and id.
update <class name> <id> <attribute name> "<attribute value>": Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
count <class name>: Retrieve the number of instances of a class
Our console also supports alternative methods to call the built-in commands:

<class name>.all(): Alternative for command 'all'
<class name>.count(): Alternative for command 'count'
<class name>.show(<id>): Alternative for command 'show'
<class name>.destroy(<id>): Alternative for command 'destroy'
<class name>.update(<id>, <attribute name>, <attribute value>): Alternative for command 'update'
<class name>.update(<id>, <dictionary representation>): update an instance based on his ID with a dictionary

### Examples of the Command Interpreter:

####Documented commands:

EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help create
Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id

(hbnb) create User 
(hbnb) destroy User 
(hbnb) show User 
** no instance found **
(hbnb) quit
