import zipfile
from app.rule import recommend as rule_commend


def run():
    data_path = "."
    result = rule_commend(data_path)
    result.to_csv('u2i.csv', index=None)
    with zipfile.ZipFile("u2i.zip", 'w') as z:
        z.write('u2i.csv')



if __name__ == "__main__":
    run()

