<template>

  <v-sheet width="300" class="mx-auto center">
    <v-alert
      density="compact"
      type="warning"
      title="Alert title"
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
  export default {
    data: () => ({
      bad_login: false,
      username: "",
      password: ""
    }),
    methods: {
      async submit (event) {
        //Submit stuff code here .  . . if
          if(this.username == "admin" && this.password == "admin") {
            window.location.href = "/tracking"
          } else {
            this.bad_login = true
          }
          
      }
    }
  }

</script>
