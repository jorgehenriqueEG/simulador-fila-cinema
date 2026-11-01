def simular_fila(clientes):
    tempo_total = 0
    resultados = {}
    fila_infantil = [c for c in clientes if c["tipo"] == "infantil"]
    fila_adulto = [c for c in clientes if c["tipo"] == "adulto"]
    
    while fila_infantil or fila_adulto:
        if fila_infantil:
            cliente = fila_infantil.pop(0)
            tempo_espera = 30
        elif fila_adulto:
            cliente = fila_adulto.pop(0)
            tempo_espera = 30
        
        tempo_total += tempo_espera
        resultados[cliente["nome"]] = tempo_total
    
    return resultados

clientes_exemplo = [
    {"nome": "Ana", "tipo": "adulto"},
    {"nome": "Lia", "tipo": "infantil"},
    {"nome": "Beto", "tipo": "adulto"},
    {"nome": "Pedro", "tipo": "infantil"}
]

saida = simular_fila(clientes_exemplo)
print(saida)