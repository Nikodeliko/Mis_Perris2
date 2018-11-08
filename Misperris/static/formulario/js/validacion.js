function validar(){

	var verificar = true;
	
	/* Expreciones regulares */
	var expRegNombre = /^[a-zA-Z—Ò¡·…ÈÕÌ”Û⁄˙‹¸\s]+$/;
	var expRegEmail = /^[\w-\.]+@([\w-]+\.)[\w-]{2,4}$/;
	var expRegRut = /^[0-9kK]{9,9}$/;
	var expRegContra = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,15}$/;
	/* ------------------ */
	var formulario = document.getElementById("formulario");

	var emailvalido = document.getElementById("email").value;
	var runvalido = document.getElementById("run").value;
	var fec_nacimientovalido = document.getElementById("fec_nacimiento").value;
	var telefonovalido = document.getElementById("telefono").value;
	var nombrevalido = document.getElementById("nombre").value;
	var apellidovalido = document.getElementById("apellido").value;
	var regionvalido = document.getElementById("region").value;
	var ciudadvalido = document.getElementById("ciudad").value;

	
	if(!runvalido.value)
	{
		alert("El campo rut es requerido");
		runvalido.focus();
		verificar = false;
	}
	else
	if(!expRegRut.exec(runvalido.value))
	{
		alert("rut 9 caracteres, solo numeros y solo una letra k");
		runvalido.focus();
		verificar = false;
	}
	else
	if(!nombrevalido.value)
	{
		alert("El campo nombre es requerido");
		nombrevalido.focus();
		verificar = false;

	}
	else
		if(!expRegNombre.exec(nombrevalido.value))
		{
			alert ("El campo nombre solo acepta letras");
			nombrevalido.focus();
			verificar = false;	
		}
	else
	if(!apellidovalido.value)
	{
		alert("El campo apellido es requerido");
		apellidovalido.focus();
		verificar = false;

	}
	else
		if(!expRegNombre.exec(nombrevalido.value))
		{
			alert ("El campo apellido solo acepta letras");
			nombrevalido.focus();
			verificar = false;	
		}
	else
	if(!emailvalido.value)
		{
			alert("El campo email es requerido");
			emailvalido.focus();
			verificar = false;
		}
		else
			if(!expRegEmail.exec(emailvalido.value))
		{
			alert ("El campo email no es valido");
			emailvalido.focus();
			verificar = false;	
		}

	if(verificar){
		alert ("Se ha enviado el formulario")
		document.formulario.submit();
	}
}


function solonumk(e){

	key = (document.all) ? e.KeyCode : e.which;

	var numeros = /[0-9-k]/;

	final_fantasy = String.fromCharCode(key);
	return numeros.test(final_fantasy);
}

function solonum(e){

	key = (document.all) ? e.KeyCode : e.which;

	var numeros = /[0-9]/;

	final_fantasy = String.fromCharCode(key);
	return numeros.test(final_fantasy);
}
/*
window.onload = function ()
{
	var botonenviar;
	botonenviar = document.formulario.btn;
	botonenviar.onclick = validar;
}
*/
