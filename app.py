import PySimpleGUI as sg


#criando o layout
def  criar_nova_tarefa():
    sg.theme('DarkBlue4')
    linha = [
             [sg.Checkbox(''),sg.Input('')]
    ] 
    layout = [
      [sg.Frame('Tarefas',layout=linha,key='container')],
      [sg.Button('Nova Tarefa'),sg.Button('Resetar')]
    ]            
    return sg.Window('Todo List',layout=layout,finalize=True)

#criando a janela
janela = criar_nova_tarefa()
while True:
  event, values = janela.read()
  if event == sg.WIN_CLOSED:
      break
  
  if event=='Nova Tarefa':
      janela.extend_layout(janela['container'], [[sg.Checkbox(''),sg.Input('')]])
      
  elif event== 'Resetar':
      janela.close()
      janela=criar_nova_tarefa()