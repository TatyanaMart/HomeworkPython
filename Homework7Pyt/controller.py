import model1 as new
import model2 as show
import model3 as search
import model4 as html
import view

value = None

def call_menu():
    view.print_menu()

def init_value():
    global value
    value = view.get_value()

def user_action():
    global value
    while value != '0':
        match value:
            case '1':
                new.new_entry(view.get_new_entry())
                view.done_message()
            case '2':
                view.print_module(search.search_name(view.get_name_search()))
            case '3':
                view.print_module(show.show_phonebook())
                view.done_message()
            case '4':
                html.create_html()
                view.done_message()
            case _: view.error_message()
        call_menu()
        init_value()