// document.body.onload = getCommands;

function reloadCommands() {
    let table = document.getElementById("listCommand");
    table.innerHTML = "";
    
    getCommands()
}

function getCommands(){

    let {PythonShell} = require('python-shell');
    let path = require('path')

    let options = {
        scriptPath: path.join(__dirname, '../core/'),
        // args: [peso, altura]
    }
    
    let table = document.getElementById("listCommand");
    let row = table.insertRow(0);
    let cmd_row
    let cmd_cell1
    let cmd_cell2
    let cmd_cell3

    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    let cell3 = row.insertCell(2);

    cell1.innerHTML = "Command";
    cell2.innerHTML = "Script"; 
    cell3.innerHTML = "Action"; 
    
    PythonShell.run('command_list.py', options, (err, results) => {
        if (err) throw err;
        if (! results) return reloadCommands();
        
        let cmd

        for (let i = 0; i < results.length; i++) {
            cmd = JSON.parse(results[i].replace(/'/g, '"'));
            cmd_row = table.insertRow(i+1);
            cmd_cell1 = cmd_row.insertCell(0)
            cmd_cell2 = cmd_row.insertCell(1)
            cmd_cell3 = cmd_row.insertCell(2)
            
            cmd_cell1.innerHTML = cmd['name'] || '';
            cmd_cell2.innerHTML = cmd['file'] || '';
            cmd_cell3.innerHTML = `<button id='${cmd['name']}'` +
            "type='button' " +
            "onclick='runCommand(this);' " +
            "class='btn btn-default'>" +
            "<span class='glyphicon glyphicon-play'></span> Run Command" +
            "</button>"
        }
    });
}

function runCommand(i){
    let cmd_run = i.id

    let {PythonShell} = require('python-shell');
    let path = require('path')

    let options = {
        scriptPath: path.join(__dirname, '../core/'),
        args: [cmd_run]
    }
    
    PythonShell.run('command_run.py', options, (err, results) => {
        if (err) throw err;
        console.log('results: %j', results);
        alert(results[0])
        return results
    });
}