function nextNum(){
	var value=document.getElementById('min').value;
	if(value>0){
		value=Number(value)-1;	
	}
	document.getElementById('min').value=value;
}
function prevNum(){
	var value=document.getElementById('min').value;
	value=Number(value)+1;
	document.getElementById('min').value=value;
}
function nextNum1(){
	var value=document.getElementById('max').value;
	if(value>0){
		value=Number(value)-1;		
	}
	document.getElementById('max').value=value;
}
function prevNum1(){
	var value=document.getElementById('max').value;
	value=Number(value)+1;
	document.getElementById('max').value=value;
}
