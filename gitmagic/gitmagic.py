import click
import os

from gitmagic.git_clean import GitClean

@click.command()
@click.option('--verbose', is_flag=True, help='Will print verbose messages')
@click.option('--add_gitignore', is_flag=True, help='Will add default gitignore for specified language')
@click.option('--language', default='python', help='Programming language of repo')
@click.option('--max_file_size', default='100', help='Maximum file size in MB - if over, added to repo .gitignore')
def cli(verbose, add_gitignore, language, max_file_size):
    if verbose:
        click.echo("""In verbose mode""")
    if add_gitignore:
        click.echo("""adding gitignore file to root of repo""")
        click.echo("""Type of add_gitignore""".format(type(add_gitignore)))

    # get the directory in which script was called
    called_dir = os.getcwd()
    # instatiate gitclean
    click.echo("""Starting git clean""")
    GC = GitClean(called_dir=called_dir)
    GC.git_magic(add_gitignore=add_gitignore,
                 language=language,
                 max_file_size=max_file_size)