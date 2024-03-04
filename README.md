# 0x00-AirBnB_clone

<h1> Welcome to the AirBnB clone project </h1>

<h3><em>First step: The command console to manage AirBnB objects</em></h3>

<ul>

<li>Create a parent class <code>BaseModel</code> (abstract?) to take care of initialization, serialization and deserialization</li>

<li>Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file</li>

<li>Create all classes used for AirBnB (<code>User</code>, <code>State</code>, <code>City</code>, <code>Place</code>…) that inherit from BaseModel</li>

<li>Create the first abstracted storage engine of the project: File storage.</li>

<li>Create all unittests to validate all our classes and storage engine
</li>

</ul>

<h3>Execution</h3>

<p>Interactive mode:</p>

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit 

(hbnb)
(hbnb)
(hbnb) quit
$
```

<p>Non ineractive mode</p>

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb)
$
```

<p>All tests should also pass in non-interactive mode: <code>$  echo "python3 -m unittest discover tests" | bash</code> </p>
