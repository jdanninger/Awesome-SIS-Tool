
--Already created tables 
/*CREATE TABLE searchHistory (
    username VARCHAR(20) NOT NULL, 
    course_ID INT NOT NULL, 
    date_searched VARCHAR(10) NOT NULL, 
    PRIMARY KEY(username, course_ID), 
    FOREIGN KEY(username) REFERENCES Login(username), 
    FOREIGN KEY(course_ID) REFERENCES CourseInfo(course_ID)
);


*/

/*create table Login(
    username VARCHAR(20) NOT NULL, 
    password VARCHAR(20) NOT NULL, 
    email VARCHAR(20) NOT NULL, 
    PRIMARY KEY(username)
);
*/


/*create table CourseInfo(
    course_ID SERIAL PRIMARY KEY, 
    course_code VARCHAR(20) NOT NUll, 
    course_name VARCHAR(20) NOT NULL, 
    professor VARCHAR(20) NOT NULL, 
    days VARCHAR(10) NOT NULL,
    time VARCHAR(20) NOT NULL
);
*/

/*create table trackedCourses(
    username VARCHAR(20) NOT NULL, 
    course_ID INT NOT NULL, 
    PRIMARY KEY(username, course_ID), 
    FOREIGN KEY(username) REFERENCES login(username), 
    FOREIGN KEY(course_ID) REFERENCES courseinfo(course_ID)
);
*/