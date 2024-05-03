import pandas as pd
import matplotlib.pyplot as plt


calificaciones = [
{"nombre": "Juan", "matematicas": 85, "ciencias": 90,
"historia": 75},
{"nombre": "María", "matematicas": 70, "ciencias": 80,
"historia": 85},
{"nombre": "Pedro", "matematicas": 95, "ciencias": 75,
"historia": 90},
{"nombre": "Ana", "matematicas": 80, "ciencias": 85, "historia":
80},
{"nombre": "Luis", "matematicas": 75, "ciencias": 70,
"historia": 95},
{"nombre": "Sofía", "matematicas": 90, "ciencias": 85,
"historia": 75},
{"nombre": "Carlos", "matematicas": 85, "ciencias": 90,
"historia": 80},
{"nombre": "Elena", "matematicas": 70, "ciencias": 75,
"historia": 85},
{"nombre": "Javier", "matematicas": 80, "ciencias": 85,
"historia": 90},
{"nombre": "Laura", "matematicas": 75, "ciencias": 70,
"historia": 95},
{"nombre": "Diego", "matematicas": 90, "ciencias": 85,
"historia": 75},
{"nombre": "Paula", "matematicas": 85, "ciencias": 90,
"historia": 80},
{"nombre": "Carmen", "matematicas": 70, "ciencias": 75,
"historia": 85}
]
alumno_mat = {}
alumno_ciencias = {}
alumno_historia = {}
mayor_mat = -999999999
mayor_ciencias = -999999999
mayor_historia = -999999999

alumnos_apro_mat = 0
alumnos_apro_ciencias = 0
alumnos_apro_historia = 0

for alumon in calificaciones:
    if(alumon["matematicas"]>mayor_mat):
        mayor_mat = alumon["matematicas"]
        alumno_mat = alumon
    if(alumon["ciencias"]>mayor_ciencias):
        mayor_ciencias = alumon["ciencias"]
        alumno_ciencias = alumon
    if(alumon["historia"]>mayor_historia):
        mayor_historia = alumon["historia"]
        alumno_historia= alumon    

    if(alumon["matematicas"]>=60):
        alumnos_apro_mat+=1
    if(alumon["ciencias"]>=60):
        alumnos_apro_ciencias+=1
    if(alumon["historia"]>=60):
       alumnos_apro_historia+=1


data_calificaciones = pd.DataFrame(calificaciones)


#PROMEDIOS DE CALIFICACIONES
promedio_mat= (data_calificaciones['matematicas'].sum())/len(data_calificaciones["matematicas"])
promedio_ciencias= (data_calificaciones['ciencias'].sum())/len(data_calificaciones["ciencias"])
promedio_historia= (data_calificaciones['historia'].sum())/len(data_calificaciones["historia"])

print('El promedio de notas de Matematica es:',promedio_mat)
print('El promedio de notas de Ciencias es:',promedio_ciencias)
print('El promedio de notas de Historia es:',promedio_historia)

# Alumnos con notas mas altas en cada materia

print(f'Nota mas alta de Matematicas, alumno {alumno_mat['nombre']}, con {alumno_mat['matematicas']} ')


print(f'Nota mas alta de Ciencias, alumno {alumno_ciencias['nombre']}, con {alumno_ciencias['ciencias']} ')

print(f'Nota mas alta de Historia, alumno {alumno_historia['nombre']}, con {alumno_historia['historia']} ')


# # #% de Aprobados en cada asignatura
cantidad_alumnos = len(calificaciones)

promedio_alumnos_mat = (alumnos_apro_mat*100)/cantidad_alumnos
print(f'El {promedio_alumnos_mat}% de los alumnos aprobo la materia de Matematicas')

promedio_alumnos_ciencias = (alumnos_apro_ciencias*100)/cantidad_alumnos
print(f'El {promedio_alumnos_ciencias}% de los alumnos aprobo la materia de ciencias')

promedio_alumnos_historia = (alumnos_apro_historia*100)/cantidad_alumnos
print(f'El {promedio_alumnos_historia}% de los alumnos aprobo la materia de historia')


# Data_Frame frecuencias
data_alumnos=[]
#Creo una lista de diccionarios  para armar el dataFrame
for alumno in calificaciones:
    promedio = (alumno['matematicas']+alumno['ciencias']+alumno['historia']) /3
    data_alumnos.append(
        {
            'nombre':alumno['nombre'],
            'promedio': promedio
        }
    )
    
#genero el DF con pandas
df_alumnos = pd.DataFrame(data_alumnos)

print(df_alumnos)


# Use el grafico este grafico porque el de barras no funciona lo dejo comentado para revision.
plt.plot(df_alumnos['nombre'], df_alumnos['promedio'])
plt.xlabel('nombre')
plt.ylabel('promedio')
plt.title('Promedio de alumnos')
plt.grid()
plt.show()

# plt.hist(df_alumnos)

# plt.show()