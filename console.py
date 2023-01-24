#!/usr/bin/python3
""" Console.py that contains the entry point of the command interpreter: """

import cmd
from datetime import datetime
from models.base_model import BaseModel
from models.__init__ import storage
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

Class HBNBCommand(cmd.Cmd):
    """ Cmd Module """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exit program"""
        return True
   
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
	
	def emptyline(self):
        """ Overrides empty lines """
		pass
		
	def do_create(self, arg):
        """
         Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg in classes:
            new_obj = classes[arg]()
            storage.new(new_obj)
            storage.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")
			
	def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
       
        condition = args.partition(" ")
        required_name = condition[0]
        required_id = condition[2]

        if required_id and ' ' in required_id:
            required_id = required_id.partition(' ')[0]

        if not required_name:
            print("** class name missing **")
            return

        if required_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not required_id:
            print("** instance id missing **")
            return

        key = required_name + "." + required_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")
			
	def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
        condition = args.partition(" ")
        required_name = new[0]
        required_id = new[2]
        if required_id and ' ' in required_id:
            required_id = required_id.partition(' ')[0]

        if not required_name:
            print("** class name missing **")
            return

        if required_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not required_id:
            print("** instance id missing **")
            return

        key = required_name + "." + required_id

        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")
			
	def do_all(self, args):
        """ Prints all string representation of all instances based or not on the class name"""
			list = []

        if args:
            args = args.split(' ')[0] 
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for key, value in storage._FileStorage__objects.items():
                if key.split('.')[0] == args:
                    list.append(str(v))
        else:
            for key, value in storage._FileStorage__objects.items():
                list.append(str(v))

        print(list)
		
	def do_update(self, args):
        """  Updates an instance based on the class name and id  """
        required_name = required_id = attribute_name = attribute_value = kwargs = ''


        args = args.partition(" ")
        if args[0]:
            required_name = args[0]
        else:  # class name not present
            print("** class name missing **")
            return
        if required_name not in HBNBCommand.classes:  
            print("** class doesn't exist **")
            return

        
        args = args[2].partition(" ")
        if args[0]:
            required_id = args[0]
        else:  # id not present
            print("** instance id missing **")
            return

        # working  with key
        key = required_name + "." + required_id

        # if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        # if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = [] 
            for key, value in kwargs.items():
                args.append(key)
                args.append(value)
        else:  
            args = args[2]
            if args and args[0] is '\"':  
                second_quote = args.find('\"', 1)
                attrbute_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

           
            if not attribute_name and args[0] is not ' ':
                attribute_name = args[0]
            
            if args[2] and args[2][0] is '\"':
                attribute_val = args[2][1:args[2].find('\"', 1)]

            
            if not attribute_val and args[2]:
                attribute_val = args[2].partition(' ')[0]

            args = [attribute_name, attribute_val]

       
        current_dict = storage.all()[key]

        # iterate through attr names and values
        for i, att_name in enumerate(args):
            # block only runs on even iterations
            if (i % 2 == 0):
                attribute_val = args[i + 1]  
                if not attribute_name:  
                    print("** attribute name missing **")
                    return
                if not attribute_val: 
                    print("** value missing **")
                    return
                
                if attribute_name in HBNBCommand.types:
                    attribute_val = HBNBCommand.types[attribute_name](attribute_val)

                # update dictionary with name, value pair
                current_dict.__dict__.update({attribute_name: attribute_val})

        current_dict.save() 
		
		
if __name__ == "__main__":
    HBNBCommand().cmdloop()
