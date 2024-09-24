package q1;

public class Humain extends Personnage{

	private int nb_deplacements; 
	private int niveau=1;
	
	public Humain(String nom, int age) {
		super(nom,age);
		this.nb_deplacements=0;
	}
	
	public void deplacer(int destination, int gain) {
		super.deplacer(destination, gain);
		nb_deplacements=nb_deplacements+1; 
		if (nb_deplacements == 4) {
			setNiveau(2); 
		}
		if (nb_deplacements == 6) {
			setNiveau(3);
		}
		
		
	}

	public int getNiveau() {
		return niveau;
	}

	public void setNiveau(int niveau) {
		this.niveau = niveau;
	}
	
	public int positionSouhaitee() {
		return(this.getPosition() + (niveau*nb_deplacements)); 
	}
	
	public String toString() {
		return("Humain " + super.toString()); 
	}
	
}
