var date = new Date();
var day= date.getDate();
var week= date.getDay();
var month= date.getMonth();
var year= date.getYear();

 var wrap = document.getElementById("cal");
var row = document.createElement("tr");
firstDay = new Date(year,month,1);


if (year<=200){
		year += 1900;
}

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December'];
monthsShort= ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun','Jul','Aug','Sept','Oct','Nov', 'Dec'];
daysInMonth = [31,28,31,30,31,31,30,31,30,31];
daysOfWeek = ['Sun','Mon','Tues','Wed','Thurs','Fri','Sat'];

firstDay = new Date(year,month,1);


if (year%4 == 0 && year != 1900) {
		daysInMonth [1]= 29;
}

total = daysInMonth[month];
var todaysDate = day + ' ' +months[month]+ ' ' +year;
beg = date;
beg.setDate(1);

if(beg.getDate() == 2){
		beg= setDate(0);
}

beg = beg.getDate();
function Default() {	
		var def = document.getElementById("DefaultMonth");
		var result = document.createTextNode(months[month]);
		def.appendChild(result);
		document.body.apphendChild(def);
}


var yr = document.getElementbyId("DefaultYear");
var yres= document.createTextNode(year);
yr.appendChild(yres);
document.body.apphendChild(yr);

function dayHeader(){
		for (var i = 0; i< daysOfWeek.length; i++){
				var hed = document.createElement("th");
				hed.setAttribute("class","dayHeader");
				el.createTextNode(daysOfWeek[i]);
				row.appendChild(hed);
		}
		wrapper.appendChild(row);
}

function DayCells() {
		dayOne = firstDay.getDay();
		var iDay = 0;
		var i = 0; 
		var lastDay = new Date(year,months[i],daysInMonth[i]);

		while ( iDay < lastDay) {
				for(i <= months.length; i++) {
						var col = document.createElement("td");
						
						if (dayOne === i || iDay > 0){
								col.setAttribute("class", "dayCell today");
						} else {
								col.setAttribute("class", "dayCell");
						}

						if (iDay < lastDay) {
								iDay++ ; 
						} else {
                                col.createTextNode(iDay);
								break;
						}

						row.appendChild(col);
				} 
				wrap.appendChild(row);
		}
}

DayHeader();
dayCells();

 default = {
		defaultView: Default (),
		aspectRatio: 1.35, 
		header = {
				left: 'title',
				center: ' ',
				right: 'today prev,next',
		}
		weekends: true,

		lazyFetching: true,
		startParam: 'start',
		endParam: 'end',

		titleFormat: {
				month: 'MMMM yyyy',
				week: "MMM d[yyyy]{ '-'[ MMM] d yyyy}",
				day: 'dddd, mmm d, yyyy'
		}
		columnFormat: {
				month: 'ddd',
				week:'ddd M/d',
				day:'dddd M/d',
		},
		timeFormat: {
				' ': 'h:mm'
				' ':'h(:mm)t'
		}}
