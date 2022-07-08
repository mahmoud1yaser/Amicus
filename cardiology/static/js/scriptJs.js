document.body.onload = function () {
  var mode = localStorage.getItem("mode");
  if (mode == "dark") {
    switchMode.checked = true;
    document.body.classList.add("dark");
  } else {
    document.body.classList.remove("dark");
    switchMode.checked = false;
  }
  setTimeout(loader,1500);
};
function loader(){
  document.querySelector('.loader').style.display='none';
  
}
var editformd = document.querySelector("#edit");
function editform() {
  editformd.style.width = "100%";
  editformd.style.height = "100vh";
}

function closeform() {
  editformd.style.width = "0";
  editformd.style.height = "0";
}

const allSideMenu = document.querySelectorAll("#sidebar .side-menu.top li a");

allSideMenu.forEach((item) => {
  const li = item.parentElement;

  item.addEventListener("click", function () {
    allSideMenu.forEach((i) => {
      i.parentElement.classList.remove("active");
    });
    li.classList.add("active");
  });
});

// TOGGLE SIDEBAR
const menuBar = document.querySelector("#content nav .bx.bx-menu");
const sidebar = document.getElementById("sidebar");

menuBar.addEventListener("click", function () {
  sidebar.classList.toggle("hide");
});

const searchButton = document.querySelector(
  "#content nav form .form-input button"
);
const searchButtonIcon = document.querySelector(
  "#content nav form .form-input button .bx"
);
const searchForm = document.querySelector("#content nav form");

searchButton.addEventListener("click", function (e) {
  if (window.innerWidth < 576) {
    e.preventDefault();
    searchForm.classList.toggle("show");
    if (searchForm.classList.contains("show")) {
      searchButtonIcon.classList.replace("bx-search", "bx-x");
    } else {
      searchButtonIcon.classList.replace("bx-x", "bx-search");
    }
  }
});

if (window.innerWidth < 768) {
  sidebar.classList.add("hide");
} else if (window.innerWidth > 576) {
  searchButtonIcon.classList.replace("bx-x", "bx-search");
  searchForm.classList.remove("show");
}

window.addEventListener("resize", function () {
  if (this.innerWidth > 576) {
    searchButtonIcon.classList.replace("bx-x", "bx-search");
    searchForm.classList.remove("show");
  }
});

const switchMode = document.getElementById("switch-mode");

switchMode.addEventListener("change", function () {
  if (this.checked) {
    document.body.classList.add("dark");
    localStorage.setItem("mode", "dark");
  } else {
    document.body.classList.remove("dark");
    localStorage.setItem("mode", "light");
  }
});

// prescription collaps
var coll = document.getElementsByClassName("collapsible");
var i;
for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function () {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight) {
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    }
  });
}
//  Validation


const Medicine = document.getElementById("textarea");
const Diagnoses = document.getElementById("textarea_1");
const prescription = document.getElementById("Message");
const form_1 = document.querySelector("#contact_id");
const form_2 =  document.getElementById('contact'); 


// if(form_1 !== null){
// form_1.addEventListener("submit", (event) => {
//   event.preventDefault();
//   validateForm_1();
// });
// }

// if(form_2 !== null){
// form_2.addEventListener("submit", (event) => {
//   event.preventDefault();
//   validateForm_2();
// });
// }





function validateForm_1() {
  // var flag = false
  if (Medicine.value == "") {
    setError(Medicine, "Please Enter The Medicine");
    //   flag = true;
  } else {
    clearerror(Medicine);
  }

  if (Diagnoses.value.trim() == "") {
    setError(Diagnoses, "Please Enter The Diagnoses");
    //     flag = true;
    // return flag
  } else {
    clearerror(Diagnoses);
    // return flag
  }

  if (prescription.value.trim() == "") {
    setError(prescription, "Please Enter The Prescription");
    //     flag = true;
    // return flag
  } else {
    clearerror(prescription);
    // return flag
  }
}
function validateForm_2() {
  // var flag = false
  if (Medicine.value == "") {
    setError(Medicine, "Please Enter The Medical History");
    //   flag = true;
  } else {
    clearerror(Medicine);
  }

  if (Diagnoses.value.trim() == "") {
    setError(Diagnoses, "Please Enter The Restricted Drugs");
    //     flag = true;
    // return flag
  } else {
    clearerror(Diagnoses);
    // return flag
  }

}
// function validateForm_3() {
//   // username
//     if (Eu.value.trim() == "") {
//       setError(Eu, "Please enter a username");
//     } else {
//       clearerror(Eu);
//     }
//     // phone-number
//     if (Ep.value.trim() == "") {
//       setError(Ep, "Please enter your number");
//     } else if (Ep.value.trim().length < 11 || Ep.value.trim().length > 11) {
//       setError(Ep, "Please enter a Valid number");
//     } else {
//       clearerror(Ep);
//     }
//     // Email
//     if (Ee.value.trim() == "") {
//       setError(Ee, "Enter Your Email");
//     } 
//     else if (!ValidateEmail(Ee)) {
//       setError(Ee, "Enter Vaild Email");
//     } 
//     else {
//       clearerror(Ee);
//     } 
//     // password
//     if (Epass.value.trim() == "") {
//       setError(Epass, "Please enter your Password");
//     } else {
//       clearerror(Epass);
//     }
// }
// function setError(element, errorMessage) {
//   const parent = element.parentElement;
//   parent.classList.add("error");
//   const paragraph = parent.querySelector("span");
//   paragraph.innerHTML = errorMessage;
// }
// function clearerror(element) {
//   const parent = element.parentElement;
//   parent.classList.remove("error");
//   const paragraph = parent.querySelector("span");
//   paragraph.innerHTML = '';
// }
// function ValidateEmail(input) {

//   var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

//   if (input.value.match(validRegex)) {
//     return true;

//   } else {
//     return false;
//   }

// }
// ----------------------