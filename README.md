## Inicio
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

#### Entidad

`@Entity`  
`public class NOMBRE_DE_LA_ENTIDAD {`  
`@Id`  
`@GeneratedValue(strategy = GenerationType.IDENTITY)`  
`private Long id;`  
`}`


#### Controller

`@RestController`

`@RequestMapping("/artistas")`

`public class ArtistaController {`

    @Autowired
    private ArtistaService artistaService;

    @GetMapping("/buscar")
    public Artista buscarPorUsername(@RequestParam String username) {
        return artistaService.buscarPorUsername(username);
    }

    @GetMapping
    public List<Artista> listarArtistas() {
        return artistaService.listarTodos();
    }

    @PostMapping
    public Artista crearArtista(@RequestBody Artista artista) {
        return artistaService.guardar(artista);
    }

    @PutMapping("/{id}")
    public Artista actualizar(@PathVariable Long id, @RequestBody Artista artista) {
        return artistaService.actualizar(id, artista);
    }

    // Eliminar un artista
    @DeleteMapping("/{id}")
    public void eliminar(@PathVariable Long id) {
        artistaService.eliminar(id);
    }
}



#### Services


`@Service`
`public class ArtistaService {`

    @Autowired
    private ArtistaRepository artistaRepository;

    public Artista buscarPorUsername(String username) {
        return artistaRepository.findByUsername(username)
                .orElseThrow(() -> new ArtistaNoEncontradoException("No se encontró al artista"));
    }

    public List<Artista> listarTodos() {
        return artistaRepository.findAll();
    }

    public Artista guardar(Artista artista) {
        if (artistaRepository.findByUsername(artista.getUsername()).isPresent()) {
            throw new IllegalArgumentException("El artista ya existe");
        }
        return artistaRepository.save(artista);
    }

    public Artista actualizar(Long id, Artista artista) {
        if (!artistaRepository.existsById(id)) {
            throw new ArtistaNoEncontradoException("No se encontró al artista con ID: " + id);
        }
        return artistaRepository.save(artista);
    }

    public void eliminar(Long id) {
        if (!artistaRepository.existsById(id)) {
            throw new ArtistaNoEncontradoException("No se encontró al artista con ID: " + id);
        }
        artistaRepository.deleteById(id);
    }

