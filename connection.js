import mysql from 'mysql2'

class Connection {

    static connection(){
        
        
        
        let connected = mysql.createConnection({
            host: 'localhost',
            user: 'root',
            password: '',
            database: 'usuario'
        })
        connected.connect()

        return connected
    }




}






/*

function mostrar (nome){
    console.log("Olá JS! Bem vindo:" + nome)
}


mostrar("Agata")

*/