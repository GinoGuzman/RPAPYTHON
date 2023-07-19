from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime
import os

def consolidate_txt_files(txt_folder):
   
        consolidated_data = []
        for filename in os.listdir(txt_folder):
            if filename.endswith(".txt"):
                with open(os.path.join(txt_folder, filename), "r") as file:
                    data = file.readlines()
                    name = data[0].strip().split(": ")[1]
                    position = data[1].strip().split(": ")[1]
                    salary = float(data[2].strip().split(": ")[1].split()[1])
                    period = data[3].strip().split(": ")[1]
                    days_worked = int(data[4].strip().split(": ")[1])
           
                    if len(data[5].strip().split(": ")) > 1:
                        days_not_worked = data[5].strip().split(": ")[1].strip()
                    else:
                        days_not_worked ="0"
                    
              
                    consolidated_data.append([name, position, salary, period, days_worked, days_not_worked])
                   
        if len(consolidated_data)>0:
             return consolidated_data

        else:
            raise ValueError("No existen txt para procesar.")
                  



def generate_pdf(consolidated_data, pdf_filename,):
    

        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

        elements = []
        table_data = [
            ["Nombre y Apellidos", "Cargo", "Sueldo", "Mes", "Días Trabajados", "Días No trabajados"]
        ] + consolidated_data

        table = Table(table_data)
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), '#a7c6db'),
            ('TEXTCOLOR', (0, 0), (-1, 0), '#000000'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), '#e8f6fc'),
            ('GRID', (0, 0), (-1, -1), 1, '#000000')
        ])
        table.setStyle(style)

        elements.append(table)

        doc.build(elements)
        messagebox.showinfo("PDF exitoso", "Se genero el pdf en la ruta: " + pdf_filename)

    


def send_email(sender_email, sender_password, receiver_email, subject, body, file_path):
    
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Leer el contenido del archivo PDF y adjuntarlo al correo electrónico
        with open(file_path, "rb") as attachment:
            pdf_data = attachment.read()

        attachment_part = MIMEApplication(pdf_data, _subtype="pdf")
        attachment_part.add_header('content-disposition', f'attachment; filename="{os.path.basename(file_path)}"')
        msg.attach(attachment_part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        messagebox.showinfo("Envío exitoso", "El correo electrónico se ha enviado correctamente. Proceso Terminad.")

      

def get_email_credentials():
    
            def send_email_click():
                try:
                    sender_email = sender_email_entry.get()
                    sender_password = sender_password_entry.get()
                    receiver_email = receiver_email_entry.get()

                    if sender_email == "" or sender_password == "" or receiver_email == "":
                        messagebox.showwarning("Advertencia", "Por favor, ingresa todos los campos.")
                    else:
                        windowEmail.destroy()
                        txt_folder = get_txt_folder()

                        if not txt_folder:
                            messagebox.showerror("Error", "Debes seleccionar una carpeta válida.")
                        else:
                   
                            pdf_filename = "consolidado_boletas.pdf"
                            current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                            pdf_filename_with_date = f"{current_date}_{pdf_filename}"

                    
                            ruta_pdf = os.path.join(txt_folder, pdf_filename_with_date)
                            consolidated_data = consolidate_txt_files(txt_folder)
                            generate_pdf(consolidated_data,ruta_pdf)

        
                            subject = "Consolidado de boletas de pago" + current_date
                            body = "Adjuntamos el consolidado de boletas de pago. Saludos."

                            send_email(sender_email, sender_password, receiver_email, subject, body, ruta_pdf)
                except Exception as e:
                    messagebox.showerror("Error",f"Se esta presentando el siguiente probleama. - {e}")
                    

            windowEmail = tk.Tk()
            windowEmail.title("Ingresar datos de Email.")

            sender_email_label = tk.Label(windowEmail, text="Email remitente:")
            sender_email_label.pack()
            sender_email_entry = tk.Entry(windowEmail)
            sender_email_entry.pack()

            sender_password_label = tk.Label(windowEmail, text="Contraseña deEmail remitente:")
            sender_password_label.pack()
            sender_password_entry = tk.Entry(windowEmail, show="*")
            sender_password_entry.pack()

            receiver_email_label = tk.Label(windowEmail, text="Email destinatario:")
            receiver_email_label.pack()
            receiver_email_entry = tk.Entry(windowEmail)
            receiver_email_entry.pack()

            send_button = tk.Button(windowEmail, text="Continuar", command=send_email_click)
            send_button.pack()

            windowEmail.mainloop()


        

def get_txt_folder():
    windowstxt = tk.Tk()
    windowstxt.withdraw()

    txt_folder = filedialog.askdirectory(title="Seleccionar carpeta con archivos .txt")
    windowstxt.destroy()
    return txt_folder


if __name__ == "__main__":
    try:
        get_email_credentials()
         
    except Exception as e:  
        messagebox.showerror("Error",f"Se estan presentando el sigueinte problema en el main: {e}")
  
    
    
       
        
 