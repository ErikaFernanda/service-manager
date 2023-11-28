
window.onload = function () {
    // Função principal para carregar outras funções
    carregarSelects();
    buscarListadeAtendimentos();
};

window.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('btn-list-customer-service-sb').addEventListener('click', function () {
        var divs = document.querySelectorAll('.main-info');
        for (var i = 0; i < divs.length; i++) {
            divs[i].style.display = 'none';
        }
        document.getElementById('main-list-service-history').style.display = "block"

    });
    document.getElementById('btn-list-service-sb').addEventListener('click', function () {

        var divs = document.querySelectorAll('.main-info');
        for (var i = 0; i < divs.length; i++) {
            divs[i].style.display = 'none';
        }
        document.getElementById('main-list-service').style.display = "block"
        buscarListadeServicos()
    });

    document.getElementById('btn-list-client-sb').addEventListener('click', function () {

        var divs = document.querySelectorAll('.main-info');
        for (var i = 0; i < divs.length; i++) {
            divs[i].style.display = 'none';
        }
        document.getElementById('main-list-client').style.display = "block"
        buscarListadeClientes()
    });


});