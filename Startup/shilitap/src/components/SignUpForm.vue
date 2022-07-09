<template>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
    @submit.prevent="signup(signupform)"
  >
    <v-text-field
      v-model="signupform.email"
      :rules="emailRules"
      label="E-mail"
      type="email"
      required
    ></v-text-field>
    <v-text-field
      v-model="signupform.password"
      :counter="10"
      :rules="nameRules"
      label="Password"
      type="password"
      required
    ></v-text-field>
    <v-text-field
      v-model="signupform.name"
      :counter="10"
      :rules="nameRules"
      label="Tên của bạn"
      type="text"
      required
    ></v-text-field>
    <v-text-field
      v-model="signupform.date"
      :counter="10"
      :rules="nameRules"
      label="Ngày sinh"
      type="date"
      required
    ></v-text-field>
    <v-select
      label="Sex"
      v-model="signupform.sex"
      :items="['Nam', 'Nữ']"
    ></v-select>
    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="signup(signupform)"
    >
      Đăng ký
    </v-btn>
    <v-alert dense outlined type="error" class="my-4" v-if="signupform.alert">
      {{ signupform.alert }}
    </v-alert>
  </v-form>
</template>
<script>
import { mapState, mapActions } from "vuex";
export default {
  computed: { ...mapState(["signupform"]) },
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
    ...mapActions(["signup"]),
  },
};
</script>