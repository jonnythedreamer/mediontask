import Vue from 'vue'
import Vuex from 'vuex'
import { User } from '../api/users'
import {
  ADD_USER,
  REMOVE_USER,
  SET_USERS,
  LOGIN_USER,
  CHANGE_USER,
  SET_PROFESSIONS,
  SET_PERMISSIONS
} from './mutation-types.js'
Vue.use(Vuex)
// Состояние
const state = {
  users: [],
  token: false,
  edituser: {},
  myfilter: {
    fired: false,
    not_fired: false
  },
  professions: [],
  permissions: []
}
// Геттеры
const getters = {
  users: state => state.users,
  professions: state => state.professions,
  token: state => state.token,
  edituser: state => state.edituser,
  permissions: state => state.permissions
}
// Мутации
const mutations = {
  [CHANGE_USER] (state, note) {
    state.edituser = {}
  },
  [LOGIN_USER] (state, note) {
    state.token = note.token
  },
  [SET_PERMISSIONS] (state, { permissions }) {
    state.permissions = permissions
  },
  // Добавляем заметку в список
  [ADD_USER] (state, note) {
    state.users = [note, ...state.users]
  },
  // Убираем заметку из списка
  [REMOVE_USER] (state, { id }) {
    state.users = state.users.filter(note => {
      return note.id !== id
    })
  },
  // Задаем список заметок
  [SET_USERS] (state, { users }) {
    state.users = users
  },
  [SET_PROFESSIONS] (state, { professions }) {
    state.professions = professions
  }
}
// Действия
const actions = {
  loginUser ({ commit }, noteData) {
    User.login(noteData).then(note => {
      commit(LOGIN_USER, note)
      User.listpermissions({token: note.token}).then(permissions => {
        commit(SET_PERMISSIONS, { permissions })
      })
      User.list({token: note.token}).then(users => {
        commit(SET_USERS, { users })
      })
    })
  },
  createUser ({ commit }, noteData) {
    User.create(noteData).then(note => {
      commit(ADD_USER, note)
    })
  },
  changeUser ({ commit }, note) {
    User.change(note).then(response => {
      commit(CHANGE_USER, note)
      User.list({token: state.token}).then(users => {
        commit(SET_USERS, { users })
      })
    })
  },
  deleteUser ({ commit }, note) {
    User.delete(note).then(response => {
      commit(REMOVE_USER, note)
    })
  },
  getUsers ({ commit }, myfilter) {
    User.list(myfilter).then(users => {
      commit(SET_USERS, { users })
    })
  },
  getProfessions ({ commit }, myfilter) {
    User.listprofessions(myfilter).then(professions => {
      commit(SET_PROFESSIONS, { professions })
    })
  }
}
export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
