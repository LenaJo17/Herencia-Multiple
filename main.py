from classEmpleado import Empleado
from classDepartamento import Departamento
from classArea import Area
from classDirector import Director
from classGerente import Gerente
from classJefeArea import JefeArea

def main():
    # Crear instancias de las clases
    empleado = Empleado()
    empleado.set_nombre("Julieta")
    empleado.set_apellido("Venegas")
    empleado.set_edad(20)
    empleado.set_empleado_id("453278")
    empleado.set_puesto("Secretaria")
    empleado.set_salario(4500)

    departamento = Departamento()
    departamento.set_numero_departamento(7)
    departamento.set_ubicacion("Piso 6")

    area = Area()
    area.set_objetivo_area("Expansion")
    area.set_lider_area("Juan")
    area.set_numero_empleados_area(52)

    director = Director()
    director.set_cargo("Director General")
    director.set_unidad_responsable("Ventas")
    director.set_estrategia("Aprender nuevas habilidades")

    gerente = Gerente()
    gerente.set_codigo_gerente(6032)
    gerente.set_departamentos_a_cargos("Marketing")
    gerente.set_años_de_experiencia(10)

    jefearea = JefeArea()
    jefearea.set_proyectos_asignados(7)
    jefearea.set_puesto("Jefe de Área")
    jefearea.set_direccion("Central")

    # Mostrar la información
    print("Empleado")
    print(empleado.mostrar_informacion())

    print("Departamento")
    print(departamento.mostrar_informacion())

    print("Area")
    print(area.mostrar_informacion())

    print("Director:")
    print(director.mostrar_informacion())

    print("Gerente:")
    print(gerente.mostrar_informacion())

    print("Jefe de Área:")
    print(jefearea.mostrar_informacion())

if __name__ == "__main__":
    main()




