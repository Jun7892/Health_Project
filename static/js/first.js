var glitchTimeline = function() {
    var timeline = new TimelineMax({
        repeat: -1,
        repeatDelay: 2,
        paused: true,
        onUpdate: function () {
            $turb.setAttribute('baseFrequency', turbVal.val + ' ' + turbValX.val);
        }
    });

    timeline
        .to(turbValX, 0.1, { val: 0.5 })
        .to(turbVal, 0.1, { val: 0.02 });
    timeline
        .set(turbValX, { val: 0.000001 })
        .set(turbVal, { val: 0.000001 });
    timeline
        .to(turbValX, 0.2, { val: 0.4 }, 0.4)
        .to(turbVal, 0.2, { val: 0.002 }, 0.4);
    timeline
        .set(turbValX, { val: 0.000001 })
        .set(turbVal, { val: 0.000001 });

    // console.log("duration is: " + timeline.duration());

    return {
        start: function() {
            timeline.play(0);
        },
        stop: function() {
            timeline.pause();
        }
    };
};

btnGlitch = new glitchTimeline();

$('.btn-glitch')
    .on('mouseenter', function () {
          $(this).addClass('btn-glitch-active');
          btnGlitch.start();
    })
    .on('mouseleave', function () {
        var $this = $(this);
        if ( $this.hasClass('btn-glitch-active') ) {
            $this.removeClass('btn-glitch-active');
            btnGlitch.stop();
        }
    });


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