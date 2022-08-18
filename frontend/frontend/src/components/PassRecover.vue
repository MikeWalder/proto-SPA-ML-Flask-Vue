<template>
    <v-container>
        <v-row>
            <v-col class="text-center mt-6">
                <span class="font-weight-bold" id="mainTitleRecoverAccount">Récupération du mot de passe</span><br>
                
            </v-col>
        </v-row>

        <v-row class="pt-8">
            <v-col cols="1" md="4"></v-col> 
            <v-col>
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
    </v-container>
</template>

<script>
import axios from 'axios'
export default {
    name: 'recover',
    data() {
        return {

        }
    },
    methods: {
        
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