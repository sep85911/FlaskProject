var div001 = document.getElementById("");


var scores = new Array();

scores[5] = 132;

console.log(scores[1]);
console.log(scores[5]);

function myOpen(){
    // var a = window.alert("警告窗口") //警告窗口
    // var b = window.prompt("接受输入窗口") //接受输入窗口
    // var c = window.confirm("确定")  //确定窗口

    console.log("c");

}

// var s = setTimeout(ShowMessage,5000);
// console.log(s + " " + typeof(s));
// setInterval(ShowMessage,1000,3);

function ShowMessage()
{
    console.log("老子牛逼！");
    window.alert("这是alert窗口!");
}

var array = [1,2,3,4,54,5,423,654,243,6,756,8]
var btn001 = document.getElementById("btn001");
btn001.onmouseup = function()
{
    window.alert(array.length);
}







