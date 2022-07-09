<template>
  <div class="container">
    <h2>Sign Up</h2>
    <form @submit.prevent="signup">
      <b-form-input type="email" placeholder="Email" v-model="email" /><br />
      <b-form-input
        type="password"
        placeholder="Password"
        v-model="password"
      /><br />
      <b-button @click="signup">Submit</b-button>
    </form>
    <b-alert show variant="danger" v-if="error">{{ error }}</b-alert>
    <hr />
    Signed in : {{ isAuthenticated }}
  </div>
</template>

<script>
import firebase from "firebase";
export default {
  name: "signup",
  data() {
    return {
      email: "",
      password: "",
      isAuthenticated: false,
      error: null,
    };
  },
  created() {
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        this.isAuthenticated = true;
          this.$router.push('/dashboard')
      }
    });
  },
  methods: {
    signup() {
      firebase
        .auth()
        .signInWithEmailAndPassword(this.email, this.password)
        .catch((error) => (this.error = error.message));
    },
  },
};
</script>

<style>
</style>