package question1;

import java.time.LocalDate;

public class Employe extends Personne{
	
	private double salaire;
	private LocalDate date_embauche; 
	
	
	 /**
     * Constructeur pour créer un employé avec les informations fournies.
     *
     * @param nom          Le nom de l'employé.
     * @param prenom       Le prénom de l'employé.
     * @param date         La date de naissance de l'employé.
     * @param salaire      Le salaire de l'employé.
     * @param date_embauche La date d'embauche de l'employé.
     */
	
	
	protected Employe(String nom, String prenom, LocalDate date, double salaire, LocalDate date_embauche) {
		super(nom, prenom, date);
		this.salaire=salaire; 
		this.date_embauche=date_embauche;
		
	}
	
	
	
	/**
     * Crée un employé avec les informations fournies si l'âge est compris entre 16 et 65 ans.
     *
     * @param nom          Le nom de l'employé.
     * @param prenom       Le prénom de l'employé.
     * @param date         La date de naissance de l'employé.
     * @param salaire      Le salaire de l'employé.
     * @param date_embauche La date d'embauche de l'employé.
     * @return Un nouvel objet Employe si l'âge est valide, sinon null.
     */
	
	
	public static Employe createEmploye(String nom, String prenom, LocalDate date, double salaire, LocalDate date_embauche){
		Personne temporaire= new Personne(nom, prenom, date); 
		if ((temporaire.avoirAge()<16) || (temporaire.avoirAge()>65)) {
			return(null);
		}
		else {
			Employe e = new Employe(nom, prenom, date, salaire, date_embauche);
			return(e);
		}
		
	}
	
	
	 /**
     * Augmente le salaire de l'employé d'un pourcentage donné.
     *
     * @param pourcentage Le pourcentage d'augmentation du salaire. 
     *                   Doit être positif.
     */
	
	public void augmenterSalaire(int pourcentage) {
		if (pourcentage<0) {
			return; 
		}
		else {
		this.salaire=salaire+(salaire*(pourcentage* Math.pow(10, -2))); /* Math.pow c'est la puissance */ 
		}
		
	}
	
	   /**
     * Retourne le salaire de l'employé.
     *
     * @return Le salaire de l'employé.
     */

	public double getSalaire() {
		return salaire;
	}

	
	/**
     * Définit le salaire de l'employé.
     *
     * @param salaire Le nouveau salaire de l'employé.
     */
	
	
	public void setSalaire(double salaire) {
		this.salaire = salaire;
	}
	
	/**
     * Retourne la date d'embauche de l'employé.
     *
     * @return La date d'embauche de l'employé.
     */
	
	public LocalDate getDateEmbauche() {
		return(date_embauche); 
	}
	
	
	/**
     * Calcule l'ancienneté de l'employé en années.
     *
     * @return Le nombre d'années depuis la date d'embauche.
     */
	
	public int calculAnnuite() {
		int annee = this.getDateEmbauche().getYear();
		LocalDate date_mtn = LocalDate.now();
	    int annee_courante =  date_mtn.getYear();
		return(annee_courante-annee+1);
	}
		
}
	
	

	


