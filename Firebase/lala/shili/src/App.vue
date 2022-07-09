<template>
  <div>
    <from>
      <h1>Login</h1>
      <label>user</label>
      <input type="text" v-model="inputUsername" />
    
      <input type="submit" value="login" />
    </from>
  </div>
  <!-- <div>
    <h1>Chat view</h1>
  </div> -->
</template>

<script>
// import db from './db'
import { reactive, onMounted, ref } from "vue";
export default {
  setup() {
    const inputUsername = ref("");
    return {
      inputUsername,
    };
  },
};
</script>

<style lang="scss">
</style>
