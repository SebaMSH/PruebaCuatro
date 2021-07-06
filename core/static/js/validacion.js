$(document).ready(function () {

    $("#error").hide();
    $("#btnenviar").click(function(event){
        var mensaje = "";
        var filtro = $("#txtrut").val();
        var digito = true;

        if($("#txtrut").val().trim().length == 0){
            mensaje += "El Rut está en blanco <br/>";
        }
        else{
            if ($("#txtrut").val().trim().length < 7){
                mensaje += "El Rut no cumple con largo indicado <br/>";
            }
            else{
                var param = {
                    rut: filtro
                };
                $.get("https://api.libreapi.cl/rut/validate", param, function (data) { 
                    digito = data.data.valid
                    if (digito != true){
                        mensaje += "Rut Incorrecto <br/>";
                        console.log(mensaje);                        
                    }

                    
                });
                
            }
        }

        if($("#txtnombre").val().trim().length == 0){
            mensaje += "El nombre está en blanco <br/>";
        }

        if($("#txtedad").val().trim().length == 0) {
            mensaje += "La edad esta en blanco <br/>"; 
        }else{
            if($("#txtedad").val() < 18) {
                mensaje += "La edad debe ser mayor a 18 <br/>"; 
            }
            if($("#txtedad").val() > 110) {
                mensaje += "La edad debe ser menor a 110 <br/>"; 
            }
        }

        if ($("#txtmail").val().trim().length == 0 && $("#txtfono").val().trim().length == 0 ) {
            mensaje += "Debe ingresar almenos un campo (telefono o Email) <br/>";
        }

        if ($("#txtcomentario").val().trim().length == 0) {
            mensaje += "Debe ingresar el comentario <br/>";
        }
        
        if ($('#ddlmotivo').val().trim() == '0') {
            mensaje += "Debe seleccionar un motivo <br/>";
    
        } 

        setTimeout(function() {
            if(mensaje != ""){
                $('#error').html(mensaje);
                $('#error').show();
                //event.preventDefault();
            }
    
          }, 2000);
       
    });

  });
