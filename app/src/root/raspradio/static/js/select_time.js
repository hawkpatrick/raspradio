function button_time_up_down_click(hour, minute) {

  var elHour = document.getElementById("hour");
  var elMin = document.getElementById("minute");
  var hourNow = elHour.value;

  var hourThen = normalize_hour(parseInt(hourNow) + parseInt(hour));
  elHour.value = to_time_str(hourThen);

  var minNow = elMin.value;
  var minThen = normalize_minute(parseInt(minNow) + parseInt(minute));
  elMin.value = to_time_str(minThen);
}



function normalize_minute(input) {
	if (input < 0) {
		return 59;
    }
    if (input > 59) {
		return 0;
    }
	return input;
}

function normalize_hour(input) {
	if (input < 0) {
		return 23;
    }
    if (input > 23) {
		return 0;
    }
	return input;
}


/**
 * E.g. from 1 to "01", from 10 to "10", etc.
 **/
function to_time_str(intValue) {
  var result = "" + intValue;
  if (result.length == 1) {
		result = "0" + result;
  }
  return result;
}
