function telaInicial() {
    window.location.href = "/";
}

function formulario() {
    window.location.href = "/formulario";
}

function verificarModalidades() {
    let segurado = document.querySelector("select#segurado").value
    let seguradosComModalidades = ["segurado especial", "segurado facultativo", "contribuinte individual"]
    let seguradosSemModalidades = ["empregado", "empregado doméstico", "trabalhador avulso"]
    let selectModalidade = document.querySelector("div#div-modalidades")


    if (seguradosComModalidades.includes(segurado)) {
        if (segurado === "contribuinte individual") {
            selectModalidade.innerHTML = `  <label for="modalidades">Modalidades</label>
                                    <select name="modalidade" id="modalidade">
                                        <option value="plano simplificado">Plano Simplificado</option>
                                        <option value="plano normal">Plano Normal</option>
                                        <option value="baixa renda">Baixa Renda</option>
                                    </select>`
        }

        else if (segurado === "segurado facultativo") {
            selectModalidade.innerHTML = `  <label for="modalidades">Modalidades</label>
                                    <select name="modalidade" id="modalidade">
                                        <option value="baixa renda">Baixa Renda</option>
                                        <option value="plano simplificado">Plano Simplificado</option>
                                        <option value="plano normal">Plano Normal</option>
                                    </select>`
        }

        else if (segurado === "segurado especial") {
            selectModalidade.innerHTML = `  <label for="modalidades">Modalidades</label>
                                    <select name="modalidade" id="modalidade">
                                        <option value="contribuição obrigatória">Contribuição Obrigatória</option>
                                        <option value="contribuição optativa">Contribuição Optativa</option>
                                    </select>`
        }
    }

    else if (seguradosSemModalidades.includes(segurado)) {
        selectModalidade.innerHTML = ` `
    }
}