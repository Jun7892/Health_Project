$(document).ready(function () {
    // 무한 반복 슬라이딩 //

    let current = 0;
    let show = 5;
    let container = $('.sliding-view .AI_container');
    let length = container.find('.AI_li').length;
    let view = $('.sliding-view').width();
    let tt = view / show; //이동거리 -한칸씩 움직이기//
    let next = $('.sliding-box .right');
    let prev = $('.sliding-box .left');

    container.css('width', 'length*tt');//컨테이너 길이 초기화//

    next.on({
        click: function () {

            if (current == length) {//마지막 엘리먼트에 다다르면 current 초기화//
                current = 0;
            }

            if (current == 0) {
                //먼저 복사된 엘리먼트 삭제하고 위치 초기화//
                container.find('.AI_li').eq(length - 1).nextAll().remove();
                container.css({ left: 0 }).stop();

                //이동//
                current++;
                container.stop().animate({ left: tt * current * -1 }, { duration: 900 });

                //엘리먼트 복사 - 컨네이너의 자식 모두 복사//
                let cloneEl = container.children().clone();
                //복사된 엘리먼트 수 만큼 길이 늘리고 붙이기//
                container.css({ width: container.innerWidth() + (tt * length) });
                cloneEl.appendTo(container);
            }
            else if (current >= 1) {

                current++;
                container.stop().animate({ left: tt * current * -1 }, { duration: 900 });
            }

        },
        mouseenter: function () {
            clearInterval(Sliding);
        },
        mouseleave: function () {
            slidingTimer();
        }
    });

    prev.on({
        click: function () {
            if (current == 0) {
                //먼저 복사된 엘리먼트 삭제하고 위치 초기화//
                container.find('.AI_li').eq(length - 1).nextAll().remove();
                container.css({ left: 0 }).stop();

                //인덱스 순서를 length로 치환해줌//
                current = length;

                //앞쪽으로 엘리먼트 복사해서 붙이기//
                //길이 & 위치 초기화 -앞쪽으로 붙었기 떄문에 늘어난 길이 만큼 left시작 위치가 -가 되어야함//
                let cloneEl = container.children().clone();

                container.css({ left: tt * length * -1, width: container.innerWidth() + (tt * length) }).stop();
                cloneEl.prependTo(container);

                //붙이고 나서 바로 이동 되도록//
                current--;
                container.stop().animate({ left: tt * current * -1 }, { duration: 900 });
            }
            else if (current > 0) {
                current--;
                container.stop().animate({ left: tt * current * -1 }, { duration: 900 });
            }

        },
        mouseenter: function () {
            clearInterval(Sliding);
        },
        mouseleave: function () {
            slidingTimer();
        }
    });


    //컨테이너에 hover 되면 타이머 일시정지//
    container.on({
        mouseenter: function () {
            clearInterval(Sliding);
        },
        mouseleave: function () {
            slidingTimer();
        }
    });

    slidingTimer();

    //자동 슬라이딩 타미머 함수 정의//
    function slidingTimer() {
        Sliding = setInterval(function () {

            next.trigger('click');

        }, 3000);
    }
});









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
// init();
// animate();
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

