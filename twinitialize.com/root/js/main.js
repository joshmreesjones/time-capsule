// global application variable to store application state
var TWINITIALIZE_APP = {};

TWINITIALIZE_APP.panelOpen = false;

function togglePanel() {
	var panel = document.getElementById("twinitialize-panel-wrap");
	// var tab = document.getElementById("twinitialize-tab-wrap")
					  // .getElementsByTagName("a")[0];
	var body = document.body;

	if (TWINITIALIZE_APP.panelOpen) {
		// close the panel

		panel.style.height = "0px";
	} else {
		// open the panel

		// height value also present in /css/main.css
		panel.style.height = "200px";
	}

	TWINITIALIZE_APP.panelOpen = !TWINITIALIZE_APP.panelOpen;
}