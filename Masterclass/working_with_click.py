import click

@click.group()
def greet():
    pass

@greet.command()
def hello(**kwargs):
    pass

@greet.command()
def goodbye(**kwargs):
    pass

if __name__ == '__main__':
    greet()