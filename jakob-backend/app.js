const express = require("express");
const app = express ();
app.use(express.json())

const port = process.env.PORT || 3000;

users = [{username : "jakobD", email: "jkd50@case.edu", password : "admin", queries : [
    {"code" : "csds",
    "number" : "233",
    "section" : "123",
    "time" : "8:30",
    "days" : "M, W, F"
    }
]}];


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

 //^*^*^*^*^*^*^*^*^*^*  get queries ^*^*^*^*^*^*^*^*^*^* 
 app.get("/getq", (request, response) => {
    var status = {
       "Status": "failed"
    };
    let user = request.query.username

    for (let n = 0; n < users.length; n++) {
        if (users[n].username == user) {
            status = {
                "Status": "sucsess",
                "Queries": users[n].queries
            }
        }
    }


    response.send(status);
 });

 //^*^*^*^*^*^*^*^*^*^*  new queries ^*^*^*^*^*^*^*^*^*^* 
 app.post("/newq", (request, response) => {
    var status = {
       "Status": "failed"
    };
    let user = request.query.username
    for (let n = 0; n < users.length; n++) {
        if (users[n].username == user) {
            let cl = {
                "code" : request.query.code,
                "number" : request.query.number,
                "section" : request.query.section,
                "time" : request.query.time,
                "days" : request.query.days
            };

            users[n].queries.push(cl)
            status = {
                "Status": "sucsess",
            }
        }
    }

    response.send(status);
 });

 //^*^*^*^*^*^*^*^*^*^*  del query ^*^*^*^*^*^*^*^*^*^* 
 app.post("/delq", (request, response) => {
    console.log(users[0].queries)
    var status = {
       "Status": "failed"
    };
    let user = request.query.username
    for (let n = 0; n < users.length; n++) {
        
        if (users[n].username == user) {
            qs = users[n].queries
            for (let m = 0; m < qs.length; m++) {
                if (qs[m]["code"] == request.query.code && qs[m]["number"] == request.query.number) {
                    qs.splice(m,1)
                    status = {
                        "Status": "passed"
                     };
                    break;
                }
            
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




