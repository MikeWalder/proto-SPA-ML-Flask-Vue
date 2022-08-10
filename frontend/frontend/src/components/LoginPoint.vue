<template>
    <div id="loginAccount">
        <v-container>
            <v-row no-gutters>
                <v-col offset-sm="0" md="6">
                    <v-img
                    src="../../public/computer-mouse-in-action.jpg"
                    aspect-ratio="1.3"
                    height="100vh"
                    transition="scroll-x-transition"
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
                                <v-row>
                                    <v-col cols="1" md="2"></v-col>
                                    <v-col cols="5" md="4">
                                        <v-checkbox v-model="checkbox" :label="`Se souvenir de moi : ${checkbox.toString()}`"></v-checkbox>
                                        </v-checkbox>
                                    </v-col>
                                    <v-col cols="5" md="4" class="pt-8">
                                        Mot de passe perdu ?<br> <!-- ici ajouter le lien de récupération du mot de passe -->
                                        {{getLogDatas[0].password}} - {{getLogDatas[0].mail}}
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="2"></v-col>
                                    <v-col cols="8 text-center">
                                        <v-btn type="submit" color="success" elevation="6" large class="text-center font-weight-bold px-12 py-2" @click.once="sendValidation()">
                                        Valider
                                        </v-btn>
                                        <v-alert color="light-green" class="mt-6" dense dark transition="scale-transition" v-if="validForm">
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
            errorMessage: '',
            validCount: 0,
            getLogDatas: '',
        }
    },
    methods: {
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
                        console.log("Vous êtes autorisé à entrer dans l'application !")
                        this.validCount += 1
                    }
                }

                if(this.validCount == 1){
                    this.validForm = true 
                    this.$emit('availableLogin', {loginValidation: this.validForm})
                    setTimeout(() => {
                        this.validForm = false
                        this.$router.push({name: "projet1"})
                    }, 2000)
                    
                } else if (this.validCount == 0){
                    this.errorForm = true
                    this.errorMessage = 'Le mail et/ou le mot de passe est incorrect.Réessayez'
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
        /* async getResponse(){
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
        }, */
        async getAllAccounts(){ // DATABASE
            const path = 'http://localhost:5000/log';
            await axios.get(path)
            .then((res) => {
                this.getLogDatas = res.data.logins;
                console.log(this.getLogDatas)
            })
            .catch((err) => {
                console.error(err);
            });
        }
    },
    created(){
        this.getAllAccounts();
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
</style>