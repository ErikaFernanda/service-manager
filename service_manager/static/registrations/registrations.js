


window.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('gerarPDF').addEventListener('click', function () {
        var select_servicos = document.getElementById('servicos')
        var servicos_selecionados = [];
        for (var i = 0; i < select_servicos.options.length; i++) {
            if (select_servicos.options[i].selected) {
                servicos_selecionados.push(select_servicos.options[i].id);
            }
        }

        var select_produtos = document.getElementById('estoque')
        var produtos_selecionados = [];
        for (var i = 0; i < select_produtos.options.length; i++) {
            if (select_produtos.options[i].selected) {
                produtos_selecionados.push(select_produtos.options[i].id);
            }
        }

        var select_client = document.getElementById('cliente').value
        dados_json = {"cliente":select_client, "servicos": servicos_selecionados,"produtos":produtos_selecionados}
        console.log(dados_json)
        fetch('/generate_pdf', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
            },
            body :  JSON.stringify(dados_json)
        })
            .then(response => response.blob())
            .then(blob => {
                const url = URL.createObjectURL(blob);
                const pdfWindow = window.open(url, '_blank');
                if (!pdfWindow) {
                    alert('O bloqueio de pop-ups está ativado. Por favor, desative para visualizar o PDF.');
                }
            });
    });
})

function carregarSelects() {
    fetch('client')
        .then(response => response.json())
        .then(data => {
            const select_client = document.getElementById('cliente');

            select_client.innerHTML = '';

            data.forEach(item => {
                const option = document.createElement('option');
                option.textContent = item.name + " - " + item.email
                select_client.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Erro ao buscar os dados da API:', error);
        });
    fetch('service')
        .then(response => response.json())
        .then(data => {
            const select_service = document.getElementById('servicos');

            select_service.innerHTML = '';

            data.forEach(item => {
                const option = document.createElement('option');
                option.textContent = item.title
                option.id = item.id
                select_service.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Erro ao buscar os dados da API:', error);
        });
    fetch('stock')
        .then(response => response.json())
        .then(data => {
            const select_stock = document.getElementById('estoque');

            select_stock.innerHTML = '';

            data.forEach(item => {
                const option = document.createElement('option');
                option.textContent = item.title
                option.id = item.id
                select_stock.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Erro ao buscar os dados da API:', error);
        });
}

