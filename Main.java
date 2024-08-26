// import java.util.Scanner;
import javax.swing.JOptionPane;

public class Main {
    public static void main(String[] args) {

        /* 
        Scanner leer = new Scanner(System.in);

        System.out.println("Ingrese su nombre: ");
        String nombre = leer.nextLine();
        System.out.println("Ingrese su salario: ");
        final Integer salario = leer.nextInt();
        
        System.out.println(nombre + " " + salario);

        leer.close();

        */

        String usuario = JOptionPane.showInputDialog("Ingrese su nombre: ");
        JOptionPane.showMessageDialog(null, "Hola " + usuario);
    }
}
