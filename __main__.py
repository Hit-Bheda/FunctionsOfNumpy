import numpy as np
import colorama
from colorama import Fore, Style, Back

colorama.init(autoreset=True)
color = colorama.Fore.WHITE + colorama.Style.BRIGHT + colorama.Back.BLACK

arr = np.array([[1,2,3],[4,5,6]],dtype='int')

oprations = {
    1 : {
        "title" : color + "reated The Numpy Array --> ",
        "value" : f"{arr}"
    },
    2 : {
        "title" : color + "The Dimention Of Array --> ",
        "value" : f"{arr.ndim}"  
    },
    3 : {
        "title" : color + "The Shape Of Array --> ",
        "value" : f"{arr.shape}"
    },
    4 : {
        "title" : color + "The Size Of Array --> ",
        "value" : f"{arr.size}"
    },
    5 : {
        "title" : color + "The Type Of Array --> ",
        "value" : f"{arr.dtype}"
    },
    6 : {
        "title" : color + "The Item Size Of Array --> ",
        "value" : f"{arr.itemsize}"
    },
    7 : {
        "title" : color + "The Data Type Of Array --> ",
        "value" : f"{arr.dtype}"
    },
    8 : {
        "title" : color + "The Total Bytes Of Array --> ",
        "value" : f"{arr.nbytes}"
    },
    9 : {
        "title" : color + "The Memory View Of Array --> ",
        "value" : f"{arr.data}"
    },
    10 : {
        "title" : color + "Get Specific Row --> ",
        "value" : f"{arr[1]}"
    },
    11 : {
        "title" : color + "Get Specific Column --> ",
        "value" : f"{arr[:,1]}"
    }
}

# Fuction To Impliment The Opration
def print_oprations():
    for i in oprations:
        print(oprations[i]["title"])
        print(oprations[i]["value"])

# Try Except To Avoid Runtime Errors
try:
    print_oprations()
except Exception as e:
    # To Print The Error
    print("Erro While Running :",e)