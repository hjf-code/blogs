window.onload = function () {
    var labels = document.getElementsByTagName("label");
    for (var i = 0; i < labels.length; i++) {
//        var r = Math.floor(Math.random() * 255);
//        var g = Math.floor(Math.random() * 255);
//        var b = Math.floor(Math.random() * 255);
	var r = 100;
	var g = 200;
	var b = 100;
        var color = 'rgba(' + r + ',' + g + ',' + b + ',0.8)';
        labels[i].style.cssText = "background-color:" + color;
    }

    document.onkeydown=function(e){  //对整个页面文档监听 
        var keyNum=window.event ? e.keyCode :e.which;  //获取被按下的键值
        if(keyNum==13){ 
            var button = document.getElementById('searchButton');
	    if (button) {
	       button.click();
	    }
        }
    }	
};

var speed = 0;

function returnTop() {
    speed -= 18;
    window.scrollBy(0, speed);
    if (document.documentElement.scrollTop > 0) {
        setTimeout('returnTop()', 50);
    } else {
        speed = 0;
    }
}

function returnBack() {
    window.history.back();
}

function goHome() {
    window.location.href = "/";
}
