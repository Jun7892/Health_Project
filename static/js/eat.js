// 윈도우가 로드될 때 휠 이벤트를 변경시키는데, e.preventDefault() 라는 함수가 보인다.
// 저 함수는 이벤트 함수를 받아서 윈도우의 기본 이벤트를 차단한다.
//
// passive 함수는 이 함수가 작동하는지에 대해 능동적 감시를 수행하는데,
// passive : false로 두면 감시가 일어나지 않기 때문에 당연히 그냥 원천 차단해버린다.

// window.addEventListener("wheel", function(e){
//     e.preventDefault();
// },{passive : false});


// js에서는 html을 변수로 두고 scrollTop을 통해 js 로드 시 혹시라도
// 만약에 뷰의 Yposition이 0이 아닐 경우를 대비해 다음과 같은 값을 추가

// var mHtml = $("html");
// var page = 1;
//
// mHtml.animate({scrollTop : 0},10);
// page는 나중에 쓰는 변수


// 만약 스크롤 애니메이팅 중일땐 바로 휠 애니메이션을 리턴한다.
//
// deltaY는 휠의 이동량을 의미하는데, delta>0이라는 것은 휠을 아래로 내리는 모션을 의미한다.
// 페이지 끝까지 내렸을때는, return을 통해 휠이동 모션을 방지한다.
//
// delta<0일때도 마찬가지다. deltaY가 음수라면 당연히 휠을 위로 올리는 모션을 의미한다.
// 처음으로 끝까지 올렸을때는, return을 통해 휠이동 모션을 방지
//
// $(window).on("wheel", function(e) {
//     if(mHtml.is(":animated")) return;
//     if(e.originalEvent.deltaY > 0) {
//         if(page == 4) return;
//         page++;
//     } else if(e.originalEvent.deltaY < 0) {
//         if(page == 1) return;
//         page--;
//     }
//     var posTop =(page-1) * $(window).height();
//     mHtml.animate({scrollTop : posTop});
// })

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
$( document ).ready(function() {
  var windowWidth = $( window ).width();
    console.log(windowWidth)
    if (windowWidth <= 1000){
        var btn = document.getElementsByClassName("myButton")
        btn.style.display= 'none';
        // $('.myButton').hide();
    }

})
$( window ).resize(function() {
   var windowWidth = $( window ).width();
    console.log(windowWidth)
    if (windowWidth <= 1000){
        $('.myButton').hide();
    }   else  {
        $('.myButton').show();
    }
});




// function block(){
//     var windowWidth = $( window ).width();
//     console.log(windowWidth)
//     if (windowWidth <= 600){
//         $('.myButton').hide();
//     }
// }

// if (document.documentElement.clientWidth <= 1000){
//     $('.myButton').style= 'display:none;'
// }



// // Skull mesh by DGordillo http://www.blendswap.com/blends/view/4792
//
// var renderer, scene, camera, group;
// var mouseX = 0;
// var mouseY= 0;
//
// var skull, leftEye, rightEye;
// var textMesh;
// var pointLights = [];
//
// var init = init();
// var animate = animate();
//
// function init() {
//
// 	// renderer
// 	renderer = new THREE.WebGLRenderer({ alpha: true });
// 	renderer.setPixelRatio( window.devicePixelRatio );
// 	renderer.setSize(window.innerWidth, window.innerHeight);
// 	renderer.shadowMap.enabled = true;
// 	document.body.appendChild(renderer.domElement);
//
// 	// camera
// 	camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, .1, 10000);
// 	camera.position.set(0, 0, 60);
// 	camera.zoom = 2;
// 	camera.updateProjectionMatrix();
//
// 	// scene
// 	scene = new THREE.Scene();
// 	scene.updateMatrixWorld();
//
// 	// lights
// 	var light = new THREE.SpotLight( 16726440, .5 );
// 	light.angle = 0.50;
// 	light.decay = 1;
// 	light.position.set( -50.56, -21.69, 50.41 );
// 	scene.add( light );
//
// 		 // var sphereSize = 10;
// 		 // var spotLightHelper = new THREE.SpotLightHelper( light, sphereSize );
// 		 //scene.add( spotLightHelper );
//
// 	var pointLight = new THREE.PointLight( 216285, 3.1 );
// 	pointLight.decay = 1;
// 	pointLight.position.set( -2.37, -18.15, 20.48 );
// 	scene.add( pointLight );
//
// 		//  var sphereSize = 1;
// 		//  var pointLightHelper = new THREE.PointLightHelper( pointLight, sphereSize );
// 		//  scene.add( pointLightHelper );
//
// 	var sphere = new THREE.SphereGeometry( 0.1, 16, 8 );
// 	for (var i = 0; i <= 8; i++) {
// 		light = new THREE.PointLight( 16726440, .8, 10 );
// 		light.add( new THREE.Mesh( sphere, new THREE.MeshBasicMaterial( { color: 16726440 } ) ) );
//
// 		scene.add( light );
// 		pointLights.push(light);
// 	}
//
//
//
// 	// grid helper
// 	var size = 100;
// 	var divisions = 10;
// 	var gridHelper = new THREE.GridHelper( size, divisions );
// 	//scene.add( gridHelper );
//
// 	// load meshes
//   var loader = new THREE.JSONLoader();
//   loader.load('https://raw.githubusercontent.com/ellenprobst/it-s-alive/master/blender/skull.json', generateSkull );
//   loader.load('https://raw.githubusercontent.com/ellenprobst/it-s-alive/master/blender/eyes.json', generateLeftEye );
//   loader.load('https://raw.githubusercontent.com/ellenprobst/it-s-alive/master/blender/eyes.json', generateRightEye );
//
//   	// create group
//   group = new THREE.Group();
//   group.position.x = 2;
// 	scene.add( group );
//
// 	// window resize
// 	window.addEventListener( 'resize', onWindowResize, false );
//
// 	// mouse move
// 	document.addEventListener('mousemove', onMouseMove, false);
//
//   	// load text
//   	generateText();
//
// };
//
// // generate text
// function generateText(){
// 	var loader = new THREE.FontLoader();
// 	loader.load( 'https://raw.githubusercontent.com/ellenprobst/it-s-alive/master/scripts/optimer_regular.typeface.json', function ( font ) {
//
// 	var textGeometry = new THREE.TextGeometry( "It's alive !", {
// 	    font: font,
// 	    size: 7.5,
// 	    height: 3,
// 	    curveSegments: 20
// 	  });
//
// 	var textMaterial = new THREE.MeshPhongMaterial(
// 	    { color: 16726440, specular: 0xffffff }
// 	);
//
// 	var mesh = new THREE.Mesh( textGeometry, textMaterial );
// 	mesh.scale.z =mesh.scale.y=mesh.scale.x=.3;
// 	mesh.position.y = -10;
// 	mesh.position.x = -6;
// 	mesh.rotation.y = .3;
//
// 	scene.add( mesh );
// 	});
//
// };
//
// // generate skull
// function generateSkull(geometry, material){
// 	geometry.computeVertexNormals();
//
// 	skull = new THREE.Mesh(geometry, material);
// 	skull.scale.y = skull.scale.z = skull.scale.x = 8.37;
//
// 	group.add( skull );
// };
//
// // generate eye
// function generateLeftEye(geometry, material){
// 	geometry.computeVertexNormals();
// 	geometry.center();
//
// 	leftEye = new THREE.Mesh(geometry, material);
// 	leftEye.scale.y = leftEye.scale.z = leftEye.scale.x = 8.5;
// 	leftEye.position.set(-4.5,1.7,4.3);
// 	leftEye.material.forEach(material => material.shininess = 40);
//
// 	// var box = new THREE.BoxHelper( eye, 0xffff00 );
// 	// scene.add( box );
//
// 	group.add( leftEye );
// };
//
// // generate eye
// function generateRightEye(geometry, material){
// 	geometry.computeVertexNormals();
// 	geometry.center();
//
// 	rightEye = new THREE.Mesh(geometry, material);
// 	rightEye.scale.y = rightEye.scale.z = rightEye.scale.x = 8.5;
// 	rightEye.position.set(0,1.7,4.3);
// 	rightEye.material.forEach(material => material.shininess = 40);
//
// 	// var box = new THREE.BoxHelper( eye, 0xffff00 );
// 	// scene.add( box );
//
// 	group.add( rightEye );
// };
//
// // Follows the mouse event
// function onMouseMove(event) {
//   event.preventDefault();
//
//   mouseX = (event.clientX / window.innerWidth) * 2 - 1;
//   mouseY = - (event.clientY / window.innerHeight) * 2 + 1;
// };
//
// // on resize
// function onWindowResize() {
//   camera.aspect = window.innerWidth / window.innerHeight;
//   camera.updateProjectionMatrix();
//   renderer.setSize( window.innerWidth, window.innerHeight );
// }
//
// // render
// function render() {
//   	renderer.render( scene, camera );
// };
//
// // animate
// function animate(event) {
//
// 	requestAnimationFrame( animate );
//
// 	if (group) {
// 		group.rotation.y = mouseX * .15;
// 		group.rotation.x = mouseY * -.15;
// 	}
//
// 	if (rightEye && leftEye) {
// 		leftEye.rotation.y = rightEye.rotation.y = mouseX * .50;
// 		leftEye.rotation.x = rightEye.rotation.x = mouseY * -.50;
// 	}
//
//   	var time = Date.now() * 0.0008 ;
// 	pointLights[0].position.x = Math.sin( time * 0.3  ) * 15;
// 	pointLights[0].position.y = Math.sin( time * 0.5  ) * 10;
// 	pointLights[0].position.z = Math.cos( time * 0.4  ) * 10;
//
//
// 	pointLights[1].position.x = Math.sin( time * 0.6  ) * 10;
// 	pointLights[1].position.y = Math.cos( time * 0.7 ) * 10;
// 	pointLights[1].position.z = Math.sin( time * 0.3 ) * 15;
//
// 	pointLights[2].position.x = Math.cos( time * 0.5  ) * 15;
// 	pointLights[2].position.y = Math.cos( time * 0.6 ) * 10;
// 	pointLights[2].position.z = Math.sin( time * 0.8 ) * 10;
//
// 	pointLights[3].position.x = Math.sin( time * 0.3  ) * 10;
// 	pointLights[3].position.y = Math.cos( time * 0.5 ) * 15;
// 	pointLights[3].position.z = Math.cos( time * 0.7 ) * 10;
//
// 	pointLights[4].position.x = Math.sin( time * 0.7  ) * 15;
// 	pointLights[4].position.y = Math.sin( time * 0.3 ) * 20;
// 	pointLights[4].position.z = Math.cos( time * 0.2 ) * 10;
//
// 	pointLights[5].position.x = Math.sin( time * 0.5  ) * 20;
// 	pointLights[5].position.y = Math.cos( time * 0.8 ) * 10;
// 	pointLights[5].position.z = Math.sin( time * 0.5 ) * 15;
//
// 	pointLights[6].position.x = Math.sin( time * 0.5  ) * 10;
// 	pointLights[6].position.y = Math.cos( time * 0.8 ) * 10;
// 	pointLights[6].position.z = Math.cos( time * 0.7 ) * 15;
//
// 	pointLights[7].position.x = Math.sin( time * 0.3  ) * 10;
// 	pointLights[7].position.y = Math.cos( time * 0.5 ) * 15;
// 	pointLights[7].position.z = Math.sin( time * 0.2 ) * 10;
//
// 	pointLights[8].position.x = Math.sin( time * 0.8  ) * 15;
// 	pointLights[8].position.y = Math.cos( time * 0.3 ) * 10;
// 	pointLights[8].position.z = Math.cos( time * 0.3 ) * 10;
//
// 	render();
// };

$(document).ready(function(){

	$('ul.tabs li').click(function(){
		var tab_id = $(this).attr('data-tab');

		$('ul.tabs li').removeClass('current');
		$('.tab-content').removeClass('current');

		$(this).addClass('current');
		$("#"+tab_id).addClass('current');
	})

})