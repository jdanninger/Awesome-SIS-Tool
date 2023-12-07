<template>

  <v-sheet width="300" class="mx-auto center">
    <v-alert
      density="compact"
      type="warning"
      title="Alert"
      text="Username or Password is invalid"
      visible="false"
      v-if="bad_login"
    ></v-alert>

    <v-form @submit.prevent>
      <v-text-field
        label="Username"
        v-model="username"
      ></v-text-field>
      <v-text-field type="password"
        v-model="password"
        label="Password"
      ></v-text-field>
      <v-btn type="submit" block class="mt-2" @click = "submit">Submit</v-btn>
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
import { reactive } from 'vue';
import $ from 'jquery';
  export default {
    data: () => ({
      bad_login: false,
      username: "",
      password: ""
    }),
    methods: {
      async submit (event) {

        var settings = {
          "url": "http://localhost:8000/api/login",
          "method": "POST",
          "timeout": 0,
          "headers": {
            "Content-Type": "application/json"
          },
          "data": JSON.stringify({
            "username": this.username,
            "password": this.password,
          }),
        };
        let resp;
        this.$globalState.myGlobalVariable = this.username
        var name = this.username

        $.ajax(settings).done(function (response) {
          resp = resp
          console.log(response)
          if (response.message == "SUCCESS") {
            window.location.href = "/tracking/"+name
          } 
        });

        setTimeout(() => {
        this.bad_login = true;
        }, 250);
        

      }
    }
  }

</script>
