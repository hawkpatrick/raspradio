function onConfigureCheckboxClick(checkbox, configSection, configKey, dependencies) {
	var hiddenField = document.getElementById(configSection+"_"+configKey);
    if (hiddenField) {
		hiddenField.value = checkbox.checked ? "Yes" : "No"
	}
	if (dependencies) {
		dependencies.disabled = !checkbox.checked;
	}
}
