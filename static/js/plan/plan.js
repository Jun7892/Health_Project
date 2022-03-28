var currentTitle = document.getElementById('yearMonth');
var calendarBody = document.getElementById('calendar-body');
var today = new Date();
var first = new Date(today.getFullYear(), today.getMonth(), 1);
var dayList = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
var monthList = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'];
var leapYear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
var notLeapYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
var pageFirst = first;
var pageYear;
var mainTodayDay = document.getElementById('main-day');
var mainTodayDate = document.getElementById('main-date');
if (first.getFullYear() % 4 === 0) {
    pageYear = leapYear;
} else {
    pageYear = notLeapYear;
}

function showCalendar() {
    let monthCnt = 100;
    let cnt = 1;
    for (var i = 0; i < 6; i++) {
        var $tr = document.createElement('tr');
        $tr.setAttribute('id', monthCnt);
        for (var j = 0; j < 7; j++) {
            if ((i === 0 && j < first.getDay()) || cnt > pageYear[first.getMonth()]) {
                var $td = document.createElement('td');
                $tr.appendChild($td);
            } else {
                var $td = document.createElement('td');
                $td.textContent = cnt;
                $td.setAttribute('id', cnt);
                $tr.appendChild($td);
                cnt++;
            }
        }
        monthCnt++;
        calendarBody.appendChild($tr);
    }
}

showCalendar();

function removeCalendar() {
    let catchTr = 100;
    for (var i = 100; i < 106; i++) {
        var $tr = document.getElementById(catchTr);
        $tr.remove();
        catchTr++;
    }
}

function prev() {
    inputBox.value = "";
    const $divs = document.querySelectorAll('#input-list > div');
    $divs.forEach(function (e) {
        e.remove();
    });
    const $btns = document.querySelectorAll('#input-list > button');
    $btns.forEach(function (e1) {
        e1.remove();
    });
    if (pageFirst.getMonth() === 1) {
        pageFirst = new Date(first.getFullYear() - 1, 12, 1);
        first = pageFirst;
        if (first.getFullYear() % 4 === 0) {
            pageYear = leapYear;
        } else {
            pageYear = notLeapYear;
        }
    } else {
        pageFirst = new Date(first.getFullYear(), first.getMonth() - 1, 1);
        first = pageFirst;
    }
    today = new Date(today.getFullYear(), today.getMonth() - 1, today.getDate());
    currentTitle.innerHTML = first.getFullYear() + '년' + '&nbsp;&nbsp;&nbsp;&nbsp;' + monthList[first.getMonth()];
    removeCalendar();
    showCalendar();
    showMain();
    clickedDate1 = document.getElementById(today.getDate());
    clickedDate1.classList.add('active');
    clickStart();
    reshowingList();
}

function next() {
    inputBox.value = "";
    const $divs = document.querySelectorAll('#input-list > div');
    $divs.forEach(function (e) {
        e.remove();
    });
    const $btns = document.querySelectorAll('#input-list > button');
    $btns.forEach(function (e1) {
        e1.remove();
    });
    if (pageFirst.getMonth() === 12) {
        pageFirst = new Date(first.getFullYear() + 1, 1, 1);
        first = pageFirst;
        if (first.getFullYear() % 4 === 0) {
            pageYear = leapYear;
        } else {
            pageYear = notLeapYear;
        }
    } else {
        pageFirst = new Date(first.getFullYear(), first.getMonth() + 1, 1);
        first = pageFirst;
    }
    today = new Date(today.getFullYear(), today.getMonth() + 1, today.getDate());
    currentTitle.innerHTML = first.getFullYear() + '년' + '&nbsp;&nbsp;&nbsp;&nbsp;' + monthList[first.getMonth()];
    removeCalendar();
    showCalendar();
    showMain();
    clickedDate1 = document.getElementById(today.getDate());
    clickedDate1.classList.add('active');
    clickStart();
    reshowingList();
}

currentTitle.innerHTML = first.getFullYear() + '년' + '&nbsp;&nbsp;&nbsp;&nbsp;' + monthList[first.getMonth()];

function showMain() {
    mainTodayDay.innerHTML = dayList[today.getDay()];
    mainTodayDate.innerHTML = today.getDate();
}

showMain();

var clickedDate1 = document.getElementById(today.getDate());
clickedDate1.classList.add('active');
var prevBtn = document.getElementById('prev');
var nextBtn = document.getElementById('next');
prevBtn.addEventListener('click', prev);
nextBtn.addEventListener('click', next);
var tdGroup = [];

function clickStart() {
    for (let i = 1; i <= pageYear[first.getMonth()]; i++) {
        tdGroup[i] = document.getElementById(i);
        tdGroup[i].addEventListener('click', changeToday);
    }
}

function changeToday(e) {
    for (let i = 1; i <= pageYear[first.getMonth()]; i++) {
        if (tdGroup[i].classList.contains('active')) {
            tdGroup[i].classList.remove('active');
        }
    }
    clickedDate1 = e.currentTarget;
    clickedDate1.classList.add('active');
    today = new Date(today.getFullYear(), today.getMonth(), clickedDate1.id);
    showMain();
    keyValue = today.getFullYear() + '' + today.getMonth() + '' + today.getDate();
    reshowingList();
}

clickStart();

function reshowingList() {
    keyValue = today.getFullYear() + '' + today.getMonth() + '' + today.getDate();
    if (todoList[keyValue] === undefined) {
        inputList.textContent = '';
        todoList[keyValue] = [];
        const $divs = document.querySelectorAll('#input-list > div');
        $divs.forEach(function (e) {
            e.remove();
        });
        const Cdivs = document.querySelectorAll('#input-list > div');
        Cdivs.forEach(function (e2) {
            e2.remove();
        });
        const $btns = document.querySelectorAll('#input-list > button');
        $btns.forEach(function (e1) {
            e1.remove();
        });
    } else if (todoList[keyValue].length === 0) {
        inputList.textContent = "";
        const $divs = document.querySelectorAll('#input-list > div');
        $divs.forEach(function (e) {
            e.remove();
        });
        const Cdivs = document.querySelectorAll('#input-list > div');
        Cdivs.forEach(function (e2) {
            e2.remove();
        });
        const $btns = document.querySelectorAll('#input-list > button');
        $btns.forEach(function (e1) {
            e1.remove();
        });
    } else {
        const $divs = document.querySelectorAll('#input-list > div');
        $divs.forEach(function (e) {
            e.remove();
        });
        const Cdivs = document.querySelectorAll('#input-list > div');
        Cdivs.forEach(function (e2) {
            e2.remove();
        });
        const $btns = document.querySelectorAll('#input-list > button');
        $btns.forEach(function (e1) {
            e1.remove();
        });
        var $div = document.createElement('div');
        for (var i = 0; i < todoList[keyValue].length; i++) {
            var $div = document.createElement('div');
            var Cdiv = document.createElement('div')
            Cdiv.textContent = todoList[keyValue][i];
            $div.setAttribute('class', 'noCheck');
            Cdiv.setAttribute('class', 'workoutList');
            var $btn = document.createElement('button');
            $btn.setAttribute('type', 'button');
            $btn.setAttribute('id', 'del-ata');
            $btn.setAttribute('id', dataCnt + keyValue);
            $btn.setAttribute('class', 'del-data');
            $btn.setAttribute('class', 'del-data');
            $btn.textContent = delText;
            inputList.appendChild($div);
            $div.appendChild(Cdiv);
            $div.appendChild($btn);
            $div.addEventListener('click', checkList);
            $btn.addEventListener('click', deleteTodo);
            inputBox.value = '';

            function deleteTodo() {
                $div.remove();
                Cdiv.remove();
                $btn.remove();
            }
        }
    }

}

var inputBox = document.getElementById('input-box');
var inputDate = document.getElementById('input-data');
var inputList = document.getElementById('input-list');
var delText = 'X';
inputDate.addEventListener('click', addTodoList);
var dataCnt = 1;
var keyValue = today.getFullYear() + '' + today.getMonth() + '' + today.getDate();
let todoList = [];
todoList[keyValue] = [];

function addTodoList() {
    var $div = document.createElement('div');
    var Cdiv = document.createElement('div');
    Cdiv.textContent = inputBox.value;
    $div.setAttribute('class', 'noCheck');
    Cdiv.setAttribute('class', 'workoutList');
    var $btn = document.createElement('button');
    $btn.setAttribute('type', 'button');
    $btn.setAttribute('id', 'del-ata');
    $btn.setAttribute('id', dataCnt + keyValue);
    $btn.setAttribute('class', "del-data");
    $btn.textContent = delText;
    inputList.appendChild($div);
    $div.appendChild(Cdiv);
    $div.appendChild($btn);
    todoList[keyValue].push(inputBox.value);
    dataCnt++;
    inputBox.value = '';
    $div.addEventListener('click', checkList);
    $btn.addEventListener('click', deleteTodo);

    function deleteTodo() {
        $div.remove();
        Cdiv.remove();
        $btn.remove();
    }
}

console.log(keyValue);

function checkList(e) {
    e.currentTarget.classList.add('checked');
}

//// 식단 토글 /////

const items = document.querySelectorAll('.meal');
function openToggle(){
    const mealList = this.id.replace('meal','list');

    if(document.getElementById(mealList).style.display ==='block'){
        document.getElementById(mealList).style.display = 'none';
        document.getElementById(this.id + '-toggle').textContent = '+';
    } else {
      document.getElementById(mealList).style.display = 'block';
      document.getElementById(this.id + '-toggle').textContent = '-';
    }
}

items.forEach(item => item.addEventListener('click', openToggle));

