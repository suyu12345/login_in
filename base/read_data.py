import yaml,os


def read_data(file_name):
    with open("./data"+os.sep+file_name, "r",encoding="utf-8") as f:
        data_disc = yaml.load(f)
        return data_disc
