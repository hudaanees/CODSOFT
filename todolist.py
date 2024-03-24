import tkinter as tk
from tkinter import messagebox

class TodoListGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.tasks = {}

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(master, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.update_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=0, padx=10, pady=10)

        self.complete_button = tk.Button(master, text="Mark as Completed", command=self.mark_as_completed)
        self.complete_button.grid(row=2, column=1, padx=10, pady=10)

        self.display_tasks()

    def add_task(self):
        task_name = self.task_entry.get()
        if task_name:
            task_id = len(self.tasks) + 1
            self.tasks[task_id] = {"name": task_name, "completed": False}
            self.task_entry.delete(0, tk.END)
            self.display_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task name.")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_id = selected_index[0] + 1
            new_name = self.task_entry.get()
            if new_name:
                self.tasks[task_id]["name"] = new_name
                self.display_tasks()
            else:
                messagebox.showwarning("Warning", "Please enter a new task name.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def mark_as_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_id = selected_index[0] + 1
            self.tasks[task_id]["completed"] = True
            self.display_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task_id, task in self.tasks.items():
            status = "Completed" if task["completed"] else "Not Completed"
            self.task_listbox.insert(tk.END, f'{task_id}. {task["name"]} - {status}')

def main():
    root = tk.Tk()
    todo_app = TodoListGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
