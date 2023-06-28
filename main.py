import customtkinter
from tkinter import filedialog
import pywhatkit
import time

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.filename = ''

        # configure window
        self.title("BotSendWhats")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="BotWhats",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame,
                                                            text='Observações:\n\nAo clicar em "Iniciar Envio"\n\nnão mexer no computador!',
                                                            anchor="w")
        self.appearance_mode_label.grid(row=2, column=0, padx=20, pady=(10, 0))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Aparencia:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        # create main entry and button
        self.entry = customtkinter.CTkButton(master=self, text='Selecionar Imagem', border_width=2,
                                             command=self.selecionar_img)
        self.entry.grid(row=5, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, text='Iniciar Envio', border_width=2,
                                                     text_color=("gray10", "#DCE4EE"), command=self.iniciar_envio)
        self.main_button_1.grid(row=5, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.label_log = customtkinter.CTkLabel(self, text='')
        self.label_log.grid(row=0, column=1, padx=1, pady=1)

        self.label_number = customtkinter.CTkLabel(self, text='Numeros (separados por ",")', anchor="w")
        self.label_number.grid(row=1, column=1, padx=1, pady=1)
        self.textbox_number = customtkinter.CTkTextbox(self, width=250)
        self.textbox_number.grid(row=2, column=1, padx=(20, 0), pady=(1, 0), sticky="nsew")

        self.label_msg = customtkinter.CTkLabel(self, text="Mensagem:", anchor="w")
        self.label_msg.grid(row=3, column=1, padx=1, pady=1)
        self.textbox_msg = customtkinter.CTkTextbox(self, width=250)
        self.textbox_msg.grid(row=4, column=1, padx=(20, 0), pady=(1, 0), sticky="nsew")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def iniciar_envio(self):

        try:
            textbox_number = self.textbox_number.get("0.0", "end")
            textbox_msg = self.textbox_msg.get("0.0", "end")
            numbers = str(textbox_number)
            arr_numbers = numbers.split(',')

            for number in arr_numbers:
                time.sleep(3)
                if self.filename is None or self.filename == '':
                    pywhatkit.sendwhatmsg_instantly("+55" + str(number), str(textbox_msg))
                else:
                    pywhatkit.sendwhats_image("+55" + str(number), self.filename, str(textbox_msg))

            self.setValoresDefault()

        except Exception as e:
            self.label_log.configure(text='Ocorreu um erro', fg_color="red")

    def selecionar_img(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.filename = filename
            self.entry.configure(text=filename)

    def setValoresDefault(self):
        self.entry.configure(text='Selecionar Imagem')
        self.textbox_number.delete("0.0", "end")
        self.textbox_msg.delete("0.0", "end")
        self.label_log.configure(text='Mensagens enviadas com sucesso!', fg_color="green")


if __name__ == "__main__":
    app = App()
    app.mainloop()
