<template>
  <v-container>
    <v-list-item-title class="text-h5 my-5">
      {{ page == "Login" ? "Sign up" : "Login" }}
    </v-list-item-title>

    <SignUpForm v-if="page == 'Login'" />
    <LoginForm v-else />
    <v-btn
      elevation="2"
      class="my-4"
      @click="page == 'Login' ? (page = 'Sign up') : (page = 'Login')"
      >{{ page }}</v-btn
    >
  </v-container>
</template>

<script>
import LoginForm from "../components/LoginForm";
import SignUpForm from "../components/SignUpForm";
import { mapState, mapActions } from "vuex";
export default {
  components: {
    LoginForm,
    SignUpForm,
  },
  computed: { ...mapState(["uid"]) },
  data: () => ({
    page: "Login",
  }),
  created() {
   
    if (this.uid) {
      this.$router.push({ name: "UserPrivate", params: { userid: this.uid } });
    } 
  },
  methods: {
    ...mapActions(["logout", "getcurrentUser"]),
  },
};
</script>


