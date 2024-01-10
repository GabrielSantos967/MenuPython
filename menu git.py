import json

listaAlunos = {}
listaProf = {}
matriculas = {}
turmas = {}
disciplinas = {}

def lerAlunos():
    try:
        with open("alunos.json", "r", encoding="utf-8") as arquivo:
            listaAlunos = json.load(arquivo)
    except FileNotFoundError:
        listaAlunos = {}
    return listaAlunos

def salvarAlunos(listaAlunos):
    with open("alunos.json", "w", encoding="utf-8") as arquivo:
        json.dump(listaAlunos, arquivo, ensure_ascii=False)

def incluir_aluno():
    codigo = input("Insira o código do aluno: ")
    nome = input("Coloque o nome do aluno: ")
    cpf = input("Coloque o CPF do aluno: ")

    lista_alunos = lerAlunos()
    
    if codigo not in lista_alunos:
        lista_alunos[codigo] = {"nome": nome, "CPF": cpf}
        print("Aluno cadastrado com sucesso!")
        salvarAlunos(lista_alunos)
    else:
        print("Aluno já cadastrado com esse código.")

def listar_alunos():
    listaAlunos = lerAlunos()
    if listaAlunos:
        print("Lista de Alunos:")
        for codigo, aluno in listaAlunos.items():
            print(f"Código: {codigo}, Nome: {aluno['nome']}, CPF: {aluno['CPF']}")

def excluir_aluno():
    codigo = input("Qual o código do aluno que deseja excluir: ")
    lista_alunos = lerAlunos()
    
    if codigo in lista_alunos:
        del lista_alunos[codigo]
        salvarAlunos(lista_alunos)
        print(f"Aluno com código {codigo} excluído com sucesso!")
    else:
        print(f"Aluno com código {codigo} não encontrado.")

def atualizar_aluno():
    codigo = input("Qual o código do aluno que deseja editar: ")
    lista_alunos = lerAlunos()
    
    if codigo in lista_alunos:
        del lista_alunos[codigo]
        salvarAlunos(lista_alunos)
        print(f"Aluno com código {codigo} atualizado com sucesso!")
        incluir_aluno()
    else:
        print(f"Aluno com código {codigo} não encontrado.")

def lerProf():
    try:
        with open("profs.json", "r", encoding="utf-8") as arquivo:
            listaProf = json.load(arquivo)
    except FileNotFoundError:
        listaProf = {}
    return listaProf

def salvarProf(listaProf):
    with open("profs.json", "w", encoding="utf-8") as arquivo:
        json.dump(listaProf, arquivo, ensure_ascii=False)

def incluir_prof():
    codigo = input("Insira o código do professor: ")
    nome = input("Coloque o nome do professor: ")
    cpf = input("Coloque o cpf do professor: ")

    lista_prof = lerProf()
    if codigo not in lista_prof:
        lista_prof[codigo] = {"nome": nome, "CPF": cpf}
        print("Professor cadastrado com sucesso!")
        salvarProf(lista_prof)
    else:
        print("Professor já cadastrado.")

def listar_prof():
    listaProfs = lerProf()
    if listaProfs:
        print("Lista de Professores:")
        for codigo, prof in listaProfs.items():
            print(f"Código: {codigo}, Nome: {prof['nome']}, CPF: {prof['CPF']}")

def excluir_prof():
    codigo = input("Qual o código do professor que deseja excluir: ")
    lista_prof = lerProf()
    
    if codigo in lista_prof:
        del lista_prof[codigo]
        salvarProf(lista_prof)
        print(f"Professor com código {codigo} excluído com sucesso!")
    else:
        print(f"Professor com código {codigo} não encontrado.")

def atualizar_prof():
    codigo = input("Qual o código do professor que deseja editar: ")
    lista_prof = lerProf()
    
    if codigo in lista_prof:
        del lista_prof[codigo]
        salvarProf(lista_prof)
        print(f"Professor com código {codigo} atualizado com sucesso!")
        incluir_prof()
    else:
        print(f"Professor com código {codigo} não encontrado.")

def lerDisc():
    try:
        with open("disciplinas.json", "r", encoding="utf-8") as arquivo:
            disciplinas = json.load(arquivo)
    except FileNotFoundError:
        disciplinas = {}
    return disciplinas

def salvarDisc(disciplinas):
    with open("disciplinas.json", "w", encoding="utf-8") as arquivo:
        json.dump(disciplinas, arquivo, ensure_ascii=False)

def incluir_disciplina():
    codigo = input("Insira o código da disciplina: ")
    nome = input("Coloque o nome da disciplina: ")
    disciplinas[codigo] = {"nome": nome}
    salvarDisc(disciplinas)
    print(f"Disciplina com o código {codigo} criada com sucesso!")

def listar_disciplinas():
    disciplinas = lerDisc()
    if disciplinas:
        print("Disciplinas:")
        for codigo, disc in disciplinas.items():
            print(f"Código: {codigo}, Nome: {disc['nome']}")

def excluir_disciplinas():
    codigo = input("Digite o código da disciplina que deseja excluir: ")
    if codigo in disciplinas:
        del disciplinas[codigo]
        salvarDisc(disciplinas)
        print(f"Disciplina com código {codigo} excluída com sucesso!")
    else:
        print(f"Disciplina com código {codigo} não encontrada.")

def atualizar_disciplinas():
    codigo = input("Qual o código da disciplina que deseja editar: ")
    if codigo in disciplinas:
        del disciplinas[codigo]
        incluir_disciplina()
    else:
        print(f"Disciplina com código {codigo} não encontrada.")

def lerTurma():
    try:
        with open("turmas.json", "r", encoding="utf-8") as arquivo:
            turmas = json.load(arquivo)
    except FileNotFoundError:
        turmas = {}
    return turmas

def salvarTurmas(turmas):
    with open("turmas.json", "w", encoding="utf-8") as arquivo:
        json.dump(turmas, arquivo, ensure_ascii=False)

def incluir_turmas():
    codigo = input("Insira o código da turma: ")
    codigoProf = input("Coloque o código do professor: ")
    codigoDisc = input("Coloque o código da disciplina: ")
    
    with open("profs.json", "r", encoding="utf-8") as arquivo:
        listaProf = json.load(arquivo)

    with open("disciplinas.json", "r", encoding="utf-8") as arquivo:
        disciplinas = json.load(arquivo)
    
    if codigoProf in listaProf and codigoDisc in disciplinas:
        turmas[codigo] = {
            "código da turma": codigo,
            "professor": listaProf[codigoProf]["nome"],
            "disciplina": disciplinas[codigoDisc]["nome"]
        }
        salvarTurmas(turmas)
        print(f"Turma com código {codigo} adicionada com sucesso!")
    else:
        print("Professor ou disciplina não encontrados. Verifique os códigos informados.")

def listar_turmas():
    turmas = lerTurma()
    if turmas:
        print("Lista de Turmas:")
        for codigo, turma in turmas.items():
            professor = turma["professor"]
            disciplina = turma["disciplina"]
            print(f"Código: {codigo}, com o professor: {professor}, e a matéria de {disciplina}")

def excluir_turmas():
    codigo = input("Digite o código da turma que deseja excluir: ")
    if codigo in turmas:
        del turmas[codigo]
        salvarTurmas(turmas)
        print(f"Turma com código {codigo} excluída com sucesso!")
    else:
        print(f"Turma com código {codigo} não encontrada.")

def atualizar_turmas():
    codigo = input("Qual o código da turma que deseja editar: ")
    if codigo in turmas:
        del turmas[codigo]
        incluir_turmas()
    else:
        print(f"Turma com código {codigo} não encontrada.")

def lerMat():
    try:
        with open("matriculas.json", "r", encoding="utf-8") as arquivo:
            matriculas = json.load(arquivo)
    except FileNotFoundError:
        matriculas = {}
    return matriculas

def salvarMat(matriculas):
    with open("matriculas.json", "w", encoding="utf-8") as arquivo:
        json.dump(matriculas, arquivo, ensure_ascii=False)

def incluir_matriculas():
    codigo = input("Coloque o código de matrícula: ")
    codigoAluno = input("Coloque o código do aluno: ")
    codigoTurma = input("Coloque o código da turma: ")
    

    try:
        with open("matriculas.json", "r", encoding="utf-8") as arquivo:
            matriculas = json.load(arquivo)
    except FileNotFoundError:
        matriculas = {}  

    with open("alunos.json", "r", encoding="utf-8") as arquivo:
        listaAlunos = json.load(arquivo)

    with open("turmas.json", "r", encoding="utf-8") as arquivo:
        turmas = json.load(arquivo)
    
    if codigoAluno in listaAlunos and codigoTurma in turmas:
        matricula = {
            "código da matrícula": codigo,
            "aluno": listaAlunos[codigoAluno]["nome"],
            "turma": turmas[codigoTurma]["código da turma"]
        }
        
        matriculas[codigo] = matricula
        
        with open("matriculas.json", "w", encoding="utf-8") as arquivo:
            json.dump(matriculas, arquivo, indent=4)
            
        print(f"Matrícula com código {codigo} adicionada com sucesso!")
    else:
        print("Aluno ou turma não encontrados. Verifique os códigos informados.")

def menu_principal():
    while True:
        print('''
          ---MENU---
          1. Estudantes
          2. Professores
          3. Disciplinas
          4. Turmas
          5. Matrículas
          6. Sair
        ''')
        menu = int(input("Digite uma opção: "))

        if menu == 1:
            print("*** Estudantes ***")
            while True:
                print('''
                    1. Incluir aluno
                    2. Listar alunos
                    3. Excluir aluno
                    4. Editar aluno  
                    5. Voltar ao menu principal
                ''')
                opcao = int(input("Digite uma opção: "))

                if opcao == 1:
                    incluir_aluno()
                elif opcao == 2:
                    listar_alunos()
                elif opcao == 3:
                    excluir_aluno()
                elif opcao == 4:
                    atualizar_aluno()
                elif opcao == 5:
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        if menu == 2:
            print("***Professores***")
            while True:
                print('''
                    1. Incluir professor
                    2. Listar professor
                    3. Excluir professor
                    4. Editar professor  
                    5. Voltar ao menu principal
                ''')
                opcao = int(input("Digite uma opção: "))
                if opcao == 1:
                    incluir_prof()
                elif opcao == 2:
                    listar_prof()
                elif opcao == 3:
                    excluir_prof()
                elif opcao == 4:
                    atualizar_prof()
                elif opcao == 5:
                    break
        elif menu == 3:
            print("***Disciplinas***")
            while True:
                print('''
                    1. Incluir disciplinas
                    2. Listar disciplinas
                    3. Excluir disciplinas
                    4. Editar disciplinas  
                    5. Voltar ao menu principal
                ''')
                opcao = int(input("Digite uma opção: "))
                if opcao == 1:
                    incluir_disciplina()
                elif opcao == 2:
                    listar_disciplinas()
                elif opcao == 3:
                    excluir_disciplinas()
                elif opcao == 4:
                    atualizar_disciplinas()
                elif opcao == 5:
                    break
        elif menu == 4:
            print("***Turmas***")
            while True:
                print('''
                    1. Incluir turmas
                    2. Listar turmas
                    3. Excluir turmas
                    4. Editar turmas 
                    5. Voltar ao menu principal
                ''')
                opcao = int(input("Digite uma opção: "))
                if opcao == 1:
                    incluir_turmas()
                elif opcao == 2:
                    listar_turmas()
                elif opcao == 3:
                    excluir_turmas()
                elif opcao == 4:
                    atualizar_turmas()
                elif opcao == 5:
                    break  
        elif menu == 5:
            print("***Matrículas***")
            while True:
                print('''
                    1. Incluir matrículas
                    2. Listar matrículas
                    3. Excluir matrículas
                    4. Editar matrículas 
                    5. Voltar ao menu principal
                ''')
                opcao = int(input("Digite uma opção: "))
                if opcao == 1:
                    incluir_matriculas()
                elif opcao == 2:
                    listar_turmas()
                elif opcao == 3:
                    excluir_turmas()
                elif opcao == 4:
                    atualizar_turmas()
                elif opcao == 5:
                    break 
        elif menu == 6:
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()