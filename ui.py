import customtkinter as ctk
from tkinter import messagebox

from auth import login_user, register_user
from tasks import add_task, load_tasks, mark_task_completed, delete_task, sort_tasks


class TaskManager(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Task Manager")
        self.geometry("520x520")

        self.current_user = None
        self.show_login()


    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()


    # -------- LOGIN --------
    def show_login(self):
        self.clear()

        ctk.CTkLabel(self, text="Login", font=("Arial", 20)).pack(pady=20)

        username = ctk.CTkEntry(self, placeholder_text="Username")
        username.pack(pady=10)

        password = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        password.pack(pady=10)

        msg = ctk.CTkLabel(self, text="")
        msg.pack()

        def login():
            if not username.get() or not password.get():
                msg.configure(text="Fields cannot be empty", text_color="red")
                return

            if login_user(username.get(), password.get()):
                self.current_user = username.get()
                self.show_menu()
            else:
                msg.configure(text="Invalid credentials", text_color="red")

        ctk.CTkButton(self, text="Login", command=login).pack(pady=10)
        ctk.CTkButton(self, text="Register", command=self.show_register).pack()


    # -------- REGISTER --------
    def show_register(self):
        self.clear()

        ctk.CTkLabel(self, text="Register", font=("Arial", 20)).pack(pady=20)

        username = ctk.CTkEntry(self, placeholder_text="Username")
        username.pack(pady=10)

        password = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        password.pack(pady=10)

        msg = ctk.CTkLabel(self, text="")
        msg.pack()

        def register():
            success, message = register_user(username.get(), password.get())
            msg.configure(text=message, text_color="green" if success else "red")

        ctk.CTkButton(self, text="Register", command=register).pack(pady=10)
        ctk.CTkButton(self, text="Back", command=self.show_login).pack()


    # -------- MENU --------
    def show_menu(self):
        self.clear()

        ctk.CTkLabel(self, text=f"Welcome {self.current_user}", font=("Arial", 18)).pack(pady=10)

        ctk.CTkButton(self, text="Add Task", command=self.add_task_ui).pack(pady=5)
        ctk.CTkButton(self, text="View Tasks", command=self.view_tasks).pack(pady=5)
        ctk.CTkButton(self, text="Mark Completed", command=self.mark_task_ui).pack(pady=5)
        ctk.CTkButton(self, text="Delete Task", command=self.delete_task_ui).pack(pady=5)
        ctk.CTkButton(self, text="Logout", command=self.show_login).pack(pady=10)


    # -------- VIEW TASKS --------
    def render_tasks(self, container, search_text=""):
        tasks = load_tasks(self.current_user)

        if search_text:
            tasks = [t for t in tasks if search_text.lower() in t["task"].lower()]

        tasks = sort_tasks(tasks)

        for t in tasks:
            text = f"ID:{t['id']} | {t['task']} | {t['status']} | {t.get('created_at','')}"
            color = "gray" if t["status"] == "Completed" else "white"
            ctk.CTkLabel(container, text=text, text_color=color).pack(anchor="w")


    def view_tasks(self):
        self.clear()

        search = ctk.CTkEntry(self, placeholder_text="Search...")
        search.pack(pady=10)

        container = ctk.CTkFrame(self)
        container.pack(fill="both", expand=True)

        def refresh():
            for w in container.winfo_children():
                w.destroy()
            self.render_tasks(container, search.get())

        ctk.CTkButton(self, text="Search", command=refresh).pack()
        refresh()

        ctk.CTkButton(self, text="Back", command=self.show_menu).pack(pady=10)


    # -------- ADD --------
    def add_task_ui(self):
        self.clear()

        entry = ctk.CTkEntry(self, placeholder_text="Task description")
        entry.pack(pady=20)

        msg = ctk.CTkLabel(self, text="")
        msg.pack()

        def add():
            success, message = add_task(self.current_user, entry.get())
            msg.configure(text=message, text_color="green" if success else "red")

        ctk.CTkButton(self, text="Add", command=add).pack()
        ctk.CTkButton(self, text="Back", command=self.show_menu).pack(pady=10)


    # -------- MARK --------
    def mark_task_ui(self):
        self.clear()

        container = ctk.CTkFrame(self)
        container.pack(fill="both", expand=True)

        self.render_tasks(container)

        entry = ctk.CTkEntry(self, placeholder_text="Task ID")
        entry.pack(pady=10)

        def mark():
            try:
                success, msg = mark_task_completed(self.current_user, int(entry.get()))
            except:
                success, msg = False, "Invalid ID"

            messagebox.showinfo("Result", msg)

        ctk.CTkButton(self, text="Mark Completed", command=mark).pack()
        ctk.CTkButton(self, text="Back", command=self.show_menu).pack(pady=10)


    # -------- DELETE --------
    def delete_task_ui(self):
        self.clear()

        container = ctk.CTkFrame(self)
        container.pack(fill="both", expand=True)

        self.render_tasks(container)

        entry = ctk.CTkEntry(self, placeholder_text="Task ID")
        entry.pack(pady=10)

        def delete():
            try:
                task_id = int(entry.get())
            except:
                messagebox.showerror("Error", "Invalid ID")
                return

            if not messagebox.askyesno("Confirm", "Delete task?"):
                return

            success, msg = delete_task(self.current_user, task_id)
            messagebox.showinfo("Result", msg)

        ctk.CTkButton(self, text="Delete", command=delete).pack()
        ctk.CTkButton(self, text="Back", command=self.show_menu).pack(pady=10)