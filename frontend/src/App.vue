<template lang="pug">
  #app
    section.container.grid-960
      .columns
        .column.col-2
        .column.col-8.col-md-12
          header.text-center
            h2(v-if="!$store.state.token") Войти
          login-user
          header.text-center
            h4(v-if="$store.state.edituser.id") Редактировать
          change-user
          header.text-center
            h2(v-if="!$store.state.edituser.id") Список Пользователей
          user-list(v-if="!$store.state.edituser.id")
        .column.col-2
</template>
<script>
import CreateUser from './components/CreateUser'
import UserList from './components/UserList'
import Login from './components/Login'
import ChangeUser from './components/ChangeUser'
export default {
  name: 'app',
  components: {
    'create-user': CreateUser,
    'user-list': UserList,
    'login-user': Login,
    'change-user': ChangeUser
  }
}
</script>
<style>
  @import url(https://fonts.googleapis.com/css?family=Eczar);
  @import url(https://fonts.googleapis.com/css?family=Work+Sans);
  body {
    font-family: "Work Sans", "Segoe UI", "Helvetica Neue", sans-serif;
  }
  h1, h2, h3, h4, h5, h6 {
    font-family: "Eczar", sans-serif;
  }
</style>
