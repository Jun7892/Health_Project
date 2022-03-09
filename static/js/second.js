// 버튼 클릭시 display: flex 값 / 닫기 버튼 클릭시 modal display none 값

const modal = document.getElementById("modal")

function modalOn() {
    modal.style.display = "flex"
}

function modalOff() {
    const modal = document.getElementById("modal")
    console.log(modal)
    modal.style.display = "none"
}