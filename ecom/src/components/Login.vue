<template>
  <div class="container">
    <b-form>
      <b-form-group
        id="input-group-1"
        label="Email address:"
        label-for="input-1"
        description="We'll never share your email with anyone else."
      >
        <b-form-input
          id="input-1"
          v-model="form.email"
          type="email"
          placeholder="Enter email"
          required
        ></b-form-input>
      </b-form-group>
      <b-form-input
        id="input-1"
        v-model="form.name"
        type="text"
        placeholder="Enter name"
        required
      ></b-form-input>
      <b-form-group id="input-group-2" label="Your Name:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.password"
          placeholder="Enter password"
          required
        ></b-form-input>
      </b-form-group>
    </b-form>
    <b-button @click="onSubmit" variant="primary">Submit</b-button>
    <b-button @click="dangnhap" variant="primary">dn</b-button>
    <b-button @click="out" variant="primary">out</b-button>
    {{ user }}
  </div>
</template>

<script>
import { fb } from "../firebase";

export default {
  data() {
    return {
      form: {
        name: "",
        email: "",
        password: "",
      },
      user: "",
    };
  },
  methods: {
    onSubmit() {
      fb.auth()
        .createUserWithEmailAndPassword(this.form.email, this.form.password)
        .then((userCredential) => {
          this.user = userCredential.user;
          fb.auth()
            .user.sendEmailVerification()
            .then(() => {
              // Email verification sent!
              // ...
            });
        })
        .catch(() => {});
    },
    dangnhap() {
      fb.auth()
        .signInWithEmailAndPassword(this.form.email, this.form.password)
        .then((userCredential) => {
          this.user = userCredential.user;
          fb.auth()
            .userCredential.sendEmailVerification()
            .then(() => {
            console.log("121")
              // ...
            });
        })
        .catch(() => {});
    },
    out() {
      fb.auth()
        .signOut()
        .then(() => {
          this.$router.replace("/");
        })
        .catch(() => {
          console.log("loi dx");
        });
    },
  },
};
</script>