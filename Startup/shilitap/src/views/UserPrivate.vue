<template>
  <div class="login">
    <h1>Đăng nhập thành công</h1>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "Home",
  computed: { ...mapState(["uid"]) },
  created() {
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        this.$router.push({ name: "Login" });
      }
    });
  },
  methods: {
    ...mapActions(["getcurrentUser"]),
  },
};
</script>
