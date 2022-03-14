// 윈도우가 로드될 때 휠 이벤트를 변경시키는데, e.preventDefault() 라는 함수가 보인다.
// 저 함수는 이벤트 함수를 받아서 윈도우의 기본 이벤트를 차단한다.
//
// passive 함수는 이 함수가 작동하는지에 대해 능동적 감시를 수행하는데,
// passive : false로 두면 감시가 일어나지 않기 때문에 당연히 그냥 원천 차단해버린다.

window.addEventListener("wheel", function(e){
    e.preventDefault();
},{passive : false});


// js에서는 html을 변수로 두고 scrollTop을 통해 js 로드 시 혹시라도
// 만약에 뷰의 Yposition이 0이 아닐 경우를 대비해 다음과 같은 값을 추가

var mHtml = $("html");
var page = 1;

mHtml.animate({scrollTop : 0},10);
// page는 나중에 쓰는 변수


// 만약 스크롤 애니메이팅 중일땐 바로 휠 애니메이션을 리턴한다.
//
// deltaY는 휠의 이동량을 의미하는데, delta>0이라는 것은 휠을 아래로 내리는 모션을 의미한다.
// 페이지 끝까지 내렸을때는, return을 통해 휠이동 모션을 방지한다.
//
// delta<0일때도 마찬가지다. deltaY가 음수라면 당연히 휠을 위로 올리는 모션을 의미한다.
// 처음으로 끝까지 올렸을때는, return을 통해 휠이동 모션을 방지

$(window).on("wheel", function(e) {
    if(mHtml.is(":animated")) return;
    if(e.originalEvent.deltaY > 0) {
        if(page == 4) return;
        page++;
    } else if(e.originalEvent.deltaY < 0) {
        if(page == 1) return;
        page--;
    }
    var posTop =(page-1) * $(window).height();
    mHtml.animate({scrollTop : posTop});
})

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

const modal4 = document.getElementById("modal4")

function modalOn4() {
    const modal4 = document.getElementById("modal4")
    modal4.style.display = "flex"
}

function modalOff4() {
    const modal4 = document.getElementById("modal4")
    console.log(modal4)
    modal4.style.display = "none"
}