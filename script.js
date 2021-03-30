function aten(){
  var freq =parseInt(document.getElementById("frequencia").value) 
  if (freq>=250 && freq<=1000)
    var atenuacao=40
  else if (freq>=2000 && freq<=3000)
    var atenuacao = 45
  else if (freq>=4000 && freq<=8000)
    var atenuacao = 50
  return atenuacao;
}

function mask(){
  atenuacao = aten()
  var limiar = parseInt(document.getElementById("limiar").value)
  var limiarcontr = parseInt(document.getElementById("limiarcontr").value)
  var freq =parseInt(document.getElementById("frequencia").value)
  if(limiar-atenuacao>limiarcontr-10){
    document.write("Precisa mascarar!", "<br>")
    var maskmin=limiar-atenuacao-limiarcontr+10+10+limiarcontr
    var maskmax=limiar-15+atenuacao
    var supermax=limiar-10+atenuacao
    document.write("O mascaramento mínimo para " + freq + "Hz é: " + maskmin, "<br>")
    document.write("O mascaramento máximo para " + freq + "Hz é: " + maskmax, "<br>")
    document.write("O supermascaramento para " + freq + "Hz é: " + supermax, "<br>")

  } else{
    document.write("Não precisa mascarar!")
  }
    return limiar, maskmin, supermax;
}
  
function loop(){
  var limiar = parseInt(mask())
  var resposta1= prompt("O paciente respondeu? Se não, aumente 5dB de tom puro na orelha testada. Se ele responder, aumente 5dB de ruído")
  
  while (resposta1=="nao"){
    resposta1 = prompt("Respondeu? Se não respondeu, aumente 5")
    limiar=limiar+5
    }
  if (resposta1=="sim"){
      document.write("O mascaramento foi suficiente!")
    }
  console.log("limiar: " + limiar1)
}