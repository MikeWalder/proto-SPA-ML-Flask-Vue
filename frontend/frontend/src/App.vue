<template>
  <v-app>

    <v-navigation-drawer
      v-model="drawer"
      app
      color="light-green lighten-5"
    >
      <app-nav></app-nav>
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
import AppNav from "./components/AppNav";
export default {
  name: "App",

  data: () => ({
    drawer: null,
  }),
  components: {
    AppNav
  }
};
</script>
