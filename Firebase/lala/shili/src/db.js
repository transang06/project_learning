import firebase from 'firebase/app';
import "firebase/database";

const config = {
    apiKey: "AIzaSyALER0DFLLwnhXUqpaupbpyDFx0CecF0sM",
    authDomain: "shili-4a7b0.firebaseapp.com",
    projectId: "shili-4a7b0",
    storageBucket: "shili-4a7b0.appspot.com",
    messagingSenderId: "885342513615",
    appId: "1:885342513615:web:9a0b057d1ad778e9814aba",
    measurementId: "G-M8SCHGM5QF"
}
const db =  firebase.initializeApp(config);
export default db;