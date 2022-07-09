import Vue from 'vue'
import Vuex from 'vuex'
import firebase from "firebase/app";
import { db } from "../main";
import router from '../router'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    uid: null,
    infouser: {},
    signupform: {
      email: "",
      password: "",
      name: "",
      date: null,
      sex: '',
      alert: null,
    },
    loginForm: {
      email: "",
      password: "",
      alert: null,

    },
  },
  getters: {

  },
  mutations: {
    GET_CURRENT_USER(state, uid) {
      state.uid = uid
    },
    GET_LOGIN_FORM(state, loginForm) {
      state.loginForm = loginForm
    },
    GET_SIGNUP_FORM(state, signupform) {
      state.signupform = signupform
    },
    GET_INFO_USER(state, infouser) {
      state.infouser = infouser
    },

  },
  actions: {
    getcurrentUser(context) {
      firebase.auth().onAuthStateChanged((user) => {
        if (user) {
          context.commit('GET_CURRENT_USER', user.uid)
        } else {
          context.commit('GET_CURRENT_USER', null)
        }
      });
    },
    signup(context, signupform) {
      delete signupform.alerts;
      firebase
        .auth()
        .createUserWithEmailAndPassword(signupform.email, signupform.password)
        .then((cred) => {
          db.collection("users").doc(cred.user.uid).set(signupform);
          firebase
            .auth()
            .currentUser.sendEmailVerification()
            .then(() => {
            });
          router.push({ name: 'UserPrivate', params: { userid: userCredential.user.uid } })
        })
        .catch((error) => {
          signupform.alert = error
          context.commit('GET_SIGNUP_FORM', signupform)
        });
    },
    login(context, loginForm) {
      firebase
        .auth()
        .signInWithEmailAndPassword(loginForm.email, loginForm.password)
        .then((userCredential) => {
          context.commit('GET_CURRENT_USER', userCredential.user)
          router.push({ name: 'UserPrivate', params: { userid: userCredential.user.uid } })
        })
        .catch((error) => {
          loginForm.alert = error
          context.commit('GET_LOGIN_FORM', loginForm)
        });
    },
    logout(context) {
      firebase.auth().signOut().then(() => {
        context.commit('GET_CURRENT_USER', null)
        router.push({ name: 'Login' })
        console.log(123123)
      }).catch(() => {
      });
    },
    getinfouser(context, uid) {

      var docRef = db.collection("users").doc(uid)
      docRef
        .get()
        .then((doc) => {
          if (doc.exists) {
            context.commit('GET_INFO_USER', doc.data())

          } else {
            console.log("No such document!");
          }
        })
        .catch((error) => {
          console.log("Error getting document:", error);
        });



      var docRef1 = db.collection("users").doc(uid).collection("category").doc('nganhang')


      console.log("Cached document data:", docRef1.get());









    }
  },
  modules: {
  }
})
