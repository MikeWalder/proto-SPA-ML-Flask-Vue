<template>
    <div>
        <p class="mt-16 font-weight-bold text-center" id="titleDashboard">Tableau de bord</p>
            <v-container fluid class="pt-12">
                <v-row id="dashboardContainer">
                    <v-col
                    cols="6"
                    id="accountPart"
                    >
                        <div class="text-center font-weight-bold
                        ">
                            <span class="purple--text text-center">Données personnelles</span>
                        </div>
                    </v-col>

                    <v-col
                    cols="6"
                    id="chartPart"
                    >
                        <div class="text-center">
                            <span class="text-center">Partie données</span>
                        </div>
                    </v-col>
                </v-row>
            </v-container>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'dashboard', 
    data() {
        return {
            msg: "This is the dashboard page here ! ",
            exampleMail: '',
            examplePass: '',
            res: '',
            resultLogins: '',
            errorForm: false,
            connectCookie: null,
        }
    },
    methods: {
        getReponse(){
            const path = 'http://localhost:5000/dashboard/get';
            axios.get(path)
            .then((result) => {
                this.resultLogins = result.data.logins;
                console.log(this.resultLogins)
            })
            .catch(err => {console.log(err)});
        },
        getLoginDatas() {
            const path = 'http://localhost:5000/dashboard/new'
            let loginDatas = {
                mail: this.exampleMail,
                pass: this.examplePass
            }
            if(this.exampleMail !=='' && this.examplePass !==''){
                axios.post(path, loginDatas)
                .then(res => {
                    this.res = res.data
                    console.log(this.res)
                    this.getReponse()
                    })
                .catch(err => {console.log(err)});
            } else {
                this.errorForm = true
            }
        },
    },
}
</script>

<style>
.v-main__wrap {
    background-image: url('../../public/grid_project.jpg') !important;
    background-size: cover !important;
}

#titleDashboard {
    font-size: 30px !important;
}

#dashboardContainer {
    min-height: 80vh !important;
    border: 2px solid black !important;
}

#chartPart {
    background-color: rgba(31, 64, 209, 0.5) !important;
    min-height: 78vh !important;
}

#accountPart {
    background-color: rgba(224, 184, 26, 0.765) !important;
    min-height: 78vh !important;
    border-right: 2px solid black !important;
}

@media only screen and (max-width: 920px) {
    #titleDashboard {
        font-size: 20px !important;
    }
}
</style>