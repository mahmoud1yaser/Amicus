const form_1 = document.querySelector('#contact')
const doctor = document.querySelector('#doctors')
const Input = document.getElementById("hf");
const messageInput = document.getElementById("Message");

form_1.addEventListener('submit',(event)=>{
    event.preventDefault();
         validateForm_1();
})

// form_1.addEventListener('submit',(event)=>{
    
//      if(validateForm_1()){
//       event.preventDefault();
//      }
//    })
   
   function validateForm_1(){
    // var flag = false
    if(doctor.value=='Select your doctor'){
      setError(Input,"please select your doctor");
    //   flag = true;
    }
    else{
      clearerror(Input);
    }
    if(messageInput.value.trim()==''){
        setError(messageInput,"please enter a message");
        flag = true;
        // return flag
      }
      else{
        clearerror(messageInput);
        // return flag
        
      }
  
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
  }