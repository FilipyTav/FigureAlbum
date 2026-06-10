# Sistema de Álbum de Figurinhas
Simulação de gerenciamento, estatísticas e intercâmbio de álbuns de figurinhas colecionáveis via terminal.

---

## Arquitetura de Dados

Foram usadas diferentes estruturas de dados para cada funcionalidade do sistema:

* **Álbum de Figurinhas (`Album`):** Gerencia a coleção de figurinhas utilizando-se de uma **Lista Encadeada Simples**.

* **Fila de Histórico(`Queue`):** Implementada como uma **Fila baseada em Lista Encadeada Simples**, seguindo a lógica **FIFO** (*First-In, First-Out*). Ela registra cronologicamente os pares de figurinhas envolvidos em trocas (saídas e entradas).

* **Navegação (Interface): (`MenuStack`)** Os menus e telas do sistema são controlados por uma **Pilha (Stack)**, seguindo a lógica **LIFO** (*Last-In, First-Out*). Isso permite que o usuário navegue entre submenus de gerenciamento e retorne perfeitamente à tela anterior.

---

## Estrutura do Projeto

| Diretório / Arquivo | Descrição |
| :--- | :--- |
| `src/main.py` | Ponto de entrada da aplicação. |
| `src/data/` | Armazenamento de persistência de dados do usuário, oponente e histórico em arquivos CSV. |
| **src/structs/** | **Núcleo de Estruturas de Dados** |
| ├─ `Album.py` | Classe principal do álbum. Gerencia as figurinhas adquiridas e lógica de troca. |
| ├─ `Figurine.py` | Define a classe `Figurine` (atributos como nome, raridade, posição e ID). |
| ├─ `Queue.py` | Estrutura de fila encadeada para armazenar o histórico de trocas (FIFO). |
| ├─ `MenuStack.py` | Pilha para gerenciar o empilhamento e retorno de telas da interface (LIFO). |
| └─ `Menu.py` | Definições das opções de navegação e componentes visuais do menu. |
| **src/ui/** | **Gerenciamento de Estado e Telas** |
| ├─ `screen_manager.py` | Centraliza a renderização de telas. |
| └─ `state.py` | Controla o estado global da aplicação (`AppState`), como o álbum ativo. |
| **src/utils/** | **Auxiliares e Estilização** |
| ├─ `colors.py` | Enumerações e constantes ANSI para formatação e cores no terminal. |
| ├─ `config.py` | Parâmetros de configuração global do sistema. |
| ├─ `figurine_examples.py`| Banco de dados blueprint de figurinhas disponíveis para o álbum. |
| ├─ `input.py` | Tratamento, limpeza de strings e validação robusta de entradas do usuário. |
| ├─ `strings.py` | Funções utilitárias para manipulação e centralização de textos no terminal. |
| └─ `types.py` | Definições de tipos customizados e enums (como Raridades e Posições). |

---

## Como Executar

### 1. Pré-requisitos
* **Python 3.10** ou superior.

### 2. Instalação
1. Clone o repositório para sua máquina:
```bash
git clone https://github.com/FilipyTav/FigureAlbum.git
cd FigurineAlbum
```

### 3. Execução
Execute o arquivo principal:
```bash
python src/main.py
```
