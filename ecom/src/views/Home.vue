<template>
<div>
  <Navbar />
  <Login  class="container"/>
</div>



</template>

<script>
  import Navbar from '../components/Navbar'
  import Login from '../components/Login'

  export default {
    name: 'Home',

    components: {
      Navbar,Login
    },
  }
</script>
