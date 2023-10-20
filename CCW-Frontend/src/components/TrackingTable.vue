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
          v-for="item in Courses"
          :key="item.name"
        >
          <td>{{ item.code }}</td>
          <td>{{ item.number }}</td>
          <td>{{ item.section }}</td>
          <td>{{ item.days }}</td>
          <td>{{ item.time }}</td>
          <td><v-btn> <v-icon icon="mdi-close-circle-outline"/> </v-btn></td>
        </tr>
      </tbody>
    </v-table>
    </v-container>
    </v-card>

    <v-btn class = "center-below"> Add New Search</v-btn>
   
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
          Courses: [
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
    }
  </script>