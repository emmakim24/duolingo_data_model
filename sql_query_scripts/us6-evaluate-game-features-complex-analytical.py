#!/usr/bin/env python3

import psycopg2
conn = psycopg2.connect(dbname="project", user="isdb", host="localhost")
cur = conn.cursor()

# User Story
us = '''
User Story 6: Evaluate Game Features

   As a:  Content creator
 I want:  To measure how different gamified elements affect lesson completion rates
So That:  I can determine which engagement tools are most effective
'''

print(us)

def evaluate_game_features():
    """
    Evaluate effectiveness of different game feature types
    Shows completion rates, scores, and engagement by feature type
    """
    
    print("\n" + "="*80)
    print("TABLES BEFORE QUERY:")
    print("="*80)
    
    print("\nLesson table:")
    cur.execute("SELECT * FROM lesson")
    for row in cur.fetchall():
        print(row)
    
    print("\nGame_feature table:")
    cur.execute("SELECT * FROM game_feature")
    for row in cur.fetchall():
        print(row)
    
    print("\nDesign_metric table:")
    cur.execute("SELECT * FROM design_metric")
    for row in cur.fetchall():
        print(row)
    
    print("\n" + "="*80)
    print("EXECUTING QUERY:")
    print("="*80)
    
    query = '''
SELECT gf.type AS game_feature_type,
       COUNT(gf.feature_id) AS feature_count,
       ROUND(AVG(dm.completion_rate), 2) AS avg_completion_rate,
       ROUND(AVG(dm.avg_score), 2) AS avg_score,
       ROUND(AVG(dm.engagement_level), 2) AS avg_engagement_level
  FROM game_feature gf
       JOIN design_metric dm ON gf.feature_id = dm.game_feature_feature_id
       JOIN lesson l ON gf.lesson_lid = l.lid
 WHERE gf.is_active = true
 GROUP BY gf.type
 ORDER BY avg_completion_rate DESC
'''
    
    print(query)
    
    cur.execute(query)
    rows = cur.fetchall()
    
    print("\n" + "="*80)
    print("RESULTS:")
    print("="*80)
    
    print("\nGame Feature Effectiveness Analysis:")
    print("-" * 80)
    for row in rows:
        print(f"Type: {row[0]}")
        print(f"  Feature Count: {row[1]}")
        print(f"  Avg Completion Rate: {row[2]}%")
        print(f"  Avg Score: {row[3]}")
        print(f"  Avg Engagement: {row[4]}/10")
        print()
    
    if rows:
        best = rows[0]
        print("="*80)
        print(f"MOST EFFECTIVE: {best[0]} with {best[2]}% completion rate")
        print("="*80)

evaluate_game_features()

cur.close()
conn.close()

