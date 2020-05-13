from cx_Freeze import setup, Executable
exe = Executable(

    script="page-accueil.py",

    base="Win32GUI",

    )

setup(
    name = "Brick-shooter",
    version = "0.1",
    description = "Jeu Brick-shooter ",
    executables = [exe]
)



 

