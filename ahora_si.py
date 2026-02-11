class BateriaAgotadaError (Exception):
    pass
class SistemaCalienteError(Exception):
    pass

class Robot:
    def __init__ (self, nombre, bateria):
        self.nombre = nombre
        self.bateria = bateria 
        
    
    def gastar_bateria (self,cantidad=20):
        if self.bateria < 20:
            raise BateriaAgotadaError ("No hay suficiente bateria.")
        self.bateria -=cantidad
 
       
       # self._bateria = 100
       # print(f"bateria recargada... bateria restante: {self._bateria}")

class Cirujano (Robot):    
    def __init__ (self, nombre, bateria, temperatura):
        super().__init__(nombre,bateria)
        self.temperatura = temperatura
      
        
    def operar(self):
        self.gastar_bateria(30)
        if self.temperatura > 40:
            raise SistemaCalienteError ("CUIDADO, sistema sobrecalentandose")
        print("operacion exitosa")
    
class Clinica:
    def __init__ (self):
      
        self.lista_robots = []
    
    def agregar_robot(self, robot): # <--- ESTE es el que te falta
        self.lista_robots.append(robot)
    
    def agregar(self, robot):
        self.lista_robots.append(robot)
 
    def revisar_robots (self):
        for robots in self.lista_robots:
            try:
              robots.operar()
            
            except BateriaAgotadaError as e:
                # 2. Si falla por batería, lo arreglás acá
                print(f"Clínica: {e}. Cargando a {robots.nombre}...")
                robots.bateria = 100
            except SistemaCalienteError as e:
                # 3. Si falla por calor, lo arreglás acá
                print(f"Clínica: {e}. Enfriando a {robots.nombre}...")
                robots.temperatura = 20



# Robot 1: Sin batería (tiene 10, pero operar consume 30)
r1 = Cirujano("Dr. Hierro", bateria=10, temperatura=25)

# Robot 2: Muy caliente (70 grados, el límite es 40)
r2 = Cirujano("Dra. Tuerca", bateria=100, temperatura=70)

# Robot 3: El único que anda bien
r3 = Cirujano("RoboCop", bateria=100, temperatura=20)

mi_hospital = Clinica() # Se crea vacío
mi_hospital.agregar_robot(r1)
mi_hospital.agregar_robot(r2)
mi_hospital.agregar_robot(r3)

mi_hospital.revisar_robots()