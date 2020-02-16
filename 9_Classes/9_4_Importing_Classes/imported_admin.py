import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from Inheritance.privileges1 import Admin

Admin1 = Admin('Youlong','Tang')
Admin1.privileges.show_privileges()