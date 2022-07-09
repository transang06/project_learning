<template>
  <v-app>
    <NavBar />
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import NavBar from "./components/NavBar";
import {  mapActions } from "vuex";
export default {
  name: "App",
  components: { NavBar },
  data: () => ({
    //
  }),   
 
};
</script>
