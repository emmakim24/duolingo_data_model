DROP database if EXISTS project;


CREATE database project;
\c project

CREATE TYPE LB_TYPE AS ENUM('League', 'Friends');
CREATE TYPE GF_TYPE AS ENUM ('PROGRESS_BAR', 'ACHIEVEMENT_BADGE', 'COMBO_METER', 'TIMED_CHALLENGE', 'STORY_MODE');

\i project_create.sql



\copy users(uid, email, valid) FROM data/users.csv csv header;
\copy learners(uid, join_date, daily_goal, current_streak, highest_streak, last_goal_met_date) FROM data/learners.csv csv header;
\copy courses(cid, language, state) FROM data/courses.csv csv header;
\copy courses_taken(uid,cid) FROM data/courses_taken.csv csv header;
\copy leaderboard(lbid, start_date, end_date, type) FROM data/leaderboard.csv csv header;
\copy lesson_progress(lpid, streak_count,daily_xp, uid, cid) FROM data/lesson_progress.csv csv header;
\copy leaderboard_spot(lbsid, points,last_updated_date, last_updated_time,rank, lbid, lpid) FROM data/leaderboard_spot.csv csv header;
\copy lesson(lid, name, difficulty_level, description, skill, cid, Lesson_lid) FROM data/lesson.csv csv header;
\copy exercise(eid, name, type, accuracy, target_accuracy, num_attempts, score, lid, uid) FROM data/exercise.csv csv header;
\copy prop(pid, name, type, uid) FROM data/prop.csv csv header;
\copy virtual_lesson(vlid, topic, language, start_time, end_time) FROM data/virtual_lesson.csv csv header;
\copy attendance(uid, vlid, join_time, leave_time) FROM data/attendance.csv csv header;
\copy game_feature(feature_id, fname, type, description, is_active, Lesson_lid) FROM data/game_feature.csv csv header;
\copy design_metric(metric_id, completion_rate, avg_score, engagement_level, Game_feature_feature_id) FROM data/design_metric.csv csv header;
\copy vocabulary(vocab_id, vocab, translation, example_sentence, difficulty_level, Lesson_lid) FROM data/vocabulary.csv csv header;
\copy sus_account(flag_id, reason, is_resolved, Users_uid) FROM data/sus_account.csv csv header;
