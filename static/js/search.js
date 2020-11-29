function setLoading() {
	var key = document.getElementById('words').value
	var city = document.getElementById('city').value
	var province = document.getElementById("province").value
	var min = Number(document.getElementById("min").value)
	var max = Number(document.getElementById("max").value)
	var field = document.getElementById('field').value
	if (key == '') {
		window.alert("请输入职位关键词")
	}
	else if (province == "请选择省份") {
		window.alert('请选择省份')
	}
	else if (field == "请选择行业") {
		window.alert("请选择行业")
	}
	else if (min >= max) {
		window.alert("最小薪资不能大于或等于最大薪资")
	}
	else {
		for (var i = 0; i < regionInfo.length; i++) {
			if (regionInfo[i].city == city) {
				city=regionInfo[i].code
				break
			}
		}
		var get_data = {
			'key':key,
			"city": city,
			'min':min,
			'max':max,
			'field':arr_dic[field]	
		}
		$.ajax({
			url: "/ajaxtest",
			type: "GET",
			dataType: "text",
			async: true,
			data: get_data,
			ContentType: "application/x-www-form-urlencoded;charset=UTF-8",
			success: function (result) {
				window.location.href='http://127.0.0.1:8080/showImage';
			},
			error: function (XMLHttpRequest, textStatus, errorThrown) {
				alert(XMLHttpRequest.status)
				alert(XMLHttpRequest.readyState)
				alert(textStatus)
			}
		});
		


		
	 }

}


