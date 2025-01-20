import tkinter as tk
import random

class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz Application")
        self.root.geometry("900x500")
        self.score = 0
        self.current_answer = None
        self.question_label = tk.Label(root, text="", font=("Arial", 18))
        self.question_label.place(relx=0.05,rely=0.05)
        self.answer_entry = tk.Entry(root, font=("Arial", 14))
        self.answer_entry.place(relx=0.05,rely=0.15)
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.place(relx=0.05,rely=0.25)
        self.answer_label = tk.Label(root, text="Score: " + str(self.score), font=("Arial", 18))
        self.answer_label.place(relx=0.05,rely=0.35)
        self.generate_question()
    
    def generate_question(self):
        operations = ['+', '-', '*', '/']
        operation = random.choice(operations)
        if operation == '/':
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 10)
            num1 = num1 * num2  # Ensure it's divisible
        else:
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
        self.current_question_text = f"What is {num1} {operation} {num2}?"
        self.current_answer = eval(f"{num1} {operation} {num2}")
        self.question_label.config(text=self.current_question_text)
        
        
    def check_answer(self):
        try:
            user_answer = float(self.answer_entry.get().strip())
            if user_answer == self.current_answer:
                self.score += 1
                self.answer_label.configure(text="Score: " + str(self.score))
            self.answer_entry.delete(0, tk.END)
            self.generate_question()
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
        
    
root = tk.Tk()
app = MathQuizApp(root)
root.mainloop()

