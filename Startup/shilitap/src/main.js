import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import { firestorePlugin } from 'vuefire'
import firebase from 'firebase/app'
import 'firebase/analytics'
import 'firebase/firestore'
require('firebase/auth');




Vue.config.productionTip = false
Vue.use(firestorePlugin)
var firebaseConfig = {
  apiKey: "AIzaSyDx0OQnQ-u1pE1oqqgVMuubNh6BNdpWus8",
  authDomain: "shili-tap.firebaseapp.com",
  projectId: "shili-tap",
  storageBucket: "shili-tap.appspot.com",
  messagingSenderId: "566638345471",
  appId: "1:566638345471:web:2b30a8d982c34812ce60ca",
  measurementId: "G-RFDFD1W5W7"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();
export const db = firebase.firestore()
new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
