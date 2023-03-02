$(document).ready(function(){
    setInterval(function(){
        $.ajax({
            url: '{% url "get_last_results" %}',
            success: function(data) {
                // Atualiza o conteudo do template com os novos dados
                var html = '';
                for (var i = 0; i < data.lenght; i++) {
                    html += '<div id="box" class="move square" style="background: ' + data[i].background + ';">';
                    if (data[i].number == 0) {
                        html += '<div class="icon-1"></div>';
                    } else {
                        html += '<div class="icon-1">' + data[i].number + '</div>';
                    }
                    html += '</div>';
                }
                $('.moves').html(html);
            }
        });
    }, 7000); // Solicita a cada 7 segundos
});