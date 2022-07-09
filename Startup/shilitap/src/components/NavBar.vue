<template>
  <div>
    <v-app-bar color="deep-purple" dark>
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
      <v-toolbar-title>Shili Tap</v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list nav dense>
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
          <router-link  tag="div" :to="{ name: 'Home' }">
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-home</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Home</v-list-item-title>
            </v-list-item>
          </router-link>
          <router-link  tag="div" :to="{ name: 'Login' }" v-if="!uid">
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-home</v-icon>
              </v-list-item-icon>
              <v-list-item-title> Sign Up </v-list-item-title>
            </v-list-item>
          </router-link>
          <v-list-item @click="logout" v-if="uid">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title> Logout </v-list-item-title>
          </v-list-item>
          <router-link            
            tag="div"
            :to="{ name: 'UserPrivate', params: { userid: uid } }"
            v-if="uid"
          >
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-account</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Account</v-list-item-title>
            </v-list-item>
          </router-link>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  computed: { ...mapState(["uid"]) },
  data() {
    return {
      drawer: false,
      group: null,
    };
  },
  created() {
    this.getcurrentUser();
  },
  methods: {
    ...mapActions(["logout", "getcurrentUser"]),
  },
};
</script>