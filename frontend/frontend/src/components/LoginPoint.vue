<template>
    <div id="loginAccount">
        <v-container>
            <v-row>
                <v-col offset-sm="0" md="6" class="hidden-sm-and-down">
                    <v-img
                    src="../../public/computer-mouse-in-action.jpg"
                    aspect-ratio="1.3"
                    height="100vh"
                    transition="scale-transition"
                    origin="center center"
                    >
                    </v-img>
                </v-col>

                <v-col cols="12" md="6" class="grey lighten-2">
                    <div class="text-center form_part">
                        <span class="display-3 mainTitleAppli">Drawer Base</span><br><br>
                        <span class="overline">Bienvenue, veuillez vous connecter à votre compte</span>

                        <div>
                            <v-container>

                                <v-row>
                                    <v-col cols="1" md="2"></v-col>
                                    <v-col cols="10" md="8">
                                        <v-text-field name="mail" id="mailLog" v-model="mail" label="E-mail" :rules="emailRules" required>
                                        </v-text-field>
                                    </v-col>
                                </v-row>

                                <v-row>
                                    <v-col cols="1" md="2"></v-col>
                                    <v-col cols="10" md="8">
                                        <v-text-field  name="password" id="passLog" v-model="password" :type="show1 ? 'text' : 'password'" :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" @click:append="show1 = !show1" label="Password" :rules="passRules" required>
                                        </v-text-field>
                                    </v-col>
                                </v-row>

                                <v-row align="center" justify="center">
                                    <v-col cols="0" md="2"></v-col>
                                    <v-col cols="6" md="4">
                                        <v-checkbox v-model="checkbox" id="accountCookie" :label="`Se souvenir de moi`">
                                        </v-checkbox>
                                    </v-col>
                                    <v-col cols="6" md="4">
                                        <v-list-item to="/recover" @click="redirectPasswordForgot()" id="passForget">
                                            Mot de passe perdu ?
                                            <router-view />
                                        </v-list-item> 
                                    </v-col>
                                </v-row>

                                <v-row>
                                    <v-col cols="2"></v-col>
                                    <v-col cols="8 text-center">
                                        <v-btn type="submit" color="success" elevation="6" large class="text-center font-weight-bold px-12 py-2" @click.once="sendValidation()">
                                        Valider
                                        </v-btn>
                                        <v-alert color="light-green" class="mt-6" dense dark transition="scale-transition" v-if="validAlertForm">
                                            <v-icon class="mr-4">mdi-check-circle</v-icon>
                                            Bienvenue sur Drawer Base !<br>
                                            <span class="ml-6">Redirection...</span> 
                                            <v-progress-circular indeterminate color="green" class="ml-6"></v-progress-circular>
                                        </v-alert>
                                        <v-alert color="#C51162" class="mt-6" dense dark transition="scale-transition" v-if="errorForm">
                                            {{errorMessage}}
                                        </v-alert>
                                    </v-col>
                                </v-row>

                            </v-container>
                        </div>
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
            checkbox: false,
            show1: false, // password interaction
            emailRules: [
                v => !!v || 'E-mail est requis',
                v => /.+@.+/.test(v) || 'E-mail invalide'
            ],
            passRules: [
                v => !!v || 'Le mot de passe est requis',
                v => v.length <= 10 || 'Votre mot de passe doit être inférieur à 10 caractères'
            ],
            validAlertForm: false, // for validate alert 
            errorForm: false, // for error alert
            errorMessage: '',
            validCount: 0,
            getLogDatas: '',
        }
    },
    methods: {
        rememberAccount(){ // Partie cookie : gestion de validateCookie du store
            if(this.checkbox == true){
                this.$cookies.set('connexion', true, 1);
                this.$store.state.validateCookie = this.$cookies.get('connexion')
                console.log(this.$store.state.validateCookie)
                console.log(this.$cookies.get('connexion'))
            } else if(this.checkbox == false){
                this.$cookies.remove('connexion')
                this.$store.state.validateCookie = false
                console.log(this.$store.state.validateCookie)
            }
        },
        sendValidation() {
            //console.log("Le formulaire est activé")
            const mail = document.getElementById('mailLog')
            const pass = document.getElementById('passLog')
            let mailLog = mail.value
            let passLog = pass.value

            if(mailLog != '' && passLog != ''){
                // ici traitement entre le mail, password entré et les données de getLogDatas
                for(let i = 0; i < this.getLogDatas.length; i++){
                    if(mailLog == this.getLogDatas[i].mail && passLog == this.getLogDatas[i].password){
                        this.validCount += 1
                    }
                }

                if(this.validCount == 1){
                    this.validAlertForm = true
                    // send validForm data to parent component (with delay)
                    setTimeout(() => {
                        this.rememberAccount();
                        this.$store.state.validateForm = true
                        this.$emit('availableLogin', {loginValidation: this.$store.state.validateForm})
                        this.$router.push({name: "projet1"})
                    }, 2000)
                    
                } else if (this.validCount == 0){
                    this.errorForm = true
                    this.errorMessage = 'E-mail et/ou mot de passe incorrect. Réessayez'
                    setTimeout(() => {
                        this.errorForm = false
                        // reload the page (JS METHOD)
                        window.location.reload()
                    }, 2000)
                }

            } else {
                this.errorForm = true
                this.errorMessage = 'Les champs renseignés sont vides.'
                setTimeout(() => {
                    this.errorForm = false
                    // reload the page (JS METHOD)
                    window.location.reload()
                }, 2000)
                
            }
        },
        async getAllAccounts(){ // DATABASE
            const path = 'http://localhost:5000/log';
            await axios.get(path)
            .then((res) => {
                this.getLogDatas = res.data.logins;
                //console.log(this.getLogDatas)
            })
            .catch((err) => {
                console.error(err);
            });
        },
        async checkCookieConnexion() {
            if(this.$cookies.isKey('connexion')){
                this.$store.state.validateForm = true
                console.log(this.$store.state.validateForm)
            } else {
                this.$store.state.validateForm = false
                console.log(this.$store.state.validateForm)
            }
        },
        redirectPasswordForgot() {
            // console.log("Redirection vers la partie récupération du mot de passe")
            this.$router.push({name: "recover"})
        },
    },
    created(){
        this.getAllAccounts();
        this.checkCookieConnexion();
    }
}
</script>

<style>
.form_part {
    height: 95vh !important;
    padding-top: 30vh;
}
.mainTitleAppli {
    font-weight: bold !important;
    text-shadow: 2px 2px 0px #d60, 2px 2px 2px #d60 !important;
}

#accountCookie:hover, #passForget:hover {
    color: black;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.4s ease-in-out;
}
</style>