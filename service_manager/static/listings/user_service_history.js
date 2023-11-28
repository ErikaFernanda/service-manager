function buscarListadeAtendimentos() {
    fetch('customer_service')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('table-customer-service');

            tableBody.innerHTML = '';

            data.forEach(item => {
                const row = document.createElement('tr');

                const idCell = document.createElement('td');
                idCell.textContent = new Date(item.created_at).toLocaleDateString();
                row.appendChild(idCell);

                const nameCell = document.createElement('td');
                nameCell.textContent = item.client.name;
                row.appendChild(nameCell);

                const actionsCell = document.createElement('td');
                const button = document.createElement('button');
                button.textContent = 'Ver nota'; 
                button.classList.add('action-button'); 

                button.addEventListener('click', function () {
                    console.log('Botão clicado para o ID:', item.id);
                });

                actionsCell.appendChild(button);
                row.appendChild(actionsCell);

                tableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Erro ao buscar os dados da API:', error);
        });
}
function buscarListadeServicos() {
    fetch('service')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('table-service');
            tableBody.innerHTML = '';

            data.forEach(item => {
                const row = document.createElement('tr');

                const title = document.createElement('td');
                title.textContent = item.title
                row.appendChild(title);

                const description = document.createElement('td');
                description.textContent = item.description;
                row.appendChild(description);

                const value = document.createElement('td');
                value.textContent = item.value;
                row.appendChild(value);
                

                tableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Erro ao buscar os dados da API:', error);
        });
}