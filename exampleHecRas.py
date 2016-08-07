import datetime as dt 
import time

from pyras.controllers import RAS500, RAS41, kill_ras
from pyras.controllers.hecras import ras_constants as RC

project = r'D:\PROYECTOS\Ángel Ruiz\HECRAS\samples\Patricia\tesiscinpuentenu.prj'
rc = RAS41()
rc.ShowRas()
rc.Project_Open(project)

river = 'Rio Malacatos'

#longitud
reach = '13'

rs = '15813.16'

flow = [123]
res = rc.SteadyFlow_SetFlow(river, reach, rs, flow)
print(res)
