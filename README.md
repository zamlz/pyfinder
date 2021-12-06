PyFinder
========
A simple shell for pathfinder

Install using setup.py
----------------------

The simplest way of installing this is to install the `requirements.txt` file
and then install the package itself. Note, this will install to your local
`site-packages` directory which I don't really recommend. It's much better to
setup a virtual environment of some sort. See the next section for using
`pipenv` instead!

```bash
$ pip install --user -r requirements.txt
```

```bash
$ pip instll --user .
```

Now to run the program,

```bash
$ pyfinder
```

Install using pipenv
--------------------

Best way to run this is to have `pipenv` installed. Install the python
package using your preferred method.

```bash
$ pip install --user pipenv
```

Now to run the shell, execute the following:

```bash
$  pipenv run pyfinder
```

This will install the pyfinder application in a virtual environment.
