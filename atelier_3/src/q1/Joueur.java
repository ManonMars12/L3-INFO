package q1;

import q1.Personnage;

import java.util.ArrayList;

public class Joueur {

	private String nom; 
	private String code; 
	private static int nb_joueurs=1; 
	private int nb_points;
	private ArrayList <Personnage> liste_perso;
	
	public Joueur(String nom) {
		this.nom=nom;
		this.code=("J"+nb_joueurs);
		this.liste_perso= new ArrayList<>();
		nb_joueurs=nb_joueurs+1;
		
		
	}

	public ArrayList<Personnage> getListe_perso() {
		return liste_perso;
	}

	public void setListe_perso(ArrayList<Personnage> liste_perso) {
		this.liste_perso = liste_perso;
	}

	public void ajouterPersonnage(Personnage personnage){
	        if (personnage.getProprietaire() != null) {
	            System.out.println("Le personnage est déjà attribué");
	        } else {
	            this.liste_perso.add(personnage); 
	            personnage.setProprietaire(this); 
	        }
	    } 
		
	
	public void modifierPoints(int nb) {
		this.nb_points=nb_points + nb; 
	}
	
	public boolean peutJouer() {
		return !this.liste_perso.isEmpty();
	}
	
	public String toString() {
		if (!this.liste_perso.isEmpty()) {
			return(code + " " +nom + "(" + nb_points + "points ) avec " + " " + liste_perso.size() + " personnages");
		}
		else {
			return(code + nom + "(" + nb_points + "points ) avec aucun personnages");
		}
}

	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	}

	public String getCode() {
		return code;
	}

	public void setCode(String code) {
		this.code = code;
	}

	public int getNb_points() {
		return nb_points;
	}

	public void setNb_points(int nb_points) {
		this.nb_points = nb_points;
	}
	
}

