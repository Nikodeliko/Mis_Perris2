$(document).on("ready", configurarApp);

function configurarApp ()
{
	var canvas = document.getElementbyId("canvasa");
	var ctx = canvas.getContext("2d");
	canvas.width = screen.availWidth();
}