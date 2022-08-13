<template>
    <div class="img text-center">
        <!-- <p class="mt-16 font-weight-bold">Ceci est la page de déconnexion de l'application</p> -->
        <p class="mt-16 font-weight-bold display-1">Uploadez depuis votre PC ou entrez l'URL :</p>
                
                <v-container>
                    
                    <v-row>
                        <v-col 
                        cols="1"
                        md="4"
                        ></v-col>
                        <v-col 
                        cols="10"
                        md="4"
                        >
                        <div id="imageRender">
                            <img id="blah" v-if="imgURL !== null">
                        </div>
                        </v-col>
                        <v-col 
                        cols="1"
                        md="4"
                        ></v-col>
                    </v-row>

                    <v-row>
                        <v-col
                        cols="2"
                        md="4"
                        >
                        </v-col>

                        <v-col
                        cols="8"
                        md="4"
                        >
                        <v-file-input
                        v-model="imgURL"
                        show-size
                        label="Uploadez une image (JPEG, JPG ou PNG)"
                        :rules="imgRules"
                        accept="image/png, image/jpeg, image/jpg"
                        prepend-icon="mdi-camera"
                        name="imageTest"
                        onchange="document.getElementById('blah').src = window.URL.createObjectURL(this.files[0])"
                        ></v-file-input>
                        </v-col>

                        <v-col
                        cols="2"
                        md="4"
                        >
                        </v-col>
                    </v-row>
                    <v-btn color="success" elevation="12" @click="getImageRecognition()" class=" mx-0my-12">Informations</v-btn>
                
                </v-container>
                    <hr class="my-2">
                <v-container>
                    <v-row>
                        <v-col 
                        cols="1"
                        md="4"
                        ></v-col>
                        <v-col 
                        cols="10"
                        md="4"
                        >
                            <v-text-field 
                            prepend-icon="mdi-vector-link"
                            v-model="urlString" 
                            placeholder="https://exemple.com" 
                            :rules="rules" 
                            @change="imgUpload()">
                            </v-text-field>
                            <div class="rend" v-if="validateImgUrl">
                                <span color="text-green subtitle-1">Extension de fichier valide !</span> 
                            </div>
                        </v-col>
                        <v-col 
                        cols="1"
                        md="4"
                        ></v-col>
                    </v-row>
                    <v-row>
                        <v-col 
                        cols="1"
                        md="4"
                        ></v-col>
                        <v-col 
                        cols="10"
                        md="4"
                        >
                            <div id="imageRenderURL">
                                <img id="blahblah" v-if="urlString !== null" :src=urlString>
                            </div>
                            <div class="redux">
                                <div v-if="res !== ''">
                                    Catégorie : {{resJSON.result.categories[0].name.en}}
                                    <p>Précision : {{(resJSON.result.categories[0].confidence).toPrecision(4)}} %</p>
                                </div>
                            </div>
                        </v-col>
                        <v-col 
                        cols="1"
                        md="4"
                        ></v-col>
                    </v-row>
                </v-container>

    </div>
</template>


<script>
import axios from 'axios';
export default {
    name: 'LogOut', 
    data() {
        return {
            imgURL: null,
            imageResult: '',
            imgRules: [
                value => !value || value.size < 2000000 || "La taille est supérieure à 2 MB",
            ],
            res: '',
            resJSON: null,
            urlString: null,
            rules: [
                (value) => !!value || "Required.",
                (value) => this.isURL(value) || "URL is not valid",
            ],
            validateImgUrl: false,
            errorValidImageURL: false,
        }
    },
    methods: {
        async getImageRecognition() {
            const path = 'http://localhost:5000/image'
            let imgDatas = {
                imageName: this.imgURL.name,
                imageSize: this.imgURL.size,
            }
            //console.log(this.imgURL)
            axios.post(path, imgDatas)
            .then(res => {
                this.res = res.data
                console.log(this.res.response_text)
                })
            .catch(err => {console.log(err)});
        },
        isURL(str) {
            let url;

            try {
                url = new URL(str);
            } catch (_) {
                return false;
            }

            return url.protocol === "http:" || url.protocol === "https:";
        },
        imgUpload() {
            console.log(this.urlString)
            if(this.urlString.match(/\.(jpeg|jpg|png)$/)){
                //this.alertImgUrl = "Extension de fichier valide"
                this.validateImgUrl = true
                console.log(this.alertImgUrl)
                // on lance la reconnaissance d'image
                // 1) Requête Axios
                const path = 'http://localhost:5000/image/url'
                let imgDatas = {
                    imageURL: this.urlString,
                }
                axios.post(path, imgDatas)
                .then(res => { // Récupération des données
                    this.res = res.data
                    console.log(this.res.response_text)
                    this.resJSON = JSON.parse(this.res.response_text)
                    //console.log(this.resJSON.result.categories[0].name.en)
                    //console.log(this.resJSON.result.categories[0].confidence)
                    })
                .catch(err => {console.log(err)});
            }
            else {
                console.log("Format d'image invalide !")
                this.errorValidImageURL = true
            }
        },
        
    }
}
</script>

<style>
/* #imageRender {
    width: 220px !important;
    height: 220px !important;
    margin: 0 auto !important;
} */

#imageRender img, #imageRenderURL img {
    max-width: 200px !important;
    max-height: 200px !important;
    min-height: 150px !important;
    width: auto !important;
    height: auto !important;
    margin: 0 auto !important;
}

img {
    display: none !important;
    text-align: center !important;
    
    opacity: 0 !important;
    transition: all 0.4s ease-in !important;
}

img[src] {
    display: block !important;
    opacity: 1 !important;
}
.imgRender {
    text-align: center;
}
</style>