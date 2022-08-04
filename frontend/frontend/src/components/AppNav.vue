<template>
    <v-card flat color="light-green lighten-5">
        <v-card-title color="light-green">Hello</v-card-title><hr>
    <router-link to="/">
        <v-icon class="mx-6">
            mdi-account
        </v-icon>
        <span class="font-weight-bold overline item-nav mt-3">Login</span>
    </router-link> <br class="my-3">
    <router-link to="/dashboard" @loginAccount="validate_log" v-if="validate_log">
        <v-icon class="mx-6">
            mdi-monitor-dashboard
        </v-icon>
        <span class="font-weight-bold overline item-nav">Tableau de bord</span>
    </router-link>
    </v-card>

</template>

<script>
export default {
    name: 'logPart',
    props: ['validate_log'],
    data() {
        return {

        }
    }
}
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