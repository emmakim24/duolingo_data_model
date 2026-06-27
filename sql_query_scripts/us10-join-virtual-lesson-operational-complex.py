from common import *

us = '''
* Complex US10: Join a virtual lesson

   As a:  Language Learner
 I want:  To be able to join and attend real-time virtual lessons
So That: I can practice conversation skills in real time and receive feedback
'''

print(us)


def list_virtual_lessons():

    cols = 'vlid topic language start_time end_time current_attendees'

    tmpl = '''
SELECT vl.vlid, vl.topic, vl.language, vl.start_time, vl.end_time, COUNT(a.uid) AS current_attendees
  FROM Virtual_Lesson AS vl
       LEFT JOIN Attendance AS a ON vl.vlid = a.vlid
 GROUP BY vl.vlid, vl.topic, vl.language, vl.start_time, vl.end_time
 ORDER BY vl.start_time;
'''
    cur.execute(tmpl)
    rows = cur.fetchall()
    show_table(rows, cols)

def join_virtual_lesson(uid, vlid):

    tmpl_lesson = '''
SELECT vl.vlid, vl.topic, vl.language, vl.start_time, vl.end_time, COUNT(a.uid) AS current_attendees
  FROM Virtual_Lesson AS vl
       LEFT JOIN Attendance AS a ON vl.vlid = a.vlid
 WHERE vl.vlid = %s
 GROUP BY vl.vlid, vl.topic, vl.language, vl.start_time, vl.end_time;
'''
    cmd = cur.mogrify(tmpl_lesson, (vlid,))
    print_cmd(cmd)
    cur.execute(cmd)
    lesson_row = cur.fetchone()

    if lesson_row is None:
        print(f"\nLesson {vlid} does not exist.\n")
        return

    (vlid_db, topic, language, start_time, end_time, current_attendees) = lesson_row

    tmpl_check = '''
SELECT uid
  FROM Attendance
 WHERE uid = %s AND vlid = %s;
'''
    cmd = cur.mogrify(tmpl_check, (uid, vlid))
    print_cmd(cmd)
    cur.execute(cmd)
    already = cur.fetchone()

    if already:
        print(f"\nUser {uid} is already registered for lesson {vlid} ({topic}, {language}).\n")
        return

    tmpl_insert = '''
INSERT INTO Attendance(uid, vlid)
VALUES (%s, %s);
'''
    cmd = cur.mogrify(tmpl_insert, (uid, vlid,))
    print_cmd(cmd)
    cur.execute(cmd)
    conn.commit()

    print("SUCCESSFULLY JOINED LESSON")
    print(f"User:        {uid}")
    print(f"Lesson ID:   {vlid_db}")
    print(f"Topic:       {topic}")
    print(f"Language:    {language}")
    print(f"Start time:  {start_time}")
    print(f"End time:    {end_time}")

list_virtual_lessons()

uid_input = int(input("Enter your user ID (uid): ").strip())
vlid_input = int(input("Enter the lesson ID (vlid) you want to join: ").strip())

join_virtual_lesson(uid_input, vlid_input)
