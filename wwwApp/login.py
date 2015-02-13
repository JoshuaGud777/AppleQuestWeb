import library as lib

def main():
    lib.print_header()
    form = lib.get_cgi_data()
    if form.getvalue('key') == 'send_login':
        lib.print_me(lib.DIR_REDIRECT + 'to_game.html')
    else:
        lib.print_me(lib.HTML_DIR + 'login0.html')
        lib.print_me(lib.HTML_DIR + 'login1.html')
        lib.get_cookies()
    print(form)
    
if __name__ == '__main__':
    main()
