<template>
    <p class="text-center pa-6">{{ msg }}</p>
</template>

<script>
import axios from 'axios'
export default {
    name: 'dashboard', 
    data() {
        return {
            msg: "This is the dashboard page here ! ",
        }
    },
    methods: {
        getReponse(){
            const path = 'http://localhost:5000/dashboard';
            axios.get(path)
            .then((res) => {
                console.log(res.data)
                this.msg = res.data;
            })
            .catch((err) => {
                console.error(err);
            });
        }
    },
    created(){
        this.getReponse();
    }
}
</script>