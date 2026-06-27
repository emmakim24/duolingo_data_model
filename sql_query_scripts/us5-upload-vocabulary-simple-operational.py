import psycopg2

conn = psycopg2.connect(dbname="project", user="isdb", host="localhost")
cur = conn.cursor()

us = '''
User Story 5: Upload Vocabulary

   As a:  Content creator
 I want:  To upload new vocabulary items with their translations and example sentences
So That:  I can expand the learning content for students
'''

print(us)

def upload_vocabulary(vocab_word, translation, example, difficulty, lesson_id):
    """
    Upload a new vocabulary item to the database
    """
    
    print("\n" + "="*80)
    print("TABLES BEFORE INSERT:")
    print("="*80)
    
    print("\nVocabulary table:")
    cur.execute("SELECT * FROM vocabulary ORDER BY vocab_id")
    for row in cur.fetchall():
        print(row)

    print("\nLesson table:")
    cur.execute("SELECT lid, name, cid FROM lesson ORDER BY lid")
    for row in cur.fetchall():
        print(row)
    
    print("\n" + "="*80)
    print("EXECUTING INSERT:")
    print("="*80)
    
    cur.execute("SELECT MAX(vocab_id) FROM vocabulary")
    max_id = cur.fetchall()[0][0]
    next_id = 1 if max_id is None else max_id + 1
    
    query = '''
INSERT INTO vocabulary (vocab_id, vocab, translation, example_sentence, difficulty_level, Lesson_lid)
VALUES (%s, %s, %s, %s, %s, %s)
'''
    
    print(f"\nQuery: {query}")
    print(f"Values: ({next_id}, '{vocab_word}', '{translation}', '{example}', {difficulty}, {lesson_id})")
    
    cur.execute(query, (next_id, vocab_word, translation, example, difficulty, lesson_id))
    conn.commit()
    
    print("\n" + "="*80)
    print("TABLES AFTER INSERT:")
    print("="*80)
    
    print("\nVocabulary table (showing new entry):")
    cur.execute("SELECT * FROM vocabulary ORDER BY vocab_id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    print("\n" + "="*80)
    print(f"SUCCESS: Added vocabulary item '{vocab_word}' to lesson {lesson_id}")
    print("="*80)

upload_vocabulary("libro", "book", "Me gusta leer un libro means I like to read a book", 1, 1)

cur.close()
conn.close()
