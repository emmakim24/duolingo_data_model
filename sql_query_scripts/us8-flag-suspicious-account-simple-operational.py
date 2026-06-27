import psycopg2

conn = psycopg2.connect(dbname="project", user="isdb", host="localhost")
cur = conn.cursor()

us = '''
User Story 8: Flag Suspicious Account

   As a:  Operation
 I want:  To flag a user account as suspicious
So That:  I can investigate potentially problematic accounts and maintain platform safety
'''

print(us)

def flag_suspicious_account(user_id, reason):
    """
    Flag a user account as suspicious by:
    1. Adding entry to sus_account table with is_resolved=false
    2. Setting user's valid status to false
    """
    
    print("\n" + "="*80)
    print("TABLES BEFORE FLAGGING:")
    print("="*80)
    
    print(f"\nUser {user_id} details:")
    cur.execute("SELECT uid, email, valid FROM users WHERE uid = %s", (user_id,))
    user = cur.fetchall()
    for row in user:
        print(row)
    
    if not user:
        print(f"ERROR: User {user_id} not found!")
        return
    
    print("\nAll flagged accounts:")
    cur.execute("SELECT flag_id, Users_uid, reason, is_resolved FROM sus_account ORDER BY flag_id")
    for row in cur.fetchall():
        print(row)
    
    print("\n" + "="*80)
    print("EXECUTING FLAG:")
    print("="*80)
    
    cur.execute("SELECT MAX(flag_id) FROM sus_account")
    max_id = cur.fetchall()[0][0]
    next_id = 1 if max_id is None else max_id + 1
    
    query1 = '''
INSERT INTO sus_account (flag_id, reason, is_resolved, Users_uid)
VALUES (%s, %s, %s, %s)
'''
    print(f"\n1. {query1}")
    print(f"   Values: ({next_id}, '{reason}', false, {user_id})")
    cur.execute(query1, (next_id, reason, False, user_id))
    
    query2 = "UPDATE users SET valid = false WHERE uid = %s"
    print(f"2. {query2} with uid={user_id}")
    cur.execute(query2, (user_id,))
    
    conn.commit()
    
    print("\n" + "="*80)
    print("TABLES AFTER FLAGGING:")
    print("="*80)
    
    print(f"\nUser {user_id} details (now flagged):")
    cur.execute("SELECT uid, email, valid FROM users WHERE uid = %s", (user_id,))
    for row in cur.fetchall():
        print(row)
    
    print("\nAll flagged accounts (showing new entry):")
    cur.execute("SELECT flag_id, Users_uid, reason, is_resolved FROM sus_account ORDER BY flag_id")
    for row in cur.fetchall():
        print(row)
    
    print("\n" + "="*80)
    print(f"SUCCESS: User {user_id} flagged as suspicious")
    print(f"Reason: {reason}")
    print("User account set to invalid until issue is resolved")
    print("="*80)

flag_suspicious_account(3, "Automated bot behavior detected")

cur.close()
conn.close()
