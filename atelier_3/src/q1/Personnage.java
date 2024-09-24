package q1;

import q1.Joueur; 

public abstract class Personnage {

	private String nom;
	private int age; 
	private int position;
	private Joueur proprietaire;
	
	public Personnage(String nom, int age) {
		this.nom=nom;
		this.age=age; 
	}
	
	public void deplacer(int destination, int gain) {
		this.position=destination;
		proprietaire.modifierPoints(gain); 
	}
	
	public void penaliser(int penalite) {
		proprietaire.modifierPoints(-1*penalite);
	}
	
	public String toString() {
		return(nom);
	}
	
	public Joueur getProprietaire() {
		return proprietaire;
	}

	public void setProprietaire(Joueur proprietaire) {
		this.proprietaire = proprietaire;
	}

	public abstract int positionSouhaitee();

	public int getPosition() {
		return position;
	}

	public void setPosition(int position) {
		this.position = position;
	}

	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	} 
}
