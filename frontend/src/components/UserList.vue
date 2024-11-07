<template lang="pug">
  #app
    .form.form-horizontal()
      .form-group
        .col-4
          label Уволеннные
          br
          input(type="checkbox" @change="userChange" v-model="fired")
        .col-4
          label Не уволенные
          br
          input(type="checkbox" @change="userChange" v-model="not_fired")
        .col-4
          input.form-input(@change="userChange" type="date" v-model="fired_date")
      .form-group
        .col-6
          select.form-input(@change="userChange" default='' v-model="profession" placeholder="Должность")
            option(value="" selected="selected") ***Должность***
            option(v-for="profession in $store.state.professions" v-bind:value="profession.id") {{profession.name }}
        .col-1
          label
        .col-5
          input(type="text" @change="userChange" v-model="name" placeholder="ФИО")
    .card(v-for="user in users")
      .card-header
        button.btn.btn-clear.float-right(v-if="$store.state.permissions.delete" @click="deleteUser(user)")
        button.btn.btn-edit.float-right(v-if="$store.state.permissions.change" @click="updateUser(user)") Редактироваь
        .card-title ФИО: {{ user.full_name }}
        .card-subtitle Профессия: {{ user.profession_name }}
      .card-body(v-if="user.fired") Уволен {{ formatDate(user.fired_date) }}
      .card-body(v-if="!user.fired") Не уволен
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'user-list',
  data () {
    return {
      'fired': false,
      'not_fired': false,
      'name': '',
      'profession': '',
      'fired_date': ''
    }
  },
  computed: mapGetters(['users']),
  methods: {
    formatDate (date) {
      if (date) {
        return date.substring(0, 10)
        // return mydate.getDay() + '/' + mydate.getMonth() + '/' + mydate.getFullYear()
      }
    },
    userChange (event) {
      this.$store.dispatch('getUsers', {token: this.$store.state.token, fired: this.fired, not_fired: this.not_fired, name: this.name, profession: this.profession, fired_date: this.fired_date})
    },
    updateUser (user) {
      this.$store.state.edituser = user
    },
    deleteUser (user) {
      this.$store.dispatch('deleteUser', {user: user, token: this.$store.state.token})
    }
  },
  beforeMount () {
    this.$store.dispatch('getUsers', {token: this.$store.state.token})
    this.$store.dispatch('getProfessions', {token: this.$store.state.token})
  }
}
</script>
<style>
  header {
    margin-top: 50px;
  }
</style>
