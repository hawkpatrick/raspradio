
function validateNewAlarmForm() {
    var hour = document.forms["newAlarmForm"]["hour"].value;
    var minute = document.forms["newAlarmForm"]["minute"].value;
	var stream = document.forms["newAlarmForm"]["stream"].value;
    var isValid = true;
	var reason = "";
	if (!stream) {
		isValid = false;
		reason = "Stream ist nicht gesetzt!";
	}
    if (isNaN(hour) || isNaN(minute)) {
		isValid = false;
		reason = "Stunde oder Minute ist keine Zahl!";
    }
    if (!(isInt(hour) && isInt(minute))) {
		isValid = false;
		reason = "Stunde oder Minute ist keine Ganzzahl!";
    }
    var hourInt = parseInt(hour);
    if (hourInt > 23 || hourInt < 0) {
		isValid = false;
		reason = "Stunde ist nicht valide!";
    }
    var minuteInt = parseInt(minute);
    if (minuteInt > 59 || minuteInt < 0) {
		isValid = false;
		reason = "Minute ist nicht valide!";
    }
    if (!isValid) {
		alert("Bitte folgende Felder korrigieren: " + reason);
        return false;
    }
    return true;
}

function validateConfigureSettingsForm() {

} 

function onCustomCheckboxClick(checkbox, configSection, configKey) {
	var hiddenField = document.getElementById(configSection+"_"+configKey);
	if (checkbox.checked) {
		hiddenField.value = "Yes"
	} else {
		hiddenField.value = "No"
	}
}

function isInt(value) {
  var x = parseFloat(value);
  if (value.indexOf(".") !== -1) {
    return false;
  }
  if (value.indexOf(",") !== -1) {
    return false;
  }
  return !isNaN(value) && (x | 0) === x;
}

function onRepeatTypeChanged() {
	var x = document.getElementById("selectRepeatType").value;
	if (x == 'custom') {
		document.getElementById("divRepeatSelectDays").style = "";
		document.getElementById("divNewAlarm").style = "display: none;";
	} else {
		document.getElementById("divRepeatSelectDays").style = "display: none;";
		document.getElementById("divNewAlarm").style = "";
	}
}

function onRepeatSelectedDaysConfirmed() {
	document.getElementById("divRepeatSelectDays").style = "display: none;";
	document.getElementById("divNewAlarm").style = "";
}


function onTurnOfCheckBoxClicked(element) {
	if (! element.checked) {
		document.getElementById("duration").style = "display: none;";
    } else {
		document.getElementById("duration").style = "";
	}
}

