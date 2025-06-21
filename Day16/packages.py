# python packages - are created by the users
# from PyPI - Python Package Index

from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Carmander", "Fire"],
    ]
)

table.align = "l"  # Left align the column names
print(table)