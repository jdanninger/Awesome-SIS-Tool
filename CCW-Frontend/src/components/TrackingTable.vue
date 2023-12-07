<template>
    <v-card>
    <v-container>
    <v-table>
      <thead>
        <tr>
          <th class="text-left">
            Code
          </th>
          <th class="text-left">
            Number
          </th>
          <th class="text-left">
            Name
          </th>
          <th class="text-left">
            Days
          </th>
          <th class="text-left">
            Time
          </th>
          <th>
            
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in courses"
          :key="item.name"
        >
          <td>{{ item.course_code }}</td>
          <td>{{ item.course_id }}</td>
          <td>{{ item.course_name }}</td>
          <td>{{ item.days }}</td>
          <td>{{ item.time }}</td>
          <td><v-btn @click = "del_row(item)"> <v-icon icon="mdi-close-circle-outline"/> </v-btn></td>
        </tr>
      </tbody>
    </v-table>
    </v-container>
    </v-card>
    <br>


  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      persistent
      width="1024"
    >
      <template v-slot:activator="{ props }">
        <v-btn
          color="primary"
          v-bind="props"
        >
          New Search
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">New Search</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                :rules="[value => !!value || 'Required']"
                  label="Class Code*"
                  v-model="code"
                ></v-text-field>                
              </v-col>

              <v-col
                cols="12"
                sm="6"
                md="4"
              >
              <v-text-field
                  label="Class Name"
                  v-model="name"
                ></v-text-field>
              </v-col>

              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  label="Class Section"
                  v-model="section"
                ></v-text-field>
              </v-col>
              
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
              <v-autocomplete
                  :items="['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']"
                  v-model="days"
                  label="Days Offered"
                  multiple
                ></v-autocomplete>
                <v-text-field
                  label="Professor"
                  v-model="professor"
                ></v-text-field>
              </v-col>

              <v-col
                cols="12"
                sm="6"
                md="4"
              >
              <v-autocomplete
                  :items="['8am', '9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm', '8pm', '9pm', '10pm',]"
                  label="Starts on or after"
                  multiple
                ></v-autocomplete>
              </v-col>

              <v-col
                cols="12"
                sm="6"
                md="4"
              >
              <v-autocomplete
                  :items="['8am', '9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm', '8pm', '9pm', '10pm',]"
                  label="End on or before"
                  multiple
                ></v-autocomplete>
              </v-col>
              

            
            </v-row>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue-darken-1"
            variant="text"
            @click="dialog = false"
          >
            Close
          </v-btn>
          <v-btn
            color="blue-darken-1"
            variant="text"
            @click="submit"
          >
            Add
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
    
   
  </template>



<style>
    .center-below {
        top: 3.5%;
        left: 45%;
    }

</style>



  <script>
  import $ from 'jquery';
    export default {
      data () {
        return {
          un : '',
          days:[],
          code: '',
          number: '',
          section: '',
          dialog: false,
          courses: null,
          professor: '',
          name: '',
        }
      },
      mounted() {
        this.un = this.$route.path.slice(10)
        console.log(this.un)
        var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        var raw = JSON.stringify({
          "user_name": this.un
        });

        var requestOptions = {
          method: 'POST',
          headers: myHeaders,
          body: raw,
          redirect: 'follow'
        };

        fetch("http://localhost:8000/api/get-tracked-courses", requestOptions)
          .then(response => response.text())
          .then(result =>  {
            this.courses = JSON.parse(result); 
            if (this.courses[0] == null){
              console.log("here")
              this.courses = []
            }
            console.log(this.courses)
          })
          .catch(error => console.log('error', error));

        

      },
      methods: {
      del_row (item) {



        // do server stuff here!
        console.log(item)
        this.courses = this.courses.filter((obj) => {
          return obj != item
        })
      },
      async submit(event){

        var settings = {
          "url": "http://localhost:8000/api/add-course",
          "method": "POST",
          "timeout": 0,
          "headers": {
            "Content-Type": "application/json"
          },
          "data": JSON.stringify({
            "course_id": this.number,
            "course_code": this.code,
            "days": "Mon Wed Fri",
            "time": "9:00-11:00pm",
            "course_name": this.name,
            "professor": this.professor,
            "section": this.section,
            "user_name": this.un
          }),
        };

        $.ajax(settings).done(function (response) {
          console.log(response);
        }); 


        this.courses.push(
          {
            "course_id": this.number,
            "course_code": this.code,
            "days": "Mon Wed Fri",
            "time": "9:00-11:00pm",
            "course_name": this.name,
            "professor": this.professor,
            "section": this.section,
            "user_name": this.un
          }
        )
        // add to server stuff



      },
    }
    }



  </script>