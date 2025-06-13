function loadId(url, idHTML, value) {
    url += `?value=${value}`;
    const loadingImage = document.getElementById('loading_image');
    const contentArea = document.getElementById(idHTML);


    if (loadingImage && contentArea) {
        loadingImage.style.display = 'block'; // Exibir a figura de carregamento
        contentArea.innerHTML = ''; // Limpar conteúdo anterior
    }


    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erro HTTP! Status: ${response.status}`);
            }
            return response.text();
        })
        .then(data => {
            if (contentArea) {
                contentArea.innerHTML = data;
            } else {
                console.error(`Elemento com id "${id}" não encontrado.`);
            }
        })
        .catch(error => {
            console.error('Existe problemas de erro na operação de rede lógica:', error);
        })
        .finally(() => {
            if (loadingImage) {
                loadingImage.style.display = 'none'; // Ocultar a figura de carregamento
            }
        });
}


function modalInfo(titulo, conteudo) {
    document.getElementById('modalTitulo').innerText = titulo;
    document.getElementById('modalConteudo').innerHTML = conteudo;
    document.getElementById('modalRodape').innerHTML = '<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fechar</button>';
    new bootstrap.Modal(document.getElementById('divModal')).show();
}


function modalInfoLoad(titulo, url, value) {
    url += `?value=${value}`;
    const loadingImage = document.getElementById('loading_image');


    if (loadingImage) {
        loadingImage.style.display = 'block'; // Exibir a figura de carregamento
    }


    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erro HTTP! Status: ${response.status}`);
            }
            return response.text();
        })
        .then(data => {
            document.getElementById('modalTitulo').innerText = titulo;
            document.getElementById('modalConteudo').innerHTML = data
            document.getElementById('modalRodape').innerHTML = '<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fechar</button>';
            new bootstrap.Modal(document.getElementById('divModal')).show();
        })
        .catch(error => {
            console.error('Existe problemas de erro na operação de rede lógica:', error);
        })
        .finally(() => {
            if (loadingImage) {
                loadingImage.style.display = 'none'; // Ocultar a figura de carregamento
            }
        });
}


function modalConfirm(titulo, conteudo, funcaoConfirmar) {
    document.getElementById('modalTitulo').innerText = titulo;
    document.getElementById('modalConteudo').innerHTML = conteudo;
    document.getElementById('modalRodape').innerHTML = `
           <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
           <button type="button" class="btn btn-danger" onclick="${funcaoConfirmar}">Confirmar</button>
       `;
    new bootstrap.Modal(document.getElementById('divModal')).show();
}


function getValue(id) {
    return document.getElementById(id).value;
}


function getText(id) {
    var select = document.getElementById(id);
    var textoSelecionado = select.options[select.selectedIndex].text;
    return textoSelecionado;
}


function getMultiple(id) {
    var select = document.getElementById(id);
    var opcoesSelecionadas = Array.from(select.querySelectorAll('option:checked')).map(function (opcao) {
        return {
            id: opcao.value,
            text: opcao.text
        };
    });
    return opcoesSelecionadas;
}


function printMultiple(id) {
    opcoesSelecionadas = getMultiple(id);
    var resultadoTexto = opcoesSelecionadas.map(function (opcao) {
        return "Id: " + opcao.id + ", Texto: " + opcao.text;
    }).join('<br>'); // Junta os pares com quebras de linha


    return resultadoTexto;
}
