##  Semana 5: Repertorio de instrucciones

Objetivo: conocer las caracteristicas principales de los repertorios de instrucciones

## Tabla de contenido

* [Repertorio_de_instrucciones](#Repertorio_de_instrucciones)


## Repertorio_de_instrucciones


| OpCode | Mnemonic     | Description
|--------|--------------|------------
| 00     | **LDA** xxx  | Cargar el contenido de la dirección de memoria xxx en el registro ACC
| 01     | **STA** xxx  | Almacenar el contenido del registro ACC en la dirección de memoria xxx
| 10     | **ADD** xxx  | Sumar el registro ACC con el contenido de memoria xxx
| 11     | **HLT**      | Detiene la ejecución


#### Instrucciones_implementadas

Vamos a implementar las instrucciones de saltos:

- [x] LDA
- [x] STA
- [x] ADD
- [x] HLT
- [ ] JMP
- [ ] JMZ