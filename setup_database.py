import mysql.connector
from database import Database

def setup():
    print("Setting up TEST ARENA database...")
    
    # 1. Create Database
    # We connect without a database first to create it
    db_config = Database()
    try:
        conn = mysql.connector.connect(
            host=db_config.host,
            user=db_config.user,
            password=db_config.password
        )
        cursor = conn.cursor()
        
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_config.database}")
        cursor.execute(f"USE {db_config.database}")
        print(f"Database '{db_config.database}' selected.")
        
        # 2. Create Tables
        tables = [
            """
            CREATE TABLE IF NOT EXISTS User (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                email VARCHAR(100),
                phone VARCHAR(20)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Exam (
                exam_id INT AUTO_INCREMENT PRIMARY KEY,
                exam_name VARCHAR(50) NOT NULL,
                duration_minutes INT NOT NULL,
                total_questions INT NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Subject (
                subject_id INT AUTO_INCREMENT PRIMARY KEY,
                subject_name VARCHAR(50) NOT NULL,
                exam_id INT,
                FOREIGN KEY (exam_id) REFERENCES Exam(exam_id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Question (
                question_id INT AUTO_INCREMENT PRIMARY KEY,
                exam_id INT,
                subject_id INT,
                question_text TEXT NOT NULL,
                option_a TEXT NOT NULL,
                option_b TEXT NOT NULL,
                option_c TEXT NOT NULL,
                option_d TEXT NOT NULL,
                correct_option CHAR(1) NOT NULL,
                solution TEXT,
                FOREIGN KEY (exam_id) REFERENCES Exam(exam_id),
                FOREIGN KEY (subject_id) REFERENCES Subject(subject_id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Score (
                score_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                exam_id INT,
                mode VARCHAR(20),
                attempt_number INT,
                total_marks INT,
                correct_answers INT,
                wrong_answers INT,
                unanswered INT,
                time_taken_minutes INT,
                attempt_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES User(user_id),
                FOREIGN KEY (exam_id) REFERENCES Exam(exam_id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS UserAnswer (
                answer_id INT AUTO_INCREMENT PRIMARY KEY,
                score_id INT,
                question_id INT,
                selected_option CHAR(1),
                is_correct BOOLEAN,
                FOREIGN KEY (score_id) REFERENCES Score(score_id),
                FOREIGN KEY (question_id) REFERENCES Question(question_id)
            )
            """
        ]
        
        for table_sql in tables:
            cursor.execute(table_sql)
        print("Tables created successfully.")
            
        # 3. Insert Initial Data (Exams and Subjects)
        # Check if data exists to avoid duplicates
        cursor.execute("SELECT COUNT(*) FROM Exam")
        if cursor.fetchone()[0] == 0:
            print("Inserting initial Exam and Subject data...")
            # Exams: ID, Name, Duration, Total Qs
            exams = [(1, 'PSC', 60, 100), (2, 'UPSC', 120, 100), (3, 'KEAM', 150, 120), (4, 'NEET', 180, 180), (5, 'JEE', 180, 90)]
            cursor.executemany("INSERT INTO Exam (exam_id, exam_name, duration_minutes, total_questions) VALUES (%s, %s, %s, %s)", exams)
            
            # Subjects: ID, Name, ExamID
            subjects = [(1, 'General Knowledge', 1), (2, 'English', 1), (3, 'Mathematics', 1), (4, 'Mathematics', 3), (5, 'Physics', 3), (6, 'Chemistry', 3), (7, 'General Studies', 2), (8, 'Physics', 4), (9, 'Chemistry', 4), (10, 'Biology', 4), (11, 'Mathematics', 5), (12, 'Physics', 5), (13, 'Chemistry', 5)]
            cursor.executemany("INSERT INTO Subject (subject_id, subject_name, exam_id) VALUES (%s, %s, %s)", subjects)
            
        conn.commit()
        print("Setup completed! You can now run 'add_questions.py' to populate questions.")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    setup()