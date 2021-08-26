$(document).ready(function(){

		$('#consultar').click(function(){
		$.ajax({
			type: "GET",
			url: "/consultarT",
			success: function(data) {
				$("#mostrardatos").html(data);
			}
		});
	});
				
	$('#consultarsesion').click(function(){
		var nUsuario = document.getElementById('sesionBuscada').value;
		$.ajax({
			type: "GET",
			url: "/consultarS",
			data:{
				"sesionB":nUsuario
			},
			success: function(data) {
				$("#mostrarsesion").html(data);
			}
		});
	});
				
	$('#estadistica').click(function(){
		var nUsuario = document.getElementById('sesionestadistica').value;
		$.ajax({
			type: "GET",
			url: "/estadistica",
			data:{
				"sesionE":nUsuario
			},
			success: function(data) {
				$("#mostrarestadistica").html(data);
			}
		});
	});

	$('#centroide').click(function(){
		var nUsuario = document.getElementById('sesioncentroide').value;
		var nCentroide = document.getElementById('numcentroide').value;
		
		$.ajax({
			type: "GET",
			url: "/centroides",
			data:{
				'sesionC':nUsuario,
				'Cen': nCentroide
			},
			success: function(data) {
				$("#mostrarcentroide").html(data);
				var url='../static/prueba.png';
				$('#imagen').find("img").attr('src', url+'?'+Math.random());
			}});
	});

	$('#centroide2').click(function(){
		var nUsuario = document.getElementById('sesioncentroide2').value;
		var nCentroide = document.getElementById('numcentroide2').value;
		
		$.ajax({
			type: "GET",
			url: "/centroides2",
			data:{
				'sesionC2':nUsuario,
				'Cen2': nCentroide

			},
			success: function(data) {
				$("#mostrarcentroide2").html(data);
				var url2='';
				var url2='../static/prueba.png';
				$('#imagen2').find("img").attr('src', url2+'?'+Math.random());				
			}});
	});

});