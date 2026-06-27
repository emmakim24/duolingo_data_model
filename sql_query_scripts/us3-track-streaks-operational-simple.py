from common import *

us = '''
* Complex US3: Track streaks/ daily goals

   As a:  Language Learner
 I want:  To track streaks and daily goals
So That:  So I don’t lose progress, stay motivated and incline me to stay consistent
'''

print(us)

def show_streaks_and_goals(user_id):

    cols = 'u.uid u.email l.daily_goal l.current_streak l.highest_streak total_daily_xp total_streak_count'

    tmpl = '''
SELECT u.uid, u.email, l.daily_goal, l.current_streak, l.highest_streak, 
       COALESCE(SUM(lp.daily_xp), 0) AS total_daily_xp, COALESCE(SUM(lp.streak_count), 0) AS total_streak_count
  FROM Learners AS l
       JOIN Users AS u ON l.uid = u.uid
       LEFT JOIN Lesson_Progress AS lp ON l.uid = lp.uid
 WHERE l.uid = %s
 GROUP BY u.uid, u.email, l.daily_goal, l.current_streak, l.highest_streak;
'''

    cmd = cur.mogrify(tmpl, (user_id,))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()

    if not rows:
        print(f"User {user_id} not found as a learner.")
        return

    show_table(rows, cols)

    row = rows[0]
    daily_goal = int(row[2])
    total_daily_xp = int(row[5])

    if total_daily_xp >= daily_goal:
        print(f"\n Goal met! You earned {total_daily_xp} XP "
              f"today (goal: {daily_goal}).")
    else:
        print(f"\n Goal not met yet. You earned {total_daily_xp} XP "
              f"today (goal: {daily_goal}).")

uid = int(input("Enter user ID (uid): "))
show_streaks_and_goals(uid)
