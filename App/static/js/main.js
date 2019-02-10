var timeid = 0;
$(document).ready(function(){

    timeid = setInterval(PrintTime,1000);

})

function PrintTime()
{
    var sNow = new Date();

    var nHour = sNow.getHours();
    var nMin = sNow.getMinutes();
    var nSec = sNow.getSeconds();

    // 普通写法
    document.getElementById("now").innerHTML = "现在时间:"+ nHour +"时" + nMin +"分" + nSec + "秒";
    // JQuery写法
    // $("#now").innerHTML = "现在时间:"+ nHour +"时" + nMin +"分" + nSec + "秒";
}


console.log("id")
console.log("id" + timeid);

$("#Test1").click(function(){
    clearInterval(timeid);
})

$("#Test2").click(function(){
    timeid = setInterval(PrintTime,1000);

    
})






