import firebase  from 'firebase'

const config = {
    apiKey: "AIzaSyALER0DFLLwnhXUqpaupbpyDFx0CecF0sM",
    authDomain: "shili-4a7b0.firebaseapp.com",
    projectId: "shili-4a7b0",
    storageBucket: "shili-4a7b0.appspot.com",
    messagingSenderId: "885342513615",
    appId: "1:885342513615:web:9a0b057d1ad778e9814aba",
    measurementId: "G-M8SCHGM5QF"
  };

  

  const firebaseApp = firebase.initializeApp(config)

const db = firebaseApp.firestore()
const usersCollection = db.collection('users')

export const createUser = user => {
  return usersCollection.add(user)
}

export const getUser = async id => {
  const user = await usersCollection.doc(id).get()
  return user.exists ? user.data() : null
}

export const updateUser = (id, user) => {
  return usersCollection.doc(id).update(user)
}

export const deleteUser = id => {
  return usersCollection.doc(id).delete()
}

export const useLoadUsers = () => {
  const users = ref([])
  const close = usersCollection.onSnapshot(snapshot => {
    users.value = snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }))
  })
  onUnmounted(close)
  return users
}
