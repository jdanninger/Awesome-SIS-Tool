use `case-coursewatch`;

create table CourseInfo(
course_ID INT AUTO_INCREMENT PRIMARY KEY,
course_code VARCHAR (20) NOT NULL,
course_name VARCHAR(20) NOT NULL,
professor VARCHAR(20) NOT NULL,
days VARCHAR(10) NOT NULL, 
time VARCHAR(20) NOT NULL
);

create table Login(
username VARCHAR (20) NOT NULL, 
password VARCHAR (20) NOT NULL,
email VARCHAR (20) NOT NULL,
primary key(username)
);

create table searchHistory(
username VARCHAR (20) NOT NULL,
course_ID INT AUTO_INCREMENT,
date_searched VARCHAR(10) NOT NULL,
primary key(username, course_ID), 
foreign key(username) references Login(username), 
foreign key(course_ID) references CourseInfo(course_ID)
);

create table trackedCourses(
username VARCHAR (20) NOT NULL,
course_ID INT AUTO_INCREMENT,
primary key(username, course_ID), 
foreign key(username) references Login(username), 
foreign key(course_ID) references CourseInfo(course_ID)
); 


/*Error Code: 3780. Referencing column 'course_ID' and referenced column 'course_ID' in foreign key constraint 'searchhistory_ibfk_2' are incompatible.

*/
 





