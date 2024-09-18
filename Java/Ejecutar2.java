import javax.swing.JOptionPane;

public class Ejecutar2 extends Ejemplo {
    
    String ciudad;
    String trabajo;

    public Ejecutar2(){

    }
    public Ejecutar2(String ciudad, String trabajo){
        this.ciudad = ciudad;
        this.trabajo = trabajo;
    }
    public String getCiudad(){
        return ciudad;
    }
    public void setCiudad(String ciudad){
        this.ciudad = ciudad;
    }
    public String getTrabajo(){
        return trabajo;
    }
    public void setTrabajo(String trabajo){
        this.trabajo = trabajo;
    }

    public static void main(String[] args) {
        
        Ejecutar2 ejecut = new Ejecutar2();
        Ejecutar2 ejecut2 = new Ejecutar2();

        String id = JOptionPane.showInputDialog("Ingrese la ID del usuario: ");
        String nombre = JOptionPane.showInputDialog("Ingrese el nombre del usuario: ");
        String edad = JOptionPane.showInputDialog("Ingrese la edad del usuario: ");
        String ciudad = JOptionPane.showInputDialog("Ingrese la ciudad del usuario: ");
        String trabajo = JOptionPane.showInputDialog("Ingrese el trabajo del usuario: ");

        ejecut.setId(id);
        ejecut.setNombre(nombre);
        ejecut.setEdad(edad);
        ejecut.setCiudad(ciudad);
        ejecut.setTrabajo(trabajo);

        System.out.println(ejecut.getCiudad());
        System.out.println(ejecut2.getCiudad());
        System.out.println(ejecut.getEdad());

    }
  
}
