from tkinter import *
from tkinter import  messagebox
import  base64
import os





class MEAD_APP:
    def __init__(self,root):
        self.root=root
        self.root.iconbitmap('images/ENCR-ICON.ico')
        Label(self.root,text='Enter Text For Encryption And Decryption',
              bg='#f4f4f4',fg='#018',font=('Arial',18,'bold')).place(x=10,y=25)


        self.txt_area=Text(self.root,bd=2,relief='ridge',font=('Arial',13,'bold'),width=64,height=10)
        self.txt_area.place(x=10,y=75)

        # input pass
        Label(self.root, text='Enter Secret Key For Encrypt And Decrypt',
              bg='#f4f4f4', fg='#018', font=('Arial', 18, 'bold')).place(x=10, y=290)
        self.input_pas=Entry(self.root,show='*',bd=2,relief='ridge',font=('Arial',25,'bold'),width=32)
        self.input_pas.place(x=10,y=340)

        # btbns
        Button(self.root,text='Encrypt',bg='#ed3833',fg='white',
               width=20,height='2',bd=0,font=('aria',16,'bold'),command=self.encrypt).place(x=10,y=395)

        Button(self.root, text='Decrypt', bg='#00bd56', fg='white',
               width=20, height='2', bd=0,command=self.decrypt, font=('aria', 16, 'bold')).place(x=300, y=395)

        self.lb_btn=Label(self.root, cursor='hand2',bg='#1089ff', fg='white',
               width=90, height='3', bd=0, )
        self.lb_btn.place(x=0, y=480)
        Button(self.lb_btn,command=self.reset,text='Reset',bg='#1089ff',fg='white',font=('aria', 16, 'bold'),
               bd=0,justify=CENTER,activebackground='#1089ff').place(x=260,y=5)

        self.lb = Label(self.root, text='POWERED BY : ENG-CJ',font=('aria', 14),cursor='hand2', bg='#f4f4f4', fg='#858585',
                             bd=0, ).place(x=180,y=560)

    # encry
    def encrypt(self):
        self.validate_encrypt(self.input_pas.get())

    def decrypt(self):
        self.validate_decrypt(self.input_pas.get())

    # valid
    def validate_encrypt(self,inputPasscode):
        self.inputPasscode=inputPasscode
        if self.inputPasscode=='':
            messagebox.showerror('Err','Plz Provide The Secret Key')
        elif inputPasscode!='@just':
            messagebox.showerror('ERROR','Invalid Key')
        else:
            self.encrypt_screen()

    # valid
    def validate_decrypt(self, inputPasscode):
        self.inputPasscode = inputPasscode
        if self.inputPasscode == '':
            messagebox.showerror('Err', 'Plz Provide The Secret Key')
        elif inputPasscode != '@just':
            messagebox.showerror('ERROR', 'Invalid Key')
        else:
            self.decrypt_screen()

    def encrypt_screen(self):
        screen=Toplevel()
        screen.iconbitmap('images/ENCR-ICON.ico')
        screen.geometry('520x330')
        screen.focus_force()
        screen.resizable(0,0)
        screen.title('ENCRYPTION SCREEN')
        screen.config(bg='#520027')

        Label(screen,text='ECRYPTION BOARD',bg='#520027',fg='white',
              font=('Verdana',18,'bold')).place(x=10,y=15)
        self.text_encry = Text(screen,wrap=WORD, bd=2, relief='groove', font=('Arial', 13, 'bold'), width=55, height=10)
        self.text_encry.place(x=10, y=70)

        # message encode
        message=self.txt_area.get('1.0',END)
        encode_message=message.encode('ascii')
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode('ascii')

        self.text_encry.insert(END,encrypt)



    def decrypt_screen(self):
        screen = Toplevel()
        screen.geometry('520x330')
        screen.focus_force()
        screen.iconbitmap('images/dec-icon.ico')
        screen.resizable(0, 0)
        screen.title('ENCRYPTION SCREEN')
        screen.config(bg='#0a3820')

        Label(screen, text='DECRYPTION BOARD', bg='#0a3820', fg='white',
              font=('Verdana', 18, 'bold')).place(x=10, y=15)
        self.text_decry= Text(screen, wrap=WORD, bd=2, relief='groove', font=('Arial', 13, 'bold'), width=55,
                               height=10)
        self.text_decry.place(x=10, y=70)

        # message encode
        message = self.txt_area.get('1.0', END)
        decode_message = message.encode('ascii')
        base64_bytes = base64.b64decode(decode_message)
        decrpt = base64_bytes.decode('ascii')

        self.text_decry.insert(END, decrpt)


    def reset(self):
        self.txt_area.delete('1.0',END)
        self.input_pas.delete(0,END)
        self.txt_area.focus()


if __name__=='__main__':
    rot=Tk()
    app=MEAD_APP(rot)
    rot.title('Message Encrypt And Decrypt App')
    rot.config(bg='#f4f4f4')
    rot.geometry('600x630+0+0')
    rot.resizable(0,0)
    rot.mainloop()
