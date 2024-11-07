<template lang="pug">
  form.form-horizontal(@submit="submitForm" v-if="!$store.state.token")
    .form-group
      .col-3
        label.form-label Логин
      .col-9
        input.form-input(v-if="!$store.state.token" type="text" v-model="username" placeholder="Логин")
    .form-group
      .col-3
        label.form-label Пароль
      .col-9
        input.form-input(v-if="!$store.state.token" type="password" v-model="password" placeholder="Пароль")
    .form-group
      .col-3
      .col-9
        button.btn.btn-primary(type="submit") Зайти
</template>
<script>
export default {
  name: 'login-user',
  data () {
    return {
      'username': '',
      'password': '',
      'logpass': false
    }
  },
  methods: {
    submitForm (event) {
      this.Login()
      //  if (this.$store.getters.token) this.logpass = true
      //  console.log(this.$store.getters.token)
      this.username = ''
      this.password = ''
      event.preventDefault()
    },
    Login () {
      this.$store.dispatch('loginUser', { username: this.username, password: this.password })
    }
  }
}
</script>
