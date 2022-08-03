<template>
    <p class="text-center pa-6">{{ msg }}</p>
</template>

<script>
export default {
    name: 'dashboard', 
    data() {
        return {
            msg: "This is the dashboard page",
        }
    },
}
</script>