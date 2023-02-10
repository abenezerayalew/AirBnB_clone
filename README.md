# AirBnB_clone - The Console

## Description
The project is the initial phase in developing the AirBnB clone's whole web application. We are creating a console in this initial stage, a custom command interpreter that will be used in later AirBnB projects to handle the objects of our classes.

We'll be able to accomplish the following using this console:

✔️ Create a new object (ex: a new User or a new Place)
✔️ Retrieve an object from a file, a database etc…
✔️ Do operations on objects (count, compute stats, etc…)
✔️ Update attributes of an object
✔️ Destroy an object

## Usage
✔️ The console can be run in both:- 
* interactive mode
* non-interactive mode
✔️ It prints a prompt **(hbnb)** and waits for input from the user

### Interactive Mode

```cmd
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

### Non-Interactive Mode

```cmd
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
## Commands
