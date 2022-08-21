import Vue from "vue";
import Vuex from "vuex";
/* import createPersistedState from "vuex-persistedstate"; */

Vue.use(Vuex);

export default new Vuex.Store({
  state() {
    return {
      count: 0,
      validating: false,
      validateForm: null,
      validateCookie: null,
    }
  },
  getters: {
  },
  mutations: {
  },
  actions: {},
  modules: {},
});