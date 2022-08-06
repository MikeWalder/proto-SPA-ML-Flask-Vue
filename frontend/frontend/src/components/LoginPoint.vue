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

                        <v-form v-model="valid" action="" method="post">
                            <v-container>
                                <v-row>
                                    <v-col cols="1"></v-col>
                                    <v-col cols="10">
                                        <v-text-field id="mailLog" v-model="mail" label="E-mail" :rules="emailRules" required>
                                        </v-text-field>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="1"></v-col>
                                    <v-col cols="10">
                                        <v-text-field  id="passLog" v-model="password" :type="show1 ? 'text' : 'password'" :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" @click:append="show1 = !show1" label="Password" :rules="passRules" required>
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
                                        Mot de passe perdu ?<br>
                                        {{msg}}
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="1"></v-col>
                                    <v-col cols="10 text-center">
                                        <v-btn color="success" elevation="6" large class="text-center font-weight-bold px-12 py-2" @click="sendValidation">
                                        Valider
                                        </v-btn>
                                        <v-alert color="light-green" class="mt-6" dense dark dismissible transition="scale-transition" v-if="validForm">
                                            <v-icon class="mr-4">mdi-check-circle</v-icon>
                                            L'inscription est validée !<br>
                                            <span class="ml-6">Redirection...</span> 
                                            <v-progress-circular indeterminate color="green" class="ml-6"></v-progress-circular>
                                        </v-alert>
                                        <v-alert color="#C51162" class="mt-6" dense dark dismissible transition="scale-transition" v-if="errorForm">
                                            Les informations entrées sont erronées. Réessayez.
                                        </v-alert>
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
import axios from 'axios';
export default {
    name: 'LoginPoint',
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
            validForm: false,
            errorForm: false,
            msg: '',
            getLogData: '',
        }
    },
    methods: {
        sendValidation() {
            console.log("Le formulaire est activé")
            const mailLog = document.getElementById('mailLog')
            const passLog = document.getElementById('passLog')
            //const messageForm = document.querySelector('#messageForm')
            //console.log(messageForm)

            if(mailLog != '' && passLog != ''){
                this.sendDatasLogin(mailLog.value, passLog.value);
                if(mailLog.value == 'mike_walder@hotmail.fr' && passLog.value == '123456'){
                    //this.$router.push('/dashboard')
                    this.validForm = true 
                    //console.log("ValidForm est à " + this.validForm)
                    
                    setTimeout(() => {this.$router.push('/dashboard')}, 2000)
                }
                else if(mailLog.value !== 'mike_walder@hotmail.fr' && passLog.value !== '123456') {
                    this.errorForm = true
                    console.log(this.errorForm)
                    setTimeout(() => {this.$router.push({path: '/'})}, 1500)
                }
            }
        },
        async getResponse(){
            const path = 'http://localhost:5000/';
            await axios.get(path)
            .then((res) => {
                console.log(res.data)
                this.msg = res.data.cardDatas.data[0].desc;
                console.log(this.msg)
            })
            .catch((err) => {
                console.error(err);
            });
        },
        async sendDatasLogin(mail, pass) {
            console.log(mail + ' et ' + pass)
            const dataLogin = {mailLog: mail, passLog: pass}
            axios.post("http://localhost:5000/", dataLogin)
            .then(response => this.getLogData = response.data).catch((err) => console.error(err))
        }

    },
    created(){
        this.getResponse();
    }
}
</script>

<style>
.form_part {
    height: 95vh !important;
    padding-top: 30vh;
}
</style>