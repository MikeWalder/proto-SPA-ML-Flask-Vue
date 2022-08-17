<template>
    <!-- <p class="text-center pa-6">{{ msg }}</p> -->
    <div>
        <br><br>
        <v-text-field v-model="exampleMail" placeholder="Enter a e-mail"></v-text-field><br>
        <input v-model="examplePass" placeholder="Enter a password"><br>
        <v-btn color="success" dark elevation="8" @click="getLoginDatas()">Add datas here !</v-btn><br>
        {{res.password}}
        <ul>
            <li v-for="item in resultLogins" :key="item.id">
                {{item.mail}} - {{item.password}}
            </li> 
        </ul>
        <div v-if="errorForm">Log is null !</div>
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
        }
    },
}
</script>