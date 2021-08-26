$(document).ready(function(){
				
	var intevalId=null;
				
	function iniciarSesion(){
		if($('#sesionUser').val().length >= 1){
			var nUsuario = document.getElementById('sesionUser').value; 
			$.ajax({
				type: "GET",
				url: '/data-update',
				data:{
					"sesionU":nUsuario
				},
				success: function(data) {
					$('#dateChange').text(data.date);
					$('#content').text(data.content);

					actualizar(parseInt(data.date));
					actualizar2(parseInt(data.content));
				}
			});
			return true;
		}else{
			return false;
		}
	}
				
	var dps = [];
	var xVal = 0;
	var yVal = 100; 
	var updateInterval = 1000;
	var dataLength = 20;

	var chart = new CanvasJS.Chart("chartContainer", {
		title :{
			text: "RR"
		},
		axisY: {
			includeZero: false
		},      
		data: [
			{
				type: "line",
				dataPoints: dps
			}
		]
	});
			
	function actualizar(num) {			
		dps.push({
			x: xVal,
			y: num
		});
					
		xVal++;
				
		if (dps.length > dataLength) {
			dps.shift();
		}
		chart.render();
	}
    

	var dps2 = [];
	var xVal2 = 0;
	var yVal2 = 100; 
	var updateInterval2 = 1000;
	var dataLength2 = 20;

	var chart2 = new CanvasJS.Chart("chartContainer2", {
		title :{
			text: "HR"
		},
		axisY: {
			includeZero: false
		},      
		data: [
			{
				type: "line",
				dataPoints: dps2
			}
		]
	});
			
	function actualizar2(num2) {			
		dps2.push({
			x: xVal2,
			y: num2
		});
					
		xVal2++;
				
		if (dps2.length > dataLength2) {
			dps2.shift();
		}
		chart2.render();
	}
			
	$('#iniciar').click(function(){
		if(iniciarSesion()==true){
			intervalId = setInterval(iniciarSesion,2000);	
		}else{
			alert("Digite la sesion:  ");
		}
	});
		
	$('#detener').click(function(){
		clearInterval(intervalId);
	});
});
