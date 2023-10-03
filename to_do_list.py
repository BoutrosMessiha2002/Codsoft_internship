from tkinter import*
def add_to_list():
    to_do.insert(to_do.size(),str(to_do.size()+1)+"-"+task.get())
    to_do.config(height=to_do.size())
def delete_from_list():
    to_do.delete(to_do.curselection())
    to_do.config(height=to_do.size())
def backspace():
    task.delete(len(task.get())-1,END)
window=Tk()
window.title("to do list")
window.geometry("450x450")
window.config(bg="#f7fae1")
to_do=Listbox(window,
              font=('Times New Roman',15,'bold'),
              bg="white",
              width=30,
              height=30)
task=Entry(window,font=("Times New Roman",15),width=30)
add_task=Button(window,text='add task'
                ,fg='black'
                ,bg='white',
                command=add_to_list)

delete_task=Button(window,text='delete task'
                ,fg='black'
                ,bg='white'
                ,command=delete_from_list)

backspace_button=Button(window,text='backspace'
                ,fg='black'
                ,bg='white'
                ,command=backspace)
to_do.place(x=120,y=80)
task.place(x=30,y=20)
add_task.place(x=30,y=80)
delete_task.place(x=30,y=110)
backspace_button.place(x=30,y=140)
window.mainloop()
