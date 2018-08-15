
import configparser

def create_ini(std_id,std_pw):
    config = configparser.ConfigParser()
    config['ACCOUNT'] = {
        'std_id':std_id,
        'std_pw':std_pw
    }
    with open('config.ini','w') as file:
        config.write(file)
    print("create file 'config.ini' success")
    return config