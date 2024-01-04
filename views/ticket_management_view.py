class TicketManagementView:
    @staticmethod
    def display_purchase_confirmation():
        display = """
            <html>
                <head>
                    <title>Purchase Confirmation</title>
                    <style>
                        body { font-family: 'Montserrat', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background: linear-gradient(58deg, rgba(241,99,52,1) 0%, rgba(237,46,53,1) 40%, rgba(231,45,113,1) 64%, rgba(179,43,93,1) 100%); }
                        img { width: 200px; height: auto; margin-bottom: 25px; }
                        .confirmation-container { text-align: center; }
                        .message { color: #FFFFFF; font-size: 56px; margin-bottom: 20px; font-family: 'Montserrat', sans-serif; }
                        .info { color: #FFFFFF; font-size: 36px; font-family: 'Montserrat', sans-serif; }
                    </style>
                </head>
                <body>
                    <div class="confirmation-container">
                        <img src='static/confirm.svg' alt='Logo'>
                        <div class="message">Purchase Successful!</div>
                        <div class="info">You will be redirected shortly.</div>
                    </div>
                    <script>
                        setTimeout(function() {
                            window.location.href = '/event';
                        }, 3000);  // Redirect after 3 seconds
                    </script>
                </body>
            </html>
        """
        return display
