import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import UserPrivate from '../views/UserPrivate.vue'
import Show from '../views/Show.vue'
import Edit from '../views/Edit.vue'
import Login from '../views/Login.vue'

Vue.use(VueRouter)
const routes = [
  {
    path: '', name: 'Home', component: Home, children: [
      { path: ':userid', name: 'UserPublic', component: Show },
      { path: ':userid/dash', name: 'UserPrivate', component: UserPrivate },
      { path: ':userid/edit', name: 'UserEdit', component: Edit }
    ]
  },
  // { path: '/user/login', name: 'User', component: User },
  { path: '/login/login' ,name: 'Login', component: Login}
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
export default router
