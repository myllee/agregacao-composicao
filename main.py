from Funcionario import Funcionario
from Endereco import Endereco

endereco = Endereco("Rua Delegado Carlos Paulo Lima", 12, "Bairro Bela Vista", "descoberto", "minas gerais", "Brasil")
funcionario = Funcionario("Camyle Vitória", 19, endereco, 2000)
print(funcionario)