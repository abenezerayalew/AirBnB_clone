
## Description
The project is the initial phase in developing the AirBnB clone's whole web application. We are creating a console in this initial stage, a custom command interpreter that will be used in later AirBnB projects to handle the objects of our classes.

We'll be able to accomplish the following using this console:

  create a Python package
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

Command | Description
--- | ---
`quit` | Exits the program
`EOF` | Exits the program
`create <class>` | Creates an instance of a class
`show <class> <id>` | Prints the string representation of an instance of a class based on class name and id
`destroy <class> <id>` | Deletes instance of a class based on class name and id
`all` | Prints all string representations of all instances
`all <class>` | Prints all string representations of all instances based on class name
`update <class> <id> <attribute name> "<attribute value>"` | Updates an attribute of an instance based on class name and id
`<class>.all()` | Retrieves all instances of a class
`<class>.count()` | Retrieves the number of instances of a class
`<class>.show(<id>)` | Retrieves an instance based on its id
`<class>.destroy(<id>)` | Destroys an instance based on its id

---
