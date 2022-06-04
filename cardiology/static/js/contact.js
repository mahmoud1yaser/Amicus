const form_2 = document.querySelector("#contact");
const doctor = document.querySelector('#doctors');
const Input = document.getElementById("hf");
const messageInput = document.getElementById("Message");


form_2.addEventListener('submit',(event)=>{
  if (validateForm_2()){
    event.preventDefault();
   }
  })
function validateForm_2(){
  var flag = false;
 
  if(doctor.value=='Select doctor'){
    setError(Input,"Please select your doctor");
    flag = true;
  }
  else{
    clearerror(Input);
    
  }
  
  
  

    if(messageInput.value.trim()==''){
      setError(messageInput,"write your message ,please");
      flag = true;
    }
    else{
      clearerror(messageInput);
      
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
