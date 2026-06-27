from common import *

us = '''
* Complex US2: View Leaderboard Rank

   As a:  Language Learner
 I want:  To see my rank and status against other learners on a leaderboard
So That:  I can track my progress and stay motivated to improve
'''

print(us)

def view_leaderboard_rank(lbid, uid):

    cols = 'rank points uid streak_count daily_xp language'

    tmpl = f'''
SELECT lbs.rank, lbs.points, u.uid, lp.streak_count, lp.daily_xp, c.language
  FROM Leaderboard_Spot AS lbs
       JOIN Lesson_Progress AS lp ON lbs.lpid = lp.lpid
       JOIN Users AS u ON lp.uid = u.uid
       JOIN Courses AS c ON lp.cid = c.cid
       JOIN Leaderboard AS lb ON lbs.lbid = lb.lbid
 WHERE lb.lbid = %s
 ORDER BY lbs.rank ASC;
'''

    cmd = cur.mogrify(tmpl, (lbid,))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()

    show_table(rows, cols)
    found = False
    for r in rows:
        if r[2] == uid:     # r[2] = uid
            found = True
            print("USER FOUND")
            print(f"Rank:         {r[0]}")
            print(f"Points:       {r[1]}")
            print(f"User ID:      {r[2]}")
            print(f"Streak Count: {r[3]}")
            print(f"Daily XP:     {r[4]}")
            print(f"Language:     {r[5]}")
            print(f"\nYou are ranked #{r[0]} out of {len(rows)} learners.\n")
            break

    if not found:
        print(f"User {uid} not found on leaderboard {lbid}.\n")


lbid_input = int(input("Enter leaderboard ID (lbid): ").strip())
uid_input = int(input("Enter user ID (uid): ").strip())

view_leaderboard_rank(lbid_input, uid_input)
