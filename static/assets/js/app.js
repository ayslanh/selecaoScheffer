/**
 * @author Ayslan Siqueira <ayslan.henryque@gmail.com>
 */

//url app
var appURL = 'http://localhost:8000/';
var csrftoken = '';
var app = {
    init: function () {
        csrftoken = app.getCookie('csrftoken');
        $("#formAddProd").ajaxForm(function (response) {
            console.log(response);
            json = JSON.parse(response);
            $("#formAddProd").trigger("reset");
            $.notify({
                message: json.msg,
                type: 'success'
            });
        });
    },
    getCookie: function (name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    },

    Buscar: function () {

        $.ajax({
            url: appURL + 'buscaEstoque/' + $("#sFaz").val(), 
            type: "GET",
            headers: {
                'X-CSRFToken': csrftoken,
               
            },
            dataType: "json",
            success: function (json) {
               // console.log(json);
                app.bootGridJsonFormat(json,'tabEstoque');
                //$("#tabEstoque").bootgrid(json);
            },
            error: function () {
                console.log('Erro na Busca!');
            }

        });
    },

    bootGridJsonFormat: function (json, table) {
        //var aux = JSON.stringify(json);
        var data = '';
        console.log(json.length);
        if (json.length == 0) {
            $('#tb').html('');
        } else {
            $.each(json, function (i, item) {
                data +='<tr>';  
                data +='<td>'+item.idEstoque+'</td>';
                data +='<td>'+item.fazenda+'</td>';
                data +='<td>'+item.qtde+'</td>';
                data +='<td>'+item.algodaoTipo+'</td>';
                data +='<td>'+item.dtEntrada+'</td>';        
                data +='</tr>';
               });
               //console.log(data);
              $('#tb').append(data);
              $('#' + table).bootgrid();
        }
    },

    addEstoque: function () {
        $("#cardEstoqueFazAdd").html("");
        $("#cardEstoqueFazAdd").append($("#sFaz option:selected").text());
        $("#idFazAdd").val($("#sFaz").val());
        $("#cardAddProd").show("slow");
    },

    hideAddEstoque: function () {
        $("#cardAddProd").hide("hide");
    },

}

