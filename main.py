import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from CodeEditor import QCodeEditor
from ScrollLabel import ScrollLabel
from Compiler import Compiler

class MainWindow(qtw.QWidget):

    def __init__(self, file):
        super().__init__()

        self.errors = []
        self.currentFile = file

        # text_edit = qtw.QPlainTextEdit()
        self.text=open(file).read()
        # text_edit.setPlainText(text)

        # Title
        self.setWindowTitle("Proyecto 01")

        self.setFixedWidth(1400)
        self.setFixedHeight(900)

        # Vertical Layout
        self.setLayout(qtw.QVBoxLayout())

        # Label
        self.label_1 = qtw.QLabel(file, self)

        self.layout().addWidget(self.label_1)

        # Spin Box
        self.my_textFile =  qtw.QTextEdit(self
        )
        self.my_textFile.resize(1380, 30)
        self.my_textFile.move(10, 0)

        self.my_textFile.setPlainText(file)

        # Button
        self.my_buttonFile = qtw.QPushButton("Abrir archivo", clicked = lambda: abrirArchivo())
        
        self.layout().addWidget(self.my_buttonFile)
        
        codeEditor = QCodeEditor()
        
        codeEditor.setPlainText(self.text)
        
        self.layout().addWidget(codeEditor)
        
        # Button
        self.my_button = qtw.QPushButton("Compilar", clicked = lambda: compilar())
        
        self.layout().addWidget(self.my_button)

        # Consola
        
        # Creating Scroll Label
        label_2 = ScrollLabel()
        
        # setting text to the label
        label_2.setText("Consola\n\n\n\n\n\n\n\n\n\n\n")

        f = label_2.font()
        label_2.setFont(f)

        # Add label to layout
        self.layout().addWidget(label_2)

        # Label
        f.setPointSize(13)
        self.label_1.setFont(f)
        self.my_textFile.setFont(f)
        self.my_buttonFile.setFont(f)
        self.my_button.setFont(f)

        def compilar():
            f = open(self.currentFile, "w")
            f.write(codeEditor.toPlainText())
            f.close()
            compiler = Compiler()
            compiler.compile(self.currentFile, codeEditor.toPlainText())
            errorText = '''Consola\n
            '''
            for i in compiler.errors:
                errorText += i + '\n'
            label_2.setText(errorText)

            # ! TODO: APPEND STRING OF INTERMEDIATE CODE IF ANY, OTHERWISE WILL BE NONE
            # String of intermediate code
            i_code = None

            # Si hay codigo intermedio
            if i_code:
                # Create new window
                self.i_code_window = SecondaryWindow(i_code)
                
                self.i_code_window.show()

        def abrirArchivo():
            self.text=open(self.my_textFile.toPlainText()).read()
            codeEditor.setPlainText(self.text)
            self.currentFile = self.my_textFile.toPlainText()
        
        self.show()

class SecondaryWindow(qtw.QWidget):
    def __init__(self, i_code):
        super().__init__()

        # Vertical Layout
        self.setLayout(qtw.QVBoxLayout())

        self.setFixedWidth(700)
        self.setFixedHeight(450)

        # Label
        self.label_1 = qtw.QLabel("Codigo Intermedio", self)

        self.layout().addWidget(self.label_1)

        # Title
        self.setWindowTitle("Codigo Intermedio")

        # Title
        print(i_code)

        # i_code
        label = ScrollLabel()

        # setting text to the label
        label.setText("Pruebaaasss\n\n\n\n\n\n\n\n\n\n\n")

        f = label.font()
        label.setFont(f)

        # Add label to layout
        self.layout().addWidget(label)

        

app = qtw.QApplication([])
mw = MainWindow('test2.cl')

# run
app.exec_()