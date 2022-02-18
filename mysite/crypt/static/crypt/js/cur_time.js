mainLoop = () => {
    var today = new Date()
    var year = today.getFullYear()
    var month = ('0'  + (today.getMonth()+1)).slice(-2)
    var date = ('0'  + today.getDate()).slice(-2)

    var calen_el = document.getElementById('calendar')
    calen_el.innerText = date + '/' + month + '/' + year

    var today = new Date()
    var hours = ('0'  + today.getHours()).slice(-2)
    var minutes = ('0'  + today.getMinutes()).slice(-2)
    var seconds = ('0'  + today.getSeconds()).slice(-2)

    var clock_el = document.getElementById('clock')
    clock_el.innerText = hours + ':' + minutes + ':' + seconds

    setTimeout(() => {
        requestAnimationFrame(this.mainLoop);
    }, 1000 / 1); // 1 FPS
}
mainLoop()