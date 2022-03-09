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

let isPlaying = false;
let audio = document.getElementById("myAudio");

function charm(sound1) {

    // let audio = new Audio(sound1);
    audio.loop = true;
    audio.volume = 0.5;
    isPlaying ? audio.pause() : audio.play();


    audio.onplaying = function () {
        isPlaying = true;
    };
    audio.onpause = function () {
        isPlaying = false;
    };
    console.log('aaaa');
}