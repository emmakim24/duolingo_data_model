from common import *

us = '''
* Simple US4: View a user's exercise accuracy

   As a:  Content Creator
 I want:  To view a user's accuracy scores for their exercises
So That: I can identify where they struggle and adjust content if needed
'''

print(us)

def show_user_exercise_accuracy(uid):

    cols = 'eid name type accuracy target_accuracy accuracy_dif num_attempts score'

    tmpl = '''
SELECT e.eid, e.name, e.type, e.accuracy, e.target_accuracy, (e.target_accuracy - e.accuracy) as "accuracy_dif", e.num_attempts, e.score
  FROM Exercise AS e
 WHERE e.uid = %s
 ORDER BY e.accuracy ASC;
'''

    cmd = cur.mogrify(tmpl, (uid,))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()

    if not rows:
        print(f"No exercises found for user {uid}.\n")
        return

    show_table(rows, cols)

uid = int(input("Enter user ID (uid): ").strip())
show_user_exercise_accuracy(uid)
