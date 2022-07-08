// Booking form

const form = document.querySelector('.input-group-register');
const day=document.querySelector('#day');
const doctors = document.querySelector('#doctors');

const doctorInput = document.getElementById("hf");


form.addEventListener('submit',(event)=>{
  if (validateForm()){
    event.preventDefault();
   }
  })
function validateForm(){
  var flag = false;
  if(doctors.value=='Select your doctor'){
    setError(doctorInput,"Please select your doctor");
    flag = true;
  }
  else{
    clearerror(doctorInput);
    
  }
  
  
  

    if(day.value.trim()==''){
      setError(day,"Select day");
      flag = true;
    }
    else{
      clearerror(day);
      
    }
   return flag;

  }





function setError(element,errorMessage){
    const parent=element.parentElement;
    parent.classList.add('error');
    const paragraph=parent.querySelector('span');
    paragraph.innerHTML = errorMessage;
}
function clearerror(element){
  const parent=element.parentElement;
  parent.classList.remove('error');
  const paragraph=parent.querySelector('span');
  paragraph.innerHTML = "";
}
// input date validation
var DOB=document.querySelector('#day')
var date=new Date()
var tdate=date.getDate()
var month=date.getMonth()+1

if(tdate<10){
  tdate="0"+tdate
}
if(month<10){
  month="0"+month
}
var year=date.getUTCFullYear()
var curdate=year+"-"+month+"-"+tdate
DOB.min=curdate
