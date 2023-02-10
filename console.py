#!/usr/bin/python3
"""
Console.py that contains the entry point of the command interpreter
"""
import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review}

class HBNBCommand(cmd.Cmd):
    """
    handles objects
    """

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """exit the program 
        """
        print()
        return True

    def do_quit(self, arg):
        """quit command to exit the program
        """
        return True

    def emptyline(self):
        """  """
        return False

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id
        """
        args = arg.split()
        if len(args) == 0 or arg is None:
            print("** class name missing **")
        else:
            if len(args) == 1 and args[0] in self.classes:
                new_instance = self.classes.get(args[0])()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance 
        based on the class name and id
        """
   
        args = arg.split()
        instances = storage.all()

        if len(args) < 2:

            if len(args) == 0:
             print("** class name missing **")

        else:
            print("** instance id missing **")
        return

        if args[0] not in classes:

            print("** class doesn't exist **")
            return

        record  = "{}.{}".format(args[0], args[1])

        if record in instances:
            print(instances[record])

        else:
            print("** no instance found **")




    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id 
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1 and args[0] in self.classes:
            print("** instance id missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            instance_id = "{}.{}".format(args[0], args[1])
            try:
                del(instances[instance_id])
                storage.save()
            except:
                print("** no instance found **")

    def do_all(self, arg=""):
        """
        Prints all string representation of all instances
        based or not on the class name
        """

        instances = storage.all()
        
        if not arg:
            for instances in instances.values():
                print(str(instances))
        
        elif arg not in classes:
            print("**class doesn't exits**")

        else:
            for key, instances in instances.instancess():

                if key.split('.')[0] == arg:
                    print(str(instances))
       
def do_update(self, arg):
        """
       Updates an instance based on the class name and id  
        """
        args = arg.split()
        instance_check = False
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            for key, value in instances.instancess():
                print("This is the key {}".format(key))
                if args[3][0] == "" and args[3][-1] == "":
                    args[3] = args[3][1:-1]
                instance_id = "{0}.{1}".format(args[0], args[1])
                if key == instance_id:
                    setattr(value, args[2], args[3])
                    storage.save()
                    instance_check = True
        if instance_check is False:
            print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()