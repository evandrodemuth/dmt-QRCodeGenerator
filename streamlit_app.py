# Importar bibliotecas
import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# Função para gerar o QR Code
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    return img.convert('RGB')

# Configurar o aplicativo Streamlit
st.title("Gerador de QR Code com Streamlit")

# Entrada de dados pelo usuário
data = st.text_input("Insira o texto ou URL para gerar o QR Code:")

if st.button("Gerar QR Code"):
    if data:
        # Gerar o QR Code
        img = generate_qr_code(data)
        
        # Exibir o QR Code no aplicativo
        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.image(byte_im, caption='Seu QR Code', use_column_width=True)
        
        # Opção para baixar a imagem do QR Code
        st.download_button(
            label="Baixar QR Code",
            data=byte_im,
            file_name="qrcode.png",
            mime="image/png"
        )
    else:
        st.warning("Por favor, insira um texto ou URL para gerar o QR Code.")