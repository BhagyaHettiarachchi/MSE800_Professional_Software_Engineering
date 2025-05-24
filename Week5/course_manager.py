from database import create_connection
import sqlite3

def assign_user_to_course(user_id, course_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO user_enrollment (user_id, course_id) VALUES (?, ?)", (user_id, course_id))
        conn.commit()
        print(f"✅ User {user_id} assigned to Course {course_id}")
    except sqlite3.IntegrityError:
        print("⚠️ This user is already enrolled in that course or the IDs are invalid.")
    conn.close()

def get_courses_by_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT c.id, c.name, c.unit
        FROM course c
        INNER JOIN user_course uc ON c.id = uc.course_id
        WHERE uc.user_id = ?
    ''', (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

