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
      <b-button @click="createNewAccount">Submit</b-button>
    </form>
    <b-alert show variant="danger" v-if="error">{{ error }}</b-alert>
    <hr />
    Signed in : {{ isAuthenticated }}
  </div>
</template>

<script>
import firebase from "firebase";
import { db } from "../main";
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
        this.$router.push("/dashboard");
      }
    });
  },

  methods: {
    signup() {
      firebase
        .auth()
        .createUserWithEmailAndPassword(this.email, this.password)
        .then((cred) => {
          db.collection("users").doc(cred.user.uid).set({
            name: "Tran Van Sang",
            born: 2000,
          });
          firebase
            .auth()
            .currentUser.sendEmailVerification()
            .then(() => {
              // Email verification sent!
              // ...
            });
        })
        .catch((error) => (this.error = error.message));
    },
  async createNewAccount() {
    try {
        const userAuth = await firebase.auth().createUserWithEmailAndPassword(this.email, this.password);
        var user = {
            name: "Raja",
            phone: "779797329",
            address: "474 Mercer Drive",
            uid: userAuth.uid,
            email: userAuth.email
        }
        writeUserData(user)

    } catch (error) {
        console.log(error.message)
    }
}
  },
};
</script>

<style>
</style>