#!/usr/bin/env python3

from loguru import logger

from pyfinder.character import Character

# TODO: Actually implement this
class CommandCompletion(object):
    pass

class PathfinderShell(object):

    def __init__(self):
        # TODO: Add logic to make this not hardcoded
        self.character = Character()

    def run(self):
        while True:

            user_input = input("PathFinder> ").split(' ')

            # its kinda guaranteed to have atleast one item
            user_cmd = user_input[0]
            user_args = [] if len(user_input) == 1 else user_input[1:]

            if user_cmd == '':
                continue

            try:
                logger.debug(f"Got command: {user_cmd} {user_args}")

                if user_cmd == 'quit' or user_cmd == 'exit':
                    logger.info("Quitting Pathfinder Shell")
                    exit(0)

                # Character Sheet Operations
                elif user_cmd == 'load':
                    self.character = Character.load_from_file(*user_args)

                elif user_cmd == 'save':
                    Character.save_to_file(self.character, *user_args)

                elif user_cmd == 'view':
                    self.character.view()

                # Final catchall
                else:
                    logger.error(f"Unkown Command: {user_cmd} {user_args}")
            except Exception:
                logger.exception("Unkown Exception Caught")

def start_shell():
    logger.info("Starting PyFinder")
    try:
        pf_shell = PathfinderShell()
    except Exception:
        logger.exception("Unable to setup pyfinder shell!")
        exit(1)
    pf_shell.run()
