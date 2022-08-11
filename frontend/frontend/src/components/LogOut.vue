<template>
    <div class="img text-center">
        <p class="mt-16 font-weight-bold">Ceci est la page de déconnexion de l'application</p>

            
                <v-container>
                    <v-row>
                        <v-col
                        cols="0"
                        md="4"
                        >
                        </v-col>

                        <v-col
                        cols="12"
                        md="4"
                        >
                        <v-file-input
                        v-model="imgURL"
                        label="Uploadez une image (JPEG, JPG ou PNG)"
                        :rules="imgRules"
                        accept="image/png, image/jpeg, image/jpg"
                        prepend-icon="mdi-camera"
                        name="imageTest"
                        ></v-file-input>
                        </v-col>

                        <v-col
                        cols="0"
                        md="4"
                        >
                        </v-col>
                    </v-row>
                    <v-btn color="success" elevation="12" @click="getImageRecognition()" class="my-12">Informations</v-btn>
                </v-container>
            

        <div v-if="imgURL['name'] !==''">
            <p>{{imgURL['name']}}</p>
            <img :src="imgURL['name']"></img>
        </div>

    </div>
</template>


<script>
import axios from 'axios';
export default {
    name: 'LogOut', 
    data() {
        return {
            imgURL: '',
            imageResult: '',
            imgRules: [
                value => !value || value.size < 2000000 || "La taille est supérieure à 2 MB",
            ],
        }
    },
    methods: {
        async getImageRecognition() {
            const path = 'http://localhost:5000/image'
            let imgDatas = {
                image: this.imgURL['image']
            }
            console.log(this.imgURL)
            axios.post(path, imgDatas)
            .then(res => {
                this.res = res.data
                console.log(this.res)
                })
            .catch(err => {console.log(err)});
            
            /* axios.get(path)
            .then((result) => {
                this.imageResult = result.data;
                console.log(this.imageResult)
            })
            .catch(err => {console.log(err)}); */
            /* await axios.post(path, imgData, {
                headers: {
                    'Access-Control-Allow-Origin': '*'
                }
            })
            .then((result) => {
                this.imageResult = result.data;
                console.log(this.imageResult)
            })
            .catch(err => {console.log(err)}); */
        }
    }
}
</script>