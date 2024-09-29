public class Ejemplo {

    String id, nombre, edad;

    public Ejemplo (){

    }
    public Ejemplo(String id, String nombre, String edad){
        this.id = id;
        this.nombre = nombre;
        this.edad = edad;
    }
    public String getId(){
        return id;
    }
    public void setId(String id){
        this.id = id;
    }
    public String getNombre(){
        return nombre;
    }
    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    public String getEdad(){
        return edad;
    }
    public void setEdad(String edad){
        this.edad = edad;
    }
    public void caminar(){
        System.out.println("Está caminando.");
    }
    public void dormir(){
        System.out.println("Está durmiendo.");
    }
}