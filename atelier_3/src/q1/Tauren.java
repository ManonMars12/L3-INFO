package q1;


public class Tauren extends Personnage {
	
	private int taille; 
	
	public Tauren(String nom, int age, int taille) {
		super(nom, age); 
		this.taille=taille; 
	}
	
	public int positionSouhaitee(){
		int ajout= (int)((Math.random() * taille) + 1);
		return(this.getPosition() +  ajout);
	}
	
	public String toString() {
		return("Tauren " + super.toString()); 
	}

}
