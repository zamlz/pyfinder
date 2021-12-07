PyFinder 
========

A simple interactive shell for PathFinder Character Sheets

```
   ▄███████▄ ▄██   ▄      ▄████████  ▄█  ███▄▄▄▄   ████████▄     ▄████████    ▄████████
  ███    ███ ███   ██▄   ███    ███ ███  ███▀▀▀██▄ ███   ▀███   ███    ███   ███    ███
  ███    ███ ███▄▄▄███   ███    █▀  ███▌ ███   ███ ███    ███   ███    █▀    ███    ███
  ███    ███ ▀▀▀▀▀▀███  ▄███▄▄▄     ███▌ ███   ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀
▀█████████▀  ▄██   ███ ▀▀███▀▀▀     ███▌ ███   ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀
  ███        ███   ███   ███        ███  ███   ███ ███    ███   ███    █▄  ▀███████████
  ███        ███   ███   ███        ███  ███   ███ ███   ▄███   ███    ███   ███    ███
 ▄████▀       ▀█████▀    ███        █▀    ▀█   █▀  ████████▀    ██████████   ███    ███
                                                                             ███    ███
    VERSION: 0.0.1

Welcome! Type ? to list commands
(pyfinder) load examples/umbra.json
2021-12-06 19:29:35.492 | INFO     | pyfinder.character:load_from_file:23 - Loading character sheet from examples/umbra.json
2021-12-06 19:29:35.493 | INFO     | pyfinder.character:load_from_file:28 - Successfully loaded character sheet
(pyfinder) view ability_scores

ability_scores:
╒══════════════╤═════════╕
│ Label        │   Value │
╞══════════════╪═════════╡
│ strength     │      16 │
├──────────────┼─────────┤
│ dexterity    │      11 │
├──────────────┼─────────┤
│ constitution │      14 │
├──────────────┼─────────┤
│ intelligence │      14 │
├──────────────┼─────────┤
│ wisdom       │      10 │
├──────────────┼─────────┤
│ charisma     │       7 │
╘══════════════╧═════════╛

(pyfinder) _
```

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
