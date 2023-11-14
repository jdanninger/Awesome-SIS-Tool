use `case-coursewatch`;

/* Login population*/
insert into Login(username, password, email)
values('nxp330', 'Neha0315!', 'nxp330@case.edu');

insert into Login(username, password, email)
values('gcm49', 'password', 'gcm49@case.edu');

insert into Login(username, password, email)
values('taylorSwift', 'swiftie523', 'ts234@case.edu');

insert into Login(username, password, email)
values('justinBieber', 'bieber894', 'jb527@case.edu');

insert into Login(username, password, email)
values('drake', 'Drakebaby257', 'drake346@case.edu');

/* CourseInfo population*/
insert into CourseInfo(course_code, course_name, professor, days, time)
values('CSDS 101', 'The Digital Revolution: Computer and Data Science for All'
, 'Harold Connamacher', 'M W F', '12:30-1:30pm');

insert into CourseInfo(course_code, course_name, professor, days, time)
values('CSDS 132', 'Programming in Java'
, 'O Ozguner', 'M W F', '2:15-3:05pm');

insert into CourseInfo(course_code, course_name, professor, days, time)
values('CSDS 133', 'Introduction to Data Science and Engineering for Majors'
, 'L Bruckman', 'M W', '12:45-2:00pm');

insert into CourseInfo(course_code, course_name, professor, days, time)
values('CSDS 221', 'Full Stack Web Development'
, 'D Izandnegahdar', 'M W', '7:00-9:00pm');

insert into CourseInfo(course_code, course_name, professor, days, time)
values('CSDS 233', 'Introduction to Data Structures'
, 'H Podgurski', 'T Th', '1:00-2:15pm');

insert into CourseInfo(course_code, course_name, professor, days, time)
values('CSDS 234', 'Structured and Unstructured Data'
, 'Harold Connamacher', 'M W F', '12:00-1:00pm');

insert into CourseInfo(course_code, course_name, professor, days, time)
values('CSDS 236', 'Introduction to C/C++ Programming'
, 'Harold Connamacher', 'M W F', '2:00-3:00pm');

insert into CourseInfo(course_code, course_name, professor, days, time)
values('CSDS 245', 'Functional Programming in Java'
, 'Harold Connamacher', 'M W F', '12:00-1:00pm');

insert into CourseInfo(course_code, course_name, professor, days, time)
values('CSDS 275', 'Fundamentals of Robotics'
, 'N Barendt', 'M W F', '12:00-1:00pm');

insert into CourseInfo(course_code, course_name, professor, days, time)
values('CSDS 281', 'Logic Design and Computer Organization'
, 'E Gurkan Cavusoglu', 'T Th', '10:00-11:15am');

insert into CourseInfo(course_code, course_name, professor, days, time)
values('CSDS 285', 'Linux Tools and Scripting'
, 'R Loui', 'T Th', '5:30-6:45pm');

insert into CourseInfo(course_code, course_name, professor, days, time)
values('CSDS 290', 'Introduction to Computer Game Design and Implementation'
, 'M Fu', 'T Th', '8:30-9:45am');

insert into CourseInfo(course_code, course_name, professor, days, time)
values('CSDS 293', 'Software Craftsmanship'
, 'Harold Connamacher', 'M W F', '12:00-1:00pm');

insert into CourseInfo(course_code, course_name, professor, days, time)
values('CSDS 302', 'Discrete Mathematics'
, 'S Xu', 'M W', '12:45-2:00pm');

insert into CourseInfo(course_code, course_name, professor, days, time)
values('CSDS 305', 'Files, Indexes, and Access Structures for Big Data'
, 'S Xu', 'T Th', '12:00-1:00pm');

insert into CourseInfo(course_code, course_name, professor, days, time)
values('CSDS 310', 'Algorithms'
, 'M Koyuturk', 'M W F', '9:30-10:20am');

insert into CourseInfo(course_code, course_name, professor, days, time)
values('CSDS 312', 'Introduction to Data Science Systems'
, 'S Gajurel', 'M W', '5:30-6:45pm');

insert into CourseInfo(course_code, course_name, professor, days, time)
values('CSDS 313', 'Introduction of Data Analysis'
, 'M Koyuturk', 'M W', '12:40-2:00pm');

/* SearchHistory population*/
insert into searchHistory(username, course_id, date_searched)
values('nxp330', '2', '2023-11-13 20:30:00');

insert into searchHistory(username, course_id, date_searched)
values('nxp330', '10', '2023-11-13 10:30:00');

insert into searchHistory(username, course_id, date_searched)
values('nxp330', '12', '2023-11-13 8:30:00');

insert into searchHistory(username, course_id, date_searched)
values('nxp330', '3', '2023-11-13 19:00:12');

insert into searchHistory(username, course_id, date_searched)
values('nxp330', '8', '2023-11-13 19:30:30');

insert into searchHistory(username, course_id, date_searched)
values('nxp330', '6', '2023-11-13 19:32:23');


insert into searchHistory(username, course_id, date_searched)
values('gcm49', '4', '2023-10-13 20:30:00');

insert into searchHistory(username, course_id, date_searched)
values('gcm49', '8', '2023-10-13 10:30:00');

insert into searchHistory(username, course_id, date_searched)
values('gcm49', '2', '2023-10-13 8:30:00');

insert into searchHistory(username, course_id, date_searched)
values('gcm49', '1', '2023-9-13 19:00:12');

insert into searchHistory(username, course_id, date_searched)
values('gcm49', '3', '2023-9-13 19:30:30');

insert into searchHistory(username, course_id, date_searched)
values('gcm49', '8', '2023-9-13 19:32:23');

/* TrackHistory population*/

insert into trackedCourses(username, course_id)
values('gcm49', '5');

insert into trackedCourses(username, course_id)
values('gcm49', '7');

insert into trackedCourses(username, course_id)
values('gcm49', '9');

insert into trackedCourses(username, course_id)
values('nxp330', '3');

insert into trackedCourses(username, course_id)
values('nxp330', '9');

insert into trackedCourses(username, course_id)
values('nxp330', '5');

insert into trackedCourses(username, course_id)
values('nxp330', '4');



