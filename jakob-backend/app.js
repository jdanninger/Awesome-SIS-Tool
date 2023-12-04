const express = require("express");
const app = express ();
app.use(express.json())

const port = process.env.PORT || 3000;

users = [{username : "jakobD", email: "jkd50@case.edu", password : "admin", queries : []}]


app.listen(port, () => {
    console.log("Server Listening on PORT:", port);
  });

// ^*^*^*^*^*^*^*^*^*^* REGISTER ^*^*^*^*^*^*^*^*^*^* 
  app.post("/register", (request, response) => {
    var status = {
        "Status": "registered"
     };
     let em = request.query.email
     let un = request.query.username
     let error = false

    for (let n = 0; n < users.length; n++) {
        if (users[n].email == em) {
            status = {
                "Status": "email already taken"
            }
            error = true;
        }
    }

    for (let n = 0; n < users.length; n++) {
        if (users[n].username == un) {
            status = {
                "Status": "username already taken"
            }
            error = true;
        }
    }

    if (!error) {
        users.push({username : un, email: em, password : request.query.password, queries : []})
    }
    
    response.send(status);
 });

 //^*^*^*^*^*^*^*^*^*^*  login ^*^*^*^*^*^*^*^*^*^* 
app.post("/login", (request, response) => {
    var status = {
       "Status": "invalid"
    };
    let username = request.query.username
    let password = request.query.password

    for (let n = 0; n < users.length; n++) {
        if (users[n].username == username && users[n].password == password) {
            status = {
                "Status": "valid"
            }
        }
    }


    response.send(status);
 });



// ^*^*^*^*^*^*^*^*^*^* status ^*^*^*^*^*^*^*^*^*^* 
  app.get("/status", (request, response) => {
    const status = {
       "Status": "Running"
    };
    response.send(status);
 });




