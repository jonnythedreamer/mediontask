import { HTTP } from './common'

export const User = {
  login (config) {
    return HTTP.post('/api-token-auth', config).then(response => {
      // console.log(response.data)
      return response.data
    }).catch(function (error) {
      console.log(error.response.data)
    })
  },
  create (config) {
    return HTTP.post('/customusers', config).then(response => {
      return response.data
    })
  },
  change (user) {
    console.log(user)
    return HTTP.put(`/customusers/${user.id}`, user, {
      headers: {
        Authorization: 'Token ' + user.token
      }
    }).then(response => {
      return response.data
    }).catch(function (error) {
      console.log(error.response.data)
    })
  },
  delete (user) {
    return HTTP.delete(`/customusers/${user.user.id}`, {
      headers: {
        Authorization: 'Token ' + user.token
      }
    }).catch(function (error) {
      console.log(error.response.data)
      alert(error.response.data.detail)
    })
  },
  listprofessions (myfilter) {
    return HTTP.get('/professions', {
      headers: {
        Authorization: 'Token ' + myfilter.token
      }
    }).then(response => {
      return response.data
    }).catch(function (error) {
      console.log(error.response.data)
    })
  },
  listpermissions (myfilter) {
    return HTTP.get('/permissions', {
      headers: {
        Authorization: 'Token ' + myfilter.token
      }
    }).then(response => {
      return response.data
    }).catch(function (error) {
      console.log(error.response.data)
    })
  },
  list (myfilter) {
    var url = '/customusers'
    if (myfilter.fired === true) url = url + '?fired=1'
    else url = url + '?fired=0'
    if (myfilter.not_fired === true) url = url + '&not_fired=1'
    else url = url + '&not_fired=0'
    if (myfilter.name) url = url + '&name=' + myfilter.name
    if (myfilter.profession) url = url + '&profession=' + myfilter.profession
    if (myfilter.fired_date) url = url + '&fired_date=' + myfilter.fired_date
    var headers = {}
    if (myfilter.token) headers = {Authorization: 'Token ' + myfilter.token}
    return HTTP.get(url, {
      headers: headers
    }).then(response => {
      return response.data
    }).catch(function (error) {
      console.log(error.response.data)
    })
  }
}
