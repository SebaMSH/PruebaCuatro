function registroSismo() {
    $(document).ready(function() {
        $("#msg").hide();

        $("#buscar").click(function() {
            $("#ultimoSismo").empty();

            $.get("https://chilealerta.com/api/query/?user=demo&select=ultimos_sismos", function(data) {
                $("#ultimoSismo").empty();
                $("#categorias").empty();

                var filter = $("#txtFilter").val();

                $("#msg").hide();

                if (filter <= 0 || filter > 20) {
                    $("#msg").html("El filtro debe estar entre 0 y 20");
                    $("#msg").show();
                } else {
                    $.each(data.ultimos_sismos.slice(0, 1), function(i, items) {
                        fil = "<h3>Ultimo sismo</h3>" +
                            "<br>" +
                            "Fecha: " + items.chilean_time + "<br>" +
                            "Magnitud: " + items.magnitude + "<br>" +
                            "Ubicacion: " + items.reference;



                        $("#ultimoSismo").append(fil);
                    });
                    if (!filter) {

                        $.each(data.ultimos_sismos.slice(1, Object.keys(data.ultimos_sismos).length), function(i, item) {
                            var fila;
                            fila = "<tr>" +
                                "<td>" + (i + 1) + "</td>" +
                                "<td>" + item.chilean_time + "</td>" +
                                "<td>" + item.magnitude + "</td>" +
                                "<td>" + item.reference + "</td>" +

                                "</tr>";

                            $("#categorias").append(fila);
                        });
                    } else {

                        if (filter > 0 && filter <= 20) {
                            $.each(data.ultimos_sismos.slice(0 + 1, filter), function(i, item) {

                                var fila;
                                fila = "<tr>" +
                                    "<td>" + (i + 1) + "</td>" +
                                    "<td>" + item.chilean_time + "</td>" +
                                    "<td>" + item.magnitude + "</td>" +
                                    "<td>" + item.reference + "</td>" +

                                    "</tr>";

                                $("#categorias").append(fila);
                            });
                        }


                    }
                }

            });

        });
    });

}