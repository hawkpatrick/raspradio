
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
    // TODO Implement validation
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

function init_volume_slider() {
    var rangeInput = document.getElementById("volumeSlider");
    if (rangeInput == null) {
        return;
    }
    rangeInput.addEventListener('mouseup', function () {
        var playerForm = document.getElementById("playerForm");
        playerForm.submit();
    });
}

window.onload = function(e) {
    init_volume_slider();
    show_or_hide_days();
}