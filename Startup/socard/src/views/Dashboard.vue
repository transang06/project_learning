<template>
  <v-row>
    <v-col cols="12" sm="6" offset-sm="3">
      <div>
        <div>
          <p>Upload an image to Firebase:</p>
          <input type="file" @change="previewImage" accept="image/*" />
        </div>
        <div>
          <p>
            Progress: {{ uploadValue.toFixed() + "%" }}
            <progress id="progress" :value="uploadValue" max="100"></progress>
          </p>
        </div>
        <div v-if="imageData != null">
          <img class="preview" :src="picture" />
          <br />
          <button @click="onUpload">Upload</button>
        </div>
      </div>
      <v-text-field @keyup.enter="add" v-model="title"></v-text-field>

      <v-btn elevation="2" class="my-5" @click="logout">Logout</v-btn>
      <v-card>
        <v-list two-line>
          <template v-for="(item, index) in items.slice(0, 6)">
            <v-subheader v-if="item.header" :key="item.header">
              {{ item.header }}
            </v-subheader>
            <v-divider
              v-else-if="item.divider"
              :key="index"
              :inset="item.inset"
            ></v-divider>
            <v-list-item v-else :key="item.title">
              <v-list-item-avatar>
                <img :src="item.image" />
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title v-html="item.title"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-list>
      </v-card>
    </v-col>
  </v-row>
</template>

   


<script>
import { db } from "../main";
import firebase from "firebase";
export default {
  name: "dashboard",
  data() {
    return {
      items: [],
      title: "",
      imageData: null,
      picture: null,
      uploadValue: 0,
    };
  },

  firestore: {
    items: db.collection("Category"),
  },
  methods: {
    add() {
      const category = {
        title: this.title,
      };
      db.collection("Category").add(category);
      this.title = "";
    },
    logout() {
      firebase
        .auth()
        .signOut()
        .then(() => {
          this.$router.push("/login");
        });
    },
    previewImage(event) {
      this.uploadValue = 0;
      this.picture = null;
      this.imageData = event.target.files[0];
    },

    onUpload() {
      this.picture = null;
      const storageRef = firebase
        .storage()
        .ref(`image/${this.imageData.name}`)
        .put(this.imageData);
      storageRef.on(
        `state_changed`,
        (snapshot) => {
          this.uploadValue =
            (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
        },
        (error) => {
          console.log(error.message);
        },
        () => {
          this.uploadValue = 100;
          storageRef.snapshot.ref.getDownloadURL().then((url) => {
            this.picture = url;
             console.log(this.picture)
          });
         
        }
      );
    },
  },
};
</script>


<style scoped="">
img.preview {
  width: 200px;
}
</style>