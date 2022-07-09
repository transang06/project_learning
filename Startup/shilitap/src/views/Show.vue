<template>
  <div class="login">
    <v-container>
       <v-col> 
    <v-row  justify="space-around">
      <v-avatar size="128">
        <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John" />
      </v-avatar>
    </v-row>
    <v-row justify="space-around" class="mx-auto">
      <h1> {{ infouser.name }}</h1>
    </v-row>

    <v-row class="mx-auto" justify="space-around">
      <p class="m-3">{{ infouser.email }}</p>
      <p class="m-3">{{ infouser.date }}</p>
      <p class="m-3">{{ infouser.sex }}</p>
    </v-row>
  </v-col>
      <v-container>
        <v-row dense>
          <v-col cols="12">
            <v-card color="#385F73" dark>
              <v-card-title class="text-h5">
              Unlimited music now
            </v-card-title>

            <v-card-subtitle>Listen to your favorite artists and albums whenever and wherever, online and offline.</v-card-subtitle>

              <v-card-actions>
                <v-btn text> Listen Now </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>

          <v-col v-for="(item, i) in items" :key="i" cols="12">
            <v-card :color="item.color" dark>
              <div class="d-flex flex-no-wrap justify-space-between">
                <div>
                  <v-card-title
                    class="text-h5"
                    v-text="item.title"
                  ></v-card-title>

                  <v-card-subtitle v-text="item.artist"></v-card-subtitle>

                  <v-card-actions>
                    <v-btn
                      v-if="item.artist === 'Ellie Goulding'"
                      class="ml-2 mt-3"
                      fab
                      icon
                      height="40px"
                      right
                      width="40px"
                    >
                      <v-icon>mdi-play</v-icon>
                    </v-btn>

                    <v-btn v-else class="ml-2 mt-5" outlined rounded small>
                      START RADIO
                    </v-btn>
                  </v-card-actions>
                </div>

                <v-avatar class="ma-3" size="125" tile>
                  <v-img :src="item.src"></v-img>
                </v-avatar>
              </div>
            </v-card>
          </v-col>
        </v-row>
      </v-container> 
      {{infouser}}     
    </v-container>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  computed: { ...mapState(["infouser"]) },
  data: () => ({
    items: [
      {
        color: "#1F7087",
        src: "https://cdn.vuetifyjs.com/images/cards/foster.jpg",
        title: "Supermodel",
        artist: "Foster the People",
      },
      {
        color: "#952175",
        src: "https://cdn.vuetifyjs.com/images/cards/halcyon.png",
        title: "Halcyon Days",
        artist: "Ellie Goulding",
      },
    ],
  }),
  created() {
    this.getinfouser(this.$route.params.userid);
  },
  methods: {
    ...mapActions(["getinfouser"]),
  },
};
</script>
