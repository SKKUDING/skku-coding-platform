import types from '../types'
import api from '@oj/api'

const state = {
  groups: {
    admin_groups: [],
    groups: [],
    other_groups: []
  }
}

const getters = {
}

const mutations = {
  [types.CHANGE_GROUP_LIST] (state, payload) {
    state.groups = payload.groups
  }
}

const actions = {
  async getGroupList ({ commit, rootState }) {
    try {
      console.log('call')
      const res = await api.getGroupList()
      commit(types.CHANGE_GROUP_LIST, { groups: res.data.data })
      return res
    } catch (err) {
      commit(types.CHANGE_GROUP_LIST, { groups: [] })
      throw err
    }
  }
}

export default {
  state,
  mutations,
  getters,
  actions
}
