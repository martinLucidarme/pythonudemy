import subprocess
'''
Para executar linhas de comando
'''
# Windows - ping 127.0.0.1
# Linux - ping 127.0.0.1 -c 4

proc = subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output=True,  # para capturar na variavel e nao printar apenas
    text=True
)

saida = proc.stdout
print(saida)
