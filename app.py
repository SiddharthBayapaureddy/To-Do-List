from Functions import function
import FreeSimpleGUI as gui
import time
import os


if not os.path.exists('todos.txt'):
    with open('todos.txt' , 'w') as file:
        pass

gui.theme('Black')

clock = gui.Text('' , key='time')
label = gui.Text('Type in a To-Do: ')

input_box = gui.InputText(tooltip='Enter a To-Do: ' , key='input')

add_button = gui.Button("Add")

list_box = gui.Listbox(values=function.get_todos() , key='todos' ,
                         enable_events=True , size = [35,10])

edit_button = gui.Button('Edit')
complete_button = gui.Button('Complete')
clear_button = gui.Button('Clear')
exit_button = gui.Button('Exit')
layout = [ [clock] , [label ], [input_box, add_button] , [list_box , edit_button , complete_button] , [exit_button , clear_button]]

window = gui.Window('My To-Do App' , 
                    layout= layout,
                    font=('SF Pro' , 15) , 
                    )
while True:
    event , value = window.read(timeout=1000)
    if event is None:
        break
    window['time'].update(time.strftime('%b %d %Y %H:%M:%S'))
    #try:
        #print(event)
        #print(value)
        #print(value['todos'])

    #except TypeError:
       # break



    match event:

        case "Add":
            to_dos = function.get_todos()
            new_todo = value['input'] + '\n'

            if new_todo.strip() != '':
                to_dos.append(new_todo)
            function.write_todos(to_dos)
            window['todos'].update(values=to_dos)
            window['input'].update(value='')

            
        

        case 'Edit':
            try:
                todo_to_edit = value['todos'][0].strip()
                new_todo = value['input'].strip()
                to_dos = function.get_todos()
                index = to_dos.index(todo_to_edit + '\n')
                to_dos[index] = new_todo + '\n'
                function.write_todos(to_dos)
                window['todos'].update(values=to_dos)
                window['input'].update(value='')

            except IndexError:
                gui.popup('Please Select a To-Do' , font=('SF Pro' , 15))


        case 'Complete':
            try:
                cpltd_todo = value['todos'][0]
                to_dos = function.get_todos()
                to_dos.remove(cpltd_todo)
                function.write_todos(to_dos)
                window['todos'].update(values=to_dos)
                window['input'].update(value='')

            except IndexError:
                gui.popup('Select a To-Do first.' , font=('SF Pro' , 15))

                
        case "Clear":
            to_dos = function.get_todos()
            to_dos.clear()
            function.write_todos(to_dos)
            window['todos'].update(values=to_dos)
            window['input'].update(value='')

        case 'Exit':
            break

        case "todos":
            try:
                window['input'].update(value=value['todos'][0].strip())

            except IndexError:
                window['input'].update(value='')

            

        case gui.WIN_CLOSED:
            break

window.close()
