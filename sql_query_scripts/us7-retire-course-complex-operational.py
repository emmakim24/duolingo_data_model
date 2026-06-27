import psycopg2

conn = psycopg2.connect(dbname="project", user="isdb", host="localhost")
cur = conn.cursor()

us = '''
User Story 7: Retire a Course

   As a:  Operation
 I want:  To retire a language course and replace it with a successor course
So That:  I can phase out old courses and transition learners to updated content
'''

print(us)

def retire_course(old_course_id, new_course_id):
    """
    Retire a course by:
    1. Setting state to false for old course
    2. Moving all lessons to new course
    3. Moving all learners to new course
    Uses LEAD window function to show course succession
    """
    
    print("\n" + "="*80)
    print("TABLES BEFORE RETIRING COURSE:")
    print("="*80)
    
    print("\nCourses table (with successor using LEAD):")
    window_query = '''
SELECT cid,
       language,
       state,
       LEAD(cid) OVER (ORDER BY cid) AS successor_cid,
       LEAD(language) OVER (ORDER BY cid) AS successor_language
  FROM courses
 ORDER BY cid
'''
    print(window_query)
    cur.execute(window_query)
    for row in cur.fetchall():
        print(row)
    
    print(f"\nLessons in course {old_course_id}:")
    cur.execute("SELECT lid, name, cid FROM lesson WHERE cid = %s", (old_course_id,))
    for row in cur.fetchall():
        print(row)
    
    print(f"\nLearners taking course {old_course_id}:")
    cur.execute("SELECT uid, cid FROM courses_taken WHERE cid = %s", (old_course_id,))
    for row in cur.fetchall():
        print(row)
    
    print(f"\nLesson progress in course {old_course_id}:")
    cur.execute("SELECT lpid, uid, cid FROM lesson_progress WHERE cid = %s", (old_course_id,))
    for row in cur.fetchall():
        print(row)
    
    print("\n" + "="*80)
    print("EXECUTING RETIREMENT:")
    print("="*80)
    
    query1 = "UPDATE courses SET state = false WHERE cid = %s"
    print(f"\n1. {query1} with cid={old_course_id}")
    cur.execute(query1, (old_course_id,))
    
    query2 = "UPDATE lesson SET cid = %s WHERE cid = %s"
    print(f"2. {query2} with new_cid={new_course_id}, old_cid={old_course_id}")
    cur.execute(query2, (new_course_id, old_course_id))
    
    query3 = "UPDATE courses_taken SET cid = %s WHERE cid = %s"
    print(f"3. {query3} with new_cid={new_course_id}, old_cid={old_course_id}")
    cur.execute(query3, (new_course_id, old_course_id))
    
    query4 = "UPDATE lesson_progress SET cid = %s WHERE cid = %s"
    print(f"4. {query4} with new_cid={new_course_id}, old_cid={old_course_id}")
    cur.execute(query4, (new_course_id, old_course_id))
    
    conn.commit()
    
    print("\n" + "="*80)
    print("TABLES AFTER RETIRING COURSE:")
    print("="*80)
    
    print("\nCourses table (showing retired course):")
    cur.execute("SELECT cid, language, state FROM courses ORDER BY cid")
    for row in cur.fetchall():
        print(row)
    
    print(f"\nLessons now in course {new_course_id}:")
    cur.execute("SELECT lid, name, cid FROM lesson WHERE cid = %s", (new_course_id,))
    for row in cur.fetchall():
        print(row)
    
    print(f"\nLearners now taking course {new_course_id}:")
    cur.execute("SELECT uid, cid FROM courses_taken WHERE cid = %s", (new_course_id,))
    for row in cur.fetchall():
        print(row)
    
    print("\n" + "="*80)
    print(f"SUCCESS: Retired course {old_course_id}, moved everything to course {new_course_id}")
    print("="*80)


retire_course(7, 6)

cur.close()
conn.close()
