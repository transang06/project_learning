<template>
  <div class="container">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <b-form-input type="email" placeholder="Email" v-model="email" /><br />
      <b-form-input
        type="password"
        placeholder="Password"
        v-model="password"
      /><br />
      <b-button @click="login">Submit</b-button>
    </form>
    <b-alert show variant="danger" v-if="error">{{ error }}</b-alert>
    <hr />
    <b-button @click="logout">Logout</b-button>

    Login in : {{ isAuthenticated }}<br />
    {{ user }}
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
      user: "",
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
    login() {
      firebase
        .auth()
        .signInWithEmailAndPassword(this.email, this.password)
        .then((userCredential) => {
          // Signed in
          this.user = userCredential.user;

          // ...
        })
        .catch((error) => (this.error = error.message));
    },
    logout() {
      firebase
        .auth()
        .signOut()
        .then(() => {
          this.isAuthenticated = false;
          this.user = "";
        });
    },
  },
};
</script>
<style>
</style>