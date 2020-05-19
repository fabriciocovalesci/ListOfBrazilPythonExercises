#!/bin/bash

cd /home/fabricio/Documentos/ListaExerciciosPythonBrasil/DecisionStructure

N=1
while [  $N -lt 28 ]; do
    touch number_$N.py
    let N=N+1; 
done

# gera arquivos .py automatico