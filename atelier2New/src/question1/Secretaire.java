package question1;

import java.time.LocalDate;

public class Secretaire extends Employe{
	
	private Manager[] Manager;
	private final int NBMAXMANAGER=5;
	private int nb_manager=0; 
	

	
	
	/**
     * Constructeur pour créer une secrétaire avec les informations fournies.
     *
     * @param nom           Le nom de la secrétaire.
     * @param prenom        Le prénom de la secrétaire.
     * @param date          La date de naissance de la secrétaire.
     * @param salaire       Le salaire de la secrétaire.
     * @param date_embauche La date d'embauche de la secrétaire.
     */
	public Secretaire (String nom, String prenom, LocalDate date, double salaire, LocalDate date_embauche) {
		super (nom,prenom, date, salaire, date_embauche);
		Manager = new Manager[NBMAXMANAGER];
		
	}


    /**
     * Ajoute un manager à la liste des managers gérés par la secrétaire.
     *
     * @param manager Le manager à ajouter.
     */
	
	public void ajouterManager(Manager manager) {
        if (nb_manager < NBMAXMANAGER) {
            Manager[nb_manager] = manager;
            nb_manager=nb_manager+1;
        }
        else {
        	System.out.println("Impossible trop de managers ");
        }
	}
	

    /**
     * Supprime un manager de la liste des managers gérés par la secrétaire.
     *
     * @param manager     Le manager à supprimer.
     * @param numero_a_supp L'index du manager à supprimer dans le tableau.
     */
	
	public void supprimerManager(Manager manager, int numero_a_supp) {
        if (nb_manager > 0) {
            Manager[numero_a_supp] = null ;
            nb_manager=nb_manager-1;
        }
        else {
        	System.out.println("Impossible pas assez de managers ");
        }
	}
	
	
	 /**
     * Retourne la liste des managers gérés par la secrétaire.
     *
     * @return Le tableau de managers.
     */
	
	public Manager[] getManager() {
		return Manager;
	}
	
	
	/**
     * Définit la liste des managers gérés par la secrétaire.
     *
     * @param manager Le tableau de managers à définir.
     */
	

	public void setManager(Manager[] manager) {
		Manager = manager;
	}

	
	 /**
     * Retourne le nombre de managers gérés par la secrétaire.
     *
     * @return Le nombre de managers.
     */
	
	public int getNb_manager() {
		return nb_manager;
	}
	
	
	 /**
     * Définit le nombre de managers gérés par la secrétaire.
     *
     * @param nb_manager Le nouveau nombre de managers.
     */
	
	public void setNb_manager(int nb_manager) {
		this.nb_manager = nb_manager;
	}

	
	 /**
     * Augmente le salaire de la secrétaire d'un pourcentage donné,
     * en tenant compte du nombre de managers gérés.
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
		this.setSalaire(this.getSalaire()+(this.getSalaire()*((pourcentage + (0.1*nb_manager))* Math.pow(10, -2)))); /* Math.pow c'est la puissance */ 
		}
		
	}
	
    /**
     * Crée une secrétaire avec les informations fournies si l'âge est compris entre 16 et 65 ans.
     *
     * @param nom           Le nom de la secrétaire.
     * @param prenom        Le prénom de la secrétaire.
     * @param date          La date de naissance de la secrétaire.
     * @param salaire       Le salaire de la secrétaire.
     * @param date_embauche La date d'embauche de la secrétaire.
     * @return Un nouvel objet Secretaire si l'âge est valide, sinon null.
     */
	public static Secretaire createSecretaire(String nom, String prenom, LocalDate date, double salaire, LocalDate date_embauche){
		Personne temporaire= new Personne(nom, prenom, date); 
		if ((temporaire.avoirAge()<16) || (temporaire.avoirAge()>65)) {
			return(null);
		}
		else {
			Secretaire e = new Secretaire(nom,prenom, date, salaire, date_embauche);
			return(e);
		}
	}
	
}
