<template lang="pug">
  form.form-horizontal(@submit="submitForm", v-if="$store.state.edituser.id")
    .form-group
      .col-3
        label.form-label Уволен
      .col-9
        label Да
        input(type="radio" v-model="$store.state.edituser.fired" value="true")
        label Нет
        input(type="radio" v-model="$store.state.edituser.fired" value="false")
        input.form-input(type="hidden" v-model="$store.state.edituser.id" placeholder="id")
    .form-group
      .col-3
        label.form-label Дата Уволнения
      .col-9
        span {{ formatDate($store.state.edituser.fired_date) }}
        input.form-input(type="date" value="$store" v-model="$store.state.edituser.fired_date")
    .form-group
      .col-3
        label.form-label ФИО
      .col-9
        input.form-input(v-model="$store.state.edituser.full_name" rows=8 placeholder="ФИО")
    .form-group
      .col-3
        label.form-label Должность
      .col-9
        select.form-input(v-model="$store.state.edituser.profession")
          option(v-for="profession in $store.state.professions" v-bind:value="profession.id") {{profession.name }}
    .form-group
      .col-3
      .col-9
        button.btn.btn-primary(type="submit") Обновить
</template>
<script>
export default {
  name: 'change-user',
  data () {
    return {
      'id': '',
      'full_name': ''
    }
  },
  methods: {
    formatDate (date) {
      if (date) {
        return date.substring(0, 10)
        // return mydate.getDay() + '/' + mydate.getMonth() + '/' + mydate.getFullYear()
      }
    },
    submitForm (event) {
      this.createUser()
      // this.name = ''
      // this.full_name = ''
      event.preventDefault()
    },
    createUser () {
      console.log(this.$store.state.edituser)
      this.$store.dispatch('changeUser', { token: this.$store.state.token, id: this.$store.state.edituser.id, full_name: this.$store.state.edituser.full_name, fired: this.$store.state.edituser.fired, fired_date: this.$store.state.edituser.fired_date, profession: this.$store.state.edituser.profession })
    }
  }
}
</script>
