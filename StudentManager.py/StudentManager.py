import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

filename = "Assessment 1 - Skills Portfolio\A1 - Resources\studentMarks.txt"

def load_students():
    students = []
    try:
        with open(filename, "r") as f:
            lines = f.read().strip().split("\n")
            count = int(lines[0])
            for line in lines[1:]:
                parts = line.split(",")
                code = parts[0]
                name = parts[1]
                c1, c2, c3 = map(int, parts[2:5])
                exam = int(parts[5])
                students.append({
                    "code": code,
                    "name": name,
                    "cw": [c1, c2, c3],
                    "exam": exam
                })
    except FileNotFoundError:
        messagebox.showerror("Error", "studentMarks.txt not found!")
    return students

def save_students(students):
    with open(filename, "w") as f:
        f.write(str(len(students)) + "\n")
        for s in students:
            f.write(f"{s['code']},{s['name']},{s['cw'][0]},{s['cw'][1]},{s['cw'][2]},{s['exam']}\n")

def calculate_totals(student):
    cw_total = sum(student['cw'])
    exam = student['exam']
    overall = (cw_total + exam) / 160 * 100

    if overall >= 70: grade = "A"
    elif overall >= 60: grade = "B"
    elif overall >= 50: grade = "C"
    elif overall >= 40: grade = "D"
    else: grade = "F"

    return cw_total, exam, overall, grade

def format_student(student):
    cw_total, exam, overall, grade = calculate_totals(student)
    return (f"Name: {student['name']}\n"
            f"Code: {student['code']}\n"
            f"Coursework Total: {cw_total}/60\n"
            f"Exam Mark: {exam}/100\n"
            f"Overall: {overall:.2f}%\n"
            f"Grade: {grade}\n")

class StudentManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Manager")
        self.students = load_students()

        # MAIN LAYOUT: Left = buttons, Right = output
        main_frame = tk.Frame(root, bg="#6A5ACD")
        main_frame.pack(fill="both", expand=True)

        # LEFT SIDE MENU
        menu_frame = tk.Frame(main_frame, bg="#7785cc")
        menu_frame.pack(side="left", fill="y", padx=10, pady=10)

        # TABLE OUTPUT
        self.output = ttk.Treeview(main_frame, columns=("code", "name", "cw", "exam", "overall", "grade"), 
                                   show="headings", height=25)
        self.output.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Define column titles
        self.output.heading("code", text="Code")
        self.output.heading("name", text="Name")
        self.output.heading("cw", text="CW Total")
        self.output.heading("exam", text="Exam")
        self.output.heading("overall", text="Overall %")
        self.output.heading("grade", text="Grade")

        # Column widths
        self.output.column("code", width=80)
        self.output.column("name", width=150)
        self.output.column("cw", width=90)
        self.output.column("exam", width=90)
        self.output.column("overall", width=90)
        self.output.column("grade", width=60)


        # Buttons with functions
        options = [
            ("1. View All Records", self.view_all),
            ("2. View Individual Record", self.view_single),
            ("3. Highest Mark", self.highest),
            ("4. Lowest Mark", self.lowest),
            ("5. Sort Records", self.sort_records),
            ("6. Add Student", self.add_student),
            ("7. Delete Student", self.delete_student),
            ("8. Update Student", self.update_student),
        ]

        for text, cmd in options:
            tk.Button(menu_frame, text=text, font=("Ariel", 10), width=25, command=cmd, bg="#5647ca", fg="white", 
                      activebackground="#adf5ff", activeforeground="black").pack(pady=10)
            
    def fill_table(self):
        for row in self.output.get_children():
            self.output.delete(row)

        for s in self.students:
            cw_total, exam, overall, grade = calculate_totals(s)
            self.output.insert("", tk.END, values=(
                s["code"],
                s["name"],
                f"{cw_total}/60",
                f"{exam}/100",
                f"{overall:.2f}%",
                grade
            ))

    def view_all(self,):
        self.fill_table()

    def fill_table_custom(self, list_of_students):
        for row in self.output.get_children():
            self.output.delete(row)

        for s in list_of_students:
            cw_total, exam, overall, grade = calculate_totals(s)
            self.output.insert("", tk.END, values=(
                s["code"],
                s["name"],
                f"{cw_total}/60",
                f"{exam}/100",
                f"{overall:.2f}%",
                grade
            ))

    def view_single(self):
        code = simpledialog.askstring("Student Lookup", "Enter student code:")
        if not code:
            return

        for s in self.students:
            if s["code"] == code:
                self.fill_table_custom([s])
                return

        messagebox.showerror("Error", "Student not found.")

    def highest(self):
        student = max(self.students, key=lambda s: calculate_totals(s)[2])
        self.fill_table_custom([student])

    def lowest(self):
        student = min(self.students, key=lambda s: calculate_totals(s)[2])
        self.fill_table_custom([student])

    def sort_records(self):
        order = messagebox.askyesno("Sort", "Sort ascending? (No = descending)")
        self.students.sort(key=lambda s: calculate_totals(s)[2], reverse=not order)
        save_students(self.students)
        messagebox.showinfo("Sorted", "Records sorted.")
        self.view_all()

    def add_student(self):
        code = simpledialog.askstring("New Student", "Student Code:")
        name = simpledialog.askstring("New Student", "Student Name:")
        c1 = int(simpledialog.askstring("Coursework 1 (0-20)", "C1Mark:"))
        c2 = int(simpledialog.askstring("Coursework 2 (0-20)", "C2Mark:"))
        c3 = int(simpledialog.askstring("Coursework 3 (0-20)", "C3Mark:"))
        exam = int(simpledialog.askstring("Exam Mark (0-100)", "Mark:"))

        self.students.append({
            "code": code,
            "name": name,
            "cw": [c1, c2, c3],
            "exam": exam
        })
        save_students(self.students)
        messagebox.showinfo("Added", "Student record added.")
        self.view_all()

    def delete_student(self):
        code = simpledialog.askstring("Delete Student", "Enter student code:")
        if not code: return

        for s in self.students:
            if s['code'] == code:
                self.students.remove(s)
                save_students(self.students)
                messagebox.showinfo("Deleted", "Student removed.")
                self.view_all()
                return

        messagebox.showerror("Error", "Student not found.")

    def update_student(self):
        code = simpledialog.askstring("Update Student", "Enter student code:")
        if not code: return

        for s in self.students:
            if s['code'] == code:
                field = simpledialog.askstring(
                    "Update",
                    "Enter field to update (name, cw1, cw2, cw3, exam):"
                )

                if field == "name":
                    s["name"] = simpledialog.askstring("New Name", "Enter new name:")
                elif field in ["cw1", "cw2", "cw3"]:
                    index = int(field[-1]) - 1
                    s["cw"][index] = int(simpledialog.askstring("New Mark", "Enter mark:"))
                elif field == "exam":
                    s["exam"] = int(simpledialog.askstring("New Mark", "Enter mark:"))
                else:
                    messagebox.showerror("Error", "Invalid field.")
                    return

                save_students(self.students)
                messagebox.showinfo("Updated", "Student updated.")
                self.view_all()
                return

        messagebox.showerror("Error", "Student not found.")

root = tk.Tk()
root.title("Student Manager")
root.iconbitmap("StudentManager.py\SM.ico")

app = StudentManager(root)
root.mainloop()