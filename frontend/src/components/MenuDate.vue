<template>

{{date}}

</template>

<script>
export default {
    name: "MenuDate",
    data() {
        return {
            interval: null,
            date: '',
        }
    },
    beforeUnmount() {
        clearInterval(this.interval)
    },
    methods: {
        getDate() {
            this.date = Intl.DateTimeFormat(navigator.language, {
                day: 'numeric',
                month: 'numeric',
                year: 'numeric'
            }).format()
        }
    },
    created() {
        this.getDate()
    },
    mounted() {
        this.interval = setInterval(() => {
            this.getDate()
        }, 10000)
    }
}
</script>