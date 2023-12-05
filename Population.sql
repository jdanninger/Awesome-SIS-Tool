
-- Add a new column 'NewColumnName' to table 'TableName' in schema 'SchemaName'
ALTER TABLE courseinfo
  ADD USER_NAME /*new_column_name*/ VARCHAR(30) /*new_column_datatype*/ ; /*new_column_nullability*/



/*CREATE TABLE courseInfo2(
    course_code VARCHAR(50),
    course_ID SERIAL PRIMARY KEY,
    course_name VARCHAR(50),
    section VARCHAR(50),
    professor VARCHAR(50),
    days VARCHAR(10),
    time VARCHAR(20)
);

INSERT INTO courseInfo2(course_code,course_ID, course_name, section, professor, days, time)
SELECT course_name, course_code, professor, days, time, course_ID
FROM courseinfo;

DROP TABLE courseinfo;

*/

/*INSERT INTO courseinfo (
    course_code,
    days,
    time,
    course_name,
    professor
  )
VALUES (
    'CSDS 233',
    'TTh',
    '1:00-2:15pm',
    'Introduction to Data Structures',
    'H Podgurski'
  );

  INSERT INTO courseinfo (
    course_code,
    days,
    time,
    course_name,
    professor
  )
VALUES (
    'CSDS 234',
    'MWF',
    '12:00-1:00pm',
    'Structured and Unstructured Data',
    'Harold Connamacher'
  );

INSERT INTO courseinfo (
    course_code,
    days,
    time,
    course_name,
    professor
  )
VALUES (
    'CSDS 236',
    'MWF',
    '2:00-3:00pm',
    'Introduction to C/C++ Programming',
    'Harold Connamacher'
  );

  INSERT INTO courseinfo (
    course_code,
    days,
    time,
    course_name,
    professor
  )
VALUES (
    'CSDS 245',
    'MWF',
    '12:00-1:00pm',
    'Functional Programming in Java',
    'Harold Connamacher'
  );

  INSERT INTO courseinfo (
    course_code,
    days,
    time,
    course_name,
    professor
  )
VALUES (
    'CSDS 275',
    'MWF',
    '12:00-1:00pm',
    'Fundamentals of Robotics',
    'N Barendt'
  );

   INSERT INTO courseinfo (
    course_code,
    days,
    time,
    course_name,
    professor
  )
VALUES (
    'CSDS 281',
    'TTh',
    '10:00-11:15am',
    'Logic Design and Computer Organization',
    'E Gurkan Cavusoglu'
  );

INSERT INTO courseinfo (
    course_code,
    days,
    time,
    course_name,
    professor
  )
VALUES (
    'CSDS 285',
    'TTh',
    '5:30-6:45pm',
    'Linux Tools and Scripting',
    'R Loui'
  );


  INSERT INTO courseinfo (
    course_code,
    days,
    time,
    course_name,
    professor
  )
VALUES (
    'CSDS 290',
    'TTh',
    '5:30-6:45pm',
    'Introduction to Game Design',
    'M Fu'
  );

 INSERT INTO courseinfo (
    course_code,
    days,
    time,
    course_name,
    professor
  )
VALUES (
    'CSDS 293',
    'MWF',
    '12:00-1:00pm',
    'Software Craftsmanship',
    'Harold Connamacher'
  );

 INSERT INTO courseinfo (
    course_code,
    days,
    time,
    course_name,
    professor
  )
VALUES (
    'CSDS 302',
    'MW',
    '12:45-2:00pm',
    'Discrete Mathematics',
    'S Xu'
  );

INSERT INTO courseinfo (
    course_code,
    days,
    time,
    course_name,
    professor
  )
VALUES (
    'CSDS 305',
    'TTh',
    '12:00-1:00pm',
    'Files, Indexes, and Access Structures',
    'S Xu'
  );

  INSERT INTO courseinfo (
    course_code,
    days,
    time,
    course_name,
    professor
  )
VALUES (
    'CSDS 310',
    'MWF',
    '9:30-10:20am',
    'Algorithms',
    'M Koyuturk'
  );


  INSERT INTO courseinfo (
    course_code,
    days,
    time,
    course_name,
    professor
  )
VALUES (
    'CSDS 312',
    'MW',
    '5:30-6:45pm',
    'Introduction to Data Science',
    'S Gajurel'
  );


 INSERT INTO courseinfo (
    course_code,
    days,
    time,
    course_name,
    professor
  )
VALUES (
    'CSDS 313',
    'MW',
    '12:40-2:00pm',
    'Introduction of Data Analysis',
    'M Koyuturk'
  );
*/

--Already added 
/*INSERT INTO courseinfo (
    course_code,
    days,
    time,
    course_name,
    professor
  )
VALUES (
    'CSDS 133',
    'MW',
    '12:45-2:00pm',
    'Introduction to Data Science',
    'L Bruckman'
  );

INSERT INTO courseinfo (
    course_code,
    days,
    time,
    course_name,
    professor
  )
VALUES (
    'CSDS 221',
    'MW',
    '7:00-9:00pm',
    'Full Stack Web Development',
    'D Izandnegahdar'
  );

*/


