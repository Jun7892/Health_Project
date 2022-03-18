// var btn = document.getElementById('inputBtn')


    //XMLHttpRequest 객체 생성
    var xhr = new XMLHttpRequest();
    //요청을 보낼방식, url, 비동기 여부
    xhr.open('GET','/plan',true)

    //HTTP요청 헤더 설정
    // xhr.setRequestHeader('Content-type','application/json');

    xhr.send();

    xhr.onreadystatechange =function (){
        //서버가 응답시 발생하는 로직
        // 서버 응답 완료 && 정상 응답일시 그대로 리턴
         if (xhr.readyState !== XMLHttpRequest.DONE) return;


    }