function show_or_hide_days() {
	update_selected_days();
	var selectedDaysDiv = document.getElementById('selectedDaysDiv');
	var selectDaysSlider = document.getElementById('selectDaysSlider');
    if (! selectDaysSlider.checked) {
        selectedDaysDiv.style.display = "none";
	} else {
        selectedDaysDiv.style.display = "";
	}
}


function update_selected_days() {
	update_selected_day('divMo', 'checkMo');
	update_selected_day('divDi', 'checkDi');
	update_selected_day('divMi', 'checkMi');
	update_selected_day('divDo', 'checkDo');
	update_selected_day('divFr', 'checkFr');
	update_selected_day('divSa', 'checkSa');
	update_selected_day('divSo', 'checkSo');
}

function update_selected_day(divId, checkboxId) {
    var theDiv = document.getElementById(divId);
	if (document.getElementById(checkboxId).checked) {
		theDiv.setAttribute('class', 'selected_day is_selected_day');
	} else {
		theDiv.setAttribute('class', 'selected_day is_not_selected_day');
	}
}


function set_day_checked(day) {
	var element = document.getElementById('check'+day);
	element.checked = !element.checked;
	update_selected_days()
}

