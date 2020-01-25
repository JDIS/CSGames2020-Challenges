function render_table(tableId, data) {
    console.log(data)
    table = document.getElementById(tableId);
    table.innerHTML = "";

    columns = Object.keys(data[0])

    // Render table columns
    const colRow = table.createTHead().insertRow();
    columns.forEach(c => {
        const th = document.createElement('th');
        th.appendChild(document.createTextNode(c));        
        colRow.appendChild(th);
    });


    // Render table rows
    const table_TB = table.createTBody();
    for(const row in data) {
        if (row == "flag") continue;

        const newRow = table_TB.insertRow();
        
        // Append a text node to the cell
        columns.forEach(col => {
            const newCell = newRow.insertCell();
            newCell.appendChild(document.createTextNode(data[row][col]));
        })
    }
}

function render_error(error) {
    document.getElementById('error').innerHTML = `<div class="alert alert-danger" role="alert">${error}</div>`;
    document.getElementById('output').innerHTML = '';
}

function render_flag(flag) {
    document.getElementById('flag').innerHTML = `<div class="alert alert-success" role="alert">${flag}</div>`;
}