"""
[PT]
1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.

[EN]
1. Make a program that displays the message "Hello world" on the screen. 
"""
import emoji
import emojis

def helloworld(frase: str):
    return True


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = emojis.encode(':clap:')
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(helloworld, "hello world", True)
    test(helloworld, "Ola Mundo!", True)


