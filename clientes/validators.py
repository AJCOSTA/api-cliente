import re
from validate_docbr import CPF

def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

def formatar_cpf(numero_cpf):
    cpf = CPF()
    return cpf.mask(numero_cpf)

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(numero_rg):
    return len(numero_rg) == 9

def celular_valido(numero_celular):
    modelo = re.compile(r'^\d{2} \d{5}-\d{4}$')
    return bool(modelo.match(numero_celular))

# # # Exemplo de uso:
# # cpf = "12345678909"
# # nome = "JohnDoe"
# # rg = "123456789"
# # celular = "99 12345-6789"

# # Validar CPF
# if cpf_valido(cpf):
#     print(f"CPF {cpf} é válido.")
# else:
#     print(f"CPF {cpf} é inválido.")

# # Formatar CPF
# cpf_formatado = formatar_cpf(cpf)
# print(f"CPF formatado: {cpf_formatado}")

# # Validar Nome
# if nome_valido(nome):
#     print(f"Nome {nome} é válido.")
# else:
#     print(f"Nome {nome} é inválido.")

# # Validar RG
# if rg_valido(rg):
#     print(f"RG {rg} é válido.")
# else:
#     print(f"RG {rg} é inválido.")

# # Validar Celular
# if celular_valido(celular):
#     print(f"Celular {celular} é válido.")
# else:
#     print(f"Celular {celular} é inválido.")
