var fondo = document.getElementById("fondo")
var tope = document.getElementById("tope")

tope.style.opacity = 0
var control = 1

setInterval(()=>{
    if(control==1){
        contarArriba().next().value
    }
    if(control==0){
        contarAbajo().next().value
    }
    console.log(tope.style.opacity);
    
},350)



function* contarArriba(){     
    if(tope.style.opacity == 0.9){
        control = 0
    }
    yield tope.style.opacity = 0.9
}

function* contarAbajo(){ 
    if(tope.style.opacity == 0.1){
        control = 1
    }
    yield tope.style.opacity -= 0.1
}
