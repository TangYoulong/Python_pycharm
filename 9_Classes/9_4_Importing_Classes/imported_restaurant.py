import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #当前程序上上一级目录，这里为mycompany
sys.path.append(BASE_DIR) #添加环境变量

from Creating_and_using_a_class.restaurant import Restaurant
Restaurant_1 = Restaurant('Hai_Di_Lao','hot_pot')
Restaurant_1.describe_restaurant()

