from colorama import Fore, Style

def console_log(*values: object, color=Fore.WHITE, style=Style.NORMAL, separator=' ', end='\n'):
    formatted_values = separator.join(map(str, values))
    formatted_output = f"{style}{color}{formatted_values}{Style.RESET_ALL}"
    print(formatted_output, end=end)