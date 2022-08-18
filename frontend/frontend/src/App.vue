<template>
  <v-app>

    <v-navigation-drawer
      v-model="drawer"
      app
      color="light-green lighten-5"
    >
      <v-card flat color="light-green lighten-5" class="ma-0" no-gutters>
        <v-card-title color="light-green" class="pa-0">
          <v-img
          src="../src/assets/b_icon.png"
          contain
          max-height="50" min-height="40" max-width="50" min-width="40" class="ma-0">
          </v-img>
          <span class="pt-6">DRAWER BASE</span>
        </v-card-title>
        <v-divider class="mt-2"></v-divider>
          <div v-if="!validateForm">
            <br class="pt-8">
            <router-link to="/">
                <v-icon class="mx-4">
                    mdi-account
                </v-icon>
                <span class="font-weight-bold overline item-nav my-3 navItem h5">Connexion</span>
            </router-link> <br class="my-3">
          </div>

          <div v-if="validateForm">
            <br class="pt-8">
            <router-link to="/logout">
              <v-icon class="mx-4">
                  mdi-logout-variant
              </v-icon>
              <span class="font-weight-bold overline item-nav my-3 navItem h3">Déconnexion</span>
            </router-link><br class="my-4">
            
            <router-link to="/projet1">
              <v-icon class="mx-4">
                  mdi-account
              </v-icon>
              <span class="font-weight-bold overline item-nav my-3 navItem">Projet 1</span>
            </router-link> <br class="my-6">
            
            <router-link to="/dashboard">
              <v-icon class="mx-4">
                  mdi-monitor-dashboard
              </v-icon>
              <span class="font-weight-bold overline item-nav my-4 navItem">Tableau de bord</span>
            </router-link>

          </div>

      </v-card>

    </v-navigation-drawer>

    <v-app-bar app elevation="8" color="light-green lighten-5">
      <v-app-bar-nav-icon @click="drawer = !drawer">
        <div v-if="drawer"><v-icon>mdi-backburger</v-icon></div>
        <div v-if="!drawer"><v-icon>mdi-forwardburger</v-icon></div>
      </v-app-bar-nav-icon>
      <v-toolbar-title>
        <v-container fluid class="fill-height">
          
        </v-container>
      </v-toolbar-title>
    </v-app-bar>

    <v-main id="app">
      <router-view @availableLogin="enableLogin" />
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
    dialog: false,
  }),
  methods: {
    enableLogin(payload){
      console.log(payload.loginValidation)
      this.validateForm = payload.loginValidation;
      console.log(this.validateForm);
    },
    verifyConnection(){
      if (this.$cookies.isKey("connexion")) {
        this.validateForm == true;
      }
    }
  },
  created() {
    this.verifyConnection();
  },
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
.custom-dialog {
  align-self: flex-start !important;
}
.navItem {
  font-size: 40px !important;
}
.router-link-active {
  font-size: 1.2em !important;
}
</style>