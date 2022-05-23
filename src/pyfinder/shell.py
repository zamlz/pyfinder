#!/usr/bin/env python3

import os
from cmd import Cmd
from loguru import logger

from pyfinder.kernel import PyfinderKernel
from pyfinder import static

if os.name == 'nt':
    clear_screen = lambda: os.system('cls')
else:
    clear_screen = lambda: os.system('clear')

class PyfinderShell(Cmd):
    prompt = static.PROMPT
    intro = static.BANNER

    def __init__(self):
        self.kernel = PyfinderKernel()
        super(PyfinderShell, self).__init__()

    def emptyline(self):
        pass

    def onecmd(self, line):
        try:
            return super(PyfinderShell, self).onecmd(line)
        except Exception:
            logger.exception("Exception caught!")

    def do_clear(self, args):
        """Clear the screen"""
        clear_screen()

    def do_exit(self, args):
        """Exit the Pyfinder Shell (Equivalent to Quit)"""
        print("quitting...")
        return True

    def do_quit(self, args):
        """Quit the Pyfinder Shell (Equivalent to Exit)"""
        return self.do_exit(args)

    def do_load(self, args):
        """Load a character from json file"""
        self.kernel.load_from_file(args)

    def do_save(self, args):
        """Save character to json file"""
        self.kernel.save_to_file(args)

    def do_view(self, args):
        """View character stats"""
        self.kernel.view(args.split())

    def do_dict_view(self, args):
        """View character stats in dictionary mode"""
        self.kernel.dict_view()

def start_shell():
    logger.info("Starting PyFinder")
    try:
        pf_shell = PyfinderShell()
    except Exception:
        logger.exception("Unable to setup pyfinder shell!")
        exit(1)
    pf_shell.cmdloop()
