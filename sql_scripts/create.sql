-- Created by Redgate Data Modeler (https://datamodeler.redgate-platform.com)
-- Last modification date: 2025-12-09 21:30:51.21

-- tables
-- Table: Attendance
CREATE TABLE Attendance (
    uid int  NOT NULL,
    vlid int  NOT NULL,
    join_time time  NOT NULL,
    leave_time time  NOT NULL,
    CONSTRAINT Attendance_pk PRIMARY KEY (uid,vlid)
);

-- Table: Courses
CREATE TABLE Courses (
    cid int  NOT NULL,
    language text  NOT NULL,
    state boolean  NOT NULL,
    CONSTRAINT Courses_pk PRIMARY KEY (cid)
);

-- Table: Courses_Taken
CREATE TABLE Courses_Taken (
    uid int  NOT NULL,
    cid int  NOT NULL,
    CONSTRAINT Courses_Taken_pk PRIMARY KEY (uid,cid)
);

-- Table: Design_metric
CREATE TABLE Design_metric (
    metric_id int  NOT NULL,
    completion_rate int  NOT NULL,
    avg_score int  NOT NULL,
    engagement_level int  NOT NULL,
    Game_feature_feature_id int  NOT NULL,
    CONSTRAINT Design_metric_pk PRIMARY KEY (metric_id)
);

-- Table: Exercise
CREATE TABLE Exercise (
    eid int  NOT NULL,
    name text  NOT NULL,
    type text  NOT NULL,
    accuracy int  NOT NULL,
    target_accuracy int  NOT NULL,
    num_attempts int  NOT NULL,
    score int  NOT NULL,
    lid int  NOT NULL,
    uid int  NOT NULL,
    CONSTRAINT Exercise_pk PRIMARY KEY (eid)
);

-- Table: Game_feature
CREATE TABLE Game_feature (
    feature_id int  NOT NULL,
    fname text  NOT NULL,
    type GF_TYPE  NOT NULL,
    description text  NOT NULL,
    is_active boolean  NOT NULL,
    Lesson_lid int  NOT NULL,
    CONSTRAINT Game_feature_pk PRIMARY KEY (feature_id)
);

-- Table: Leaderboard
CREATE TABLE Leaderboard (
    lbid int  NOT NULL,
    start_date date  NOT NULL,
    end_date date  NOT NULL,
    type LB_TYPE  NOT NULL,
    CONSTRAINT Leaderboard_pk PRIMARY KEY (lbid)
);

-- Table: Leaderboard_Spot
CREATE TABLE Leaderboard_Spot (
    lbsid int  NOT NULL,
    points int  NOT NULL,
    last_updated_date date  NOT NULL,
    last_updated_time time  NOT NULL,
    rank int  NOT NULL,
    lbid int  NOT NULL,
    lpid int  NOT NULL,
    CONSTRAINT Leaderboard_Spot_pk PRIMARY KEY (lbsid)
);

-- Table: Learners
CREATE TABLE Learners (
    uid int  NOT NULL,
    join_date date  NOT NULL,
    daily_goal text  NOT NULL,
    current_streak int  NOT NULL,
    highest_streak int  NOT NULL,
    last_goal_met_date date  NOT NULL,
    CONSTRAINT Learners_pk PRIMARY KEY (uid)
);

-- Table: Lesson
CREATE TABLE Lesson (
    lid int  NOT NULL,
    name text  NOT NULL,
    difficulty_level int  NOT NULL,
    description text  NOT NULL,
    skill text  NOT NULL,
    cid int  NOT NULL,
    Lesson_lid int  NOT NULL,
    CONSTRAINT Lesson_pk PRIMARY KEY (lid)
);

-- Table: Lesson_Progress
CREATE TABLE Lesson_Progress (
    lpid int  NOT NULL,
    streak_count int  NOT NULL,
    daily_xp int  NOT NULL,
    uid int  NOT NULL,
    cid int  NOT NULL,
    CONSTRAINT Lesson_Progress_pk PRIMARY KEY (lpid)
);

-- Table: Prop
CREATE TABLE Prop (
    pid int  NOT NULL,
    name text  NOT NULL,
    type text  NOT NULL,
    uid int  NOT NULL,
    CONSTRAINT Prop_pk PRIMARY KEY (pid)
);

-- Table: Users
CREATE TABLE Users (
    uid int  NOT NULL,
    email text  NOT NULL,
    valid boolean  NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY (uid)
);

-- Table: Virtual_Lesson
CREATE TABLE Virtual_Lesson (
    vlid int  NOT NULL,
    topic text  NOT NULL,
    language text  NOT NULL,
    start_time time  NOT NULL,
    end_time time  NOT NULL,
    CONSTRAINT Virtual_Lesson_pk PRIMARY KEY (vlid)
);

-- Table: Vocabulary
CREATE TABLE Vocabulary (
    vocab_id int  NOT NULL,
    vocab text  NOT NULL,
    translation text  NOT NULL,
    example_sentence text  NOT NULL,
    difficulty_level int  NOT NULL,
    Lesson_lid int  NOT NULL,
    CONSTRAINT Vocabulary_pk PRIMARY KEY (vocab_id)
);

-- Table: sus_account
CREATE TABLE sus_account (
    flag_id int  NOT NULL,
    reason text  NOT NULL,
    is_resolved boolean  NOT NULL,
    Users_uid int  NOT NULL,
    CONSTRAINT sus_account_pk PRIMARY KEY (flag_id)
);

-- foreign keys
-- Reference: Attendance_Learners (table: Attendance)
ALTER TABLE Attendance ADD CONSTRAINT Attendance_Learners
    FOREIGN KEY (uid)
    REFERENCES Learners (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Attendance_Virtual_Lesson (table: Attendance)
ALTER TABLE Attendance ADD CONSTRAINT Attendance_Virtual_Lesson
    FOREIGN KEY (vlid)
    REFERENCES Virtual_Lesson (vlid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Courses_Lesson (table: Lesson)
ALTER TABLE Lesson ADD CONSTRAINT Courses_Lesson
    FOREIGN KEY (cid)
    REFERENCES Courses (cid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Courses_Lesson_Progress (table: Lesson_Progress)
ALTER TABLE Lesson_Progress ADD CONSTRAINT Courses_Lesson_Progress
    FOREIGN KEY (cid)
    REFERENCES Courses (cid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Courses_Taken_Courses (table: Courses_Taken)
ALTER TABLE Courses_Taken ADD CONSTRAINT Courses_Taken_Courses
    FOREIGN KEY (cid)
    REFERENCES Courses (cid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Courses_Taken_Users (table: Courses_Taken)
ALTER TABLE Courses_Taken ADD CONSTRAINT Courses_Taken_Users
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Design_metric_Game_feature (table: Design_metric)
ALTER TABLE Design_metric ADD CONSTRAINT Design_metric_Game_feature
    FOREIGN KEY (Game_feature_feature_id)
    REFERENCES Game_feature (feature_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Exercise_Users (table: Exercise)
ALTER TABLE Exercise ADD CONSTRAINT Exercise_Users
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Game_feature_Lesson (table: Game_feature)
ALTER TABLE Game_feature ADD CONSTRAINT Game_feature_Lesson
    FOREIGN KEY (Lesson_lid)
    REFERENCES Lesson (lid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Leaderboard_Spot_Leaderboard (table: Leaderboard_Spot)
ALTER TABLE Leaderboard_Spot ADD CONSTRAINT Leaderboard_Spot_Leaderboard
    FOREIGN KEY (lbid)
    REFERENCES Leaderboard (lbid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Lesson_Exercise (table: Exercise)
ALTER TABLE Exercise ADD CONSTRAINT Lesson_Exercise
    FOREIGN KEY (lid)
    REFERENCES Lesson (lid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Lesson_Lesson (table: Lesson)
ALTER TABLE Lesson ADD CONSTRAINT Lesson_Lesson
    FOREIGN KEY (Lesson_lid)
    REFERENCES Lesson (lid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Lesson_Progress_Leaderboard_Spot (table: Leaderboard_Spot)
ALTER TABLE Leaderboard_Spot ADD CONSTRAINT Lesson_Progress_Leaderboard_Spot
    FOREIGN KEY (lpid)
    REFERENCES Lesson_Progress (lpid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Prop_Users (table: Prop)
ALTER TABLE Prop ADD CONSTRAINT Prop_Users
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Users_Learner (table: Learners)
ALTER TABLE Learners ADD CONSTRAINT Users_Learner
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Users_Lesson_Progress (table: Lesson_Progress)
ALTER TABLE Lesson_Progress ADD CONSTRAINT Users_Lesson_Progress
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Vocabulary_Lesson (table: Vocabulary)
ALTER TABLE Vocabulary ADD CONSTRAINT Vocabulary_Lesson
    FOREIGN KEY (Lesson_lid)
    REFERENCES Lesson (lid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: sus_account_Users (table: sus_account)
ALTER TABLE sus_account ADD CONSTRAINT sus_account_Users
    FOREIGN KEY (Users_uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

