document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title,addEventButton',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        customButtons: {
            addEventButton: {
                text: 'add event...',
                click: function () {
                    var dateStr = prompt('시작 날짜를 입력하세요');
                    var date = new Date(dateStr + 'T00:00:00'); // will be in local time
                    var modal =document.getElementById('fullcalModal')
                    if (!isNaN(date.valueOf())) {
                        calendar.addEvent({
                            title: 'dynamic event',
                            start: date,
                            end:date,
                            allDay: true
                        });
                        alert('Great. Now, update your database...');
                    } else {
                        alert('Invalid date.');
                    }
                }
            }
        }
    });

    calendar.render();
});

$(document).ready(function () {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        // dateClick:function (info){
        //     alert('Clicked on: ' + info.dateStr);
        // }
        events: [
            {
                id: 1,
                title: 'Project Start',
                start: '2022-03-04',
                end: '2022-03-04'
            },
            {
                id: 2,
                title: 'SA submit',
                start: '2022-03-11',
                end: '2022-03-13'
            },
            {
                id: 3,
                title: 'Presentation',
                start: '2022-03-31',
                end: '2022-04-01'
            },
            {
                id: 4,
                title: 'Camp Finish',
                start: '2022-04-13',
                end: '2022-04-14'
            },
        ]
    });

    calendar.render();
})

