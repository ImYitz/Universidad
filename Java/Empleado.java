public class Empleado {

    String cedula, nombre;
    int salario;

    //Constructor vacío
    public Empleado(){

    }
    // Constructor con parámetros
    public Empleado(String pNombre) {
        nombre = pNombre;
    }
    public Empleado(String pCedula, String pNombre, int pSalario) {
        cedula = pCedula;
        nombre = pNombre;
        salario = pSalario;
    }
    public String getCedula() {
        return cedula;
    }
    public String getNombre() {
        return nombre;
    }
    public int getSalario() {
        return salario;
    }
    public void setCedula(String cedula) {
        this.cedula = cedula;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public void setSalario(int salario) {
        this.salario = salario;
    }
    public int duplicarSalario(int pSalario){
        return pSalario * 2;
    }
    public Double calcularAumentoSalario(){
        return salario * 0.05;
    }
    public Double calcularAporteEps(){
        return (salario + calcularAumentoSalario()) * 0.07;
    }
    public Double mostrarSalarioNeto(){
        return salario + calcularAumentoSalario() - calcularAporteEps();
    }
}