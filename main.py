"""
TEST ARENA - Quiz Application
Main Application File
"""
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from database import Database

class QuizApp:
    def __init__(self):
        self.db = Database()
        self.root = tk.Tk()
        self.root.title("TEST ARENA")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        self.current_user = None
        self.current_exam = None
        self.questions = []
        self.user_answers = {}
        self.start_time = None
        self.current_question_index = 0
        self.quiz_mode = None
        self.timer_id = None
        
        # Styles
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TButton", padding=10, font=('Helvetica', 10))
        self.style.configure("TLabel", background="#f0f0f0", font=('Helvetica', 11))
        self.style.configure("Header.TLabel", font=('Helvetica', 18, 'bold'), foreground="#0056b3")
        self.style.configure("TFrame", background="#f0f0f0")

    def clear_window(self):
        """Clear all widgets from the window"""
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
            
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_header(self, title):
        """Create a standard header"""
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill=tk.X, pady=20)
        
        lbl_title = ttk.Label(header_frame, text=title, style="Header.TLabel")
        lbl_title.pack()
        
        ttk.Separator(self.root, orient='horizontal').pack(fill=tk.X, padx=20, pady=10)

    def start(self):
        """Start the application"""
        if not self.db.connect():
            messagebox.showerror("Database Error", "Failed to connect to database.\nPlease check your configuration.")
            return
        
        self.show_login_menu()
        self.root.mainloop()
        self.db.disconnect()

    def show_login_menu(self):
        self.clear_window()
        self.create_header("Welcome to TEST ARENA")
        
        frame = ttk.Frame(self.root)
        frame.pack(expand=True)
        
        ttk.Button(frame, text="Login", command=self.show_login, width=20).pack(pady=10)
        ttk.Button(frame, text="Sign Up", command=self.show_signup, width=20).pack(pady=10)
        ttk.Button(frame, text="Exit", command=self.root.quit, width=20).pack(pady=10)

    def show_login(self):
        self.clear_window()
        self.create_header("Login")
        
        frame = ttk.Frame(self.root)
        frame.pack(expand=True)
        
        ttk.Label(frame, text="Username:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        entry_user = ttk.Entry(frame, width=30)
        entry_user.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        entry_pass = ttk.Entry(frame, show="*", width=30)
        entry_pass.grid(row=1, column=1, padx=5, pady=5)
        
        def attempt_login():
            username = entry_user.get().strip()
            password = entry_pass.get().strip()
            user = self.db.verify_user(username, password)
            if user:
                self.current_user = user
                messagebox.showinfo("Success", f"Welcome back, {user['name']}!")
                self.show_main_menu()
            else:
                messagebox.showerror("Error", "Invalid username or password!")

        ttk.Button(frame, text="Login", command=attempt_login).grid(row=2, column=0, columnspan=2, pady=20)
        ttk.Button(frame, text="Back", command=self.show_login_menu).grid(row=3, column=0, columnspan=2)

    def show_signup(self):
        self.clear_window()
        self.create_header("Sign Up")
        
        frame = ttk.Frame(self.root)
        frame.pack(expand=True)
        
        entries = {}
        fields = ["Full Name", "Username", "Password", "Confirm Password", "Email", "Phone"]
        
        for i, field in enumerate(fields):
            ttk.Label(frame, text=f"{field}:").grid(row=i, column=0, padx=5, pady=5, sticky=tk.E)
            entry = ttk.Entry(frame, width=30)
            if "Password" in field:
                entry.configure(show="*")
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries[field] = entry
            
        def attempt_signup():
            name = entries["Full Name"].get().strip()
            username = entries["Username"].get().strip()
            password = entries["Password"].get().strip()
            confirm = entries["Confirm Password"].get().strip()
            email = entries["Email"].get().strip()
            phone = entries["Phone"].get().strip()
            
            if not name or not username or not password:
                messagebox.showerror("Error", "Please fill in required fields.")
                return
                
            if self.db.check_username_exists(username):
                messagebox.showerror("Error", "Username already exists!")
                return
                
            if password != confirm:
                messagebox.showerror("Error", "Passwords do not match!")
                return
                
            if self.db.create_user(name, username, password, email, phone):
                messagebox.showinfo("Success", "Account created! Please login.")
                self.show_login()
            else:
                messagebox.showerror("Error", "Failed to create account.")

        ttk.Button(frame, text="Sign Up", command=attempt_signup).grid(row=len(fields), column=0, columnspan=2, pady=20)
        ttk.Button(frame, text="Back", command=self.show_login_menu).grid(row=len(fields)+1, column=0, columnspan=2)

    def show_main_menu(self):
        self.clear_window()
        self.create_header(f"Main Menu - {self.current_user['name']}")
        
        frame = ttk.Frame(self.root)
        frame.pack(expand=True)
        
        buttons = [
            ("Start Quiz", self.show_exam_selection),
            ("View Scores", self.show_scores),
            ("About", self.show_about),
            ("Logout", self.logout)
        ]
        
        for text, cmd in buttons:
            ttk.Button(frame, text=text, command=cmd, width=25).pack(pady=10)

    def logout(self):
        self.current_user = None
        self.show_login_menu()

    def show_exam_selection(self):
        self.clear_window()
        self.create_header("Select Exam")
        
        frame = ttk.Frame(self.root)
        frame.pack(expand=True, fill=tk.BOTH, padx=50)
        
        exams = self.db.get_all_exams()
        
        if not exams:
            ttk.Label(frame, text="No exams available.").pack()
            ttk.Button(frame, text="Back", command=self.show_main_menu).pack(pady=20)
            return

        # Scrollable list
        canvas = tk.Canvas(frame, bg="#f0f0f0")
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        for exam in exams:
            btn_text = f"{exam['exam_name']}\n{exam['duration_minutes']} mins | {exam['total_questions']} Qs"
            btn = ttk.Button(
                scrollable_frame, 
                text=btn_text, 
                command=lambda e=exam: self.show_mode_selection(e)
            )
            btn.pack(fill=tk.X, pady=5, padx=5)
            
        ttk.Button(self.root, text="Back", command=self.show_main_menu).pack(pady=20)

    def show_mode_selection(self, exam):
        self.current_exam = exam
        self.clear_window()
        self.create_header(f"{exam['exam_name']} - Select Mode")
        
        frame = ttk.Frame(self.root)
        frame.pack(expand=True)
        
        ttk.Button(frame, text="Exam Mode\n(Timed, No Feedback)", 
                  command=lambda: self.start_quiz("Exam"), width=30).pack(pady=10)
        ttk.Button(frame, text="Free Trial Mode\n(Immediate Feedback)", 
                  command=lambda: self.start_quiz("Free Trial"), width=30).pack(pady=10)
        ttk.Button(frame, text="Back", command=self.show_exam_selection).pack(pady=20)

    def start_quiz(self, mode):
        self.quiz_mode = mode
        self.questions = self.db.get_questions_by_exam(self.current_exam['exam_id'])
        
        if not self.questions:
            messagebox.showwarning("Warning", "No questions available for this exam.")
            return
            
        self.questions = self.questions[:self.current_exam['total_questions']]
        self.user_answers = {}
        self.current_question_index = 0
        self.start_time = datetime.now()
        
        self.show_question()

    def show_question(self):
        self.clear_window()
        
        if self.current_question_index >= len(self.questions):
            self.finish_quiz()
            return
            
        question = self.questions[self.current_question_index]
        
        # Header with Timer and Progress
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill=tk.X, padx=20, pady=10)
        
        ttk.Label(header_frame, text=f"Question {self.current_question_index + 1}/{len(self.questions)}", 
                 font=('Helvetica', 12, 'bold')).pack(side=tk.LEFT)
        
        self.lbl_timer = ttk.Label(header_frame, text="", font=('Helvetica', 12, 'bold'), foreground="red")
        self.lbl_timer.pack(side=tk.RIGHT)
        
        if self.quiz_mode == "Exam":
            self.update_timer()
        
        # Question Content
        content_frame = ttk.Frame(self.root)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=10)
        
        ttk.Label(content_frame, text=f"Subject: {question['subject_name']}", foreground="gray").pack(anchor="w")
        
        # Question Text (using Message for wrapping)
        msg = tk.Message(content_frame, text=question['question_text'], width=700, font=('Helvetica', 14), bg="#f0f0f0")
        msg.pack(pady=20, anchor="w")
        
        # Options
        self.var_answer = tk.StringVar(value="N")
        
        options_frame = ttk.Frame(content_frame)
        options_frame.pack(fill=tk.X, pady=10)
        
        for opt, text in [('A', question['option_a']), ('B', question['option_b']), 
                          ('C', question['option_c']), ('D', question['option_d'])]:
            btn = tk.Radiobutton(options_frame, text=f"{opt}. {text}", variable=self.var_answer, 
                                value=opt, font=('Helvetica', 11), bg="#f0f0f0", activebackground="#f0f0f0",
                                anchor="w", justify="left")
            btn.pack(fill=tk.X, pady=5)
            
        # Navigation
        nav_frame = ttk.Frame(self.root)
        nav_frame.pack(fill=tk.X, padx=40, pady=20)
        
        if self.quiz_mode == "Free Trial":
            ttk.Button(nav_frame, text="Check Answer", command=self.check_answer_trial).pack(side=tk.RIGHT)
        else:
            ttk.Button(nav_frame, text="Next", command=self.next_question).pack(side=tk.RIGHT)

    def update_timer(self):
        if self.quiz_mode != "Exam":
            return
            
        duration = self.current_exam['duration_minutes']
        end_time = self.start_time + timedelta(minutes=duration)
        remaining = end_time - datetime.now()
        
        if remaining.total_seconds() <= 0:
            self.finish_quiz()
            return
            
        minutes = int(remaining.total_seconds() // 60)
        seconds = int(remaining.total_seconds() % 60)
        self.lbl_timer.config(text=f"Time Left: {minutes:02d}:{seconds:02d}")
        
        self.timer_id = self.root.after(1000, self.update_timer)

    def check_answer_trial(self):
        selected = self.var_answer.get()
        question = self.questions[self.current_question_index]
        
        if selected == "N":
            messagebox.showinfo("Skipped", "You skipped this question.")
        elif selected == question['correct_option']:
            messagebox.showinfo("Correct!", "That is the correct answer!")
        else:
            msg = f"Wrong answer.\nCorrect option: {question['correct_option']}"
            if question['solution']:
                msg += f"\n\nSolution: {question['solution']}"
            messagebox.showerror("Incorrect", msg)
            
        self.user_answers[question['question_id']] = selected
        self.current_question_index += 1
        self.show_question()

    def next_question(self):
        selected = self.var_answer.get()
        question = self.questions[self.current_question_index]
        self.user_answers[question['question_id']] = selected
        self.current_question_index += 1
        self.show_question()

    def finish_quiz(self):
        self.clear_window()
        
        correct = 0
        wrong = 0
        unanswered = 0
        
        for question in self.questions:
            answer = self.user_answers.get(question['question_id'], 'N')
            if answer == 'N':
                unanswered += 1
            elif answer == question['correct_option']:
                correct += 1
            else:
                wrong += 1
                
        total_marks = correct
        time_taken = int((datetime.now() - self.start_time).total_seconds() / 60)
        
        self.db.save_score(
            self.current_user['user_id'],
            self.current_exam['exam_id'],
            self.quiz_mode,
            total_marks,
            correct,
            wrong,
            unanswered,
            time_taken
        )
        
        self.create_header("Quiz Results")
        
        frame = ttk.Frame(self.root)
        frame.pack(expand=True)
        
        results = [
            ("Exam", self.current_exam['exam_name']),
            ("Mode", self.quiz_mode),
            ("Time Taken", f"{time_taken} minutes"),
            ("Total Questions", str(len(self.questions))),
            ("Correct Answers", str(correct)),
            ("Wrong Answers", str(wrong)),
            ("Unanswered", str(unanswered)),
            ("Total Marks", f"{total_marks}/{len(self.questions)}")
        ]
        
        for i, (label, value) in enumerate(results):
            ttk.Label(frame, text=label + ":", font=('Helvetica', 11, 'bold')).grid(row=i, column=0, sticky=tk.E, padx=10, pady=5)
            ttk.Label(frame, text=value).grid(row=i, column=1, sticky=tk.W, padx=10, pady=5)
            
        ttk.Button(frame, text="Back to Menu", command=self.show_main_menu).grid(row=len(results), column=0, columnspan=2, pady=20)

    def show_scores(self):
        self.clear_window()
        self.create_header("Your Scores")
        
        frame = ttk.Frame(self.root)
        frame.pack(expand=True, fill=tk.BOTH, padx=20)
        
        # Treeview
        columns = ("Exam", "Mode", "Attempt", "Score", "Date")
        tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)
            
        scores = self.db.get_user_scores(self.current_user['user_id'])
        for score in scores:
            date = score['attempt_date'].strftime('%Y-%m-%d %H:%M')
            tree.insert("", tk.END, values=(
                score['exam_name'],
                score['mode'],
                f"#{score['attempt_number']}",
                score['total_marks'],
                date
            ))
            
        tree.pack(fill=tk.BOTH, expand=True)
        
        ttk.Button(self.root, text="Back", command=self.show_main_menu).pack(pady=20)

    def show_about(self):
        self.clear_window()
        self.create_header("About TEST ARENA")
        
        frame = ttk.Frame(self.root)
        frame.pack(expand=True, padx=40)
        
        text = ("TEST ARENA is a comprehensive quiz application designed to help\n"
                "students prepare for competitive exams like PSC, UPSC, KEAM, NEET, and JEE.\n\n"
                "Features:\n"
                "• Exam Mode - Timed exams with realistic exam conditions\n"
                "• Free Trial Mode - Practice with immediate feedback\n"
                "• Score Tracking - Track your progress over time\n"
                "• Multiple Subjects - Questions categorized by subject\n\n"
                "Developed as a DBMS Project\nVersion 1.0")
        
        msg = tk.Message(frame, text=text, width=600, font=('Helvetica', 11), bg="#f0f0f0")
        msg.pack()
        
        ttk.Button(frame, text="Back", command=self.show_main_menu).pack(pady=20)


if __name__ == "__main__":
    app = QuizApp()
    app.start()
