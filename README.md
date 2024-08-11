# POO
 Programação Orientada a Objetos em Ptyhon


 POO
A Programação Orientada a Objetos (POO) é um paradigma amplamente utilizado na programação, permitindo criar programas organizados, modulares e reutilizáveis. Vamos explorar os conceitos-chave da POO:

Classes
São tipos de dados definidos pelo desenvolvedor que atuam como modelos para objetos. Imagine classes como moldes de bolo, e bolos como objetos. No Python as classes são nomeadas com a sintaxe "PascalCase" usando a palavra reservada class para defini-las.

Uma classe define um novo tipo, assim como, string, boolean, integer, etc. Por exemplo, no Python temos os construtores tuple(), set(), dict(), str(), etc. que nada mais são d que classes que definem esses tipos.

Atributos
Representam as características ou propriedades do objeto. Por exemplo, um objeto “Carro” pode ter atributos como “cor”, “modelo” e “ano”. No Python os atributos são definidos, preferivelmente, no método construtor. Neste caso, são criados como variáveis, mas com a palavra chave self instanciada. Também podem ser definidos no contexto da classe.

Métodos
São funções definidas dentro de uma classe que descreve os comportamentos (Verbos) do objeto. Por exemplo, um método “ligar()” pode ser usado para ligar o carro. Usamos def para criar métodos e o parâmetro self é obrigatório.

Método construtor
É um método especial que é executado automaticamente quando um objeto de uma classe é instanciado. Ele é usado para inicializar os atributos da classe. No Python, o método construtor é chamado de __init__() e é definido dentro da classe.

Objetos
São instâncias de uma classe. Eles podem representar entidades do mundo real (como Carro, Pessoa, Usuário) ou abstratas (como Temperatura, Umidade, Medição, Configuração). Cada objeto criado (instanciado) a partir de uma classe é independente dos outros.

Herança
Permite criar uma nova classe baseada em uma classe existente, reutilizando seus atributos e métodos.

Polimorfismo
Permite que objetos de diferentes classes sejam tratados de maneira uniforme. Por exemplo, um método pode funcionar com diferentes tipos de objetos.

Encapsulamento
Refere-se a ocultar detalhes internos de uma classe, expondo apenas o necessário para o uso externo.

Getters e Setters
São métodos específicos para manipular atributos protegidos e privados. Um método getter permite acessar o valor do atributo, e um método setter permite modificá-lo de maneira controlada.

Visibilidade
É como se controla o acesso externo para leitura e modificação, principalmente dos atributos, mas também de métodos de um objeto. Por exemplo, no Python:

Público → pode ser acessado diretamente de qualquer parte do programa. No diagrama, usamos + para representar.
Protegido → só pode ser acessado de objetos filho, herdeiros. São identificados pelo _ no início do identificador. No diagrama, usamos # para representar.
Privado → não pode ser acessado externamente. Somente pela própria classe. São identificados pelos __ no início do identificador. Sò podem ser manipulados pelos gettere setter correspondentes. No diagrama, usamos - para representar.
Diagrama de classe
É uma representação gráfica utilizada na programação para descrever a estrutura de um sistema. Ele apresenta as classes do sistema, seus atributos, operações e as relações entre os objetos.

    ┌──────────────────────────┐
    │           User           │    ← Nome da classe
    ├──────────────────────────┤
    │ - id: integer            │
    │ - name: string           │
    │ - email: string          │    ← Atributos da classe
    │ - login: string          |
    │ - password: string       │
    ├──────────────────────────┤
    │ # addUser(): boolean     │
    │ # editUser(): collection │
    │ # deleteUser(): boolean  │    ← Métodos da classe
    │ + viewUser(): collection │
    │ + login(): collection    │
    │ + logout(): boolean      │
    └──────────────────────────┘
Relacionamentos
Em um diagrama de classes UML, os conectores usados para representar os relacionamentos entre as classes são:

Herança (Generalização): Representada por uma linha sólida com um triângulo aberto na ponta, indicando que uma classe filha herda de uma classe pai.
──────────▷

Realização: Uma linha tracejada com um triângulo aberto, mostrando que uma classe implementa uma interface.
─ ─ ─ ─ ─ ─▷

Composição: Uma linha sólida com um losango preenchido na ponta, indicando uma relação "parte-todo" forte, onde a parte não pode existir sem o todo.
──────────◆

Agregação: Uma linha sólida com um losango aberto, representando uma relação "parte-todo" mais fraca, onde a parte pode existir independentemente do todo.
──────────◇

Associação: Uma linha sólida simples, que pode ter setas para indicar a direção da navegação, mostrando que as classes estão relacionadas.
──────────

Dependência: Uma linha tracejada com uma seta, indicando que uma classe depende temporariamente de outra.
- - - - ->

Esses conectores ajudam a visualizar a estrutura e as interações entre as classes no sistema.

Conclusão
Em resumo, a POO se concentra em objetos interagindo entre si, tornando o código mais modular e fácil de manter.

Referências
Classes e Objetos em POO: Uma visão detalhada
W3Schools - Python Classes and Objects
Wikipedia - Programação orientada a objetos
Wikipedia - Diagrama de classes
