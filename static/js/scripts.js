$(document).ready(
	function(){
		$('#addTaskButton').click(function(){
			document.getElementById("addTask").submit();
		});
		$('#addEditedTaskButton').click(function(){
			document.getElementById("addEditedTask").submit();

		});

	});