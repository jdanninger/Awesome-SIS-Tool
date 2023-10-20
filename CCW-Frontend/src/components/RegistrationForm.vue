<template>
    <v-sheet width="300" class="mx-auto center">
        <v-form @submit.prevent>
        <v-text-field
            label="Email"
        ></v-text-field>
        <v-text-field
            label="Username"
        ></v-text-field>
        <v-text-field type="password"
            label="Password"
        ></v-text-field>
        <v-text-field type="password"
            label="Confirm Password"
        ></v-text-field>
        <v-btn type="submit" block class="mt-2">Submit</v-btn>
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
    
    <script setup>
    
    
      //
    </script>
    