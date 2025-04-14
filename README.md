Antes de empezar a modificar el proyecto
`git pull`
Cada uno va estar designado a hacer cierta parte del código.
#### Ejemplo:
Romina-->Services
Jhonatan-->Entity
Miguel-->Repository
Leo-->Controller

Esta sujeto a cambios

#### Cada que uno acabe su parte

`git add .`
`git commit -m "lo que hiciste, claro y corto                            (de ser necesario especifico)"`
`git push origin main `


#### Comandos:
`git pull                     # Traer últimos cambios`
`git add .                    # Agregar todo lo que                                      cambiaste`
`git commit -m "mensaje"      # Guardar los cambios`
`git push                     # Subir al repo`
`git status                   # Ver en qué estás`



### Estructuras:
Estructura general de una entidad

`@Entity`  
`public class NOMBRE_DE_LA_ENTIDAD {`  
`@Id`  
`@GeneratedValue(strategy = GenerationType.IDENTITY)`  
`private Long id;`  
`}`