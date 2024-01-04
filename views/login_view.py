class LoginView:
    @staticmethod
    def display_login_form():
        # HTML and CSS for the enhanced login page
        display = """
            <style>
                body { 
                    font-family: 'Montserrat', sans-serif; 
                    display: flex; 
                    justify-content: center; 
                    align-items: center; 
                    height: 100vh; 
                    background: linear-gradient(58deg, rgba(241,99,52,1) 0%, rgba(237,46,53,1) 40%, rgba(231,45,113,1) 64%, rgba(179,43,93,1) 100%); 
                }
                .info-header { font-size: 36px; margin-bottom: 20px; font-weight: bold; color: #333; }
                .login-container { 
                    background: white; 
                    padding: 20px; 
                    border-radius: 20px; 
                    box-shadow: 0 8px 16px rgba(0,0,0,0.3); 
                    width: 450px; 
                    align-items: center; 
                    text-align: center; 
                }
                .logo img { 
                    width: 450px; 
                    height: auto; 
                }

                .form-input { 
                    margin-bottom: 20px; 
                    width: 100%; 
                    padding: 15px; 
                    border: 1px solid #ddd; 
                    font-size: 16px;
                    border-radius: 20px; 
                    box-sizing: border-box; 
                    transition: border-color 0.3s; 
                }
                .form-input:focus {
                    border-color: #007bff; 
                    outline: none; 
                }
                .login-button { 
                    width: 100%; 
                    padding: 10px; 
                    background-color: #ea2d56;
                    border: none; 
                    border-radius: 20px; 
                    font-size: 18px;
                    color: white; 
                    cursor: pointer; 
                    transition: background-color 0.3s; 
                }
                .login-button:hover { 
                    background-color: #ed2e35; 
                }
            </style>
            <div class='login-container'>
                <img src='static/logo.svg' alt='Logo'>
                <div class="info-header">Login</div>
                <form action='/login' method='post'>
                    <input type='text' name='username' class='form-input' placeholder='Username' required>
                    <input type='password' name='password' class='form-input' placeholder='Password' required>
                    <button type='submit' class='login-button'>Login</button>
                </form>
            </div>
        """
        return display
