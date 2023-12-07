<template>
    <v-sheet width="300" class="mx-auto center">
        <v-form @submit.prevent>
            <v-text-field
                v-model = "email"
                :rules="email_rules"
                label="Email"
                type="text"
            ></v-text-field>

            <v-text-field
                v-model = "username"
                :rules="username_rules"
                label="Username"
                type="text"

            ></v-text-field>


            <v-text-field type="password"
                v-model = "password"
                :rules="password_rules"
                label="Password"
            ></v-text-field>

            <v-text-field type="password"
                v-model = "conf_password"
                :rules="[() => this.conf_password == this.password || 'Passwords must match']" 
                label="Confirm Password"

            ></v-text-field>
            
            <v-btn @click = "submit" type="submit" block class="mt-2">Submit</v-btn>
        </v-form>
    </v-sheet>   
</template>
    
    <style>
      .mx-auto.center {
        width: 5px;
        margin-top: 50px;
        border: 3px solid green;
      }
    </style>
    
    <script>
import $ from 'jquery';
  export default {
    data: () => ({
      email: '',
      username: '',
      password: '',
      conf_password: '',
      email_rules: [
        email => {
          if (email) {
            if (String(email).toLowerCase().match(/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)) {
                return true
            }
            return 'invalid email'
          }
          return 'You must enter an email'
        },
      ],
      username_rules: [
        username => {
            if (String(username)) {
                return true
            }
            return 'You must choose a username'
        }
      ],
      password_rules: [
        password => {
            if (String(password).length >= 6) {
                return true
            }
            return 'your password must be at least 6 chars'
        }

      ],
      conf_password_rules: [
        password => {
            
            console.log(String(this.data.password))
            if (String(password) == String(Vue)) {
                return true
            }
            return 'passwords must match'
        }
      ]
    }),

    methods: {
      async submit (event) {
        let valid_email = String(this.email).toLowerCase().match(/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)
        let valid_password = String(this.password).length >= 6
        let valid_conf_password = String(this.password) == String(this.conf_password)
        // can add username validation and see if email is already registerd!
        if (!valid_email) {

        } else if (!valid_password) {

        } else if (!valid_conf_password) {

        } else {

          var settings = {
            "url": "http://localhost:8000/api/sign-up",
            "method": "POST",
            "timeout": 0,
            "headers": {
              "Content-Type": "application/json"
            },
            "data": JSON.stringify({
              "username": this.username,
              "password": this.password,
              "email": this.email
            }),
          };

          $.ajax(settings).done(function (response) {
            console.log(response)
            if (response.message == "SUCCESS") {
              window.location.href = "/login"
            } else {
              alert("registration failed!")
            }
          });




            //todo: send data to server!
            // window.location.href = "/login"
            return
        }


      },
    },

  }

    </script>
    