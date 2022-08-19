<template>
    <div class="img text-center">
        <!-- <p class="mt-16 font-weight-bold">Ceci est la page de déconnexion de l'application</p> -->
        <p class="mt-16 font-weight-bold" id="titleProjet">Entrez l'URL d'une image</p>
                
                <v-container>
                    
                    <v-row v-if="resLocalJSON == true">
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

                    <v-row v-if="resLocalJSON == true">
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
                        onchange="(setTimeout(() => {document.getElementById('blah').src = window.URL.createObjectURL(this.files[0])}, 500))"
                        ></v-file-input>
                        <br>
                        </v-col>

                        <v-col
                        cols="2"
                        md="4"
                        >
                        </v-col>
                    </v-row>
                    <v-btn v-if="imgURL !== null" large color="success" elevation="12" @click="getImageRecognition()" class=" mx-0 my-4">Valider</v-btn>
                
                </v-container>

                    <v-divider class="my-4" v-if="resLocalJSON == true"></v-divider>

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
                            :hint="alertImgURL"
                            @change="imgUpload()">
                            </v-text-field>
                            <!-- <div class="rend" v-if="validateImgUrl">
                                <v-subheader>{{alertImgURL}}</v-subheader>
                            </div>
                            <div class="rend" v-if="errorValidImageURL">
                                <v-subheader>{{alertImgURL}}</v-subheader>
                            </div> -->
                        </v-col>
                        <v-col 
                        cols="1"
                        md="4"
                        ></v-col>
                    </v-row>
                    <v-row>
                        <v-col 
                        cols="0"
                        md="2"
                        ></v-col>
                        <v-col 
                        cols="12"
                        md="4"
                        >
                            <div id="imageRenderURL">
                                <img id="blahblah" v-if="urlString !== null" :src=urlString>
                            
                                <div class="redux">
                                    <div v-if="res !== ''">
                                        Catégorie : {{resJSON.result.categories[0].name.en}}
                                        <p>Précision : {{(resJSON.result.categories[0].confidence).toPrecision(4)}} %</p>
                                    </div>
                                </div>
                            </div>
                        </v-col>
                        <v-col 
                        cols="12"
                        md="4"
                        >
                            <div class="text-center">
                                <canvas id="myChart"></canvas>
                            </div>

                        </v-col>
                        <v-col 
                        cols="0"
                        md="2"
                        ></v-col>
                    </v-row>
                </v-container>

    </div>
</template>


<script>
import axios from 'axios';
export default {
    name: 'projet1', 
    data() {
        return {
            imgURL: null,
            imageResult: '',
            imgRules: [
                value => !value || value.size < 2000000 || "La taille est supérieure à 2 MB",
            ],
            res: '',
            resJSON: null,
            resLocalJSON: null,
            resultLabels: [],
            resultProportions: [],
            myChart: null,
            urlString: null,
            rules: [
                (value) => !!value || "URL requis",
                (value) => this.isURL(value) || "URL invalide",
            ],
            validateImgUrl: false,
            errorValidImageURL: false,
            alertImgURL: '',
            srcImagePc: '',
            selectedFile : null,
        }
    },
    methods: {
        refreshImage() {
            this.srcImagePc = document.getElementById("blah").src
        },
        getImageRecognition() {
            const path = 'http://localhost:5000/image/local'
            this.refreshImage()
            console.log(this.srcImagePc)
            let imgDatas = {
                imageLocal: this.srcImagePc,
            }
            axios.post(path, imgDatas)
            .then(result => {
                this.result = result.data
                console.log(this.result.response_text)
                this.resLocalJSON = JSON.parse(this.result.response_text)
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
        chartApiDatas() {

            // Vérifier si un chart existe déjà, auquel cas le détruire
            console.log(this.myChart)
            if(this.myChart !== null) {
                this.myChart.destroy();
            }
            const labels = this.resultLabels;
            const data = {
                labels: labels,
                datasets: [{
                    label: 'Classification de l\'image',
                    backgroundColor: [
                        'rgb(255, 99, 132)',
                        'rgb(54, 162, 235)',
                        'rgb(255, 205, 86)'
                    ],
                    borderColor: 'rgb(0, 0, 0)',
                    borderWidth: 3,
                    data: this.resultProportions,
                }]
            };

            const config = {
                type: 'bar',
                data: data,
                options: {
                    indexAxis: 'y',
                    responsive: true,
                    legend: {
                        display: true,
                        position: 'top',
                        labels: {
                            color: 'rgb(255, 99, 132)'
                        }
                    },
                    plugins: {
                        legend: {
                            position: 'bottom'

                        },
                        title: {
                            display: true,
                            text: 'Résultat par catégorie et pourcentage',
                            font: {
                                size: 16,
                            },
                        },
                    },
                    animation: {
                        animateScale: true,
                        animateRotate: true
                    }
                }
            };

            let myChart = new Chart(
                document.getElementById('myChart'),
                config
            );
            this.myChart = myChart

            return myChart
        },
        imgUpload() {
            console.log(this.urlString)
            this.alertImgURL = ''
            this.resultLabels = []
            this.resultProportions = []
            if(this.urlString.match(/\.(jpeg|jpg|png)$/)){

                this.validateImgUrl = true
                this.alertImgURL = ''
                this.alertImgURL = 'Extension d\'image valide'
                console.log(this.alertImgUrl)

                // Requête Axios
                const path = 'http://localhost:5000/image/url'
                let imgDatas = {
                    imageURL: this.urlString,
                }
                axios.post(path, imgDatas)
                .then(res => { // Récupération des données
                    this.res = res.data
                    console.log(this.res.response_text)
                    this.resJSON = JSON.parse(this.res.response_text)
                    // Insertion des données dans des tableaux 
                    let count = this.resJSON.result.categories.length
                    if(count > 3){
                        count = 3
                    }
                    for(let i = 0; i < count; i++){
                        this.resultLabels[i] = this.resJSON.result.categories[i].name.en
                        this.resultProportions[i] = (this.resJSON.result.categories[i].confidence)
                    }
                    console.log(this.resultProportions)
                    this.chartApiDatas();
                    //console.log(this.resJSON.result.categories[0].name.en)
                    //console.log(this.resJSON.result.categories[0].confidence)
                    })
                .catch(err => {console.log(err)});
            }
            else {
                this.errorValidImageURL = true
                this.alertImgURL = "Format d'image invalide"
            }
        },
        verifyConnection() {
            if(this.$cookies.isKey("connexion")){
                console.log("Le cookie est existant")
            }
        },
    },
    beforeMount() {
        this.verifyConnection()
    },
}

</script>

<style>
#titleProjet {
    font-size: 30px !important;
}

#imageRenderURL {
    display: inline-block !important;
    vertical-align: middle !important;
    margin: auto 0 !important;
}

#imageRender img, #imageRenderURL img {
    max-width: 500px !important;
    max-height: 500px !important;
    min-height: 450px !important;
    min-width: 450 px !important;
    width: auto !important;
    height: auto !important;
    margin: auto !important;
    display: inline-block !important;
    vertical-align: middle !important;
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
    text-align: center !important;
    display: inline-block !important;
    vertical-align: middle !important;
}

#myChart {
    height: auto !important;
    min-height: 200px !important;
    width: auto !important;
    min-width: 300px !important;
    margin: 0 auto !important;
}
.v-main__wrap {
    background-image: url('../../public/grid_project.jpg') !important;
    background-size: cover !important;
}

@media only screen and (max-width: 920px) {
    .v-main__wrap {
        background-image: none !important;
        background-color: #e5e5e5 !important;
    }
    #titleProjet {
        font-size: 20px !important;
    }
}
</style>