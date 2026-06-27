from common import *

us = '''
* Simple US1: Track Props (boosters)

   As a:  Language Learner
 I want:  To keep track of my unused props (streak-freezer etc.)
So That:  I am constantly engaging with the gamification features of Duolingo
'''

print(us)

def show_user_props(user_id):

    cols = 'p.pid p.name p.type u.uid u.email'

    tmpl = '''
SELECT p.pid, p.name, p.type, u.uid, u.email
  FROM Prop AS p
       JOIN Users AS u ON (p.uid = u.uid)
 WHERE u.uid = %s
 ORDER BY p.type, p.name;
'''

    cmd = cur.mogrify(tmpl, (user_id,))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()

    if not rows:
        print(f"User {user_id} has no props.")
    else:
        show_table(rows, cols)

uid = int(input("Enter user ID (uid): "))
show_user_props(uid)
