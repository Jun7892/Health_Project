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


// $(function () {
// // 회원가입, 로그인 창 닫기
// $('.btn-close').click(function (e) {
//     // 회원가입, 로그인 창 닫을 시 현재 화면으로 새로고침
//     location.reload();
// });

// 회원가입 진행
$('.btn-signup').click(function (e) {
    // btn-signup 클래스 부분을 클릭 시, 링크 이동 등 어떠한 행위도 동작하지 않도록 해주는 함수 -> ajax 작동 위해 필요한 선행 작업
    e.preventDefault();
    // user-signup 아이디(여기선 회원가입 form 태그) 부분의 html 태그를 form 변수에 저장
    var form = $('#user-signup')[0];
    // form 태그 안에 있는 모든 input으로 입력한 value값을 'name'을 key로 하여, formData 변수에 저장
    // --> ex. <input type="text" placeholder="이메일 주소 입력" class="form-control" id="login-user-email" name="email"> 에서 유저가 positipman@gmail.com을 입력했다면, formData에서 key는 email, value는 positipman@gmail.com 이 된다.
    var formData = new FormData(form);
    var realName = $('#signup-nickname').val();
    $.ajax({
        url: 'http://127.0.0.1:8000/second/',
        // form에 file type 이 있는 경우 enctype: 'multipart/form-data'를 설정해야 한다.
        enctype: 'multipart/form-data',
        // formData를 이용하기 위해서 아래 processData, contentType을 반드시 false로 설정해줘야 한다.
        processData: false,
        contentType: false,
        // ajax 통신 중, cache가 남아서 갱신 데이터를 받아오지 못하는 경우 사용한다.
        cache: false,
        type: "POST",
        // data로는 formData를 request로 보낸다.
        data: formData,
    }).done(function (data) {
        // request 보낸 url에서 회원가입 정상 진행해도 무방하여 {'works':True}를 JsonResponse로 보낸 경우
        if (data.works) {
            alert('환영합니다 ' + realName + '님\n' + '회원가입이 성공적으로 완료되었습니다');
            location.reload();
            // request 보낸 url에서 사용자 이름이 없다고 {'noRealName':True}를 JsonResponse로 보낸 경우
        } else if (data.noRealName) {
            alert('이름을 입력해주세요');
            // request 보낸 url에서 사용자 패스워드가 없다고 {'noPassword':True}를 JsonResponse로 보낸 경우
        } else if (data.noPassword) {
            alert('비밀번호를 입력해주세요');
            // 그 밖 모든 data를 JsonResponse로 보낸 경우
        } else {
            alert('정상 요청이 아닙니다');
        }
    });
});

// 로그인 진행
$('.btn-login').click(function (e) {
    e.preventDefault();
    var form = $('#user-login')[0];
    var formData = new FormData(form);

    $.ajax({
        url: 'http://127.0.0.1:8000/second/',
        enctype: 'multipart/form-data',
        processData: false,
        contentType: false,
        cache: false,
        method: 'POST',
        data: formData,
    }).done(function (data) {
        if (data.works) {
            alert('로그인되었습니다')
            location.reload();
        } else if (data.wrongInformation) {
            alert('입력된 정보와 일치하는 회원 정보가 없습니다');
            $('#login-user-password').val("");

        } else if (data.noPassword) {
            alert('비밀번호를 입력해주세요');
        } else {
            alert('정상 요청이 아닙니다');
        }
    });
});


//     // 로그아웃 진행
//     $('.user-logout').click(function (e) {
//         e.preventDefault();
//         var url = $(this).attr('href');
//         var check = confirm('로그아웃 하시겠습니까?');
//         if (check == true) {
//             $.ajax({
//                 url: url,
//                 method: "POST",
//                 data: {
//                     'csrfmiddlewaretoken': '{{csrf_token}}',
//                 },
//             }).done(function (data) {
//                 if (data.works) {
//                     alert('로그아웃 되었습니다.');
//                     location.reload();
//                 } else {
//                     alert('정상 요청이 아닙니다.');
//                 }
//             });
//         } else {
//             location.reload();
//         }
//     });
// });