 function visibilidad(id) {
    var e = document.getElementById(id);
	if(e.style.display == 'none'){
         e.style.display = 'block';
	     e.style.zIndex = '5';
        }
     else
     {
        e.style.display = 'none';
     }
 }