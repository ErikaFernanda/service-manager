


window.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('gerarPDF').addEventListener('click', function () {
        fetch('/generate_pdf')
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
                select_stock.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Erro ao buscar os dados da API:', error);
        });
}

