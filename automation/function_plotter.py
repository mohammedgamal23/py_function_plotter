import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

class App():
    def delete_fig_agg(fig_agg):
        fig_agg.get_tk_widget().forget()
        plt.close('all')

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
        return figure_canvas_agg



    sg.theme('SystemDefault') 
    """
    ['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', ghtBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']
    """
    layout= [  [sg.Text('Enter Function Equation', size=(20, 1)), sg.InputText('6*x^2+5*x -2', key='-FUNCTION-')],
                [sg.Text('Enter Minimum value of X', size=(20, 1)), sg.InputText('-5',key='-MINIMUMX-')],
                [sg.Text('Enter Maximum value of X', size=(20, 1)), sg.InputText('11',key='-MAXIMUMX-')],
                [sg.Button('Plot'), sg.Cancel()],
                [sg.HSeparator()],
                [sg.Canvas(background_color=sg.theme_button_color()[1], size=(600,350), key='-CANVAS-')]
                
            ]


    window = sg.Window('Function Plotter', layout)

    FUNCTION_NOT_VALID_FLAG = None
    minimum = None
    maximum = None
    fig_agg = None
    while True:             
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

        if event == 'Plot':
            FUNCTION_NOT_VALID_FLAG = False
            if fig_agg is not None:
                delete_fig_agg(fig_agg)
            #validate 3 edit texts
            if (values['-FUNCTION-'] and values['-MINIMUMX-'] and values['-MAXIMUMX-']):
                # validate function is a function
                for i in values['-FUNCTION-']:
                    if i.isdigit() or i==' ' or i == 'x' or i == '+' or i == '-' or i == '*' or i == '/' or i == '^':
                        continue
                    else:
                        FUNCTION_NOT_VALID_FLAG = True
                        break

                # validate both values are numbers
                try:
                    minimum = float(values['-MINIMUMX-'])
                    maximum = float(values['-MAXIMUMX-'])
                except ValueError:
                    sg.popup_error("When I ask for a number, give me a number. Come on!")
                    continue

                
                
                if(FUNCTION_NOT_VALID_FLAG):
                    sg.popup_error('please enter a valid function. Supported operators are: + - * / ^ only')
                    continue

                if(len(values['-FUNCTION-'])* ' ' ==  values['-FUNCTION-']):
                    sg.popup_error('please enter a valid function. Supported operators are: + - * / ^ only')
                    continue
                
            else:
                # pop up an error message
                sg.popup_error('please enter all 3 values together to plot the function')
                continue
            
            #actual plotting starts here
            fig = matplotlib.figure.Figure(figsize=(5, 5), dpi=100)
            t = np.arange(minimum, maximum, .01)
            final = fig.figure.subplots()
            final.set(title="Function Representation", xlabel=r'$X$', ylabel=r'$Y$')
            try:
                final.plot(t, eval(values['-FUNCTION-'].replace('^', '**'), {'x': t}))
            except SyntaxError:
                sg.popup_error("check your function please")
                continue
            fig_agg = draw_figure(window["-CANVAS-"].TKCanvas, fig)


            

    window.close()

if __name__ == "__main__":
    App()