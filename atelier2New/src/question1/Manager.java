package question1;

import java.time.LocalDate;

public class Manager extends Employe {
	
	
	private Secretaire secretaire; 
	
	
	
	/**
     * Constructeur pour créer un manager avec les informations fournies.
     *
     * @param nom           Le nom du manager.
     * @param prenom        Le prénom du manager.
     * @param date          La date de naissance du manager.
     * @param salaire       Le salaire du manager.
     * @param date_embauche La date d'embauche du manager.
     * @param secretaire    La secrétaire assignée au manager.
     */
	
	
	public Manager(String nom, String prenom, LocalDate date, double salaire, LocalDate date_embauche, Secretaire secretaire) {
		super (nom,prenom, date, salaire, date_embauche);
 
		this.secretaire=secretaire;
	}

	
	  /**
     * Crée un manager avec les informations fournies si l'âge est compris entre 16 et 65 ans.
     *
     * @param nom           Le nom du manager.
     * @param prenom        Le prénom du manager.
     * @param date          La date de naissance du manager.
     * @param salaire       Le salaire du manager.
     * @param date_embauche La date d'embauche du manager.
     * @param secretaire    La secrétaire assignée au manager.
     * @return Un nouvel objet Manager si l'âge est valide, sinon null.
     */
	

	public static Manager createManager(String nom, String prenom, LocalDate date, double salaire, LocalDate date_embauche, Secretaire secretaire){
		Personne temporaire= new Personne(nom, prenom, date); 
		if ((temporaire.avoirAge()<16) || (temporaire.avoirAge()>65)) {
			return(null);
		}
		else {
			Manager e = new Manager(nom, prenom, date, salaire, date_embauche, secretaire);
			return(e);
		}
	}
	
	/**
     * Retourne la secrétaire assignée au manager.
     *
     * @return La secrétaire du manager.
     */
	
	public Secretaire getSecretaire() {
		return secretaire;
	}
	
	
	/**
     * Définit la secrétaire assignée au manager.
     *
     * @param secretaire La nouvelle secrétaire assignée au manager.
     */

	public void setSecretaire(Secretaire secretaire) {
		this.secretaire = secretaire;
	}

	
	 /**
     * Augmente le salaire du manager d'un pourcentage donné, en tenant compte de son ancienneté.
     *
     * @param pourcentage Le pourcentage d'augmentation du salaire. 
     *                   Doit être positif.
     */
    @Override
	

	public void augmenterSalaire(int pourcentage) {
		if (pourcentage<0) {
			return; 
		}
		else {
		this.setSalaire(this.getSalaire()+(this.getSalaire()*((pourcentage + (0.5*calculAnnuite()))* Math.pow(10, -2)))); /* Math.pow c'est la puissance */ 
		}
		
	}

}