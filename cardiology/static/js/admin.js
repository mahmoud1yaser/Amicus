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






const switchMode = document.getElementById('switch-mode');

switchMode.addEventListener('change', function () {
	if(this.checked) {
		document.body.classList.add('dark');
	} else {
		document.body.classList.remove('dark');
	}
})

const counters = document.querySelectorAll('.counter');
const speed = 100; // The lower the slower

counters.forEach(counter => {
	const updateCount = () => {
		const target = +counter.getAttribute('data-target');
		const count = +counter.innerText;

		// Lower inc to slow and higher to slow
		const inc =Math.round(target / speed) ;


		// console.log(inc);
		// console.log(count);

		// Check if target is reached
		if (count < target) {
			// Add inc to count and output in counter
			counter.innerText = count + inc;
			// Call function every ms
			setTimeout(updateCount, 1);
		} else {
			counter.innerText = target;
		}
	};

	updateCount();
});
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


var editformd = document.getElementById("edit");
function editform(){
	editformd.style.width="100%";
	editformd.style.height="100vh";
}

function closeform(){
	editformd.style.width="0";
	editformd.style.height="0";
}


var nums = document.getElementsByClassName("patientsN");
var tot = document.querySelector("#paN").getAttribute('data-target');
var r = document.querySelector(':root');
console.log(nums)
for(var i=0; i<4; i++){
	r.style.setProperty(`--spans${i+1}`, `${Math.ceil(((nums[i].innerHTML)/tot)*100)}%`);
	r.style.setProperty(`--span${i+1}`, `'${Math.ceil(((nums[i].innerHTML)/tot)*100)}%'`);

}

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
