/*1. Crea una función que devuelva el número PI con dos decimales. Utiliza la variable PI
que ya existe en JavaScript*/ 
var valorpi = Math.PI

function mostrarpi(){
    alert("el valor de pi con dos decimales es de " + (valorpi).toFixed(2))
 }

/*2. Crea una función que reciba 2 parámetros, precio e IVA, y devuelva el precio con IVA
incluido. Si no recibe el IVA, aplicará el 19 por ciento por defecto.*/

 var preciot=0
 var tarifad=0

function validar_iva (){
    var precio= prompt("digite el precio del producto sin iva");
    var tarifa= prompt("digite la tarifa de iva que desea aplicarle al producto")

    if (tarifa != null && tarifa != ''){
        tarifad=tarifa/100
        preciot=precio*tarifad
        document.write(preciot)
        }

    if(tarifa==null || tarifa==''){
        preciot=precio*0.19
        document.write(preciot)
        }
        return(preciot)
}
/*3. Crea una función que reciba un texto y lo devuelva al revés */

function texto(){
    var texto= prompt("digita un texto y lo devolvere al reves ")
    textoAlReves=texto.split('').reverse().join('')
    document.write(textoAlReves)
}
/*4. Crea una función que genere número entero aleatorio entre min y máx., que serán
pasados como parámetros. Por defecto min = 1 y máx. = 100 */

function aleatorio(min = 1, max = 100) {
    const number = min+ Math.floor(Math.random() *max );
    document.write("el numero aleatorio entre 1 y 100 es de "+number)
}

/* 5. Crea una función que genere 100 números aleatorios entre 1 y 1000 que no se repitan
y luego mostrarlos por pantalla*/
function aleatorio2(min=1, max=1000,){
    var lista = [];
    var i = 0 ;
    while (i <= 100 ){
        var numero = min+ Math.floor(Math.random() *max ) ;
        if (!(numero in lista)){
            lista.push(numero);
            i += 1;
        }
    document.write(lista);  
    }
}
