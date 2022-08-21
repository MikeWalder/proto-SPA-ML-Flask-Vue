<template>
    <div class="text-center">
        <p class="mt-16 font-weight-bold" id="titleLogout">Se déconnecter ?</p>
            <v-container>
                <v-row class="pt-16">
                    <v-col cols="3" md="4"></v-col>
                    <v-col cols="3" md="2">
                        <v-btn color="success" x-large elevation="4" @click="disconnectionAccount">Confirmer</v-btn>
                    </v-col>
                    <v-col cols="3" md="2">
                        <v-btn color="error" x-large elevation="4" onclick="window.history.back()">Annuler</v-btn>
                    </v-col>
                    <v-col cols="3" md="4"></v-col>
                </v-row>
                <v-row>
                    <v-col cols="3" md="4"></v-col>
                    <v-col cols="6" md="4">
                        <v-alert color="light-green" class="mt-6" dense dark transition="scale-transition" v-if="validateForm">
                            <v-icon class="mr-4">mdi-check-circle</v-icon>
                            Déconnection en cours ...<br>
                            <span class="ml-6">Redirection...</span> 
                            <v-progress-circular indeterminate color="green" class="ml-6"></v-progress-circular>
                        </v-alert>
                    </v-col>
                    <v-col cols="3" md="4"></v-col>
                </v-row>
            </v-container>
    </div>
</template>



<script>
import axios from 'axios';

export default {
    name: 'logout', 
    data() {
        return {
            dictionnaire: '',
            valid: false,
            validateForm: false,
        }
    },
    methods: {
        checkName() {
            console.log(this.nomVille)
            const path="http://localhost:5000/projet1/add"
            let villeData = {
                ville: this.nomVille,
                "Access-Control-Allow-Origin": true

            }
            axios.post(path, villeData)
            .then((resultat) => {
                this.dataVille = resultat.data;
                console.log(this.dataVille)
            }).catch(err => {console.log(err)});
        },
        disconnectionAccount(){
            this.validateForm = true
            // this.$emit('availableLogin', {loginValidation: this.validateForm})
            this.$cookies.remove('connexion')
            setTimeout( () => {
                this.$store.state.validateForm = false
                this.$store.state.validateCookie = false
                this.$cookies.remove('mail')
                this.$router.push({name: "login"})
            }, 2000)
        },
    },
    created() {
    }
}
</script>

<style>
#titleLogout {
    font-size: 30px !important;
}

@media only screen and (max-width: 920px) {
    #titleLogin {
        font-size: 20px !important;
    }
}
</style>