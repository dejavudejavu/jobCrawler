var arr_dic={'请选择行业':'','互联网/电商':'040','游戏产业':'420','计算机软件':'010','IT服务':'030','电子/芯片/半导体':'050','通信业':'060','计算机/网络设备':'020'}
var arr_field=Object.keys(arr_dic)
var hangye=document.getElementById('field')

var option=document.createElement('option')
option.innerHTML=arr_field[0]
hangye.appendChild(option)


for(var i=1;i<arr_field.length;i++)
{
	var option=document.createElement('option')
	option.innerHTML=arr_field[i]
	hangye.appendChild(option)	
}
