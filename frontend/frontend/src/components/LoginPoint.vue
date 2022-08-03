<template>
    <div class="">
        <!-- <p class="overline text-center">
            {{ msg1 }}
        </p> -->
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
                        <span class="display-2">Drawer Base</span><br>
                        <span class="overline">Bienvenue, veuillez vous connecter à votre compte</span>

                        <v-form v-model="valid">
                            <v-container>
                                <v-row>
                                    <v-col cols="1"></v-col>
                                    <v-col cols="10">
                                        <v-text-field v-model="mail" label="E-mail" required>
                                        </v-text-field>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="1"></v-col>
                                    <v-col cols="10">
                                        <v-text-field v-model="password" label="Password" required>
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
                                    <v-col col="1"></v-col>
                                    <v-col cols="10">
                                        <v-btn color="success" class="text-center mr-12 px-4 py-2" @click="validation">
                                        Validate
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
    data() {
            return {
            valid: false,
            mail: '',
            password: '',
            checkbox: true,
        }
    },
    methods: {
        validation() {

        }
    }
}
</script>

<style>
.form_part {
    height: 100vh !important;
    padding-top: 40vh;
}
</style>