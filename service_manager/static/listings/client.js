function buscarListadeClientes() {
    fetch('client')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('table-client');
            tableBody.innerHTML = '';

            data.forEach(item => {
                const row = document.createElement('tr');

                const name = document.createElement('td');
                name.textContent = item.name
                row.appendChild(name);

                const email = document.createElement('td');
                email.textContent = item.email;
                row.appendChild(email);

                const phone_number = document.createElement('td');
                phone_number.textContent = item.phone_number;
                row.appendChild(phone_number);

                const date = document.createElement('td');
                date.textContent = new Date(item.created_at).toLocaleDateString();
                row.appendChild(date);
                

                tableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Erro ao buscar os dados da API:', error);
        });
}