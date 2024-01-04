class QRView:
    @staticmethod
    def display_qr(qr_path):
        display = f"""
            <style>
                body {{ 
                    font-family: 'Montserrat', sans-serif; 
                    display: flex; 
                    justify-content: center; 
                    align-items: center; 
                    height: 100vh; 
                    background: linear-gradient(58deg, rgba(241,99,52,1) 0%, rgba(237,46,53,1) 40%, rgba(231,45,113,1) 64%, rgba(179,43,93,1) 100%); 
                }}
                .login-container {{ 
                    background: white; 
                    padding: 20px; 
                    border-radius: 20px; 
                    box-shadow: 0 8px 16px rgba(0,0,0,0.3); 
                    width: 400px; 
                    align-items: center; 
                    text-align: center; 
                }}
                .info-header {{ font-size: 36px; margin-bottom: 20px; font-weight: bold; font-family: 'Montserrat', sans-serif; }}
                .logo img {{ 
                    width: 360px; 
                    height: auto; 
                }}
            </style>
            <div class='login-container'>
                <img src='{qr_path}' alt='QR Code'>
                <div class="info-header">Scan QR Code</div>
            </div>
        """
        return display
