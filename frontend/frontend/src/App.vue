<template>
  <v-app>

    <v-navigation-drawer
      v-model="drawer"
      app
      color="light-green lighten-5"
    >
      <v-card flat color="light-green lighten-5">
        <v-card-title color="light-green">Hello</v-card-title><hr>
          <router-link to="/">
              <v-icon class="mx-4">
                  mdi-account
              </v-icon>
              <span class="font-weight-bold overline item-nav my-3">Login</span>
          </router-link> <br class="my-3">
          <router-link to="/projet1">
              <v-icon class="mx-4">
                  mdi-account
              </v-icon>
              <span class="font-weight-bold overline item-nav my-3">Projet 1</span>
          </router-link> <br class="my-3">
          <router-link to="/dashboard">
              <v-icon class="mx-4">
                  mdi-monitor-dashboard
              </v-icon>
              <span class="font-weight-bold overline item-nav my-3">Tableau de bord</span>
          </router-link>
      </v-card>

    </v-navigation-drawer>

    <v-app-bar app elevation="8" color="light-green lighten-5">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>
        <v-container fluid class="fill-height">
        <v-img
          src="../src/assets/logo.png"
          contain
          max-height="60"
          min-height="40"
          max-width="60"
          min-width="40"
        ></v-img>
        DRAWER BASE
        </v-container>
      </v-toolbar-title>
    </v-app-bar>

    <v-main id="app">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import LoginPoint from "@/components/LoginPoint.vue";
export default {
  name: "App",
  components: {
    LoginPoint,
  },
  data: () => ({
    drawer: null,
    validateForm: false,
  }),
  methods: {
    changeValid(payload) {
      console.log(payload.validing)
      this.validateForm = true;
      console.log(this.validateForm);
    }
  }
};
</script>


<style>
.item-nav {
    color: black;
}
.item-nav:hover {
    color: blue;
    background-color: rgb(119, 191, 119);
    transition: all 0.4s;
}
</style>