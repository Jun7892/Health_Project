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

$('#btn-signup').click(function () {
    var id = $('#user_id').val();
    var pw = $('#login-user-password').val();
    var nn = $('#user_nn').val();
    var em = $('#user_em').val();
    var ge = $("input[name='gender']:checked").val();
    var age = $('#user_age').val();

    console.log(id)
    console.log(pw)
    console.log(nn)
    console.log(ge)
    console.log(age)
    console.log(em)
    $.ajax({
        url: '/second/sign_up',
        // form에 file type 이 있는 경우 enctype: 'multipart/form-data'를 설정해야 한다.
        enctype: 'multipart/form-data',
        // formData를 이용하기 위해서 아래 processData, contentType을 반드시 false로 설정해줘야 한다.
        processData: false,
        contentType: false,
        // ajax 통신 중, cache가 남아서 갱신 데이터를 받아오지 못하는 경우 사용한다.
        cache: false,
        async: false,
        type: "POST",
        datatype: 'json',
        // data로는 formData를 request로 보낸다.
        data: JSON.stringify({'username': id, 'password': pw, 'nickname': nn, 'email': em, 'gender': ge, 'age': age}),
        success: function (data) {
            if (data.works) { //통과했으면 로그인시켜서 데이터가 넘어왔기 때문에 메인페이지로 보냄
            alert('회원가입이 성공적으로 완료되었습니다');
            window.location.href = '/main'
                // 이미 존재하는 아이디가 있을때
            } else if (data.existid) {
                alert('이미 존재하는 아이디 입니다.');
                window.location.reload();
                // 존재하는 이메일로 가입했을때
            } else if (data.existemail) {
                alert('이미 존재하는 이메일입니다.');
                window.location.reload();
                //이메일 유효성 검사 통과 못했을때
            }else if (data.invalid_email) {
                alert('유효한 이메일을 입력하세요');
                //빈칸통과 못했을때
            } else if (data.blank) {
                alert('빈칸이 있는지 확인하세요!');
                // 나이가 6~99살안에 존재하지 않을때
            } else if (data.noway) {
                alert('11세이상~99세이하의 나이로 입력해주세요');
                 // 나이가 6세미만
            } else if (data.baby) {
                alert('11세이상부터 가입이 가능합니다.');
            // 그 밖 모든 data를 JsonResponse로 보낸 경우
            } else if (data.str_age) {
                alert('나이는 숫자만 입력해주세요.');
            // 그 밖 모든 data를 JsonResponse로 보낸 경우
            } else {
                alert('정상 요청이 아닙니다');
            }
        }
    })
});

if (matchMedia("(max-width: 800px)").matches){

} else {
    window.addEventListener("mousemove",function (){
    $('.signup_desc').show()
})
}

//아이디 인풋창 입력시 로그인div 보이게하기
if (matchMedia("(max-width: 800px)").matches){
    var login_desc = document.getElementsByClassName("login_desc")
    login_desc.style.display ='none'
} else {
    const id_input = document.getElementById("user_id2");
    id_input.addEventListener("keypress",function(e){
        $(".login_desc").show();
        $(".login_desc_msg1").show()
        $(".login_desc_msg2").show()
    });
   // change functionality for larger screens
}

// 로그인 진행
$('.btn-login').click(function (e) {
    // e.preventDefault();
    var id2 = $('#user_id2').val();
    var pw2 = $('#login-user-password2').val();
    console.log(id2)
    console.log(pw2)

    $.ajax({
        url: '/second/sign_in',
        // form에 file type 이 있는 경우 enctype: 'multipart/form-data'를 설정해야 한다.
        enctype: 'multipart/form-data',
        // formData를 이용하기 위해서 아래 processData, contentType을 반드시 false로 설정해줘야 한다.
        processData: false,
        contentType: false,
        // ajax 통신 중, cache가 남아서 갱신 데이터를 받아오지 못하는 경우 사용한다.
        cache: false,
        async: false,
        type: "POST",
        datatype: 'json',
        // data로는 formData를 request로 보낸다.
        data: JSON.stringify({'username': id2, 'password': pw2}),
    }).done(function (data) {
        if (data.works) {
            alert('로그인되었습니다')
            window.location.href = '/main'

        } else if (data.no_user) {
            alert('입력된 정보와 일치하는 회원 정보가 없습니다');
            $('#login-user-password').val("");

        } else if (data.blank) {
            alert('아이디와 패스워드를 모두 입력해주세요');

        } else if (data.wrong_pw) {
            alert('비밀번호가 일치하지 않습니다.');

        } else {
            alert('정상 요청이 아닙니다');
        }
    });
});
