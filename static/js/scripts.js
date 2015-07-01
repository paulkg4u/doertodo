$(document).ready(
	function(){

		$('#addTaskButton').click(function(){
			document.getElementById("addTask").submit();
		});
		$('#addEditedTaskButton').click(function(){
			document.getElementById("addEditedTask").submit();

		});
		$('#filter').change(function(){
			$('.itemRow:hidden').show();
			var filterValue = $('#filter option:selected').val();
			
			if (filterValue=='today') {
				
				var todayDate = new Date();

				$('.itemRow').each(function(){
					var itemsDate = new Date($(this).attr("data-dueDate"));

					if ((itemsDate.getMonth()!=todayDate.getMonth())||(itemsDate.getDate()!=todayDate.getDate())||(itemsDate.getFullYear()!=todayDate.getFullYear())) {
						$(this).hide();
					};

				});
			}
			else if(filterValue=='tomorrow'){
				var tomorrowDate = new Date();
				tomorrowDate.setDate(tomorrowDate.getDate()+1);
				console.log(tomorrowDate);
				$('.itemRow').each(function(){
					var itemsDate = new Date($(this).attr("data-dueDate"));

					if ((itemsDate.getMonth()!=tomorrowDate.getMonth())||(itemsDate.getDate()!=tomorrowDate.getDate())||(itemsDate.getFullYear()!=tomorrowDate.getFullYear())) {
						$(this).hide();
					};
					
				});
			}
			else if (filterValue=='thisweek') {
				var todayDate = new Date();
				var todaySec = todayDate.getTime();
				
				var diff = 6-todayDate.getDay();
				var nextSat = todayDate.setDate(todayDate.getDate()+diff);
				
				
				$('.itemRow').each(function(){
					var itemsDate = new Date($(this).attr("data-dueDate"));
					var itemsDateSec = itemsDate.getTime();
					
					if ((itemsDateSec>nextSat)||(itemsDateSec<todaySec)) {
						$(this).hide();
					};

				});
			}
			else if (filterValue=='thismonth') {
				
				var todayDate=new Date();

				var thismonth=todayDate.getMonth();
				console.log(thismonth);
				$('.itemRow').each(function(){
					var itemsMonth = new Date($(this).attr("data-dueDate")).getMonth();
					if (thismonth!=itemsMonth) {
						$(this).hide();
					};

					

				});
			}
			else{
				console.log("else");
				$('.itemRow').each(function(){


				});
			}
		});

	});