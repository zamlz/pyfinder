#!/usr/bin/env python3

from cmd import Cmd
from loguru import logger

from pyfinder.character import Character
from pyfinder import static

class PyfinderShell(Cmd):
    prompt = static.PROMPT
    intro = static.BANNER

    def __init__(self):
        self._character = Character()
        super(PyfinderShell, self).__init__()

    def emptyline(self):
        pass

    def onecmd(self, line):
        try:
            return super(PyfinderShell, self).onecmd(line)
        except Exception:
            logger.exception("Exception caught!")

    def do_exit(self, args):
        """Exit the Pyfinder Shell (Equivalent to Quit)"""
        print("quitting...")
        return True

    def do_quit(self, args):
        """Quit the Pyfinder Shell (Equivalent to Exit)"""
        return self.do_exit(args)

    def do_load(self, args):
        """Load a character from json file"""
        self._character = Character.load_from_file(args)

    def do_save(self, args):
        """Save character to json file"""
        Character.save_to_file(self._character, args)

    def do_view(self, args):
        """View character stats"""
        self._character.view(args.split())

    def do_dict_view(self, args):
        """View character stats in dictionary mode"""
        self._character.dict_view()

def start_shell():
    logger.info("Starting PyFinder")
    try:
        pf_shell = PyfinderShell()
    except Exception:
        logger.exception("Unable to setup pyfinder shell!")
        exit(1)
    pf_shell.cmdloop()
