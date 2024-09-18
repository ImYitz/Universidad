public class Empleado {

    String cedula;
    String nombre;
    int salario;

    //Constructor vacío
    public Empleado(){

    }
    // Constructor con parámetros
    public Empleado(String pCedula, String pNombre, int pSalario) {
        cedula = pCedula;
        nombre = pNombre;
        salario = pSalario;
    }
    public String getCedula() {
        return cedula;
    }
    public void SetCedula(String pCedula){
        cedula = pCedula;
    }
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String pNombre){
        nombre = pNombre;
    }
    public int getSalario() {
        return salario;
    }
    public void setSalario(int pSalario) {
        salario = pSalario;
    }
    public int duplicarSalario(int pSalario){
        return pSalario * 2;
    }
}

