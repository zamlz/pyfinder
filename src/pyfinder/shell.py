#!/usr/bin/env python3

# TODO: Actually implement this
class CommandCompletion(object):
    pass


class PathfinderShell(object):

    def run(self):
        while True:

            user_input = input("PathFinder> ").split(' ')

            # its kinda guaranteed to have atleast one item
            user_cmd = user_input[0]
            user_args = [] if len(user_input) == 1 else user_input[1:]

            if user_cmd == '':
                continue
            elif user_cmd == 'quit' or user_cmd == 'exit':
                exit(0)
            else:
                print(f"command: {user_cmd}")
                print(f"command: {user_args}")


def start_shell():
    pf_shell = PathfinderShell()
    pf_shell.run()
