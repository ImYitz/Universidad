import javax.swing.JOptionPane;
import java.util.ArrayList; 

public class ProgramaBucle {

    public static void main(String[] args) {
        
        String nombre, cedula;
        int salario;
        ArrayList<Empleado> empleados = new ArrayList<>(); 

        while (true) {
            nombre = JOptionPane.showInputDialog("Ingrese el nombre del empleado (o 'none' para terminar):");
            if (nombre.equalsIgnoreCase("none")) {
                break; 
            }
            cedula = JOptionPane.showInputDialog("Ingrese la cédula del empleado:");
            salario = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el salario del empleado:"));
            Empleado emple = new Empleado(nombre, cedula, salario); 
            empleados.add(emple);
        }

        StringBuilder detalles = new StringBuilder();
        for (Empleado emple : empleados) {
            detalles.append(emple.getCedula())
                    .append(" (Cédula: ") 
                    .append(emple.getNombre()) 
                    .append(", Salario: ")
                    .append(emple.getSalario())
                    .append(")\n");
        }
        JOptionPane.showMessageDialog(null, "Empleados creados:\n" + detalles.toString());
    }
}