window.onload = function() {

function onClick() {
    document.querySelector('.modal_wrap').style.display ='block';
    document.querySelector('.black_bg').style.display ='block';
}
function offClick() {
    document.querySelector('.modal_wrap').style.display ='none';
    document.querySelector('.black_bg').style.display ='none';
}

document.getElementById('modal_btn').addEventListener('click', onClick);
document.querySelector('.modal_close').addEventListener('click', offClick);

};
// function follow (){
//         var pk = $(".follow").attr('value')
//         console.log(pk)
//         current = window.location.href
//         $.ajax({ // 팔로우/팔로우취소 버튼을 클릭하면 <새로고침> 없이 ajax로 서버와 통신하겠다.
//           type: "POST", // 데이터를 전송하는 방법을 지정
//           url: "/second/test/update/follow/"+pk, // 통신할 url을 지정
//           data: {'url': current}, // 서버로 데이터 전송시 옵션
//           dataType: "json", // 서버측에서 전송한 데이터를 어떤 형식의 데이터로서 해석할 것인가를 지정, 없으면 알아서 판단
//           // 서버측에서 전송한 Response 데이터 형식 (json)
//           // {'likes_count': post.like_count, 'message': message }
//           success: function(response){
//             if (response.follow){
//                 alert('팔로우 완료');
//                 window.location.href
//             } else if (response.undofollow) {
//                 alert('팔로우가 해제되었습니다')
//             } else {
//                 alert('정상적이지 않은 접근입니다.')
//             }
//           },
//           error: function(request, status, error){ // 통신 실패시 - 로그인 페이지 리다이렉트
//             console.log(error)
//             //  alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
//           },
//         });
//       }