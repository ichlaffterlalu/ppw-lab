// Calculator
var print = document.getElementById('print');

var go = function(x) {
    if (x === 'ac') {
        print.value = '0';
    } else if (x === 'eval') {
        print.value = evil(print.value).toPrecision(4);
    } else if (x === 'sin') {
        print.value = Math.sin(print.value * Math.PI / 180).toPrecision(4);
    } else if (x === 'tan') {
        print.value = Math.tan(print.value * Math.PI / 180).toPrecision(4);
    } else if (x === 'log') {
        print.value = Math.log10(print.value).toPrecision(4);
    } else {
        if (print.value === '0') {
            print.value = x;
        }
        else {
            print.value += x;
        }
    }
};

function evil(fn) {
    return new Function('return ' + fn)();
};
// END

// THEME APPLIER
var applyTheme = function(theme) {
    var bcgColor;
    var fontColor;

    for (key in theme) {
        if (theme.hasOwnProperty(key)) {
            bcgColor = theme[key].bcgColor;
            fontColor = theme[key].fontColor;
        }
    }

    $("html").css({"background-color":bcgColor});
    $("body").css({"background-color":bcgColor});
    $("footer").css({"color":fontColor});
}
// END

// Default Themes
var themes = [{"id":0,"text":"Red","bcgColor":"#F44336","fontColor":"#FAFAFA"},
{"id":1,"text":"Pink","bcgColor":"#E91E63","fontColor":"#FAFAFA"},
{"id":2,"text":"Purple","bcgColor":"#9C27B0","fontColor":"#FAFAFA"},
{"id":3,"text":"Indigo","bcgColor":"#3F51B5","fontColor":"#FAFAFA"},
{"id":4,"text":"Blue","bcgColor":"#2196F3","fontColor":"#212121"},
{"id":5,"text":"Teal","bcgColor":"#009688","fontColor":"#212121"},
{"id":6,"text":"Lime","bcgColor":"#CDDC39","fontColor":"#212121"},
{"id":7,"text":"Yellow","bcgColor":"#FFEB3B","fontColor":"#212121"},
{"id":8,"text":"Amber","bcgColor":"#FFC107","fontColor":"#212121"},
{"id":9,"text":"Orange","bcgColor":"#FF5722","fontColor":"#212121"},
{"id":10,"text":"Brown","bcgColor":"#795548","fontColor":"#FAFAFA"},
{"id":11,"text":"Black","bcgColor":"#000000","fontColor":"#FFFFFF"}
];

// Jquery when document ready
$(document).ready(function(){
     // theme initialization
    var selectedTheme = {"Black":{"bcgColor":"#000000","fontColor":"#FFFFFF"}};

    // select2 initialization
    $('.my-select').select2({
        'data': themes
    });

    // first time theme save to local storage
    var themeToApply = localStorage.getItem("selectedTheme");
    if (themeToApply === null) {
        localStorage.setItem('selectedTheme', JSON.stringify(selectedTheme));
        applyTheme(selectedTheme);
    }
    else {
        applyTheme(JSON.parse(themeToApply));
    }

    // save list of themes to local storage
    localStorage.setItem('themes', JSON.stringify(themes));
});

// theme apply button handler
$('.apply-button').on('click', function(){  // sesuaikan class button
    // [TODO] ambil value dari elemen select .my-select
    var valueTheme = $('.my-select').val();
    // [TODO] cocokan ID theme yang dipilih dengan daftar theme yang ada
    var a;
    for (a in themes) {
        if (a == valueTheme) {
            // [TODO] aplikasikan perubahan ke seluruh elemen HTML yang perlu diubah warnanya
            var text = themes[a].text;
            var bcgColor = themes[a].bcgColor;
            var fontColor = themes[a].fontColor;
            var selectedTheme = {text:{"bcgColor":bcgColor, "fontColor":fontColor}};
            applyTheme(selectedTheme);
            // [TODO] simpan object theme tadi ke local storage selectedTheme
            localStorage.setItem("selectedTheme",JSON.stringify(selectedTheme));
            break;
        }
    }
});

// chatbox text keypress handler
$(".chat-text").keypress(function(e) {
    // check whether Enter is pressed key
    if (e.which == 13) {
        e.preventDefault();
        var input = $("textarea").val().trim();

        $("textarea").val("");
        if (input !== "") {
            $(".msg-insert").append('<p class="msg-send">'+input+'</p><br/>');
        }
    }
});