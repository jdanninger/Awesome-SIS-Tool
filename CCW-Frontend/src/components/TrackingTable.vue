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
            Section
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
          <td>{{ item.code }}</td>
          <td>{{ item.number }}</td>
          <td>{{ item.section }}</td>
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
                  :rules="[value => !!value || 'Required']"
                  v-model="number"
                  label="Class Number*"
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
                  label="Days Offered"
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
    export default {
      data () {
        return {
          code: '',
          number: '',
          section: '',

          dialog: false,
          courses: [
            {
              code: 'CSDS',
              number: 233,
              section: 1234,
              days: "M W F",
              time: "8:30 am"
            },
            {
              code: 'CSDS',
              number: 132,
              section: 1234,
              days: "M W F",
              time: "8:30 am"
            },
            {
              code: 'ENGL',
              number: 101,
              section: 1234,
              days: "M W F",
              time: "8:30 am"
            },
            {
              code: 'USNA',
              number: 291,
              section: 1234,
              days: "M W F",
              time: "8:30 am"
            },
          ],
        }
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
        this.courses.push(
          {
            code: this.code,
              number: this.number,
              section: this.section,
              days: "M W F",
              time: "8:30 am"
          }
        )
      },
    }
    }
  </script>