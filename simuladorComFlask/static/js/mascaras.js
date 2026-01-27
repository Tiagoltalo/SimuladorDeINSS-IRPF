let salario = document.querySelector("input#salario")
let pensao = document.querySelector("input#pensao")

function formatarMoeda(entrada) {
    let valor = entrada.target.value.replace(/\D/g, "");

    if (!valor) {
        entrada.target.value = "";
        return;
    }

    valor = Number(valor) / 100;

    entrada.target.value = valor.toLocaleString("pt-BR", {
        style: "currency",
        currency: "BRL"
    });
}

salario.addEventListener("input", formatarMoeda)
pensao.addEventListener("input", formatarMoeda)