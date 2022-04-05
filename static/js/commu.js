// $(document).ready(function () {
//
// // CANVAS & MOBILE TEST
//     var windowWidth = $(window).width(),
//         windowHeight = $(window).height();
//     var isMobile = navigator.userAgent.match(/mobile/i);
//     var webGLTrue = false;
//
//     if (window.WebGLRenderingContext) {
//         webGLTrue = true;
//     }
//
// // CLASSES
//     if (isMobile) {
//         $('body').addClass('mobile');
//     } else if (!isMobile) {
//         $('body').addClass('desktop');
//     }
//
// // GLOBAL VARIABLES
//     var img,
//         canvas,
//         container,
//         imgRatio,
//         containerRatio;
//     var screenShotCanvas,
//         canvasDataURL,
//         canvasImage,
//         screenCaptured = false,
//         animateable = true,
//         popstate = false,
//         isFourOhFour = false,
//         inputReady = true;
//
//     var seriously,
//         sourceImage,
//         layers,
//         edge,
//         blend1,
//         linearGreen,
//         scale1,
//         blend2,
//         linearPurple,
//         scale2,
//         blend3,
//         blend4,
//         blend5,
//         target;
//
// // INITIAL LOAD FUNCTIONS
//     startupFunctions();
//
//     $(window).load(function () {
//         if (webGLTrue) {
//             captureScreen();
//         }
//         initialLoader();
//     });
//
//     function startupFunctions() {
//         if (isMobile) {
//             $('body').removeClass('noscroll');
//         }
//
//         widowControl();
//     }
//
// // IMAGE FUNCTIONS
//     function imageFunctions() {
//
//         var slickDrag = false;
//         if (isMobile) {
//             slickDrag = true;
//         }
//     }
//
// // DEBOUNCE FUNCTION
//     function debounce(func, wait, immediate) {
//         var timeout;
//
//         return function () {
//             var context = this, args = arguments;
//             var later = function () {
//                 timeout = null;
//                 if (!immediate) func.apply(context, args);
//             };
//             var callNow = immediate && !timeout;
//             clearTimeout(timeout);
//             timeout = setTimeout(later, wait);
//             if (callNow) func.apply(context, args);
//         };
//     };
//
//     var debounceAdjust = debounce(function () {
//         widowControl();
//     }, 50);
//
//     window.addEventListener('resize', debounceAdjust);
//
// // WIDOW CONTROL
//     function widowControl() {
//         windowWidth = $(window).width();
//         var widowElements = $('h1, h2, h3, h4, h5, h6, li, p, figcaption, .case-study-tagline, .large-cta').not('.discovery_cell p, #site-nav li, footer li');
//
//
//         widowElements.each(function () {
//             $(this).html($(this).html().replace(/&nbsp;/g, ' '));
//         });
//
//         if (windowWidth > 640) {
//             widowElements.each(function () {
//                 $(this).html($(this).html().replace(/\s((?=(([^\s<>]|<[^>]*>)+))\2)\s*$/, '&nbsp;$1'));
//             });
//         }
//     };
//
// // HTML CANVAS & INITIAL LOAD FUNCTIONS
//     function captureScreen() {
//         html2canvas($('.ajax'), {
//             letterRendering: true,
//             allowTaint: true,
//             onrendered: function (canvas) {
//                 screenShotCanvas = canvas;
//                 canvasDataURL = screenShotCanvas.toDataURL();
//                 canvasImage = new Image();
//                 canvasImage.src = canvasDataURL;
//                 screenCaptured = true;
//                 console.log(canvas);
//             }
//         });
//     }
//
//     function initialLoader() {
//         $('body').removeClass('noscroll');
//
//         var loadText = 'Warning: Intrusion detected.';
//         var loaderDone = false;
//         $.each(loadText.split(''), function (i, letter) {
//             setTimeout(function () {
//                 $('#loader-text').html($('#loader-text').html() + letter);
//             }, 60 * i);
//         });
//
//         setTimeout(function () {
//             loaderDone = true;
//         }, 1700);
//
//
// //check to make sure the document has been fully loaded before removing loader
//         var readyStateCheckInterval = setInterval(function () {
//             if (document.readyState === "complete" && loaderDone) {
//                 clearInterval(readyStateCheckInterval);
//                 $('#initial-loader').velocity({
//                     translateZ: 0,
//                     opacity: 0
//                 }, {
//                     display: 'none',
//                     delay: 0,
//                     duration: 800
//                 });
//
//                 if (webGLTrue) {
//                     loadPageCanvas();
//
//                     setTimeout(function () {
//                         removePageCanvas();
//                         $('#initial-loader').remove();
//                     }, 500);
//                 } else {
//                     setTimeout(function () {
//                         $('#initial-loader').remove();
//                     }, 1001);
//                 }
//             }
//         }, 10);
//     }
//
//
// // GLITCHING
//     function initializeGlitch(image, height) {
//         var container,
//             stats;
//
//         var camera,
//             scene,
//             sceneBG,
//             renderer,
//             composer,
//             composerScene;
//
//         var mesh,
//             light,
//             dotEffect,
//             shiftEffect,
//             sepiaEffect;
//
//         var glitchDtSize = 100,
//             glitchDelay = 1,
//             glitchAmplification = .5;
//
//         var fps = 20;
//         if (isFourOhFour) {
//             fps = 5;
//         }
//
//         var SCREEN_WIDTH = window.innerWidth;
//         var SCREEN_HEIGHT = height;
//         var ratio = SCREEN_WIDTH / SCREEN_HEIGHT;
//
//         if (height > 4096) {
//             SCREEN_HEIGHT = 4096;
//         }
//
//         var windowHalfX = window.innerWidth / 2;
//         var windowHalfY = height / 2;
//
//         var delta = 0.1;
//
//         function init() {
//             scene = new THREE.Scene();
//             sceneBG = new THREE.Scene();
//
//             camera = new THREE.OrthographicCamera(-windowHalfX, windowHalfX, windowHalfY, -windowHalfY, 1, 10000);
//             camera.position.z = 100;
//
// //background
//             background = new THREE.MeshBasicMaterial({
//                 map: THREE.ImageUtils.loadTexture(image),
//                 depthTest: false
//             });
//
//             background.map.needsUpdate = true;
//             var plane = new THREE.PlaneBufferGeometry(1, 1);
//
//             var bgMesh = new THREE.Mesh(plane, background);
//             bgMesh.position.z = 1;
//             bgMesh.scale.set(SCREEN_WIDTH, height, 1);
//             sceneBG.add(bgMesh);
//
//             bgMesh.material.map.needsUpdate = true;
//
//
//             var sceneMask = new THREE.Scene();
//
//             renderer = new THREE.WebGLRenderer();
//             renderer.setClearColor(0xffffff);
//             renderer.setSize(window.innerWidth, window.innerHeight);
//             renderer.setPixelRatio(window.devicePixelRatio);
//             renderer.autoClear = false;
//
//             renderer.gammaInput = true;
//             renderer.gammaOutput = true;
//
//             renderBackground = new THREE.RenderPass(sceneBG, camera);
//
//             $(renderer.domElement).attr('id', 'loader').css('height', height);
//             $('#main-body').append(renderer.domElement);
//
//             var rtParameters = {
//                 minFilter: THREE.LinearFilter,
//                 magFilter: THREE.LinearFilter,
//                 format: THREE.RGBFormat,
//                 stencilBuffer: true
//             };
//
//             var clearMask = new THREE.ClearMaskPass();
//
//             composer = new THREE.EffectComposer(renderer, new THREE.WebGLRenderTarget(SCREEN_WIDTH, SCREEN_HEIGHT, rtParameters));
//             renderScene = new THREE.TexturePass(composer.renderTarget2);
//             composer.addPass(renderBackground);
//             composer.addPass(clearMask);
//
//             composer1 = new THREE.EffectComposer(renderer, new THREE.WebGLRenderTarget(SCREEN_WIDTH, SCREEN_HEIGHT, rtParameters));
//
//             var glitch = new THREE.GlitchPass(glitchDtSize, glitchDelay, glitchAmplification);
//             glitch.renderToScreen = true;
//
//             composer1.addPass(renderScene);
//             composer1.addPass(glitch);
//
//             renderScene.uniforms['tDiffuse'].value = composer.renderTarget2;
//         }
//
//         function render() {
//             renderer.clear();
//             composer.render(delta);
//             composer1.render(delta);
//         }
//
//         function animate() {
//             if (animateable) {
//                 setTimeout(function () {
//                     render();
//                     requestAnimationFrame(animate);
//                 }, 1000 / fps);
//             }
//         }
//
//         init();
//         animate();
//     }
//
//     function loadPageCanvas() {
//         $('html').velocity('scroll', {
//             axis: 'y',
//             duration: 1000,
//             mobileHA: false
//         });
//
//         animateable = true;
//
//         initializeGlitch(canvasDataURL, screenShotCanvas.height);
//
//         $('#loader').velocity({
//             opacity: [1, 0]
//         }, {
//             duration: 1000
//         });
//     }
//
//
//     function removePageCanvas() {
//         $('#loader').velocity({
//             opacity: 0
//         }, {
//             delay: 500,
//             duration: 1000
//         });
//
//         setTimeout(function () {
//             animateable = false;
//             $('#loader').remove();
//         }, 1600);
//     }
//
//     function loadPageStatic() {
//         $('body').prepend('<div id="initial-loader" class="padded" style="opacity: 0;"><span id="loader-text"></span></div>');
//
//         $('#initial-loader').velocity({
//             translateZ: 0,
//             opacity: 1
//         }, {
//             duration: 150
//         });
//     }
//
//     function removePageStatic() {
//         var loadText = 'Loaded';
//         $.each(loadText.split(''), function (i, letter) {
//             setTimeout(function () {
//                 $('#loader-text').html($('#loader-text').html() + letter);
//             }, 60 * i);
//         });
//
//         $('#initial-loader').velocity({
//             translateZ: 0,
//             opacity: 0
//         }, {
//             display: 'none',
//             delay: 900,
//             duration: 500
//         });
//
//         setTimeout(function () {
//             $('#initialLoader').remove();
//         }, 1401);
//     }
// });


// // JS for interactive keyboard fun...
// const $key = (key) => (
//   document.querySelector(`kbd[data-key='${key}'], kbd[data-alt='${key}']`)
// );
//
// const codeToElement = {
//   'CapsLock': $key('caps'),
//   'Space': $key('space'),
//   'Backslash': document.getElementById('backslash'),
//   'Quote': document.getElementById('quote'),
//   'ShiftLeft': $key('lshift'),
//   'ShiftRight': $key('rshift'),
//   'ControlLeft': $key('lctrl'),
//   'ControlRight': $key('rctrl'),
//   'AltLeft': $key('lalt'),
//   'AltRight': $key('ralt'),
//   'MetaLeft': $key('lwin'),
//   'MetaRight': $key('rwin'),
// }
//
// window.addEventListener('keydown', (e: Event) => {
//   console.log(e);
//   const el = codeToElement[e.code] || $key(e.key.toLowerCase());
//   if (el) {
//     el.classList.add('pressed');
//     e.preventDefault();
//   }
// });
//
// window.addEventListener('keyup', (e: Event) => {
//   const el = codeToElement[e.code] || $key(e.key.toLowerCase());
//   if (el) {
//     el.classList.remove('pressed');
//     e.preventDefault();
//   }
// })

// const banner = document.getElementsByClassName('banner')[0];
// const blocks = document.getElementsByClassName('blocks');
//
//   for (var i = 1; i <400; i++){
//     banner.innerHTML += "<div class='blocks'></div>";
//     blocks[i].style.animationDelay = '$(i * 0.05)s';
//   }

// 댓글 기능(댓글 등록, 수정, 삭제, 대댓글)
function initComment() {
    var commentEmpty = $('div[ux-name="commentEmpty"]');
    var comment = $this.findName('comment');
    var userinfo;
    $ux.data.query({
        id: 'BMP_IDEA_VIEW.GET.COMMENT',
        version: '00001',
        parameter: {
            IDEAID: IDEAID
        },
        reply: function(e) {
            commentEmpty.html('');
            var data = e.result;
            for (var i = 0; i < data.length; i++) {
                var user = data[i].DEPARTMENT + ' ) ' + data[i].USERNAME;
                var content = data[i].CONTENT;
                var time = data[i].CREATEDTIME;
                var rid = data[i].REPLYID;
                var seq = data[i].SEQ;
                var isme;
                if (data[i].USERID == $ux.user.id()) {
                    isme = 'Y';
                } else {
                    isme = 'N';
                }
                if (data[i].SEQ == 0) {
                    commentEmpty.append(makeCommentTable(user, content, time, rid, isme));
                } else {
                    commentEmpty.append(makeReReplytable(user, rid, content, time, isme, seq));
                }

            }
            //totalCommentLabel.tool().setValue('전체 댓글 ' + $('div[ux-name="commentEmpty"] table').length + ' 건');
            if (replyCount())
                totalCommentLabel.tool().setValue('ㅤㅤ전체 댓글 ' + replyCount() + ' 건');
            else
                totalCommentLabel.tool().setValue('ㅤㅤ전체 댓글 0 건');
            /*댓글 기능*/
            $('button[btnType="reply"]').click(function(e) {
                var parentTable = this.parentElement.parentElement.parentElement.parentElement;
                var rid = parentTable.id.split('replyIdNo')[1];
                $(parentTable).after(makeReReply(user, rid));
                var length = $('div[ux-name="commentEmpty"] table').length;
                var top = 60 * length + 855;
                var orignTop = replyEmpty.tool().setTopPositionValue(top + 'px');
                //대댓글달기 취소
                $('button[btnType="reCancle"]').click(function(er) {
                    this.parentElement.parentElement.parentElement.parentElement.remove();
                    var length = $('div[ux-name="commentEmpty"] table').length;
                    var top = 60 * length + 855;
                    var orignTop = replyEmpty.tool().setTopPositionValue(top + 'px');
                });
                //대댓글 등록하기
                $('button[btnType="reCommit"]').click(function(er) {

                    var rid = this.parentElement.parentElement.parentElement.parentElement.id.split('replyIdNo')[1];
                    var content = $('#commentCommit')[0].value;
                    $ux.cjMessage.confirm('댓글을 등록하시겠습니까?', null, function() {
                        $ux.request({
                            name: 'BmpIdeaSaveReComment',
                            value: {
                                REPLYID: rid,
                                CONTENT: content,
                                IDEAID: IDEAID
                            },
                            reply: function(e) {
                                initComment();

                            }
                        });
                    });
                });
            });
            //댓글 수정하기
            $('button[btnType="edit"]').click(function(err) {
                var ta = this.parentElement.parentElement.querySelector('textarea');
                var editBtn = this.parentElement.parentElement.querySelector('button[btnType="edit"]');
                var cancleBtn = this.parentElement.parentElement.querySelector('button[btnType="reply"]');
                var editBtnHidden = this.parentElement.parentElement.querySelector('button[btnType="editHidden"]');
                var cancleBtnHidden = this.parentElement.parentElement.querySelector('button[btnType="replyHidden"]');
                var delBtn = this.parentElement.parentElement.querySelector('button[btnType="del"]');
                $(ta).addClass('bmp-idea-view-rere-textarea');
                $(ta).removeClass('bmp-idea-view-common-textarea');
                ta.readOnly = false;

                $(delBtn.parentElement).hide();
                $(editBtn.parentElement).hide();
                $(cancleBtn.parentElement).hide();
                //$(editBtnHidden).show();
                //$(cancleBtnHidden).show();
                $(editBtnHidden.parentElement).css('display', 'table-cell');
                $(cancleBtnHidden.parentElement).css('display', 'table-cell');
                $('button[btnType="replyHidden"]').click(function(errr) {
                    initComment();

                });
                $('button[btnType="editHidden"]').click(function(errr) {
                    var rid = this.parentElement.parentElement.parentElement.parentElement.id.split('replyIdNo')[1];
                    var content = $('#commonTextareaNo' + rid)[0].value;
                    $ux.cjMessage.confirm('수정하시겠습니까?', null, function() {
                        $ux.request({
                            name: 'BmpIdeaEditComment',
                            value: {
                                REPLYID: rid,
                                CONTENT: content,
                                IDEAID: IDEAID
                            },
                            reply: function(e) {
                                initComment();

                            }
                        });
                    });
                });
            });
            //댓글 삭제하기
            $('button[btnType="del"]').click(function(e) {
                var rid = this.parentElement.parentElement.parentElement.parentElement.id.split('replyIdNo')[1];
                var content = this.parentElement.parentElement.querySelector('textarea').value;
                //var seq = this.parentElement.parentElement.querySelector('td#reSeq').innerText;
                $ux.cjMessage.confirm('삭제하시겠습니까?', null, function() {
                    $ux.data.query({
                        id: 'BMP_IDEA_VIEW.REPLY.DELETE',
                        version: '00001',
                        parameter: {
                            IDEAID: IDEAID,
                            REPLYID: rid
                        },
                        reply: function(e) {
                            $ux.messageBox('삭제되었습니다.', '');
                            initComment();

                        }
                    });
                });
            });
            //대댓글 수정하기
            $('button[btnType="rereEdit"]').click(function(e) {
                var ta = this.parentElement.parentElement.querySelector('textarea');
                var editBtn = this.parentElement.parentElement.querySelector('button[btnType="rereEdit"]');
                var delBtn = this.parentElement.parentElement.querySelector('button[btnType="rereDel"]');
                var editBtnHidden = this.parentElement.parentElement.querySelector('button[btnType="rereEditHidden"]');
                var cancleBtnHidden = this.parentElement.parentElement.querySelector('button[btnType="rereCancleHidden"]');

                $(ta).addClass('bmp-idea-view-rere-textarea');
                $(ta).removeClass('bmp-idea-view-common-textarea-re');
                ta.readOnly = false;
                $(editBtn.parentElement).hide();
                $(delBtn.parentElement).hide();
                $(editBtnHidden.parentElement).css('display', 'table-cell');
                $(cancleBtnHidden.parentElement).css('display', 'table-cell');
                //$(editBtnHidden).show();
                //$(cancleBtnHidden).show();

                $('button[btnType="rereCancleHidden"]').click(function(errr) {
                    initComment();
                });
                $('button[btnType="rereEditHidden"]').click(function(err) {

                    var rid = this.parentElement.parentElement.parentElement.parentElement.id.split('replyIdNo')[1];
                    var content = this.parentElement.parentElement.querySelector('textarea').value;
                    var seq = this.parentElement.parentElement.querySelector('td#reSeq').innerText;
                    $ux.cjMessage.confirm('수정하시겠습니까?', null, function() {
                        $ux.request({
                            name: 'BmpIdeaEditReComment',
                            value: {
                                REPLYID: rid,
                                CONTENT: content,
                                SEQ: seq,
                                IDEAID: IDEAID
                            },
                            reply: function(e) {
                                initComment();

                            }
                        });
                    });
                });
            });
            //대댓글 삭제하기
            $('button[btnType="rereDel"]').click(function(e) {

                var rid = this.parentElement.parentElement.parentElement.parentElement.id.split('replyIdNo')[1];
                var content = this.parentElement.parentElement.querySelector('textarea').value;
                var seq = this.parentElement.parentElement.querySelector('td#reSeq').innerText;
                $ux.cjMessage.confirm('삭제하시겠습니까?', null, function() {
                    $ux.request({
                        name: 'BmpIdeaDelReComment',
                        value: {
                            REPLYID: rid,
                            SEQ: seq,
                            IDEAID: IDEAID
                        },
                        reply: function(e) {
                            initComment();

                        }
                    });
                });
            });
            var length = $('div[ux-name="commentEmpty"] table').length;
            var top = 60 * length + 855;
            var orignTop = replyEmpty.tool().setTopPositionValue(top + 'px');
        }
    });
    replyCount();

}

/*댓글 양식*/
function makeCommentTable(user, content, time, rid, isme) {
    var displayModiBtn;
    if (isme == 'Y') {
        displayModiBtn = 'inline-block';
    } else {
        displayModiBtn = 'none';
    }
    var commentTable = '<table id="replyIdNo' + rid + '" style="border:1px solid; height:60px; width:100%;box-shadow: 0 2px 3px 0 rgba(0, 0, 0, 0.05);table-layout:fixed;\
  border: solid 1.5px #d7dae2;\  background-color: #efefef;">\  <tr style="text-align:center;">\
	<td style="width:7%;"><img src="/resource/bmp/Reply_User_Icon.png" width="40px" height="40px" style="margin-top:5px;"/></td>\
    <td style="width:15%; color:#777777;font-family: CJONLYONENEWbodyRegular;font-size: 15px;">' + user + '</td>\
    <td style="width:58%; color:#3a3a3a;text-align:left !important;"><textarea readonly class="bmp-idea-view-common-textarea" id="commonTextareaNo' + rid + '">' + content + '</textarea></td>\
    <td style="width:10%; color:#777777;font-family: CJONLYONENEWbodyRegular;font-size: 15px;">' + time + '</td>\
    <td style="width:5%;"><button class="bmp-idea-comment-button" style="margin-right:8px;display:' + displayModiBtn + '" btnType="edit">수 정</button></td>\
	<td style="width:5%;"><button class="bmp-idea-comment-button" style="margin-right:16px; margin-left:8px;" id="repleBtnNo' + rid + '" btnType="reply">답 글</button></td>\
	<td style="width:5%;"><button class="bmp-idea-comment-button" style="margin-right:16px; margin-left:8px;display:' + displayModiBtn + '" id="repleBtnNo' + rid + '" btnType="del">삭 제</button></td>\
	<td style="width:5%; display:none;"><button class="bmp-idea-comment-button" style="margin-right:8px;" btnType="editHidden">등 록</button></td>\
	<td style="width:5%; display:none;"><button class="bmp-idea-comment-button" style="margin-right:16px; margin-left:8px;" btnType="replyHidden">취 소</button></td>\	<td hidden>' + rid + '</td>\</tr>\</table>';
    return commentTable;
}

/*대댓글 양식*/
function makeReReplytable(user, rid, content, time, isme, seq) {
    var displayModiBtn;
    if (isme == 'Y') {
        displayModiBtn = 'inline-block';
    } else {
        displayModiBtn = 'none';
    }
    var commentTable = '<table id="replyIdNo' + rid + '" style="border:1px solid; height:60px; width:100%;box-shadow: 0 2px 3px 0 rgba(0, 0, 0, 0.05);table-layout:fixed;\
  border: solid 1.5px #d7dae2;\  background-color: #f2f6fe;">\  <tr style="text-align:center;">\
	<td style="width:3%"></td>\
	<td style="width:3%;padding-bottom:15px"><img src="/resource/bmp/Reply_Comment_line.png" width="30" height="30"/></td>\
    <td style="width:3%;"><img src="/resource/bmp/Reply_Comment User_Icon.png" width="40px" height="40px"style="margin-top:5px;"/></td>\
    <td style="width:15%; color:#777777;font-family: CJONLYONENEWbodyRegular;font-size: 15px;">' + user + '</td>\
    <td style="width:50%; color:#3a3a3a;text-align:left !important;"><textarea readonly class="bmp-idea-view-common-textarea-re" id="commonRETextareaNo' + rid + '">' + content + '</textarea></td>\
	<td style="width:20%; color:#777777;font-family: CJONLYONENEWbodyRegular;font-size: 15px;">' + time + '</td>\
    <td style="width:5%;"><button class="bmp-idea-comment-button" style="margin-left:4px;display:' + displayModiBtn + '" btnType="rereEdit">수  정</button></td>\
	<td style="width:5%;"><button class="bmp-idea-comment-button" style="margin-left:4px;display:' + displayModiBtn + '"btnType="rereDel">삭  제</button></td>\
	<td style="width:5%; display:none;"><button class="bmp-idea-comment-button" style="margin-left:4px;" btnType="rereEditHidden">등 록</button></td>\
	<td style="width:5%; display:none; "><button class="bmp-idea-comment-button" style="margin-left:4px;" btnType="rereCancleHidden">취 소</button></td>\
	<td hidden>' + rid + '</td>\
	<td hidden id="reSeq">' + seq + '</td>\
  </tr>\
</table>';
    $($('button[btnType="rereCancleHidden"]').parentElement).hide();
    $($('button[btnType="rereEditHidden"]').parentElement).hide();
    return commentTable;
}

/*대댓글 입력 양식*/
function makeReReply(user, rid) {
    $ux.data.query({
        id: 'BMP_IDEA_VIEW.GET.REPLY.USER.INFO',
        version: '00001',
        parameter: {
            USERID: $ux.user.id()
        },
        async: false,
        reply: function(e) {
            user = e.result[0].DEPARTMENT + ' ) ' + e.result[0].USERNAME;
        }
    })
    var commentTable = '<table id="replyIdNo' + rid + '" style="border:1px solid; height:60px; width:100%;box-shadow: 0 2px 3px 0 rgba(0, 0, 0, 0.05);table-layout:fixed;\
  border: solid 1.5px #d7dae2;\  background-color: #f2f6fe;">\  <tr style="text-align:center;">\
	<td style="width:3%"></td>\
	<td style="width:3%;padding-bottom:15px"><img src="/resource/bmp/Reply_Comment_line.png" width="30" height="30"/></td>\
    <td style="width:3%;"><img src="/resource/bmp/Reply_Comment User_Icon.png" width="40px" height="40px"style="margin-top:5px;"/></td>\
    <td style="width:15%; color:#777777;font-family: CJONLYONENEWbodyRegular;font-size: 15px;">' + user + '</td>\
    <td style="width:56%; color:#3a3a3a;text-align:left !important;"><textarea class="bmp-idea-view-rere-textarea" placeholder="여기에 댓글을 입력해주세요. 권리침해, 욕설 및 특정 대상을 비하하는 내용을 게시할 경우 이용약관 및 관련 법률에 의해 제재될 수 있습니다" id="commentCommit"></textarea></td>\
	<td style="width:20%; color:#777777;font-family: CJONLYONENEWbodyRegular;font-size: 15px;"></td>\
    <td style="width:5%;"><button class="bmp-idea-comment-button" style="margin-right:8px;" btnType="reCommit">등 록</button></td>\
	<td style="width:5%;"><button class="bmp-idea-comment-button" style="margin-right:8px;margin-left:4px;"btnType="reCancle">취 소</button></td>\
	<td hidden>' + rid + '</td>\
  </tr>\
</table>';
    return commentTable;
}


// // 좋아요 버튼 처리
// // 버튼 클릭 > ajax통신 (like url로 전달) > views의 like 메소드에서 리턴하는 값 전달받기 > 성공시 콜백 호출
// $('.like').click(function() {
//     var pk = $(this).attr('name') // 클릭한 요소의 attribute 중 name의 값을 가져온다.
//     console.log(pk)
//     $.ajax({
//         type: "POST", // 데이터를 전송하는 방법을 지정한다.
//         url: "/commu/like", // 통신할 url을 지정한다.
//         data: {'pk': pk, 'csrfmiddlewaretoken': '{{ csrf_token }}'}, // 서버로 데이터를 전송할 때 이 옵션을 사용한다.
//         dataType: "json", // 서버측에서 전송한 데이터를 어떤 형식의 데이터로서 해석할 것인가를 지정한다. 없으면 알아서 판단한다.
//         // 서버측에서 전송한 데이터 views.py like 메소드
//         // context = {'likes_count' : memo.total_likes, 'message' : message}
//         // json.dump(context)를 통해서 json 형식으로 전달된다.
//
//         success: function (response) { // 성공했을 때 호출할 콜백을 지정한다.
//             id = $(this).attr('name')
//             $('#count' + pk).html("count : " + response.likes_count);
//             alert(response.message);
//             alert("좋아요수 :" + response.likes_count);
//         },
//         error: function (request, status, error) {
//             alert("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
//         }
//     });
// })