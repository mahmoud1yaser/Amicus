//Select time form

const form_1 = document.querySelector('.input-group');
const Time = document.querySelector('#Time');
const TimeInput = document.getElementById("df");


form_1.addEventListener('submit',(event)=>{
  if (validateForm_1()){
    event.preventDefault();
   }
  })
function validateForm_1(){
  var flag = false;
  
    if(Time.value=='Select Time'){
      setError(TimeInput,"Please select Time");
    flag = true;
    }
    else{
    clearerror(TimeInput);
    
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