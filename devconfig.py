import configparser
con = configparser.ConfigParser()
con.read('dev.init')
def config(env):
    data = con.get(env,'db')
    return data
config('dev')