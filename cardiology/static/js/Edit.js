const form_4 = document.querySelector("#form4");
const NameInput = document.getElementById("username");
const PhoneInput = document.getElementById("phone");
const EmailInput = document.getElementById("Email");
const passwordInput = document.getElementById("password");






  form_4.addEventListener('submit',(event)=>{
    if (validateForm_4()){
      event.preventDefault();
     }
    })
  function validateForm_4(){
    var flag = false;

  
      if(NameInput.value.trim()==''){
        setError(NameInput,"Edit here");
        flag = true;
      }
      else{
        clearerror(NameInput);
        
      }
      if(PhoneInput.value.trim()==''){
        setError(PhoneInput,"Edit here");
        flag = true;
      }
      else{
        clearerror(PhoneInput);
        
      }
      if(EmailInput.value.trim()==''){
        setError(EmailInput,"Edit here");
        flag = true;
      }
      else{
        clearerror(EmailInput);
        
      }
      if(passwordInput.value.trim()==''){
        setError(passwordInput,"Edit here");
        flag = true;
      }
      else{
        clearerror(passwordInput);
        
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
    paragraph.innerHTML = "  ";
  }
