#!/bin/bash

# Comando para executar o seu programa em Python
PROGRAMA="python3 main.py"

# Nome do arquivo de saída (mudei o nome para não sobrescrever o seu teste em C)
SAIDA="tabela_tempos_python.txt"

echo "Iniciando os testes de desempenho em Python..."

# Cria o cabeçalho da tabela no arquivo txt
echo "Tabela de Tempo de Execução (Crivo em Python)" > $SAIDA
echo "---------------------------------------------------" >> $SAIDA
echo -e "Entrada (N)\t|\tTempo User (segundos)" >> $SAIDA
echo "---------------------------------------------------" >> $SAIDA

# O laço itera para i = 3 até 10, conforme o roteiro do laboratório
for i in {3..9}; do
    # Calcula 10 elevado a i
    N=$((10**i))
    
    echo "Executando para N = $N (10^$i)..."
    
    # Executa o programa e captura apenas o tempo 'user'
    TEMPO_USER=$( { /usr/bin/time -f "%U" $PROGRAMA $N > /dev/null; } 2>&1 )
    
    # Verifica se o tempo foi capturado com sucesso (se o script não falhou por falta de RAM)
    if [ $? -eq 0 ]; then
        echo -e "10^$i\t\t|\t$TEMPO_USER" >> $SAIDA
    else
        echo -e "10^$i\t\t|\tFALHA/MEMÓRIA EXCEDIDA" >> $SAIDA
        echo "Aviso: A execução para 10^$i falhou (provavelmente devido a limites de memória)."
    fi
done

echo "Testes finalizados!"
echo "Resultados salvos em: $SAIDA"
echo "---------------------------------------------------"
cat $SAIDA