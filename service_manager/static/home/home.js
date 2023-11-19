
window.onload = function() {
    // Função principal para carregar outras funções
    carregarSelects();
    buscarListadeAtendimentos();
};

window.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('btn-create-customer-service').addEventListener('click', function () {

        document.getElementById('title-home').innerHTML = "Cadastro de Atendimento"
        document.getElementById('main-info-list').style.display="block"
        document.getElementById('main-info').style.display="none"
        document.getElementById('btn-create-customer-service').style.display="none"
        document.getElementById('gerarPDF').style.display="block"
    });

    document.getElementById('btn-create-customer-service-sb').addEventListener('click', function () {

        document.getElementById('title-home').innerHTML = "Histórico de atendimento"
        document.getElementById('main-info-list').style.display="none"
        document.getElementById('main-info').style.display="block"
        document.getElementById('btn-create-customer-service').style.display="block"
        document.getElementById('gerarPDF').style.display="none"
    });
});