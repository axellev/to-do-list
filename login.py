
def check_username_and_password(username, password):
    Okusername = "Axelle"
    Okpsw= "dada"
    if username == Okusername and password == Okpsw:
        return True
    else:
        return False

if __name__ == "__main__":
    username = input("Enter your username: ")
    psw = input("Enter your password: ")
    if check_username_and_password(username, psw):
        print("Ok")
    else:
        print("Username or password incorrect")

    assert check_username_and_password('a', 'a') == False
    assert check_username_and_password('Axelle', 'a') == False
    assert check_username_and_password('Axelle', 'dada')
    assert check_username_and_password('a', 'dada') == False