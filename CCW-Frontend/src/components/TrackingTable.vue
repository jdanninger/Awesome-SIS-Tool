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
    <v-dialog width="80%">
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" text="Open Dialog"> </v-btn>
      </template>

      <template v-slot:default="{ isActive }">
        <v-card title="Dialog">
          <v-card-text>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn
              text="Close Dialog"
              @click="isActive.value = false"
            ></v-btn>
        </v-card-actions>
        </v-card>
      </template>
    </v-dialog>
   
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
        

      }
    }
    }
  </script>