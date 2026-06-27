from common import *

us = '''
* Simple US5: View average daily XP

   As a:  Language Learner
 I want:  To see my average daily XP earned across all lessons
So That: I can understand my overall learning pace and improve my study habits
'''

print(us)

def show_avg_daily_xp(uid):

    cols = 'uid avg_daily_xp total_entries'

    tmpl = '''
SELECT lp.uid, ROUND(AVG(lp.daily_xp), 2) AS avg_daily_xp, COUNT(lpid) AS total_entries
  FROM Lesson_Progress AS lp
 WHERE lp.uid = %s
 GROUP BY lp.uid;
'''

    cmd = cur.mogrify(tmpl, (uid,))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()

    if not rows:
        print(f"No lesson progress found for user {uid}.\n")
        return

    show_table(rows, cols)

    avg_xp = rows[0][1]
    total = rows[0][2]

    print(f"\nUser {uid} has an average of {avg_xp:.2f} XP over {total} lessons.")

uid = int(input("Enter user ID (uid): ").strip())
show_avg_daily_xp(uid)
