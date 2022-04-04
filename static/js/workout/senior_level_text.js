var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var player;

function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        videoId: 'D7KExoUhSA0'
    });
}

var tag2 = document.createElement('script1');

tag2.src = "https://www.youtube.com/iframe_api";
var secondScriptTag = document.getElementsByTagName('script1')[0];
secondScriptTag.parentNode.insertBefore(tag2, secondScriptTag);

var player2;

function onYouTubeIfram() {
    player2 = new YT.Player('player2', {videoId: 'cNudQAODyyM'});
}