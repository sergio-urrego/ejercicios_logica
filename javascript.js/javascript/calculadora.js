var mostrar = document.getElementById('mostrar')
var pantalla = document.getElementById('pantalla')

function display(num){
    pantalla.value += num
}

function calcular(){
   var c =  pantalla.value;
   var l = c.length;
   var v = c.substring(l-1);
if (v == '%'){
    porc()
}else {
try{
    mostrar.value=pantalla.value;
    pantalla.value=eval(pantalla.value);    
    

}
catch(err){
    alert('valor errado')
}
}
}

function porc(){
    
    try{
        mostrar.value=pantalla.value;
        var valor = pantalla.value ;
        var l = valor.length;
        var m = valor.substring(0,(l-1));
        pantalla.value=eval(m + '/100');    
        
    
    }
    catch(err){
        alert('dato errado')
    }
    }

function limpiar(){
    pantalla.value="";
    mostrar.value="";
}

function borrar1(){
    pantalla.value=pantalla.value.slice(0,-1);
}