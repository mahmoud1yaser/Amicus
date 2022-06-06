const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

allSideMenu.forEach(item=> {
	const li = item.parentElement;

	item.addEventListener('click', function () {
		allSideMenu.forEach(i=> {
			i.parentElement.classList.remove('active');
		})
		li.classList.add('active');
	})
});




// TOGGLE SIDEBAR
const menuBar = document.querySelector('#content nav .bx.bx-menu');
const sidebar = document.getElementById('sidebar');

menuBar.addEventListener('click', function () {
	sidebar.classList.toggle('hide');
})







const searchButton = document.querySelector('#content nav form .form-input button');
const searchButtonIcon = document.querySelector('#content nav form .form-input button .bx');
const searchForm = document.querySelector('#content nav form');

searchButton.addEventListener('click', function (e) {
	if(window.innerWidth < 576) {
		e.preventDefault();
		searchForm.classList.toggle('show');
		if(searchForm.classList.contains('show')) {
			searchButtonIcon.classList.replace('bx-search', 'bx-x');
		} else {
			searchButtonIcon.classList.replace('bx-x', 'bx-search');
		}
	}
})





if(window.innerWidth < 768) {
	sidebar.classList.add('hide');
} else if(window.innerWidth > 576) {
	searchButtonIcon.classList.replace('bx-x', 'bx-search');
	searchForm.classList.remove('show');
}


window.addEventListener('resize', function () {
	if(this.innerWidth > 576) {
		searchButtonIcon.classList.replace('bx-x', 'bx-search');
		searchForm.classList.remove('show');
	}
})



const switchMode = document.getElementById('switch-mode');


//dark mode
switchMode.addEventListener("change", function () {
	if (this.checked) {
	  document.body.classList.add("dark");
	  localStorage.setItem("mode", "dark");
	} else {
	  document.body.classList.remove("dark");
	  localStorage.setItem("mode", "light");
	}
  })

  document.body.onload = function () {
	var mode = localStorage.getItem("mode");
	if (mode == "dark") {
		switchMode.checked=true
	  document.body.classList.add("dark");
	} else {
	  document.body.classList.remove("dark");
	  switchMode.checked=false
  
	}
  };
  //end dark mode
var coll = document.getElementsByClassName("collapsible");
var i;
// prescription collaps
for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    }
  });
}
//Edit form function 
var editformd = document.getElementById("edit");
function editform(){
	editformd.style.width="100%";
	editformd.style.height="100vh";
}

function closeform(){
	editformd.style.width="0";
	editformd.style.height="0";
}

//End of Edit form function
//loder function

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
