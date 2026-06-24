def main():
    camel=input("Write your camelCase sentence:")
    snake=convert(camel)
    print(snake)

def convert(camel_str):
    snake_str=""
    for str in camel_str:
        if str.isupper():
            snake_str+="_"+str.lower()
        else:
            snake_str+=str
    return snake_str

main()
