<template>
   <div class="text-center pt-8">
    <!-- Un simple projet<br>
    Datas : <span class="font-weight-bold">{{dictionnaire.type}}</span> -->
    <p class="display-3 font-weight-bold text-decoration-underline">Exemple d'API</p>
    <v-form @submit.prevent="checkName" id="checkName" method="POST">
        <v-container>
            <v-row>
                <v-col
                cols="12"
                md="4"
                ></v-col>
                </v-col>
                <v-col
                cols="12"
                md="4"
                >
                <v-text-field
                    v-model="nomVille"
                    label="Nom de la ville"
                    name="ville"
                    required
                ></v-text-field>
                </v-col>
            </v-row>
            <v-btn type="submit" color="success" form="checkName">Rechercher</v-btn>
        </v-container>

    </v-form>

   </div>
</template>



<script>
import axios from 'axios';

export default {
    name: 'projet1', 
    data() {
        return {
            msg: "This is the projet page",
            dictionnaire: '',
            valid: false,
            nomVille: '',
            dataVille: '',
            ville: ''
        }
    },
    methods: {
        getDictionnaire() {
            const path = 'http://localhost:5000/projet1'
            axios.get(path)
            .then((result) => {
                this.dictionnaire = result.data;
                console.log(this.dictionnaire)
            })
            .catch(err => {console.log(err)});
        },
        checkName() {
            console.log(this.nomVille)
            const path="http://localhost:5000/projet1/add"
            let villeData = {
                ville: this.nomVille
            }
            axios.post(path, villeData)
            .then((resultat) => {
                this.dataVille = resultat.data;
                console.log(this.dataVille)
            }).catch(err => {console.log(err)});
        }
    },
    created() {
        this.getDictionnaire();
    }
}
</script>