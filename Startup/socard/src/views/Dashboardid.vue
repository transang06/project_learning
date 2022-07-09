<template>
  <v-row>
    <v-col cols="12" sm="6" offset-sm="3"> id{{ x }} </v-col>
  </v-row>
</template>

   


<script>
// import firebase from "firebase";
import { db } from "../main";

export default {
  name: "dashboard",
  data() {
    return {
      x: [],
    };
  },

  created() {
    const fetchedId = this.$route.params.id;
    var docRef = db.collection("users").doc(fetchedId);
    docRef
      .get()
      .then((doc) => {
        if (doc.exists) {
          this.x = doc.data();
        } else {
          // doc.data() will be undefined in this case
          console.log("No such document!");
        }
      })
      .catch((error) => {
        console.log("Error getting document:", error);
      });
  },
};
</script>


<style scoped="">
img.preview {
  width: 200px;
}
</style>