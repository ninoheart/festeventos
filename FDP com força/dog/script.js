var dogimg = document.getElementById("dogimg");
var botao = document.getElementById("botao");

//função que busca imagem de dog
async function buscar() {
    //try vai rodar app normalmente
    try {
        var response = await fetch("https://dog.ceo/api/breeds/image/random");
        //armazena o conteúdo
        var dados = await response.json();
        //joga na imagem o linck da foto
        dogimg.src= dados.message;

    }catch (error) {
        //catch serve para capturar erro se der errado
        alert("Erro ao buscar dog!",error);
    }    
}
//se tiver de click no botão, chama a função buscar
botao.addEventListener("click", buscar);