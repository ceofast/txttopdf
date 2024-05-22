from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'WhatsApp Chat History', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Sayfa {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, date):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, date, 0, 1, 'L')
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_image(self, image_path):
        print(f"Trying to add image: {image_path}")  # Debugging line
        if os.path.exists(image_path):
            self.image(image_path, x=10, w=100)
            self.ln(10)
        else:
            print(f"Image not found: {image_path}")  # Debugging line
            self.set_font('Arial', 'I', 10)
            self.cell(0, 10, f'Image not found: {image_path}', 0, 1, 'L')
            self.ln(10)

def parse_whatsapp_chat(file_path, image_base_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    chats = []
    current_date = ""
    current_chat = ""

    for line in lines:
        if line.strip() == "":
            continue
        if line[0].isdigit() and '-' in line:
            if current_chat:
                chats.append((current_date, current_chat.strip()))
            parts = line.split(" - ", 1)
            if len(parts) == 2:
                current_date = parts[0]
                current_chat = parts[1]
            else:
                current_chat += " " + line.strip()
        elif "(dosya ekli)" in line:
            image_name = line.split(" ")[0].strip()
            image_path = os.path.join(image_base_path, image_name)
            print(f"Found image reference: {image_path}")  # Debugging line
            if current_chat:
                chats.append((current_date, current_chat.strip()))
                current_chat = ""
            chats.append((current_date, image_path.strip()))
        else:
            current_chat += " " + line.strip()

    if current_chat:
        chats.append((current_date, current_chat.strip()))

    return chats

def create_pdf(chat_data, output_path):
    pdf = PDF()
    pdf.add_page()
    font_path = r"C:\Windows\Fonts"
    pdf.add_font('Arial', '', os.path.join(font_path, 'arial.ttf'), uni=True)
    pdf.add_font('Arial', 'B', os.path.join(font_path, 'arialbd.ttf'), uni=True)
    pdf.add_font('Arial', 'I', os.path.join(font_path, 'ariali.ttf'), uni=True)

    for date, chat in chat_data:
        if chat.lower().endswith(('.png', '.jpg', '.jpeg')):
            pdf.chapter_title(date)
            pdf.add_image(chat)
        else:
            pdf.chapter_title(date)
            pdf.chapter_body(chat)

    pdf.output(output_path)

if __name__ == "__main__":
    input_file = r"E:\PycharmProjects\senswise\‎Emlakçı İbrahim KURTULUŞ ile WhatsApp Sohbeti.txt"
    image_base_path = r"E:\PycharmProjects\senswise"
    output_file = os.path.expanduser(r"E:\PycharmProjects\senswise\whatsapp_chat_history.pdf")

    chat_data = parse_whatsapp_chat(input_file, image_base_path)
    create_pdf(chat_data, output_file)
