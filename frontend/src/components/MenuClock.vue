<template>

{{time}}

</template>

<script>
export default {
    name: "MenuClock",
    data() {
        return {
            interval: null,
            time: '00:00:00',
        }
    },
    beforeUnmount() {
        clearInterval(this.interval)
    },
    methods: {
        getTime() {
            this.time = Intl.DateTimeFormat(navigator.language, {
                hour: 'numeric',
                minute: 'numeric',
                second: 'numeric'
            }).format()
        }
    },
    created() {
        this.getTime()
    },
    mounted() {
        this.interval = setInterval(() => {
            this.getTime()
        }, 1000)
    }
}
</script>