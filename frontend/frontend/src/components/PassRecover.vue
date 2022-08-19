<template>
    <v-container>
        <v-row>
            <v-col class="text-center mt-6">
                <span class="font-weight-bold" id="mainTitleRecoverAccount">Récupération du mot de passe</span><br>
                
            </v-col>
        </v-row>

        <v-row class="pt-8">
            <v-col cols="1" md="4"></v-col> 
            <v-col col="10" md="4">
                <v-form
                ref="form"
                v-model="valid"
                lazy-validation
                >
                    <v-text-field
                    v-model="email"
                    :rules="emailRules"
                    label="Insérez votre e-mail"
                    required
                    ></v-text-field>

                    <v-btn
                    color="success"
                    class="mr-4 px-4"
                    @click="validateRecupPass"
                    >
                    Validate
                    </v-btn>

                    <v-btn
                    color="error"
                    class="mr-4 px-4"
                    @click="resetRecupPass"
                    >
                    Reset Form
                    </v-btn>
                </v-form>
            </v-col>
            <v-col cols="1" md="4"></v-col> 
        </v-row>

        <v-row>
            <v-col cols="1" md="4"></v-col> 
            <v-col cols="10" md="4">
                <v-alert color="light-red" class="mt-6" dense dark transition="scale-transition" v-if="validForm">
                    <v-icon class="mr-4">mdi-check-circle</v-icon>
                        Retour sur le site ...<br>
                    <span class="ml-6">Redirection...</span> 
                    <v-progress-circular indeterminate color="red" class="ml-6"></v-progress-circular>
                </v-alert>
            </v-col>
            <v-col cols="1" md="4"></v-col> 
        </v-row>
    </v-container>
</template>

<script>
import axios from 'axios'
export default {
    name: 'recover',
    data() {
        return {
            resetPass: false,
        }
    },
    methods: {
        resetRecupPass() {
            this.resetPass = true
            setTimeout(() => {
                    this.$router.push({name: "projet1"})
                }, 2000)
            
        },
    }
}
</script>

<style>
#mainTitleRecoverAccount {
    font-size: 30px !important;
}

@media only screen and (max-width: 920px) {
    #mainTitleRecoverAccount {
        font-size: 20px !important;
    }
}
</style>