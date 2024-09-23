package question1;

import java.time.LocalDate;
import java.time.Month;

public class Personne {
	//Attributs ou variables d'instances
	private String nom;
	private static int init_ID=0; 
	private int ID; 
	private String prenom; 
	private LocalDate date; 
	

	/**
     * Constructeur pour créer une personne avec un nom, un âge, un prénom et une date de naissance.
     *
     * @param nom Le nom de la personne.
     * @param prenom Le prénom de la personne.
     * @param date La date de naissance de la personne.
     */
	
	
	public Personne(String nom, String prenom, LocalDate date) {
		this.nom=nom;
		this.ID=init_ID; 
		init_ID=init_ID+1;
		this.prenom=prenom;
		this.date=date;

		
	}
	
	
	 /**
     * Constructeur pour créer une personne avec un nom et un âge.
     *
     * @param nom Le nom de la personne.
     */
	//Constructeur
	public Personne(String nom) {
		this(nom,"", null);
		
	}
	
	 /**
     * Constructeur par défaut qui initialise une personne avec un nom vide.
     */
	
	public Personne() {
		this("");
	}	
	
	
	
	
	 /**
     * Définit le nom de la personne.
     *
     * @param nom Le nouveau nom de la personne.
     */
	
	public  void setNom(String nom) {
		this.nom=nom;
	}
	
	
	 /**
     * Affiche les informations de la personne (nom).
     */
	
	public void afficher() {
		System.out.println("Nom : "+this.nom);
	}
	
	 /**
     * Retourne une chaîne de caractères représentant la personne.
     *
     * @return Une représentation sous forme de chaîne de caractères du nom de la personne.
     */
	
	public String toString() {
		return this.nom;
	}
	
	/**
     * Retourne le nombre de personnes créées.
     *
     * @return Le nombre total de personnes.
     */
	
	public static int getNbPersonne() {
		return(init_ID); 
	}
	
	/**
     * Compare deux personnes pour déterminer laquelle est plus âgée.
     *
     * @param p1 La première personne à comparer.
     * @param p2 La deuxième personne à comparer.
     * @return true si la première personne est plus âgée que la seconde, sinon false.
     */
	
	public static boolean plusAgee(Personne p1, Personne p2) {
		if (p1.avoirAge() > p2.avoirAge()) {
			return(true);
		}
		else {
			return(false);
		}
		
	}
	
	 /**
     * Compare cette personne à une autre pour déterminer laquelle est plus âgée.
     *
     * @param p1 La personne à comparer.
     * @return true si cette personne est plus âgée que la personne donnée, sinon false.
     */
	
	public boolean plusAgee2(Personne p1) {
		if (this.avoirAge() > p1.avoirAge()) {
			return(true);
		}
		else {
			return(false);
		}
		
	}
	
	
	/**
	 * Calculates the age based on the current date and the birthday.
	 *
	 * @return the age in years as an integer. The calculation is based on the 
	 *         current date and the date of birth returned by {@link #getDate()}.
	 *         If the current date is before the birthday in the current year,
	 *         the age is decremented by one year.
	 */
	
	
	public int avoirAge() {
		LocalDate date_mtn = LocalDate.now();
		int annee = date_mtn.getYear();
		Month mois = date_mtn.getMonth(); 
        int jour = date_mtn.getDayOfMonth();
        
        LocalDate date_anniv=this.getDate();
        int annee_anniv = date_anniv.getYear();
        Month mois_anniv = date_anniv.getMonth(); 
        int jour_anniv = date_anniv.getDayOfMonth();
       
        if ((mois.ordinal()>=mois_anniv.ordinal())&&(jour>=jour_anniv)) {
        	return(annee-annee_anniv); 
        }
        else {
        	return(annee-annee_anniv-1);
        }
       
     

	}
	
	
	
	/**
     * Compare cette personne à une autre pour déterminer si elles sont identiques.
     *
     * @param p2 La personne à comparer.
     * @return true si les deux personnes sont identiques, sinon false.
     */
	
	public boolean equals (Personne p2){
		String nomP1 = this.getNom() ; 
		String nomP2 = p2.getNom();
		String prenomP1 = this.getPrenom();
		String prenomP2 = p2.getPrenom();
		String dateP1 = this.getDate().toString(); 
		String dateP2 = p2.getDate().toString(); 
		if ((nomP1.equals(nomP2)) && (prenomP1.equals(prenomP2)) && (dateP1.equals(dateP2))) {
			return(true);
		}
		else {
			return(false); 
			
		}
	}

	/**
     * Retourne la date de naissance de la personne.
     *
     * @return La date de naissance de la personne.
     */
    public LocalDate getDate() {
        return date;
    }

    /**
     * Définit la date de naissance de la personne.
     *
     * @param date La nouvelle date de naissance de la personne.
     */
    public void setDate(LocalDate date) {
        this.date = date;
    }

    /**
     * Retourne le nom de la personne.
     *
     * @return Le nom de la personne.
     */
    public String getNom() {
        return nom;
    }

    /**
     * Retourne le prénom de la personne.
     *
     * @return Le prénom de la personne.
     */
    public String getPrenom() {
        return prenom;
    }

  
}

