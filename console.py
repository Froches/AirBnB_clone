import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exit on EOF(Ctrl-D)"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
