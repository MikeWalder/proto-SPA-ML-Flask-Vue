<template>
    <div id="loginAccount">
        <v-container>
            <v-row no-gutters>
                <v-col offset-sm="0" md="6">
                    <v-img
                    src="https://picsum.photos/510/300?random"
                    aspect-ratio="1.7"
                    height="100vh"
                    ></v-img>
                </v-col>
                <v-col cols="12" md="6" class="grey lighten-2">
                    <div class="text-center form_part">
                        <span class="display-3">Drawer Base</span><br>
                        <span class="overline">Bienvenue, veuillez vous connecter à votre compte</span>

                        <v-form v-model="valid" action="" method="post" @submit="checkLoginForm">
                            <v-container>
                                <v-row>
                                    <v-col cols="1"></v-col>
                                    <v-col cols="10">
                                        <v-text-field v-model="mail" label="E-mail" :rules="emailRules" required>
                                        </v-text-field>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="1"></v-col>
                                    <v-col cols="10">
                                        <v-text-field v-model="password" :type="show1 ? 'text' : 'password'" :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" @click:append="show1 = !show1" label="Password" :rules="passRules" required>
                                        </v-text-field>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="1"></v-col>
                                    <v-col cols="5">
                                        <v-checkbox v-model="checkbox" :label="`Se souvenir de moi : ${checkbox.toString()}`"></v-checkbox>
                                        </v-checkbox>
                                    </v-col>
                                    <v-col cols="5" class="pt-8">
                                        Mot de passe perdu ?
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="1"></v-col>
                                    <v-col cols="10 text-center">
                                        <v-btn color="success" elevation="6" large class="text-center font-weight-bold px-12 py-2" @click="validation(validate_log)">
                                        Valider
                                        </v-btn>
                                    </v-col>
                                </v-row>
                            </v-container>
                        </v-form>
                    </div>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>

export default {
    name: 'login',
    props: ['validate_log'],
    data() {
        return {
            valid: false,
            mail: '',
            password: '',
            checkbox: true,
            show1: false,
            emailRules: [
                v => !!v || 'E-mail est requis',
                v => /.+@.+/.test(v) || 'E-mail invalide'
            ],
            passRules: [
                v => !!v || 'Le mot de passe est requis',
                v => v.length <= 10 || 'Votre mot de passe doit être inférieur à 10 caractères'
            ],
        }
    },
    methods: {
        validation(validate_log) {
            console.log("Le formulaire est activé")
            this.$emit('loginAccount', validate_log)
            validate_log = true
            console.log(this.validate_log)
            console.log(this.mail)
        },
        checkLoginForm: function(e) {
            
        }
    }
}
</script>

<style>
.form_part {
    height: 95vh !important;
    padding-top: 30vh;
}
</style>