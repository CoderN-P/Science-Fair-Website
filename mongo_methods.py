import dns
import os
import pymongo
from dotenv import load_dotenv
load_dotenv()

print(os.getenv('MONGO'))
client = pymongo.MongoClient(os.getenv('MONGO'))
registered_devices = client.main_data.registered_devices


def check_device(ip, password):
    if not registered_devices.count_documents({"_id": ip}) or not registered_devices.count_documents(
            {'Password': password}):
        return 'false'
    return 'true'


def get_device(ip, password):
    data = registered_devices.find_one({"_id": ip, "Password": password})

    return dict(data)


def check_signup(ip):
    print(ip)
    if registered_devices.count_documents({"_id": ip}):
        data = registered_devices.find_one({"_id": ip})
        if data['Password'] == None:
            return 'true'
        else:
            return 'false'
    else:
        return 'false'


def update_password(ip, password):
    registered_devices.update_one({"_id": ip}, {"$set": {'Password': password}})
