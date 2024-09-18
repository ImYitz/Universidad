import javax.swing.JOptionPane;

public class Ejecutar {
    
    public static void main(String[] args) {
        
        Ejemplo ejem = new Ejemplo();
        
        //Necesitamos recopilar id, nombre y edad.
        String id = JOptionPane.showInputDialog("Ingrese la id del usuario: ");
        String nombre = JOptionPane.showInputDialog("Ingrese el nombre del usuario: ");
        String edad = JOptionPane.showInputDialog("Ingrese la edad del usuario: ");

        //ejem.caminar();
        //ejem.dormir();

        ejem.setId(id);
        ejem.setNombre(nombre);
        ejem.setEdad(edad);

        JOptionPane.showMessageDialog(null, ejem.getId() + "\n" + ejem.getNombre() + "\n" + ejem.getEdad(), "ID", 1);


    }

}
