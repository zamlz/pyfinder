#!/usr/bin/env python3

class CommandCompletion(object):
    pass


class PathfinderShell(object):

    def run(self):
        while True:
            x = raw_input("PF> ")
            print(x)


def start_shell():
    pf_shell = PathfinderShell()
    pf_shell.run()
