var arr_province = ["请选择省份"]
var i;
for(var i=0;i<regionInfo.length;i++)
{
	if(!arr_province.includes(regionInfo[i].province))
	{
		arr_province.push(regionInfo[i].province)
		
	}
}
var j=1;
var arr_city = new Array();
arr_city[0]=['请选择城市']
var temp= new Array();
for(i=0;i<regionInfo.length;i++)
 {
 	if(regionInfo[i].province==arr_province[j])
 	{
 		temp.push(regionInfo[i].city)
 	}
	else{
		arr_city.push(temp)
		temp=[]
		temp.push(regionInfo[i].city)
		j++;
	}
 }


var sheng=document.getElementById("province");
var shi=document.getElementById("city");
//1.省级初始化显示
for (var i=0;i<arr_province.length;i++){
    var option=document.createElement("option");
    option.innerHTML=arr_province[i];
    sheng.appendChild(option);
}
//2.城市初始化显示
var option=document.createElement("option");
option.innerHTML=arr_city[0][0];
shi.appendChild(option);

//3.绑定change事件
sheng.onchange=function () {
    console.log(this.selectedIndex);  //获取this选中的索引值
    //获取被选中的索引值
    var index=this.selectedIndex;

    //先清除 shi 里面的 option选项
    shi.innerHTML="";
    for (var i=0;i<arr_city[index].length;i++){
        var option=document.createElement("option");
        option.innerHTML=arr_city[index][i];
        shi.appendChild(option);
    }
}