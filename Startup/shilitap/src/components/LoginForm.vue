<template>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
    @submit.prevent="login(loginForm)"
  >
    <v-text-field
      v-model="loginForm.email"
      :rules="emailRules"
      label="E-mail"
      type="email"
      required
    ></v-text-field>
    <v-text-field
      v-model="loginForm.password"
      :counter="10"
      :rules="nameRules"
      label="Password"
      type="password"
      required
    ></v-text-field>
    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="login(loginForm)"
    >
      Đăng nhập
    </v-btn>
    <v-alert dense outlined type="error" class="my-4" v-if="loginForm.alert">
      {{ loginForm.alert }}
    </v-alert>
  </v-form>
</template>
<script>
import { mapState, mapActions } from "vuex";
export default {
  computed: { ...mapState(["loginForm"]) },
  data: () => ({
    valid: true,
    name: "",
    nameRules: [
      (v) => !!v || "Password is required",
      (v) =>
        (v && v.length <= 10) || "Password must be less than 10 characters",
    ],
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
  }),

  methods: {
    ...mapActions(["login"]),
  },
};
</script>