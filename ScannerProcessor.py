from pyspectator.computer import Computer 
from pyspectator.processor import Cpu
from time import sleep


computer = Computer()
print(computer.processor.name)

cpu = Cpu(monitoring_latency = 1)
a = "º"
with cpu:
 
    for _ in range(100):
       re = cpu.temperature
       sleep(1.1)
       if(re <60):
            print("Processador: "+ str(re)+ str(a), "Normal")
       else:
            print("Processador: "+ str(re)+ str(a), "Toma cuidado")

        
    
