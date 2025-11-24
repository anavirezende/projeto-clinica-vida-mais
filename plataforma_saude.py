import os
from colorama import init, Fore, Style
init(autoreset=True)


def exibir_nome_plataforma():
    """Exibe o nome estilizado da plataforma na tela."""
    print(Fore.MAGENTA + Style.BRIGHT + '''
          
===Ｃｌｉｎｉｃａ Ｖｉｄａ＋===       
           ''')

def exibir_opcoes():
    """Exibe o menu principal com todas as opções do programa."""

    print(Fore.CYAN + Style.BRIGHT + '1. Cadastrar pacientes')
    print(Fore.CYAN + Style.BRIGHT + '2. Cadastrar médicos')
    print(Fore.CYAN + Style.BRIGHT + '3. Cadastrar exames')
    print(Fore.CYAN + Style.BRIGHT + '4. Agendar consultas')
    print(Fore.CYAN + Style.BRIGHT + '5. Agendar exames')
    print(Fore.CYAN + Style.BRIGHT + '6. Histórico pacientes')
    print(Fore.CYAN + Style.BRIGHT + '7. Lista de pacientes cadastrados')
    print(Fore.CYAN + Style.BRIGHT + '8. Relatórios e estatísticas')
    print(Fore.RED + Style.BRIGHT + '9. Sair\n')

def exibir_subtitulo(texto):
    """Limpa a tela e exibe um subtítulo padronizado.
    
    Args:
        texto (str): O texto do subtítulo a ser exibido.
    """
    os.system('cls')
    exibir_nome_plataforma()
    print()
    print(texto)
    print()

def finalizar_sistema():
    """Exibe uma mensagem de finalização do sistema."""

    exibir_subtitulo(Fore.YELLOW + 'Finalizando sistema')

pacientes = [] #lista para guardar informações de todos os pacientes cadastrados 

def cadastrar_pacientes():
    """Solicita os dados de um novo paciente, cria um dicionário com as
    informações e o adiciona à lista global `pacientes`.
    
    A função lida com a entrada de dados do usuário para nome, CPF, idade,
    telefone, e-mail, endereço e convênio. Ao final, exibe uma mensagem
    de sucesso.
    """

    exibir_subtitulo('Cadastro de pacientes\n')
    nome_paciente = input('Insira o nome completo do paciente: ')
    cpf = input('Insira o CPF do paciente: ')
    idade_paciente = int(input('Insira a idade do paciente: '))
    telefone_pc = input('Insira o telefone do paciente: ')
    email_pc = input('Insira o e-mail do paciente: ')
    endereço_pc = input('Insira o endereço completo do paciente: ')
    convenio_pc = input('Se houver, informe o nome do convênio. Caso contrário digite "Particular": ')

    paciente = { #dicionário usado para salvar as informações de um paciente cadastrado
        'Nome': nome_paciente,
        'CPF': cpf,
        'Idade': idade_paciente,
        'Telefone': telefone_pc,
        'E-mail': email_pc,
        'Endereço': endereço_pc,
        'Convênio': convenio_pc
    }

    pacientes.append(paciente) #adiciona esse paciente à lista de pacientes
    print(Fore.GREEN + f'\nPaciente {nome_paciente} cadastrado com sucesso')
    input('\n Pressione ENTER para retornar ao menu...')


medicos = [] #lista para guardar informações de todos os médicos cadastrados 

def cadastrar_medicos():
    """Solicita os dados de um novo médico, cria um dicionário com as
    informações e o adiciona à lista global `medicos`.
    
    A função lida com a entrada de dados do usuário para nome, CRM, data de
    nascimento, telefone, e-mail, convênio e especialidade. Ao final, exibe
    uma mensagem de sucesso.
    """

    exibir_subtitulo('Cadastro de médicos\n')
    nome_medico = input('Insira o nome completo do(a) médico(a): ')
    crm = input('Insira o CRM do(a) médico(a): ')
    data_nascimento_md = input('Insira a data de nascimento do(a) médico(a): ')
    telefone_md = input('Insira o telefone do(a) médico(a): ')
    email_md = input('Insira o e-mail do(a) médico(a): ')
    convenio_md = input('Informe qual convênio o(a) médico(a) atende. Caso não atenda, digite "Particular": ')
    especialidade = input('Informe a especialidade do(a) médico(a): ')

    

    medico = { #dicionário usado para salvar as informações de um médico cadastrado
        'Nome': nome_medico,
        'CRM': crm,
        'Data de Nascimento': data_nascimento_md,
        'Telefone': telefone_md,
        'E-mail': email_md,
        'Convênio': convenio_md,
        'Especialidade': especialidade
    }

    medicos.append(medico) #adiciona esse paciente à lista de pacientes
    print(Fore.GREEN + f'\nMédico {nome_medico} cadastrado com sucesso')
    input('\nPressione ENTER para retornar ao menu...')

exames = [] 

def cadastrar_exames():
    """Solicita os dados de um novo exame, cria um dicionário com as
    informações e o adiciona à lista global `exames`.
    
    A função lida com a entrada de dados do usuário para nome, código,
    descrição, preço, preparação e convênios aceitos. Ao final, exibe uma
    mensagem de sucesso.
    """

    exibir_subtitulo('Cadastro de exames')
    nome_exame = input('Insira o nome do exame: ')
    codigo_exame = input('Insira o código do exame: ')
    descricao = input('Descrição suscinta do exame: ')
    preco = float(input('Informe o valor do exame (R$): '))
    preparacao = input('Instruções de preparo para o exame: ')
    convenios_aceitos = input('Informe os convênios aceitos (separados por vírgula): ')
    

    exame = { 
        'Nome': nome_exame,
        'Código': codigo_exame,
        'Descrição': descricao,
        'Preço': preco,
        'Preparação': preparacao,
        'Convênios Aceitos': convenios_aceitos
    }

    exames.append(exame)
    print(Fore.GREEN + f'\nExame: {nome_exame} cadastrado com sucesso')
    input('\nPressione ENTER para retornar ao menu...')

consultas_por_paciente = {}

def agendar_consultas():
    """Agenda uma nova consulta para um paciente com um médico.

    Solicita ao usuário o nome do paciente, nome do médico e os detalhes da
    consulta. Verifica se o paciente e o médico estão cadastrados e se não
    há conflito de horário para o mesmo médico. Se tudo estiver correto,
    a consulta é adicionada ao dicionário `consultas_por_paciente`, que
    mapeia nomes de pacientes a uma lista de suas consultas.
    """
    exibir_subtitulo('Agendamento de consultas\n')

    nome_paciente = input('Digite o nome completo do paciente: ')
    nome_medico = input('Digite o nome completo do médico: ')
    data_consulta = input('Digite a data da consulta (dd/mm/aaaa): ')
    hora_consulta = input('Digite o horário da consulta (HH:MM): ')
    especialidade = input('Digite a especialidade da consulta: ')
    convenio = input('Digite o nome do convênio ou se é particular: ')

    paciente_encontrado = any(paciente['Nome'].lower() == nome_paciente.lower() for paciente in pacientes)
    medico_encontrado = any(medico['Nome'].lower() == nome_medico.lower() for medico in medicos)

    if not paciente_encontrado:
        print(Fore.RED + '\nPaciente não encontrado.')
    elif not medico_encontrado:
        print(Fore.RED + 'Médico não encontrado')
    else:
        conflito = False
        for consultas in consultas_por_paciente.values():
            for consulta in consultas:
                if (consulta['Médico'].lower() == nome_medico.lower() and
                    consulta['Data'] == data_consulta and
                    consulta['Hora'] == hora_consulta):
                    conflito = True
                    break
            if conflito:
                    break
        if conflito:
            print(Fore.RED + f'\n Já existe uma consulta agendada nesse horário com esse médico')
        else:
            consulta = {
            'Médico': nome_medico,
            'Data': data_consulta,
            'Hora': hora_consulta,
            'Especialidade': especialidade,
            'Convênio': convenio
        }
        if nome_paciente in consultas_por_paciente:
            consultas_por_paciente[nome_paciente].append(consulta)
        else:
            consultas_por_paciente[nome_paciente] = [consulta]
        
            print(Fore.GREEN + f'\nConsulta agendada com sucesso para {nome_paciente} com {nome_medico} em {data_consulta} ás {hora_consulta}.')

    input('\nPressione ENTER para retornar ao menu...')

exames_por_paciente = {}
def agendar_exames():
    """Agenda um novo exame para um paciente.

    Solicita ao usuário o nome do paciente e os detalhes do exame. Verifica
    se o paciente e o tipo de exame estão cadastrados e se não há conflito
    de horário para o mesmo tipo de exame. Se tudo estiver correto, o exame
    é adicionado ao dicionário `exames_por_paciente`, que mapeia nomes de
    pacientes a uma lista de seus exames agendados.
    """
    exibir_subtitulo('Agendamento de exames\n')

    nome_paciente = input('Digite o nome completo do paciente: ')
    nome_exame = input('Digite o nome do exame: ')
    codigo_exame = input('Digite o código do exame: ')
    data_exame = input('Digite a data do exame (dd/mm/aaaa): ')
    hora_exame = input('Digite a hora do exame (HH:MM): ')
    convenio = input('Digite o nome do convênio ou se é particular: ')

    paciente_encontrado = any(paciente['Nome'].lower() == nome_paciente.lower() for paciente in pacientes)
    exame_encontrado = any(exame['Nome'].lower() == nome_exame.lower() for exame in exames)

    if not paciente_encontrado:
        print(Fore.RED + '\nPaciente não encontrado.')
    elif not exame_encontrado:
        print(Fore.RED + '\nExame não encontrado.')
    else:
        conflito = False
        for exames_agendados in exames_por_paciente.values():
            for exame in exames_agendados:
                if (exame['Exame'].lower() == nome_exame.lower() and
                    exame['Data'] == data_exame and
                    exame['Hora'] == hora_exame):
                    conflito = True
                    break
            if conflito:
                break

        if conflito:
            print(Fore.RED + '\nJá existe o mesmo exame marcado para o horário escolhido.')
        else:
            exame = {
                'Exame': nome_exame,
                'Código': codigo_exame,
                'Data': data_exame,
                'Hora': hora_exame,
                'Convênio': convenio
            }

            if nome_paciente in exames_por_paciente:
                exames_por_paciente[nome_paciente].append(exame)
            else:
                exames_por_paciente[nome_paciente] = [exame]

            print(Fore.GREEN + f'\nExame agendado com sucesso para {nome_paciente} em {data_exame} às {hora_exame}.')

    input('\nPressione ENTER para retornar ao menu...')


def lista_pacientes_cadastrados():
    """Exibe uma lista detalhada de todos os pacientes cadastrados.
    
    A função percorre a lista global `pacientes`. Se a lista estiver vazia,
    exibe uma mensagem informativa. Caso contrário, itera sobre a lista e
    imprime os dados de cada paciente de forma organizada.
    """

    exibir_subtitulo('Lista de pacientes cadastrados')
    if not pacientes:
        print(Fore.RED + 'Não há pacientes cadastrados no momento')
        input('\nPressione ENTER para retornar ao menu...')
    else:
        for i, paciente in enumerate(pacientes, start=1):
            print(f"\nPaciente {i}:")
            for chave, valor in paciente.items():
                print(f"  {chave}: {valor}")

        input('\nPressione ENTER para retornar ao menu...')

def opcao_invalida():
    """Informa ao usuário que a opção escolhida é inválida e aguarda
    que ele pressione ENTER para retornar ao menu principal.
    """

    print(Fore.YELLOW + 'Opção inválida. Tente novamente')
    input('Digite ENTER para retornar ao menu')

def historico_paciente():
    """Busca um paciente pelo nome e exibe seu histórico completo.

    Solicita o nome de um paciente e, se encontrado na lista `pacientes`,
    exibe seus dados pessoais, consultas e exames agendados.
    """
    exibir_subtitulo('Histórico de pacientes\n')
    nome_buscado = input('Digite o nome completo do paciente: ')

    encontrado = False
    for paciente in pacientes:
        if paciente ['Nome'].lower() == nome_buscado.lower():
            print(Fore.LIGHTYELLOW_EX + '\nDados pessoais:')
            for chave, valor in paciente.items():
                print(f'{chave}: {valor}')
            encontrado = True

            print(Fore.LIGHTYELLOW_EX +'\nConsultas marcadas:')
            if nome_buscado in consultas_por_paciente:
                for consulta in consultas_por_paciente[nome_buscado]:
                    print(f"- {consulta['Data']} às {consulta['Hora']} com {consulta['Médico']} ({consulta['Especialidade']} {consulta['Convênio']})")
            else:
                print('Nenhuma consulta marcada.')
            
            print(Fore.LIGHTYELLOW_EX +'\nExames marcados:')
            if nome_buscado in exames_por_paciente:
                for exame in exames_por_paciente[nome_buscado]:
                    print(f"- {exame['Data']} às {exame['Hora']} - {exame['Exame']} ({exame['Convênio']})")
            else:
                print('Nenhum exame marcado.')
            break

    if not encontrado:
        print(Fore.RED +'\nPaciente não encontrado.')
    
    input('\nPressione ENTER para retornar ao menu...')

def relatorios_estatisticas():
    """Exibe estatísticas gerais sobre os pacientes cadastrados.

    Calcula e exibe o número total de pacientes, a idade média, e identifica
    o paciente mais novo e o mais velho. Lida com casos onde não há
    pacientes ou onde as idades são inválidas.
    """
    exibir_subtitulo('Estatísticas dos pacientes\n')

    total_pacientes = len(pacientes)

    if total_pacientes == 0:
        print(Fore.RED +'Nenhum paciente cadastrado')
        input('\nPressione ENTER para retornar ao menu...')
    
    idades = []
    for paciente in pacientes:
        try:
            idade = int(paciente['Idade'])
            idades.append((paciente['Nome'], idade))
        except ValueError:
            print(Fore.RED + f'Idade invalida para o paciente {paciente['Nome']}')
            continue
    
    if not idades:
        print(Fore.RED + 'Não foi possível calcular as estatísticas. Todas as idades são inválidas')
        input('\nPressione ENTER para retornar ao menu...')
    
    soma_idades = sum(idade for _, idade in idades) #aqui o underline é usado para ignorar o nome e selecionar apenas a idade na tupla
    idade_media = soma_idades / len(idades)
    paciente_mais_novo = min(idades, key=lambda x: x[1])
    paciente_mais_velho = max(idades, key=lambda x: x[1])

    print(f"- Total de pacientes cadastrados: {total_pacientes}")
    print(f"- Idade média: {idade_media:.2f} anos")
    print(f"- Paciente mais novo: {paciente_mais_novo[0]} ({paciente_mais_novo[1]} anos)") # 0= Nome, 1= idade
    print(f"- Paciente mais velho: {paciente_mais_velho[0]} ({paciente_mais_velho[1]} anos)")
    input('\nPressione ENTER para retornar ao menu...')




def escolher_opcao():
    """Solicita ao usuário que escolha uma opção do menu e chama a função
    correspondente.

    Retorna:
        bool: Retorna `False` se o usuário escolher sair (opção 9),
              e `True` para todas as outras opções, indicando que o
              loop principal deve continuar.
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_pacientes()
        
        elif opcao_escolhida == 2:
            cadastrar_medicos()
        
        elif opcao_escolhida == 3:
            cadastrar_exames()
        
        elif opcao_escolhida == 4:
            agendar_consultas()
        
        elif opcao_escolhida == 5:
            agendar_exames()
        
        elif opcao_escolhida == 6:
            historico_paciente()
        
        elif opcao_escolhida == 7:
            lista_pacientes_cadastrados()
        
        elif opcao_escolhida == 8:
            relatorios_estatisticas()
        
        elif opcao_escolhida == 9:
            finalizar_sistema()
            return False
        
        else:
            opcao_invalida()
    
    except:
        opcao_invalida()
    
    return True

def main():
    """Função principal que executa o loop do programa.

    Limpa a tela, exibe o nome da plataforma e o menu de opções a cada
    iteração. O loop continua até que a função `escolher_opcao` retorne
    `False`, indicando que o usuário escolheu sair.
    """
    
    while True:
        os.system('cls')
        exibir_nome_plataforma()
        exibir_opcoes()
        if not escolher_opcao():
            break


if __name__ == '__main__':
    main()
    