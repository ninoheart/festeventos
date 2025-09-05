function buscar(){
    //pegar o cep do input
    var cep = document.getElementById('cep').value;
    alert(cep);
    //link da api de cep
    var url="https://viacep.com.br/ws/"+cep+"/json/";

    //faz a busca na api de cep
fetch(url)
.then(response => response.json())
.then(dados => { 
    if(dados.erro){
        //se tiver erro
        document.getElementById('resultado').textContent = 'Cep não encontrado';
    }else{
        alert(dados.localidade);
        //se não tiver erro
        document.getElementById('resultado').innerHTML = '<strong> Cidade: </strong>' + dados.localidade + '<br>'
        + '<strong> Cep: </strong>'+ dados.cep + '<br>'
        + '<strong> Logradouro: </strong>' + dados.logradouro + '<br>'
        + '<strong> Complemento: </strong>' + dados.complemento + '<br>'
        + '<strong> bairro: </strong>' + dados.bairro + '<br>'
        + '<strong> Estado: </strong>' + dados.estado + '<br>'
        + '<strong> Região: </strong>' +dados.região + '<br>'
    }
}).catch(error => alert('Erro na conexão: '+ error));    

}
