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







// const searchButton = document.querySelector('#content nav form .form-input button');
// const searchButtonIcon = document.querySelector('#content nav form .form-input button .bx');
// const searchForm = document.querySelector('#content nav form');

// searchButton.addEventListener('click', function (e) {
// 	if(window.innerWidth < 576) {
// 		e.preventDefault();
// 		searchForm.classList.toggle('show');
// 		if(searchForm.classList.contains('show')) {
// 			searchButtonIcon.classList.replace('bx-search', 'bx-x');
// 		} else {
// 			searchButtonIcon.classList.replace('bx-x', 'bx-search');
// 		}
// 	}
// })





// if(window.innerWidth < 768) {
// 	sidebar.classList.add('hide');
// } else if(window.innerWidth > 576) {
// 	searchButtonIcon.classList.replace('bx-x', 'bx-search');
// 	searchForm.classList.remove('show');
// }


// window.addEventListener('resize', function () {
// 	if(this.innerWidth > 576) {
// 		searchButtonIcon.classList.replace('bx-x', 'bx-search');
// 		searchForm.classList.remove('show');
// 	}
// })



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

// am4internal_webpackJsonp(["ab45"],{lhmh:function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=i("aCit"),a=function(t){Object(n.b)(t,"SpriteState")&&(t.transitionDuration=400),Object(n.b)(t,"Component")&&(t.rangeChangeDuration=500,t.interpolationDuration=500,t.sequencedInterpolation=!1,Object(n.b)(t,"SankeyDiagram")&&(t.sequencedInterpolation=!0),Object(n.b)(t,"FunnelSeries")&&(t.sequencedInterpolation=!0)),Object(n.b)(t,"Chart")&&(t.defaultState.transitionDuration=2e3,t.hiddenState.transitionDuration=1e3),Object(n.b)(t,"Tooltip")&&(t.animationDuration=400,t.defaultState.transitionDuration=400,t.hiddenState.transitionDuration=400),Object(n.b)(t,"Scrollbar")&&(t.animationDuration=500),Object(n.b)(t,"Series")&&(t.defaultState.transitionDuration=1e3,t.hiddenState.transitionDuration=700,t.hiddenState.properties.opacity=1,t.showOnInit=!0),Object(n.b)(t,"MapSeries")&&(t.hiddenState.properties.opacity=0),Object(n.b)(t,"PercentSeries")&&(t.hiddenState.properties.opacity=0),Object(n.b)(t,"FunnelSlice")&&(t.defaultState.transitionDuration=800,t.hiddenState.transitionDuration=1e3,t.hiddenState.properties.opacity=1),Object(n.b)(t,"Slice")&&(t.defaultState.transitionDuration=700,t.hiddenState.transitionDuration=1e3,t.hiddenState.properties.opacity=1),Object(n.b)(t,"Preloader")&&(t.hiddenState.transitionDuration=2e3),Object(n.b)(t,"Column")&&(t.defaultState.transitionDuration=700,t.hiddenState.transitionDuration=1e3,t.hiddenState.properties.opacity=1),Object(n.b)(t,"Column3D")&&(t.hiddenState.properties.opacity=0)};window.am4themes_animated=a}},["lhmh"]);

var editformd = document.getElementById("edit");
function editform(){
	editformd.style.width="100%";
	editformd.style.height="100vh";
}

function closeform(){
	editformd.style.width="0";
	editformd.style.height="0";
}