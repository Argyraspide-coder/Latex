import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc

# Constantes

R:float =100
u_R:float=1
u_V:float=1
u_i:float=1

N=10000
N_exp=10




mesures_carac_V:float=[
    0,
]

mesures_carac_i=np.array([
    0,
])
mesures_carac_i=(1/R)*mesures_carac_i

indice_zone_passante=0 # Déterminé par l'observateur à partir des données 
V_indice_zone_passante=mesures_carac_V[indice_zone_passante]

model=sc.linregress(mesures_carac_V[indice_zone_passante:],mesures_carac_i[indice_zone_passante:])

x_model=np.linspace(0,max(mesures_carac_V),N)
y_model=np.linspace(0,max(mesures_carac_V),N)
y_model=model.slope*y_model+model.intercept

print("Rf = ",model.slope,"; V0 = ",model.intercept)

for i in range(N):
    y_model[i]=max(0,y_model[i])


# Tracé de la caractéristique 

plt.figure()
plt.plot(mesures_carac_V,mesures_carac_i,label="Exp",ls="None",marker="+")
plt.plot(x_model,y_model,label="Modèle",ls="-",marker='')
plt.grid()
plt.xlabel("Tension aux bornes de la Diode (V)")
plt.ylabel("Intensité à travers la diode (A)")
plt.legend()
plt.show()

# Bonus : Monte Carlo pour déterminer l'incertitude

def gen_mesures_V():
    mes_V=np.zeros(N_exp)
    for i in range(N_exp):
        V=mesures_carac_V[i]
        mes_V[i]=V+np.random.uniform(V-u_V,V+u_V)
    return mes_V
    
def gen_mesures_i():
    mes_i=np.zeros(N_exp)
    for k in range(N_exp):
        i=mesures_carac_i[k]
        mes_i[k]=i+np.random.uniform(i-u_i,i+u_i)
    return mes_i


tab_V0=np.zeros(N)
tab_Rf=np.zeros(N)

for i in range(N):
    mes_i=gen_mesures_i()
    mes_V=gen_mesures_V()
    model=sc.linregress(mes_V[indice_zone_passante:],mes_i[indice_zone_passante:])
    tab_V0[i],tab_Rf[i]=model.intercept,model.slope

print("Rf = ",model.slope,"; V0 = ",model.intercept)






