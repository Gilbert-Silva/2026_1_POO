package Aula_05;

class Triangulo {
    private double b = 0;
    private double h = 0;
    public Triangulo() {                        // Sobrecarga de construtor
        this.setBase(0);
        this.setAltura(0);
    }
    public Triangulo(double b, double h) {     // Sobrecarga de construtor
        this.setBase(b);
        this.setAltura(h);
    }
    public void setBase(double v) {
        if (v >= 0) this.b = v;
        else throw new IllegalArgumentException("Valor não pode ser negativo"); 
    }
    public void setAltura(double v) {
        if (v >= 0) this.h = v;
        else throw new IllegalArgumentException("Valor não pode ser negativo"); 
    }
    public double getBase() {
        return this.b;
    }
    public double getAltura() {
        return this.h;
    }
    public double calcArea() {
        return this.b * this.h / 2;
    }
    public String toString() {
        return "Triângulo com base = " + this.b + " e altura = " + this.h;
    }
}

public class ex01 {
    public static void main(String[] args) {
        Triangulo x = new Triangulo(10, 20);  // Construtor
        System.out.println(x);                     // ToString
        System.out.println(x.calcArea());
        Triangulo y = new Triangulo();
        System.out.println(y);                     // ToString
    }
}
