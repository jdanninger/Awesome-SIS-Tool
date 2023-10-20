<template>
  <div class="banner-img">
    <v-img width="100%" src="@/assets/Torre.jpeg" />
    <div class="centered">Free Yourself From SIS!</div>
  </div>
  
  <v-btn href="/register">
    Register Here!
  </v-btn>

</template>

<style>
  .centered {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .banner-img {
    font: 50px Copperplate;
    position: relative;
    text-align: center;
    color: white;
  }
</style>

<script setup>


  //
</script>
