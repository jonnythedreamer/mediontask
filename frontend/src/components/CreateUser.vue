<template lang="pug">
  form.form-horizontal(@submit="submitForm")
    .form-group
      .col-3
        label.form-label Логин
      .col-9
        input.form-input(type="text" v-model="name" placeholder="Type user title...")
    .form-group
      .col-3
        label.form-label ФИО
      .col-9
        textarea.form-input(v-model="full_name" rows=8 placeholder="Type your user...")
    .form-group
      .col-3
      .col-9
        button.btn.btn-primary(type="submit") Create
</template>
<script>
export default {
  name: 'create-user',
  data () {
    return {
      'name': '',
      'full_name': ''
    }
  },
  methods: {
    submitForm (event) {
      this.createUser()
      this.name = ''
      this.full_name = ''
      event.preventDefault()
    },
    createUser () {
      this.$store.dispatch('createUser', { name: this.name, full_name: this.full_name })
    }
  }
}
</script>
