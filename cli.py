# from functions import get_todos , write_todos. Ideal for few functions, but non-ideal for many function and to type everything
from Functions import function
import time


time_now = time.strftime('%b %d  %H:%M')
print(time_now)

print('Hello There!')

while True:
    user_action = input('Add, Show, Edit, Complete or Exit: ')


    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        
        to_dos = function.get_todos()

        to_dos.append(todo)

        function.write_todos(to_dos)



    elif "show" in user_action:

        to_dos = function.get_todos() 

        if len(to_dos)==0:
            print('You have no To-Dos')
        
        new_todos = [item.strip('\n') for item in to_dos]
            
        for index, item in enumerate(new_todos):
            item = item.title()
            print(f"{index+1}.{item}")
    


    elif user_action.startswith('edit'):
        try:
            todo_no = int(user_action[5:]) -1

            to_dos = function.get_todos()

            edit_item = to_dos[todo_no].strip('\n')
            print(f'{todo_no+1}.{edit_item}')  

            new = input("What do you want to replace it with? ")
            
            to_dos = function.get_todos()
                
            to_dos[todo_no] = new + '\n'

            function.write_todos(to_dos)

            print("It's done")

        except ValueError:
            print('Command Not Valid')
            continue



    elif user_action.startswith('clear'):
        to_dos = function.get_todos()
        
        to_dos.clear()

        function.write_todos(to_dos)
        print('All cleared')    



    if user_action.startswith('complete'):  

        try:      
            to_do_replace_no = int(user_action[9:]) -1

            to_dos = function.get_todos()
            
            done_task = to_dos[to_do_replace_no].strip('\n')
            to_dos.pop(to_do_replace_no)

            function.write_todos(to_dos)
            
            print(f"{done_task} task is done")


        except IndexError:
            print("That item number doesn't exit")
            continue    


    elif "exit" in user_action:
        break
    
    #else:
    #  print('Command not valid')
    

print('Peace!')