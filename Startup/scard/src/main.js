import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'
import store from './store'
import firebase from 'firebase'
import {firestorePlugin} from 'vuefire'
import 'firebase/firestore'


Vue.config.productionTip = false
Vue.use(firestorePlugin)

var firebaseConfig = {
  apiKey: "AIzaSyBgXYzCJTjGxpf4vXKhJal9dgzgc46sdTA",
  authDomain: "scard-8b8c2.firebaseapp.com",
  projectId: "scard-8b8c2",
  storageBucket: "scard-8b8c2.appspot.com",
  messagingSenderId: "42683741166",
  appId: "1:42683741166:web:45a581f35db902aa1314ff",
  measurementId: "G-783RC12E00"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
export const db = firebase.firestore()

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
