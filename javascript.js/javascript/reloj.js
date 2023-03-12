alert('para usar el temporizador dale al boton de ejecutar y espera instruciones :)')
var tiempo=document.querySelector('.tiempo')

function digitalclock(){
    let t=new Date ();

    let horas =t.getHours();
    let minutos =t.getMinutes();
    let segundos=t.getSeconds();
    let diasemana =t.getDay();
    var dia=t.getDate();
    var mes=t.getMonth();
    var año=t.getFullYear();



    let jornada= horas>=12 ? 'PM' : 'AM'
    var phoras=document.getElementById('horas')
     var horasf=horas%12
     if (horasf ==0){
        horasf=12
     }
    phoras.textContent=(horasf);
    var pminutos=document.getElementById('minutos')
    if (minutos<10){
        minutos='0'+minutos
    }
    pminutos.textContent=minutos;
    var psegundos=document.getElementById('segundos')
    if (segundos<10){
        segundos='0'+segundos
    }
    psegundos.textContent=segundos;
    var pjornada=document.getElementById('jornada')
    pjornada.textContent=jornada;
    var pdiasemana=document.getElementById('diasemana')
    var semana=['DOMINGO','LUNES','MARTES','MIERCOLES','JUEVES','VIERNES','SABADO']
        pdiasemana.textContent=semana[diasemana]
    var pdia=document.getElementById('dia')
    pdia.textContent=dia
    var pmes=document.getElementById('mes')
    var meses=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio','Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    pmes.textContent=meses[mes]
    var paño=document.getElementById('año')
    paño.textContent=año;

}

setInterval(() => {
    digitalclock()
}, 1000);

/* cronometro*/

const pantalla=document.getElementById('cronometro')
const play=document.getElementById('start')
const stop=document.getElementById('stop')

var interval;
let runningtime=0;

const playpausa = ()=>{
    const ispaused=!play.classList.contains('running')
    if (ispaused){
        play.classList.add('running')
        start()
    }else{
        play.classList.remove('running')
        pausa();
    }
}
const pausa= ()=>{
    play.classList.remove('running')
    clearInterval(interval)
}
const alto=()=>{
    play.classList.remove('running')
    runningtime=0;
    clearInterval(interval)
    pantalla.textContent='00:00:00';
}

const start = ()=>{
    let startime=Date.now() - runningtime
    interval=setInterval( () =>{
        runningtime=Date.now()-startime
        pantalla.textContent=calculartime(runningtime)
    },1000)
}




const calculartime= runningtime =>{
    const total_seg=Math.floor(runningtime/1000);
    const total_min=Math.floor(total_seg/60)
    const total_hors=Math.floor(total_min/60)

    const displayseg=(total_seg % 60).toString().padStart(2,'0');
    const displaymin=(total_min % 60).toString().padStart(2,'0');
    const displayhors=total_hors.toString().padStart(2,'0')

    return `${displayhors}:${displaymin}:${displayseg}`
}

/*temporizador */

const display = document.querySelector('.temp');
const minutesSpan = display.querySelector('.minutes-timer');
const secondsSpan = display.querySelector('.seconds-timer');

let secondsLeft = 0;
let timerId;

function startTimer() {
  timerId = setInterval(() => {
    secondsLeft--;
    if (secondsLeft < 0) {
      clearInterval(timerId);
      alert('el temporizador ah terminado');
    } else {
      updateDisplay();
    }
  }, 1000);
}

function stopTimer() {
  clearInterval(timerId);
}

function resetTimer() {
  clearInterval(timerId);
  secondsLeft = 0;
  updateDisplay();
}

function updateDisplay() {
  const minutes = Math.floor(secondsLeft / 60);
  const seconds = secondsLeft % 60;
  minutesSpan.textContent = minutes < 10 ? '0' + minutes : minutes;
  secondsSpan.textContent = seconds < 10 ? '0' + seconds : seconds;
}

const iniciart = document.querySelector('.iniciar');
const pausart = document.querySelector('.pausar');
const parart = document.querySelector('.parar');
const ejecutar=document.getElementById('ejec')

iniciart.addEventListener('click', () => {
  updateDisplay();
  startTimer();
});

ejecutar.addEventListener('click',()=>{
    secondsLeft = prompt('instrodusca el numero de sagundos de la cuenta regresiva');
    startTimer();
})


pausart.addEventListener('click', stopTimer);

parart.addEventListener('click', resetTimer);


