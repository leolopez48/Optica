$(document).ready(function() {
	let subtitulo = '';
	
	let datos1 = [
	8,8,8,7,7,7,6,9,9,11,9,9,6,7,6,7
	,6,6,13,12,9,9,7,6,6,6,5,8,9,7,6
	,9,6,5,5,4,6,5,8,4,4,5,4,7,8,8,7
	,6,10,11,12,8,14,10,11,7,11,16,20
	,17,13,13,13];
	let datos2 = [
	8,8,8,7,7,7,6,9,10,12,9,9,7,7,6,8
	,7,6,13,12,9,9,7,7,7,6,6,10,9,7,7
	,9,6,5,5,4,6,5,8,4,4,5,4,7,8,8,7
	,6,11,12,11,8,14,10,11,7,11,16,20
	,17,13,13,13
	];
	let datos3 = [
	26.9,26.7,26.8,31.7,31.8,29.6,32.3
	,29.6,29.6,25,25,26,26,26,26,26,26
	,26,26,25,26,26,26,26,26,26,26,26,
	26,26,26,26,26,26,26,27,27,27,28,28
	,28,28,28,28,28,28,28,28,27,27,27,24
	,24,24,24,25,26,26,26,25,24,24,24
	];
	let categorias = ["17:26 - 20/06/2019","17:37 - 20/06/2019","17:39 - 20/06/2019","17:45 - 20/06/2019","17:55 - 20/06/2019","18:06 - 20/06/2019","18:16 - 20/06/2019","13:20 - 21/06/2019","13:31 - 21/06/2019","13:41 - 21/06/2019","13:41 - 21/06/2019","13:52 - 21/06/2019","14:02 - 21/06/2019","14:06 - 02/07/2019","14:17 - 02/07/2019","14:27 - 02/07/2019","14:44 - 02/07/2019","14:51 - 02/07/2019","14:55 - 02/07/2019","17:18 - 22/08/2019","17:23 - 22/08/2019","11:11 - 11/09/2019","11:23 - 11/09/2019","11:33 - 11/09/2019","11:44 - 11/09/2019","11:54 - 11/09/2019","12:05 - 11/09/2019","12:15 - 11/09/2019","12:26 - 11/09/2019","12:30 - 11/09/2019","12:41 - 11/09/2019","12:52 - 11/09/2019","13:02 - 11/09/2019","13:11 - 11/09/2019","13:22 - 11/09/2019","13:33 - 11/09/2019","13:43 - 11/09/2019","13:54 - 11/09/2019","14:13 - 11/09/2019","14:14 - 11/09/2019","14:22 - 11/09/2019","14:30 - 11/09/2019","14:38 - 11/09/2019","14:48 - 11/09/2019","15:04 - 11/09/2019","15:15 - 11/09/2019","15:25 - 11/09/2019","15:36 - 11/09/2019","15:39 - 11/09/2019","15:52 - 11/09/2019","16:03 - 11/09/2019","16:10 - 12/09/2019","9:39 - 23/09/2019","9:59 - 23/09/2019","10:03 - 23/09/2019","10:39 - 23/09/2019","10:52 - 23/09/2019","11:13 - 23/09/2019","11:33 - 23/09/2019","11:53 - 23/09/2019","12:13 - 23/09/2019","12:33 - 23/09/2019","12:54 - 23/09/2019","12:57 - 23/09/2019"]; 

	graficar("grafico1","PM 2.5 ug/m3",subtitulo,"PM 2.5 ug/m3","ESTACION 1",datos1,categorias,'#33D3E9');
	graficar("grafico2","PM 10 ug/m3",subtitulo,"PM 10 ug/m3","ESTACION 1",datos2,categorias,'#3647EC');
	graficar("grafico3","TEMPERATURA ºC",subtitulo,"Temp ºC","ESTACION 1",datos3,categorias,'#5D36EC');
});
let graficar=(id,titulo,subtitulo,titulo_eje_y,nombre,datos,categorias,colorGraf)=>{
	Highcharts.chart(id, {
	    chart: {
	        type: 'area',
	        borderWidth:1,
	    },
	    title: {
	        text: titulo
	    },
	    subtitle: {
	        text: subtitulo
	    },
	    xAxis: {
	        allowDecimals: false,
	        labels: {
	            formatter: function () {
	                return this.value; // clean, unformatted number for year
	            }
	        },
	        // INFO DE LA DATA A MOSTRAR (EN QUE SE MIDE)
	        categories: categorias
	    },
	    yAxis: {
	    	// CAMBIAR EL TEXTO TITULO DEL EJE Y
	        title: {
	            text: titulo_eje_y
	        },
	        plotLines: [{
		        color: 'red',
		        value: calcuPromedio(datos), //Insert your average here
		        width: '1',
		        zIndex: 999
		    }]
	    },
	    credits: {
	        enabled: false
	    },
	    tooltip: {
	        pointFormat: '<b>{series.name}</b> <br/>'+titulo_eje_y+': <b>{point.y:,.0f}</b><br/> registro: <b>#{point.x}</b>'
	    },
	    // plotOptions: {
	    //     area: {
	    //         marker: {
	    //             enabled: false,
	    //             symbol: 'circle',
	    //             radius: 2,
	    //             states: {
	    //                 hover: {
	    //                     enabled: true
	    //                 }
	    //             }
	    //         }
	    //     }
	    // },
	    // LA DATA A MOSTRAR
	    series: [{
	        name: nombre,
	        data: datos,
	        // color: colorGraf
	    }]
	});
}
let calcuPromedio=(vector)=>{
	let suma = 0;
	let total = vector.length;
	for(let i=0;i<total;i++){
		suma += parseFloat(vector[i]);
	}
	return suma/total;
}