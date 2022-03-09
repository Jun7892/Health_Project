// 버튼 클릭시 display: flex 값 / 닫기 버튼 클릭시 modal display none 값

const modal = document.getElementById("modal")

function modalOn() {
    const modal = document.getElementById("modal")
    modal.style.display = "flex"
}

function modalOff() {
    const modal = document.getElementById("modal")
    console.log(modal)
    modal.style.display = "none"
}

const modal2 = document.getElementById("modal2")

function modalOn2() {
    const modal2 = document.getElementById("modal2")
    modal2.style.display = "flex"
}

function modalOff2() {
    const modal2 = document.getElementById("modal2")
    console.log(modal2)
    modal2.style.display = "none"
}

const modal3 = document.getElementById("modal3")

function modalOn3() {
    const modal3 = document.getElementById("modal3")
    modal3.style.display = "flex"
}

function modalOff3() {
    const modal3 = document.getElementById("modal3")
    console.log(modal3)
    modal3.style.display = "none"
}